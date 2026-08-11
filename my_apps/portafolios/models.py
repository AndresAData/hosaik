from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to="portfolio/projects/",
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        editable=False,
    )
    url = models.URLField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_id = str(uuid4())[:8]
            self.slug = slugify(f"{self.title}-{unique_id}")

        super().save(*args, **kwargs)


class ProjectContent(models.Model):
    class ContentTypeChoices(models.TextChoices):
        TEXT = "text", "Text"
        IMAGE = "image", "Image"
        CODE = "code", "Code"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contents",
    )
    title = models.CharField(
        max_length=100,
    )
    content_type = models.CharField(
        max_length=5,
        choices=ContentTypeChoices.choices,
    )
    image = models.ImageField(
        upload_to="portfolio/project-content/",
        blank=True,
    )
    content = models.TextField(
        blank=True,
    )
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Project Content"
        verbose_name_plural = "Project Contents"
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"{self.project.title} - {self.title}"

    def clean(self):
        if self.content_type == self.ContentTypeChoices.IMAGE and not self.image:
            raise ValidationError({"image": "An image is required for image content."})

        if (
            self.content_type
            in (
                self.ContentTypeChoices.TEXT,
                self.ContentTypeChoices.CODE,
            )
            and not self.content
        ):
            raise ValidationError(
                {"content": "Content is required for text or code content."}
            )
