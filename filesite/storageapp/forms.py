from django import forms
from django.conf import settings
from .models import Document

class UploadForm(forms.ModelForm):
    class Meta:
        model  = Document
        fields = ["file", "description"]
        widgets = {
            "description": forms.TextInput(attrs={"placeholder": "optional note"}),
        }

def clean_file(self):
    f = self.cleaned_data["file"]
    max_mb = getattr(settings, "MAX_UPLOAD_MB", 25)
    max_bytes = max_mb * 1024 * 1024
    if f.size > max_bytes:
        raise forms.ValidationError(f"File too large (>{max_mb}MB).")

    # Get the MIME type (may be missing depending on browser)
    content_type = getattr(f, "content_type", "") or ""
    allowed_prefixes = getattr(settings, "ALLOWED_MIME_PREFIXES", [])

    #If Django couldn't detect a type we just allow it
    if content_type and not any(content_type.startswith(p) for p in allowed_prefixes):
        raise forms.ValidationError(f"Unsupported file type: {content_type}")

    return f

