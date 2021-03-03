from django import forms
from .models import ImageComment


class AddCommentForm(forms.ModelForm):
    """Форма добавления комментария"""

    class Meta:
        model = ImageComment
        fields = ('text',)





