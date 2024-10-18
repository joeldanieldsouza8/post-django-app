from django.contrib import admin
from .models import Post


# Register your models here.

# Define the admin class for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',
                    'importance_level']  # Define which fields to show in the list view. By including 'id', 'title', and 'importance_level', you get an overview of each post with these details displayed
    list_filter = ['importance_level']  # Add a filter to filter posts by importance level
    search_fields = ['title', ]  # Add a search bar to filter posts by title
    list_per_page = 5  # Display 5 posts per page
    ordering = (
        '-id',)  # Order the posts by id in descending order. Specifies the default ordering for the list view, with -id ordering posts by ID in descending order, so newer posts appear first


# Register the Post model with the custom PostAdmin class in the admin site
admin.site.register(Post, PostAdmin)