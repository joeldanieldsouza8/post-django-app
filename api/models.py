import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    class ImportanceLevel(models.IntegerChoices):
        LOW = 1, _('Low')
        MEDIUM = 2, _('Medium')
        HIGH = 3, _('High')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    importance_level = models.IntegerField(choices=ImportanceLevel.choices, default=ImportanceLevel.LOW)

    # This dunder method is used to return a string representation of the instance/object of the Post class
    def __str__(self):
        return self.title