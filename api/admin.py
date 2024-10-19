from typing import List, Optional
from django.contrib import admin
from django.db.models import QuerySet
from .models import Post, Author, AuthorProfile, Tag


# Register your models here.


# Define the admin class for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "importance_level",
        "author",
        "get_tags",
    ]  # Define which fields to show in the list view. By including 'id', 'title', and 'importance_level', you get an overview of each post with these details displayed
    list_filter = [
        "importance_level"
    ]  # Add a filter to filter posts by importance level
    search_fields = [
        "title",
    ]  # Add a search bar to filter posts by title
    list_per_page = 5  # Display 5 posts per page
    ordering = (
        "-id",
    )  # Order the posts by id in descending order. Specifies the default ordering for the list view, with -id ordering posts by ID in descending order, so newer posts appear first

    @admin.display(description="Tags")
    def get_tags(self, obj: Post) -> Optional[str]:
        tags: QuerySet[Tag] = obj.tags.all() # Get all tags associated with the post
        return ", ".join([tag.name for tag in tags]) if tags else None # Return a comma-separated string of tag names if tags exist, else return None


# Register the Post model with the custom PostAdmin class in  the admin site
admin.site.register(Post, PostAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "fullname", "email"]
    search_fields = ["fullname", "email"]
    list_per_page = 5
    ordering = ("-id",)


# Register the Author model with the custom AuthorAdmin class in the admin site
admin.site.register(Author, AuthorAdmin)


class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ["author", "bio"]
    search_fields = ["author", "bio"]
    list_per_page = 5
    ordering = ("-author",)


# Register the AuthorProfile model with the custom AuthorProfileAdmin class in the admin site
admin.site.register(AuthorProfile, AuthorProfileAdmin)
