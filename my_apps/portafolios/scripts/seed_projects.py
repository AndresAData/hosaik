from my_apps.portafolios.models import Project, ProjectContent

PROJECTS = [
    {
        "title": "Hosaik Portfolio",
        "description": (
            "Personal portfolio created to showcase software development, "
            "cybersecurity projects and technical knowledge."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "About the project",
                "type": "text",
                "content": (
                    "Hosaik is a personal brand and portfolio focused on "
                    "software development, backend engineering and cybersecurity."
                ),
            },
            {
                "title": "Technology",
                "type": "code",
                "content": "Python + Django + Bootstrap 5",
            },
            {
                "title": "Project goals",
                "type": "text",
                "content": (
                    "Create a professional space to document projects, "
                    "experiments and technical growth."
                ),
            },
        ],
    },
    {
        "title": "Planner OS",
        "description": (
            "A productivity platform designed to organize projects, "
            "tasks, habits and personal goals."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Overview",
                "type": "text",
                "content": (
                    "Planner OS is designed as a personal operating system "
                    "for managing goals, projects and daily activities."
                ),
            },
            {
                "title": "Backend",
                "type": "code",
                "content": "Django + PostgreSQL + Django REST Framework",
            },
            {
                "title": "Main features",
                "type": "text",
                "content": (
                    "Projects, tasks, deadlines, notes, habits and "
                    "personal productivity metrics."
                ),
            },
        ],
    },
    {
        "title": "Cybersecurity Dashboard",
        "description": (
            "Security dashboard for monitoring vulnerabilities, incidents "
            "and system security status."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Security overview",
                "type": "text",
                "content": (
                    "A centralized dashboard designed to visualize "
                    "security-related information."
                ),
            },
            {
                "title": "Architecture",
                "type": "code",
                "content": "Python + Django + REST API + PostgreSQL",
            },
            {
                "title": "Monitoring",
                "type": "text",
                "content": (
                    "The system organizes vulnerabilities and incidents "
                    "into an easy-to-understand interface."
                ),
            },
        ],
    },
    {
        "title": "Network Monitor",
        "description": (
            "Network monitoring application designed to visualize hosts, "
            "services and connectivity."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Purpose",
                "type": "text",
                "content": (
                    "Monitor network hosts and provide a simple overview "
                    "of their availability."
                ),
            },
            {
                "title": "Network check",
                "type": "code",
                "content": "ping(host)\ncheck_port(host, port)\nget_status(host)",
            },
        ],
    },
    {
        "title": "API Management System",
        "description": (
            "Backend application for creating, documenting and managing REST APIs."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "API architecture",
                "type": "text",
                "content": (
                    "A backend-focused project exploring REST architecture, "
                    "authentication and API documentation."
                ),
            },
            {
                "title": "Stack",
                "type": "code",
                "content": "Django REST Framework + PostgreSQL + JWT",
            },
        ],
    },
    {
        "title": "Task Manager",
        "description": (
            "Task management application with projects, priorities, "
            "deadlines and status tracking."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Project description",
                "type": "text",
                "content": (
                    "A task manager designed to organize daily activities "
                    "and long-term projects."
                ),
            },
            {
                "title": "Task model",
                "type": "code",
                "content": (
                    "class Task(models.Model):\n"
                    "    title = models.CharField(max_length=150)\n"
                    "    completed = models.BooleanField(default=False)"
                ),
            },
        ],
    },
    {
        "title": "Expense Tracker",
        "description": (
            "Application for managing personal expenses, income "
            "and financial categories."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Financial tracking",
                "type": "text",
                "content": (
                    "Users can register income and expenses and organize "
                    "them into financial categories."
                ),
            },
            {
                "title": "Technology",
                "type": "code",
                "content": "Python + Django + SQLite + Bootstrap 5",
            },
        ],
    },
    {
        "title": "Password Manager",
        "description": (
            "Security-focused application for organizing and managing "
            "encrypted credentials."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Security concept",
                "type": "text",
                "content": (
                    "An experimental project focused on secure credential "
                    "management and encryption concepts."
                ),
            },
            {
                "title": "Encryption",
                "type": "code",
                "content": "encrypted_data = cipher.encrypt(data)",
            },
        ],
    },
    {
        "title": "Log Analyzer",
        "description": (
            "Tool for analyzing application logs and identifying "
            "suspicious or unusual activity."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Log analysis",
                "type": "text",
                "content": (
                    "The application processes logs to identify patterns, "
                    "errors and potentially suspicious events."
                ),
            },
            {
                "title": "Processing",
                "type": "code",
                "content": (
                    "for line in logs:\n    analyze(line)\n    detect_anomaly(line)"
                ),
            },
        ],
    },
    {
        "title": "File Management API",
        "description": (
            "REST API for uploading, managing and organizing files "
            "through a backend service."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "File API",
                "type": "text",
                "content": (
                    "A backend service designed to manage file uploads and metadata."
                ),
            },
            {
                "title": "Endpoint example",
                "type": "code",
                "content": "POST /api/files/\nGET /api/files/\nDELETE /api/files/<id>/",
            },
        ],
    },
    {
        "title": "Authentication Service",
        "description": (
            "Authentication backend implementing registration, login, "
            "sessions and permissions."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Authentication",
                "type": "text",
                "content": (
                    "Authentication is implemented using Django's built-in "
                    "authentication system."
                ),
            },
            {
                "title": "Login",
                "type": "code",
                "content": "authenticate(username=username, password=password)",
            },
        ],
    },
    {
        "title": "Blog Platform",
        "description": (
            "Modern blogging platform with posts, categories, comments "
            "and content management."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Blog system",
                "type": "text",
                "content": (
                    "A complete blogging platform designed to explore "
                    "content management with Django."
                ),
            },
            {
                "title": "Models",
                "type": "code",
                "content": "Post\nCategory\nComment\nAuthor",
            },
        ],
    },
    {
        "title": "URL Shortener",
        "description": (
            "Simple URL shortening service with unique links and usage statistics."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Short links",
                "type": "text",
                "content": (
                    "Users can generate short URLs that redirect to "
                    "long destination URLs."
                ),
            },
            {
                "title": "Redirect",
                "type": "code",
                "content": "return redirect(short_url.target)",
            },
        ],
    },
    {
        "title": "System Information Tool",
        "description": (
            "Python utility for collecting information about hardware, "
            "operating systems and processes."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "System information",
                "type": "text",
                "content": (
                    "A Python utility for learning how operating systems "
                    "expose hardware and process information."
                ),
            },
            {
                "title": "Python",
                "type": "code",
                "content": "import platform\nprint(platform.system())",
            },
        ],
    },
    {
        "title": "Server Health Monitor",
        "description": (
            "Monitoring application for tracking CPU, memory, disk "
            "and server availability."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Monitoring",
                "type": "text",
                "content": (
                    "The application monitors important server resources "
                    "and displays their current status."
                ),
            },
            {
                "title": "Metrics",
                "type": "code",
                "content": "CPU\nRAM\nDISK\nUPTIME",
            },
        ],
    },
    {
        "title": "Inventory Management",
        "description": (
            "Inventory system for managing products, stock, categories and movements."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Inventory",
                "type": "text",
                "content": (
                    "A CRUD application designed to manage products "
                    "and stock movements."
                ),
            },
            {
                "title": "Main models",
                "type": "code",
                "content": "Product\nCategory\nStockMovement",
            },
        ],
    },
    {
        "title": "Authentication API",
        "description": (
            "REST API focused on secure authentication and user authorization."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "REST authentication",
                "type": "text",
                "content": (
                    "Authentication API focused on secure access "
                    "to protected resources."
                ),
            },
            {
                "title": "Token",
                "type": "code",
                "content": "Authorization: Bearer <access_token>",
            },
        ],
    },
    {
        "title": "Data Processing Pipeline",
        "description": (
            "Python project for processing, transforming and validating "
            "structured datasets."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Data pipeline",
                "type": "text",
                "content": (
                    "A project focused on data ingestion, transformation, "
                    "validation and export."
                ),
            },
            {
                "title": "Pipeline",
                "type": "code",
                "content": (
                    "load_data()\nclean_data()\nvalidate_data()\nexport_data()"
                ),
            },
        ],
    },
    {
        "title": "Security Scanner",
        "description": (
            "Experimental security scanner for identifying common "
            "configuration and service issues."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Security scanner",
                "type": "text",
                "content": (
                    "An educational security project focused on "
                    "understanding vulnerability detection."
                ),
            },
            {
                "title": "Scanner flow",
                "type": "code",
                "content": (
                    "discover()\nenumerate_services()\nanalyze_configuration()"
                ),
            },
        ],
    },
    {
        "title": "Developer Notes",
        "description": (
            "Knowledge management application for storing programming "
            "notes, references and experiments."
        ),
        "url": "https://github.com/",
        "contents": [
            {
                "title": "Knowledge base",
                "type": "text",
                "content": (
                    "A personal knowledge base for documenting programming "
                    "concepts, experiments and useful references."
                ),
            },
            {
                "title": "Technology",
                "type": "code",
                "content": "Django + Bootstrap 5 + SQLite",
            },
        ],
    },
]


def run():
    for project_data in PROJECTS:
        contents = project_data.pop("contents")

        project, created = Project.objects.get_or_create(
            title=project_data["title"],
            defaults=project_data,
        )

        if created:
            print(f"Created project: {project.title}")
        else:
            print(f"Already exists: {project.title}")

        if created:
            for content_data in contents:
                ProjectContent.objects.create(
                    project=project,
                    title=content_data["title"],
                    content_type=content_data["type"],
                    content=content_data.get("content", ""),
                )

                print(f"  └── Created content: {content_data['title']}")

    print("\nSeed completed!")
