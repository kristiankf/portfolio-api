from django.contrib import admin

from .models import (
    ContactForm,
    Education,
    Experience,
    ExperienceDescription,
    Project,
    Skill,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_name")
    search_fields = ("name", "icon_name")


class ExperienceDescriptionInline(admin.TabularInline):
    model = ExperienceDescription
    extra = 1
    ordering = ("id",)


class ProjectInline(admin.TabularInline):
    """Projects linked to this experience (skills edited on the Project admin)."""
    model = Project
    fk_name = "experience"
    extra = 0
    exclude = ("skills",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company_name", "role", "start_date", "end_date", "location")
    search_fields = ("company_name", "role", "location")
    filter_horizontal = ("skills",)
    inlines = (ExperienceDescriptionInline, ProjectInline)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "program", "degree", "date_started", "date_completed")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "experience", "created_at")
    search_fields = ("title", "description")
    filter_horizontal = ("skills",)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    ordering = ("-submitted_at",)
