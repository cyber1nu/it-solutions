from django import forms

from it_banner.models import QueryModel


class QueryModelForm(forms.ModelForm):
    """form to get query text for video-banner """
    query = forms.CharField(widget=forms.Textarea(attrs={'width': '150px', 'height': '70px', 'resize': 'none'}))

    class Meta:
        model = QueryModel
        fields = ['query']

