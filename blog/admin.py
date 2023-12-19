from django.contrib import admin
from .models import Blog,tag,webData,BlogComment
from .models import MailMessage,Subscribers,ContactMe,Projects,ProjectTools


@admin.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)


# blogs
admin.site.register(tag)
admin.site.register(BlogComment)
admin.site.register(webData)


# mail subscriptions
admin.site.register(MailMessage)
admin.site.register(Subscribers)


#Contact Me
admin.site.register(ContactMe)

# project
admin.site.register(Projects)
admin.site.register(ProjectTools)
