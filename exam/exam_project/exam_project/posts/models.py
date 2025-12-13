from django.core.validators import MinLengthValidator
from django.db import models

from exam.exam_project.author.models import Author


class Post(models.Model):
    MAX_LEN_TITLE = 50
    MIN_LEN_TITLE = 5

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        validators=(MinLengthValidator(MIN_LEN_TITLE), ),
        null=False,
        blank=False,
        unique=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Post Image URL',
    )
    content = models.TextField(
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        null=False,
        blank=True,
        auto_now=True,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name='posts'
    )


