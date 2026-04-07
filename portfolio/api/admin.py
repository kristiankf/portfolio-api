from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(ExperienceDescription)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(ContactForm)

class ExperienceDescriptionInline(admin.TabularInline):
    model = ExperienceDescription
    extra = 1
    verbose_name = "Experience Description"
    verbose_name_plural = "Experience Descriptions"

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDescriptionInline]
