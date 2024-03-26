from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from training import views

urlpatterns = [
    path("training", views.get_or_create),
    path("training/<int:pk>", views.get_update_delete)
]

# urlpatterns = format_suffix_patterns(urlpattern