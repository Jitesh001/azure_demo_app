from django.shortcuts import render,redirect, HttpResponse
from .forms import FileUploadForm
from .models import FileUpload
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded file and associated item
            return HttpResponse("Succcessfully uploaded")
    else:
        form = FileUploadForm()

    context = {"form": form, 'files':FileUpload.objects.all()}
    return render(request, "app1/index.html", context)