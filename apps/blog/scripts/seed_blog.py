# apps/blog/scripts/seed_blog.py

from django.contrib.auth import get_user_model

from apps.blog.models import Post, PostContent, Tag

User = get_user_model()


def run():

    print("=" * 50)
    print("SEEDING BLOG DATABASE")
    print("=" * 50)

    # =========================================================
    # CREATE ADMIN USER
    # =========================================================

    print("\nCreating admin user...")

    user, created = User.objects.get_or_create(
        username="admin_demo",
        defaults={
            "email": "admin@example.com",
            "is_staff": True,
            "is_superuser": True,
        },
    )

    if created:
        user.set_password("admin123")
        user.save()

        print("Admin user created successfully")
        print("username -> admin_demo")
        print("password -> admin123")

    else:
        print("Admin user already exists")

    # =========================================================
    # CREATE TAGS
    # =========================================================

    print("\nCreating tags...")

    tags_data = [
        "Django",
        "Python",
        "Backend",
        "FastAPI",
        "API",
        "Database",
        "DevOps",
        "Programming",
    ]

    tags = []

    for tag_name in tags_data:
        tag, _ = Tag.objects.get_or_create(name=tag_name)

        tags.append(tag)

    print(f"{len(tags)} tags ready")

    # =========================================================
    # CREATE POSTS
    # =========================================================

    print("\nCreating posts...")

    for i in range(1, 16):
        post, created = Post.objects.get_or_create(
            title=f"Demo Backend Article {i}",
            author=user,
            defaults={
                "description": (
                    "This is a sample article created for testing "
                    "the Django blog layout, pagination and reusable "
                    "Django card components."
                ),
                "status": Post.Status.PUBLISHED,
                "featured": i % 3 == 0,
                "reading_time": 5 + i,
            },
        )

        if created:
            # =================================================
            # ASSIGN TAGS
            # =================================================

            selected_tags = tags[: (i % len(tags)) + 1]

            post.tags.set(selected_tags)

            # =================================================
            # CREATE HEADING BLOCK
            # =================================================

            PostContent.objects.create(
                post=post,
                content_type=PostContent.ContentType.HEADING,
                title="Introduction",
                content="Backend architecture overview",
                order=1,
            )

            # =================================================
            # CREATE TEXT BLOCK
            # =================================================

            PostContent.objects.create(
                post=post,
                content_type=PostContent.ContentType.TEXT,
                content=(
                    "Lorem ipsum dolor sit amet consectetur "
                    "adipisicing elit. Quasi, deserunt."
                ),
                order=2,
            )

            # =================================================
            # CREATE CODE BLOCK
            # =================================================

            PostContent.objects.create(
                post=post,
                content_type=PostContent.ContentType.CODE,
                content=("from fastapi import FastAPI\n\napp = FastAPI()"),
                language="python",
                order=3,
            )

            print(f"Created -> {post.title}")

        else:
            print(f"Skipped -> {post.title}")

    print("\nDatabase seeded successfully")
    print("=" * 50)
