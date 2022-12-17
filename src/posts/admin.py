from django.contrib import admin

from posts.models import BlogPost


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_updated')
    list_editable = ('published', )
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(BlogPost, BlogPostAdmin)
