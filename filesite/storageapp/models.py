from django.db import models
from django.conf import settings
from pathlib import Path
import uuid

def user_directory_path(instance, filename: str):
    # Store under media/user_<id>/<uuid>__original.ext
    ext = Path(filename).suffix
    return f"user_{instance.owner_id}/{uuid.uuid4()}__{Path(filename).name}"

class Document(models.Model):
    owner          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file           = models.FileField(upload_to=user_directory_path)
    original_name  = models.CharField(max_length=255)
    size_bytes     = models.BigIntegerField()
    content_type   = models.CharField(max_length=128, blank=True)
    uploaded_at    = models.DateTimeField(auto_now_add=True)
    description    = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.original_name} ({self.owner})"
