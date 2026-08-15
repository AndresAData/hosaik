from django import forms

from my_apps.portafolios.models import Project, ProjectContent, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Django",
                }
            ),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "url",
            "tags",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe your project...",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }


class ProjectContentForm(forms.ModelForm):
    class Meta:
        model = ProjectContent
        fields = [
            "title",
            "content_type",
            "image",
            "content",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Content title",
                }
            ),
            "content_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your content here...",
                    "rows": 10,
                }
            ),
        }
