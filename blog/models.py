from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from autoslug import AutoSlugField
from django.core.validators import FileExtensionValidator

# Create your models here.


class webData(models.Model):
    site_name = models.CharField(max_length=50)
    About_me = models.TextField()
    mine_name = models.CharField(max_length=50)
    HomePage_qoute = models.TextField()
    email = models.EmailField(max_length=254)
    # slide_img = models.ManyToManyField(sliderImages)
    my_image = models.ImageField(upload_to='Images/WebData')

    slider1 = models.ImageField(upload_to='Images/WebData', null=True)
    Socail = models.URLField(max_length=200, null=True)
    resume_url = models.URLField(max_length=500, null=True, blank=True, help_text="Google Drive preview link for resume")

    def __str__(self):
        return self.mine_name

# many to many fieleds
class tag(models.Model):
    created_on = models.DateField(auto_now=True, editable=False)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

TYPE_CHOICES = (
    ('tool','TOOL'),
    ('framework', 'FRAMEWORK'),
    ('library','LIBRARY'),
    ('language ','LANGUAGE'),
)
class ProjectTools(models.Model):
    created_on = models.DateField(auto_now=True, editable=False)
    toolName = models.CharField(max_length=50)
    logo = models.FileField(upload_to="Images/Tools", validators=[FileExtensionValidator(['svg'])])
    publish = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='tool')
    def __str__(self):
        return self.toolName
    

class Blog(models.Model):
    image = models.ImageField(upload_to='Images/BlogImages', null=True)
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title')
    summary = models.TextField(max_length=250, null=True)
    publish_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    body = models.TextField()
    tags = models.ManyToManyField(tag)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=5)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=True)
    pinned = models.BooleanField(default=False, help_text="Pin this blog to the top of the list")

    def __str__(self):
        return self.title + ' | ' + self.author.first_name



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True , default='none')
    timeStamp = models.DateTimeField(default=now)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[0:15] + '...' + " by " + self.user.username + ' on  blog(title)-' + self.post.title


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email or "No Email"


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title or "Untitled Message"


class ContactMe(models.Model):
    Full_Name = models.CharField(max_length=25, null=False)
    Email_Id = models.EmailField(null=False)
    Message_To_Me = models.TextField(null=False)
    Contacted_On = models.DateTimeField(default=now)

    def __str__(self):
        return self.Full_Name + "|" + str(self.Contacted_On)


class Projects(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    summary = models.TextField()
    projectType = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    doneOn = models.CharField(max_length=50)
    Thumbnail = models.ImageField(upload_to='Images/Projects/Thumbnail')
    link = models.URLField(max_length=200, help_text="Live demo URL")
    github_link = models.URLField(max_length=200, blank=True, null=True, help_text="GitHub repository URL")
    case_study = models.TextField(blank=True, null=True, help_text="Detailed project case study content (HTML/TinyMCE)")
    tools = models.ManyToManyField(ProjectTools)
    ranking = models.IntegerField(default=10, help_text="Ranking order (smaller values first)")

    def __str__(self):
        return self.name


class Experience(models.Model):
    EXPERIENCE_TYPES = (
        ('internship', 'Internship'),
        ('job', 'Job'),
        ('offer_letter', 'Offer Letter'),
    )
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    period = models.CharField(max_length=100, help_text="e.g. June 2023 - Aug 2023")
    responsibilities = models.TextField(help_text="Enter each responsibility on a new line")
    type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES, default='job')
    certificate = models.FileField(upload_to="Certificates/", blank=True, null=True, help_text="Upload certificate file")
    certificate_url = models.URLField(max_length=500, blank=True, null=True, help_text="Or enter certificate URL")
    publish = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Ordering index (smaller first or larger first, default is descending by id)")

    def __str__(self):
        return f"{self.role} at {self.company}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, default="Gallery Image", help_text="Label text displayed under image card")
    image = models.ImageField(upload_to='Images/Gallery')
    order = models.IntegerField(default=0, help_text="Ordering index (smaller values first)")
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Gallery Image {self.id}"


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="Emoji or icon label e.g. 🕸️, 💻, 🎨")
    order = models.IntegerField(default=0, help_text="Ordering index (smaller values first)")
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



