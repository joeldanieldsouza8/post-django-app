import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["fullname"]  # Order the authors by fullname in ascending order

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]  # Order the tags by name in ascending order

    def __str__(self):
        return f"Tag: {self.name}"


# def get_default_author():
#     author, created = Author.objects.get_or_create(fullname='System Author', email="system@example.com")

#     return author


class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author, on_delete=models.CASCADE, related_name="author_profile"
    )
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    class Meta:
        verbose_name = "Author Profile"
        verbose_name_plural = "Author Profiles"

    def __str__(self):
        return f"Profile of {self.author.fullname}"


class Post(models.Model):
    class ImportanceLevel(models.IntegerChoices):
        LOW = 1, _("Low")
        MEDIUM = 2, _("Medium")
        HIGH = 3, _("High")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    importance_level = models.IntegerField(
        choices=ImportanceLevel.choices, default=ImportanceLevel.LOW
    )

    # FK relationships
    # first_arg: The model being referenced to which the relationship is being made
    # on_delete: This ensures that if an Author is deleted, all related Posts are also deleted
    # related_name: This allows you to access all the posts of an author using author.posts in your queries
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = [
            "-importance_level"
        ]  # Order the posts by importance level in descending order

    # This dunder method is used to return a string representation of the instance/object of the Post class
    def __str__(self):
        return self.title
