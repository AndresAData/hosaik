from uuid import uuid4

from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["name"]

        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name


class Post(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()

    cover = models.ImageField(upload_to="blog/covers/", blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    status = models.CharField(
        max_length=15, choices=Status.choices, default=Status.DRAFT
    )

    featured = models.BooleanField(default=False)

    reading_time = models.PositiveIntegerField(
        default=1, help_text="Reading time in minutes"
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):

        if not self.slug:
            short_uuid = str(uuid4())[:8]

            self.slug = f"{slugify(self.title)}-{short_uuid}"

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title


class PostContent(BaseModel):
    class ContentType(models.TextChoices):
        TEXT = "TEXT", "Text"

        IMAGE = "IMAGE", "Image"

        CODE = "CODE", "Code"

        QUOTE = "QUOTE", "Quote"

        HEADING = "HEADING", "Heading"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="contents")

    content_type = models.CharField(
        max_length=20, choices=ContentType.choices, default=ContentType.TEXT
    )

    title = models.CharField(max_length=255, blank=True)

    content = models.TextField(blank=True)

    image = models.ImageField(upload_to="blog/content/", blank=True, null=True)

    language = models.CharField(
        max_length=50, blank=True, help_text="Programming language for code blocks"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

        verbose_name = "Post Content"
        verbose_name_plural = "Post Contents"

    def __str__(self):

        return f"{self.post.title} - {self.content_type}"
