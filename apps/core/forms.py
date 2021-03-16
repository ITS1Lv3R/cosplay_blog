from django import forms


class ImageUploadForm(forms.Form):
    images = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))