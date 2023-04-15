from django import forms
from .models import Uploaded_Image

class UploadForm(forms.ModelForm):
    class meta:
        model = Uploaded_Image
        fields = ['uploaded_image']