from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import strip_tags
from django.conf import settings
from blog.models import Blog, webData, BlogComment, Subscribers, MailMessage, tag, ContactMe, Projects
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
import json
import random
data = webData.objects.first()

# html pages
def subscription(request):
    Subscriber = Subscribers()
    if request.method == "POST":
        mail = request.POST['SubscriptionEmail']
        if Subscribers.objects.filter(email=mail).exists():

            return HttpResponse(f"{mail} had already Subscribed to NewsLetter")
        else:
            Subscriber.email = mail
            Subscriber.save()
            subject = f'Subscribed To Sids BLOG Newsletter!'
            html_message = render_to_string(
                'MailTempletes/Subscribe.html')
            plain_message = strip_tags(html_message)
            Mail_From = settings.EMAIL_HOST_USER
            Mail_To = [mail, ]
            send_mail(subject, plain_message, Mail_From, Mail_To,
                      html_message=html_message, fail_silently=True)
            return HttpResponse(f"<span class='text-capitalize'>congrats <i class='bi bi-stars'></i>, {mail} has been Subscribe to NewsLetter </span>")
        return HttpResponse("please fill the field.")


def home(request):
    post = Blog.objects.order_by('-publish_date')[0:3]
    PopularPosts = Blog.objects.order_by('-views')[0:3]
    return render(request, 'home.html', {'posts': post, 'PopularPosts': PopularPosts, 'data': data, 'index': ' Home'})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def contact(request):
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Message = request.POST['message']
        contactMe = ContactMe()
        contactMe.Full_Name = Name
        contactMe.Email_Id = Email
        contactMe.Message_To_Me = Message
        contactMe.save()
        subject = f'Greetings From Sudarshan'
        html_message = render_to_string(
            'MailTempletes/Contact.html', {'name': Name})
        plain_message = strip_tags(html_message)
        Mail_From = settings.EMAIL_HOST_USER
        Mail_To = [Email,'sudarshankakde1111@gmail.com' ]
        send_mail(subject, plain_message, Mail_From, Mail_To,
                  html_message=html_message, fail_silently=True)
        messages.success(
            request, f"<b class='text-capitalize'>Your Response has been saved. I Will Contact You Shortly</b>")
        return HttpResponse(f"""Your response is saved. I will contact you shortly!""")
    return render(request, 'contact.html', {'data': data, 'index': ' Contact me'})


# comment and reply on blog
def postComment(request):
    if (request.method == 'POST'):
        comment = request.POST['Postcomment']
        user = request.user
        postSno = request.POST['PostSno']
        PostSlug = request.POST['PostSlug']
        post = Blog.objects.get(id=postSno)
        parentSno = request.POST['parentSno']
        blogdetails = get_object_or_404(Blog, slug=PostSlug)
        comments = BlogComment.objects.filter(post=blogdetails, parent=None)
        comments = comments.order_by('-sno')
        replies = BlogComment.objects.filter(
            post=blogdetails).exclude(parent=None)
        replyDict = {}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno] = [reply]
            else:
                replyDict[reply.parent.sno].append(reply)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            return render(request, 'blog/comment.html', {'comments': comments, 'replyDict': replyDict,'blog':post})

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
            comment.save()
            print(parent.sno)
            return render(request, 'blog/reply.html', {'reply': comment})



# api search


def search(request):
    query = request.GET['query']
    if len(query) > 20:
        allPosts = []
    else:
        allPostsBody = Blog.objects.filter(body__icontains=query)
        allPostsTitle = Blog.objects.filter(title__icontains=query)
        try:
            tagId = tag.objects.only('id').get(tag=query).id
            allTags = Blog.objects.filter(tags=tagId)
            Posts = allPostsBody.union(allPostsTitle)
            allPosts = allPostsBody.union(allTags)
        except:
            allPosts = allPostsBody.union(allPostsTitle)

        # posts ={'allposts':allPosts}
    return render(request, 'search.html', {'data': data, 'index': 'All Blogs', 'posts': allPosts.order_by('-publish_date'), 'query': query})


# apis for user autantication
def handleSingup(request):
    Subscriber = Subscribers()
    if (request.method == 'POST'):
        # get peramenters
        username = request.POST['username'].lower()
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # check for error input
        if len(username) > 10:
            messages.error(request, 'Username must under 10 character')
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        if not username.isalnum():
            messages.error(
                request, 'username should not have specail character')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        if password1 != password2:
            messages.error(request, 'Passwords do not match. please try again')
            return redirect(request.META.get('HTTP_REFERER', 'home'))

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username Allready taken')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'this email has been registerd.')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
        # work with model
        # create user
        else:

            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            Subscriber.email = email
            Subscriber.save()
            messages.success(
                request, 'Your account has been successfully creater')
        return redirect('handleLogin')

    return render(request, 'Singup.html')


def checkForUserName(request):
    if (request.method == "GET"):
        username = request.GET['username'].lower()
        if len(username) < 1:
            return HttpResponse('<span class="text-user-primary-100 float-end text-lowercase">enter username</span>')

        if len(username) > 10:
            return HttpResponse('<span class="text-danger float-end text-lowercase">Username must under 10 character</span>')

        if not username.isalnum():
            return HttpResponse('<span class="text-danger float-end text-lowercase">Username should not have specail character</span>')

        if User.objects.filter(username=username).exists():
            return HttpResponse('<span class="text-danger float-end text-lowercase">Username Allready taken</span>')
        else:
            return HttpResponse('<span class="text-user-primary-100 float-end text-lowercase">Username Available</span>')


def checkForUserMail(request):
    if (request.method == "GET"):
        email = request.GET['email']
        if User.objects.filter(email=email).exists():
            return HttpResponse('<span class="text-danger float-end text-lowercase">Email Allready In Use</span>')
        else:
            return HttpResponse('')


def Privacy_Policy(request):
    return render(request, 'Extra/Privacy_Policy.html', {'data': data, 'index': 'Privacy Policy'})


def handleLogin(request):
    if (request.method == 'POST'):
        # get peramenters
        username = request.POST['loginusername'].lower()
        password = request.POST['loginpassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully loged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please try again')
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    return render(request, 'Login.html')


def handelLogout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(request.META.get('HTTP_REFERER', 'home'))




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
    return render(request, '404Page.html')




def aboutme(request):
    projects = Projects.objects.order_by('-id')
    if request.method == "POST":
        Name = request.POST['name']
        Email = request.POST['email']
        Message = request.POST['message']
        contactMe = ContactMe()
        contactMe.Full_Name = Name
        contactMe.Email_Id = Email
        contactMe.Message_To_Me = Message
        contactMe.save()
        subject = f'Greetings From Sudarshan'
        html_message = render_to_string(
            'MailTempletes/Contact.html', {'name': Name})
        plain_message = strip_tags(html_message)
        Mail_From = settings.EMAIL_HOST_USER
        Mail_To = [Email, ]
        send_mail(subject, plain_message, Mail_From, Mail_To,
                  html_message=html_message, fail_silently=True)
    return render(request, 'aboutMe.html', {'projects': projects, 'data': data})

