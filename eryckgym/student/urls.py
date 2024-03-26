from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from student import views

urlpatterns = [
    path("students", views.get_or_create_student),
    path("students/<int:pk>", views.get_update_delete),
]

urlpatterns = format_suffix_patterns(urlpatterns)