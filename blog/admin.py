from django.contrib import admin
from django.utils.html import format_html, format_html_join
from .models import Blog, tag, webData, BlogComment
from .models import MailMessage, Subscribers, ContactMe, Projects, ProjectTools, Experience


# ─── Custom Actions ────────────────────────────────────────────────────────────

@admin.action(description="📌 Pin selected blogs to top")
def pin_blogs(modeladmin, request, queryset):
    queryset.update(pinned=True)


@admin.action(description="📌 Unpin selected blogs")
def unpin_blogs(modeladmin, request, queryset):
    queryset.update(pinned=False)


@admin.action(description="✅ Publish selected blogs")
def publish_blogs(modeladmin, request, queryset):
    queryset.update(publish=True)


@admin.action(description="🚫 Unpublish selected blogs")
def unpublish_blogs(modeladmin, request, queryset):
    queryset.update(publish=False)


# ─── Blog Admin ────────────────────────────────────────────────────────────────

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)

    # List view columns
    list_display = (
        'title_with_pin',
        'author',
        'publish_date',
        'views_count',
        'tag_list',
        'publish',
        'pinned',
    )

    # Editable directly from list
    list_editable = ('publish', 'pinned')

    # Sidebar filters
    list_filter = ('publish', 'pinned', 'tags', 'author')

    # Search
    search_fields = ('title', 'summary', 'body')

    # Default ordering: pinned first, then newest
    ordering = ('-pinned', '-publish_date')

    # Read-only fields
    readonly_fields = ('views', 'publish_date', 'slug', 'thumbnail_preview')

    # Filter by date in sidebar
    date_hierarchy = 'publish_date'

    # Rows per page
    list_per_page = 20

    # Bulk actions
    actions = [pin_blogs, unpin_blogs, publish_blogs, unpublish_blogs]

    # Organized form layout
    fieldsets = (
        ('📝 Content', {
            'fields': ('title', 'slug', 'image', 'thumbnail_preview', 'summary', 'body'),
        }),
        ('🏷️ Metadata', {
            'fields': ('tags', 'author'),
        }),
        ('⚙️ Settings', {
            'fields': ('publish', 'pinned', 'views', 'publish_date'),
            'classes': ('collapse',),
        }),
    )

    filter_horizontal = ('tags',)

    # Custom display methods
    def title_with_pin(self, obj):
        pin = '📌 ' if obj.pinned else ''
        draft = ' 🔒' if not obj.publish else ''
        return format_html('<strong>{}{}{}</strong>', pin, obj.title, draft)
    title_with_pin.short_description = 'Title'
    title_with_pin.admin_order_field = 'title'

    def views_count(self, obj):
        return format_html('<span style="color:#9676ce;font-weight:600">👁 {}</span>', obj.views)
    views_count.short_description = 'Views'
    views_count.admin_order_field = 'views'

    def tag_list(self, obj):
        tags = obj.tags.all()
        if not tags:
            return '—'
        return format_html_join(
            ' ',
            '<span style="background:#2a2040;color:#aed2ff;padding:2px 8px;border-radius:999px;font-size:11px">{}</span>',
            ((t.tag,) for t in tags)
        )
    tag_list.short_description = 'Tags'

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:8px;margin-top:8px" />',
                obj.image.url
            )
        return '—'
    thumbnail_preview.short_description = 'Preview'


# ─── Tag Admin ─────────────────────────────────────────────────────────────────

@admin.register(tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created_on')
    search_fields = ('tag',)


# ─── Comment Admin ─────────────────────────────────────────────────────────────

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('short_comment', 'user', 'post', 'timeStamp', 'parent')
    list_filter = ('post', 'user')
    search_fields = ('comment', 'user__username', 'post__title')
    ordering = ('-timeStamp',)
    readonly_fields = ('timeStamp',)

    def short_comment(self, obj):
        return obj.comment[:60] + ('...' if len(obj.comment) > 60 else '')
    short_comment.short_description = 'Comment'


# ─── Other Models ──────────────────────────────────────────────────────────────

@admin.register(webData)
class WebDataAdmin(admin.ModelAdmin):
    list_display = ('mine_name', 'site_name', 'email')


@admin.register(MailMessage)
class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    ordering = ('-date',)
    search_fields = ('email',)


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('Full_Name', 'Email_Id', 'Contacted_On')
    search_fields = ('Full_Name', 'Email_Id')
    ordering = ('-Contacted_On',)
    readonly_fields = ('Contacted_On',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)

    list_display = ('name', 'ranking', 'slug', 'projectType', 'doneOn', 'has_case_study')
    list_editable = ('ranking',)
    search_fields = ('name', 'summary', 'case_study')
    readonly_fields = ('slug', 'thumbnail_preview')
    filter_horizontal = ('tools',)

    fieldsets = (
        ('📁 Basic Details', {
            'fields': ('name', 'slug', 'ranking', 'projectType', 'skills', 'doneOn', 'summary'),
        }),
        ('🖼️ Media', {
            'fields': ('Thumbnail', 'thumbnail_preview'),
        }),
        ('📖 Case Study & Links', {
            'fields': ('link', 'github_link', 'case_study', 'tools'),
        }),
    )

    def has_case_study(self, obj):
        return bool(obj.case_study)
    has_case_study.boolean = True
    has_case_study.short_description = 'Case Study?'

    def thumbnail_preview(self, obj):
        if obj.Thumbnail:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:8px;margin-top:8px" />',
                obj.Thumbnail.url
            )
        return '—'
    thumbnail_preview.short_description = 'Preview'


@admin.register(ProjectTools)
class ProjectToolsAdmin(admin.ModelAdmin):
    list_display = ('toolName', 'type', 'publish')
    list_filter = ('type', 'publish')
    list_editable = ('publish',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'period', 'type', 'publish', 'order', 'has_certificate')
    list_filter = ('type', 'publish')
    list_editable = ('publish', 'order')
    search_fields = ('role', 'company', 'responsibilities')
    ordering = ('order', '-id')
    readonly_fields = ('certificate_preview',)

    fieldsets = (
        ('💼 Professional Role', {
            'fields': ('company', 'role', 'type', 'period', 'order', 'publish'),
        }),
        ('📝 Responsibilities', {
            'fields': ('responsibilities',),
            'description': 'Enter each responsibility or accomplishment on a new line.',
        }),
        ('🎓 Certificate & Verification', {
            'fields': ('certificate', 'certificate_url', 'certificate_preview'),
        }),
    )

    def has_certificate(self, obj):
        return bool(obj.certificate or obj.certificate_url)
    has_certificate.boolean = True
    has_certificate.short_description = 'Cert?'

    def certificate_preview(self, obj):
        url = obj.certificate.url if obj.certificate else obj.certificate_url
        if url:
            if url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                return format_html(
                    '<img src="{}" style="max-height:150px;border-radius:6px;margin-top:4px;border:1px solid #333" />',
                    url
                )
            return format_html(
                '<a href="{}" target="_blank" style="color:#aed2ff;font-weight:600;text-decoration:underline">📄 View/Download Certificate</a>',
                url
            )
        return '—'
    certificate_preview.short_description = 'Preview'



