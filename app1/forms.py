from .models import Item, FileUpload
from django import forms

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file','item', ]