from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def file_list(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploader/file_list.html', {'files': files})
