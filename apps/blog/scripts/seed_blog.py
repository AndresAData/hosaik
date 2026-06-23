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
        "Docker",
        "SQL",
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
            # CREATE MULTIPLE CONTENT BLOCKS
            # =================================================

            contents = [
                # =====================================================
                # INTRODUCTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "Introduction",
                    "content": "Modern backend engineering",
                    "order": 1,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Backend development has evolved significantly over "
                        "the last decade. Applications now require scalable "
                        "architectures, asynchronous processing and modular "
                        "service-oriented systems."
                    ),
                    "order": 2,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Developers are increasingly combining frameworks "
                        "such as Django and FastAPI to build systems capable "
                        "of handling APIs, ETL pipelines and data-intensive "
                        "operations efficiently."
                    ),
                    "order": 3,
                },
                # =====================================================
                # DJANGO SECTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "Why Django Still Matters",
                    "content": "The power of batteries included",
                    "order": 4,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Django remains one of the most productive backend "
                        "frameworks because it provides authentication, ORM, "
                        "admin panel and security features out of the box."
                    ),
                    "order": 5,
                },
                {
                    "content_type": PostContent.ContentType.CODE,
                    "content": (
                        "from django.urls import path\n"
                        "from .views import PostListView\n\n"
                        "urlpatterns = [\n"
                        "    path('', PostListView.as_view()),\n"
                        "]"
                    ),
                    "language": "python",
                    "order": 6,
                },
                {
                    "content_type": PostContent.ContentType.QUOTE,
                    "content": ("Simple is better than complex."),
                    "order": 7,
                },
                # =====================================================
                # FASTAPI SECTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "FastAPI Microservices",
                    "content": "High performance APIs",
                    "order": 8,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "FastAPI provides asynchronous capabilities and "
                        "automatic OpenAPI documentation, making it an "
                        "excellent choice for data services and APIs."
                    ),
                    "order": 9,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Combining Django and FastAPI allows developers to "
                        "separate business logic from high-throughput "
                        "processing services."
                    ),
                    "order": 10,
                },
                {
                    "content_type": PostContent.ContentType.CODE,
                    "content": (
                        "from fastapi import FastAPI\n\n"
                        "app = FastAPI()\n\n"
                        "@app.get('/')\n"
                        "async def home():\n"
                        "    return {'message': 'hello'}"
                    ),
                    "language": "python",
                    "order": 11,
                },
                # =====================================================
                # DATABASE SECTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "Database Optimization",
                    "content": "Scaling SQL queries",
                    "order": 12,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Efficient indexing strategies improve performance "
                        "dramatically when dealing with large relational "
                        "datasets."
                    ),
                    "order": 13,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Using select_related and prefetch_related properly "
                        "in Django avoids N+1 query problems and reduces "
                        "database overhead."
                    ),
                    "order": 14,
                },
                {
                    "content_type": PostContent.ContentType.CODE,
                    "content": (
                        "Post.objects.select_related('author')\n"
                        ".prefetch_related('tags')"
                    ),
                    "language": "python",
                    "order": 15,
                },
                # =====================================================
                # ETL SECTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "Building ETL Pipelines",
                    "content": "Data engineering workflows",
                    "order": 16,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "ETL systems extract, transform and load data from "
                        "multiple sources into centralized platforms."
                    ),
                    "order": 17,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Python is especially useful for ETL development "
                        "because of its extensive ecosystem for analytics "
                        "and data processing."
                    ),
                    "order": 18,
                },
                {
                    "content_type": PostContent.ContentType.CODE,
                    "content": (
                        "import pandas as pd\n\n"
                        "df = pd.read_csv('data.csv')\n"
                        "df = df.dropna()"
                    ),
                    "language": "python",
                    "order": 19,
                },
                # =====================================================
                # DEVOPS SECTION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "DevOps and Deployment",
                    "content": "Infrastructure matters",
                    "order": 20,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Modern deployment pipelines rely heavily on "
                        "containerization and reproducible environments."
                    ),
                    "order": 21,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Docker simplifies backend deployment by packaging "
                        "applications and dependencies together."
                    ),
                    "order": 22,
                },
                {
                    "content_type": PostContent.ContentType.CODE,
                    "content": (
                        "docker build -t backend-app .\n"
                        "docker run -p 8000:8000 backend-app"
                    ),
                    "language": "bash",
                    "order": 23,
                },
                # =====================================================
                # CONCLUSION
                # =====================================================
                {
                    "content_type": PostContent.ContentType.HEADING,
                    "title": "Conclusion",
                    "content": "Final thoughts",
                    "order": 24,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "A solid backend architecture focuses on "
                        "maintainability, scalability and clean system "
                        "design principles."
                    ),
                    "order": 25,
                },
                {
                    "content_type": PostContent.ContentType.TEXT,
                    "content": (
                        "Combining Django, FastAPI and proper database "
                        "optimization techniques creates highly capable "
                        "modern backend systems."
                    ),
                    "order": 26,
                },
            ]

            PostContent.objects.bulk_create(
                [
                    PostContent(
                        post=post,
                        content_type=item["content_type"],
                        title=item.get("title", ""),
                        content=item.get("content", ""),
                        language=item.get("language", ""),
                        order=item["order"],
                    )
                    for item in contents
                ]
            )

            print(f"Created -> {post.title}")

        else:
            print(f"Skipped -> {post.title}")

    print("\nDatabase seeded successfully")
    print("=" * 50)
