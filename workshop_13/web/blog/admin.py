from django.contrib import admin
from blog.models import Post, PostImage

admin.site.register([PostImage])


class PostImageInline(admin.StackedInline):
    model = PostImage
    fields = ["image"]
    extra = 1


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "author"]
    search_fields = ["title", "content", "author__username"]
    list_filter = ["author__username", "created_at"]

    inlines = [PostImageInline]
