from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # education endpoints
    path('education/', views.EducationList.as_view(), name='education'),
    path('education/<int:pk>/', views.EducationDetail.as_view(), name='education_detail'),

    # experience endpoints
    path('experience/', views.ExperienceList.as_view(), name='experience'),
    path('experience/<int:pk>/', views.ExperienceDetail.as_view(), name='experience_detail'),
    path('experience-description/', views.ExperienceDescriptionList.as_view(), name='experience_description'),
    path('experience-description/<int:pk>/', views.ExperienceDescriptionDetail.as_view(), name='experience_description_detail'),

    # project endpoints
    path('projects/', views.ProjectList.as_view(), name='project'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),

    # skills endpoints
    path('skills/', views.SkillList.as_view(), name='skill'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skill_detail'),

    # contact endpoints
    path('contact/', views.ContactFormList.as_view(), name='contact'),
    path('contact/<int:pk>/', views.ContactFormDetail.as_view(), name='contact_detail'),

    path('test-cloudinary/', views.cloudinary_test),
]

urlpatterns = format_suffix_patterns(urlpatterns)