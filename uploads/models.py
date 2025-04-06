from django.db import models
from django_cryptography.fields import encrypt


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = encrypt(models.CharField(max_length=255, blank=True))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
