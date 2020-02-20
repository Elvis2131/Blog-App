from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField( label = 'Blog Title')
    summary = forms.CharField()
    description = forms.CharField( widget = forms.Textarea(), required = False)
    active = forms.BooleanField(label = 'Show Article?', initial = True, required = False)
    class Meta:
        model = Blog
        fields = [
            'title',
            'summary',
            'description',
            'active'
        ]

