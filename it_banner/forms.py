from django.forms import ModelForm

from it_banner.models import QueryModel


class QueryModelForm(ModelForm):
    """form to get query text for video-banner """
    class Meta:
        model = QueryModel
        fields = ['query']
