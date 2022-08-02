from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.





class webData(models.Model):
    site_name = models.CharField(max_length=50)
    About_me = models.TextField()
    mine_name = models.CharField(max_length=50)
    HomePage_qoute = models.TextField()
    # slide_img = models.ManyToManyField(sliderImages)
    my_image = models.ImageField(upload_to='images/homepage')

    slider1 = models.ImageField(upload_to='images/homepage/',null=True)


    def __str__(self):
        return self.mine_name

    
   

#blog table

class tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag
    

class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(null=False)
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=250,null=True)
    publish_date = models.DateTimeField()
    body = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.ManyToManyField(tag)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title+' | '+ str(self.author)


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True , default='none')
    timeStamp = models.DateTimeField(default=now)
    parent = models.ForeignKey("self", null=True ,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment[0:13] + '...' + " by " + self.user.username + ' on  blog(title) '  + self.post.title
    

class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.email

class MailMessage(models.Model):
    title = models.CharField(max_length=100,null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title


class ContactMe(models.Model):
    Full_Name = models.CharField(max_length=25,null=False)
    Email_Id = models.EmailField(null=False)
    Message_To_Me =models.TextField(null=False)
    Contacted_On = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.Full_Name + "|" + str(self.Contacted_On)
    



class Projects(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField()
    doneOn = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='Projects/logo')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    