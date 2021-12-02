from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog, webData, BlogComment, Subscribers, MailMessage
from django.template import RequestContext
# from django.shortcuts import render_to_response
# from blog.froms import SubscibersForm
from django.contrib.auth.models import User
from quote import quote
from django.contrib import messages
from django.contrib.auth.models import User, auth
from blog.templatetags import extras_filter
from django.core.mail import send_mail
from django_pandas.io import read_frame
import re
from django.template.loader import render_to_string

# data = {
#     'site_name': "SID's blogs",
#     'About_me': """I am 19 year old Collage Student,A programmer 💻, and A Web Developer 🕸️
#         living at Aurangabad, India. I am a Information Technology Student,
#         currently Studying at GOVERMENT POLY AMBAD.""",
#     'mine_name': 'Sudarshan kakde',
# }

data = webData.objects.first()


# html pages


def home(request):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    Subscriber = Subscribers()
    if request.method == "POST":
        mail = request.POST['SubscriptionEmail']
        if Subscribers.objects.filter(email=mail).exists():
            messages.success(
                request, f"{mail} had already Subscribed to NewsLetter")
        else:
            Subscriber.email = mail
            Subscriber.save()
            messages.success(
                request, f"<h5 class='text-capitalize'>congrats <i class='bi bi-stars'></i>, {mail} has been Subscribe to NewsLetter </h5>")

    post = Blog.objects.order_by('-publish_date')[0:3]
    PopularPosts = Blog.objects.order_by('-views')[0:3]
    return render(request, 'home.html', {'posts': post, 'PopularPosts': PopularPosts, 'data': data, 'index': ' Home'})


def contact(request):
    return render(request, 'contact.html', {'data': data, 'index': ' Contact me'})


def detail(request, slug):
    blogdetails = get_object_or_404(Blog, slug=slug)
    comments = BlogComment.objects.filter(post=blogdetails, parent=None)
    comments = comments.order_by('-sno')
    replies = BlogComment.objects.filter(post=blogdetails).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    blogdetails.views = blogdetails.views + 1
    blogdetails.save()
    return render(request, 'detail.html', {'blog': blogdetails, 'data': data, 'comments': comments, 'replyDict': replyDict})


def AllBlogs(request):
    posts = Blog.objects.order_by('-publish_date')
    return render(request, 'all blogs.html', {'posts': posts, 'data': data, 'index': 'All Blogs'})

# api search


def search(request):
    query = request.GET['query']
    if len(query) > 20:
        allposts = []
    else:
        allPostsBody = Blog.objects.filter(body__icontains=query)
        allPostsTitle = Blog.objects.filter(title__icontains=query)
        allPosts = allPostsBody.union(allPostsTitle)

    # posts ={'allposts':allPosts}
    return render(request, 'search.html', {'data': data, 'index': 'All Blogs', 'posts': allPosts, 'query': query})


# apis for user autantication
def handleSingup(request):
    if (request.method == 'POST'):
        # get peramenters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # check for error input
        if len(username) > 10:
            messages.error(request, 'Username must under 10 character')
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, 'username should not have specail character')
            return redirect('home')
        if password1 != password2:
            messages.error(request, 'Passwords do not match. please try again')
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username Allready taken')
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'this email has been registerd.')
            return redirect('home')
        # work with model
        # create user
        else:
            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(
                request, 'Your account has been successfully creater')

        return redirect('home')

    else:
        return render(request, 'search.html', {'data': data, 'index': '404 not found'})


def handleLogin(request):
    if (request.method == 'POST'):
        # get peramenters
        username = request.POST['loginusername']
        password = request.POST['loginpassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully loged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please try again')
            return redirect('home')


def handelLogout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


# api for post comment
def postComment(request):
    if (request.method == 'POST'):
        comment = request.POST['Postcomment']
        user = request.user
        postSno = request.POST.get("PostSno")
        PostSlug = request.POST.get("PostSlug")
        post = Blog.objects.get(id=postSno)
        parentSno = request.POST.get('parentSno')

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(
                request, 'your comment has been posted  successfully')

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
            messages.success(
                request, 'your reply has been posted  successfully')
        comment.save()

    return redirect(f"/{PostSlug}")


# api for send mail news letter

def newsletter(request):
    if request.method == "POST":
        mail_title = request.POST['title']
        mail_message = request.POST['message']
        emails = Subscribers.objects.all()
        data_frame = read_frame(emails, fieldnames=['email'])
        mail_list = data_frame['email'].values.tolist()
        print(mail_list)
        send_mail(mail_title,
                  mail_message,
                  '',
                  mail_list,
                  fail_silently=False
                  )
        mail = MailMessage(message=mail_message, title=mail_title)
        mail.save()

    return render(request, 'newsletter.html', {'data': data})


def error_404_view(request, exception):
    return render(request, '404.html')


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
