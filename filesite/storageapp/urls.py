from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("upload/", views.upload_file, name="upload_file"),
    path("file/<int:pk>/", views.file_detail, name="file_detail"),
    path("file/<int:pk>/download/", views.download_file, name="download_file"),
    path("file/<int:pk>/delete/", views.delete_file, name="delete_file"),
    path("file/<int:pk>/preview/", views.preview_file, name="preview_file"),
]
