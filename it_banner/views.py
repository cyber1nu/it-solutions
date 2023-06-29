from django.http import FileResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormMixin

from it_banner.forms import QueryModelForm
from it_banner.models import QueryModel
from it_banner.utils import make_banner, logger


class IndexView(FormMixin, View):
    """ index page for getting video-banner (scrolling text from left to right) """
    form_class = QueryModelForm

    def get(self, request):
        some_text = request.GET.get('query')
        if some_text is not None:
            logger.info(f'Введен запрос: {some_text}')
            QueryModel.objects.create(query=some_text)
            make_banner(some_text)
            return FileResponse(open('it_banner/media/wgite1.mp4', 'rb'))
        return render(request, 'index.html', context={'form': self.form_class})
