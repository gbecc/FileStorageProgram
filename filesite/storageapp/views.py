from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UploadForm
from .models import Document
from django.utils.encoding import smart_str
import mimetypes

@login_required
def dashboard(request):
    q = request.GET.get("q", "").strip()
    docs = Document.objects.filter(owner=request.user)
    if q:
        docs = docs.filter(Q(original_name__icontains=q) | Q(description__icontains=q))
    return render(request, "storage/dashboard.html", {"docs": docs, "q": q})

@login_required
def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            up = form.cleaned_data["file"]
            doc = form.save(commit=False)
            doc.owner = request.user
            doc.original_name = up.name
            doc.size_bytes = up.size
            doc.content_type = getattr(up, "content_type", "")
            doc.save()
            return redirect("dashboard")
    else:
        form = UploadForm()
    return render(request, "storage/upload.html", {"form": form})

@login_required
def file_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.owner_id != request.user.id:
        return HttpResponseForbidden("Not yours.")
    return render(request, "storage/detail.html", {"doc": doc})

@login_required
def download_file(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.owner_id != request.user.id:
        return HttpResponseForbidden("Not yours.")
    response = FileResponse(doc.file.open("rb"), as_attachment=True, filename=doc.original_name)
    if doc.content_type:
        response["Content-Type"] = doc.content_type
    return response

@login_required
def delete_file(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.owner_id != request.user.id:
        return HttpResponseForbidden("Not yours.")
    if request.method == "POST":
        doc.file.delete(save=False)
        doc.delete()
        return redirect("dashboard")
    return render(request, "storage/confirm_delete.html", {"doc": doc})

@login_required
def preview_file(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    if doc.owner_id != request.user.id:
        return HttpResponseForbidden("Not yours.")

    # Figure out content type
    ctype = doc.content_type or mimetypes.guess_type(doc.file.name)[0] or ""
    # Load small text previews into memory (avoid unecessarily huge reads)
    text_preview = None
    if ctype.startswith("text/"):
        with doc.file.open("rb") as fh:
            text_preview = fh.read(200_000).decode("utf-8", errors="replace")

    ctx = {"doc": doc, "ctype": ctype, "text_preview": text_preview}
    return render(request, "storage/preview.html", ctx)

def logout_get(request):
    logout(request)
    return redirect("login")