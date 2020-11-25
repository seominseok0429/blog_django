from django.contrib import admin
from .models import Post

@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'photo', 'created_at', 'updated_at']
    list_display_links = ['title']
    # form = PostForm
"""
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None
"""
