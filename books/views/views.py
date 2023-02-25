from django.http import Http404
from django.shortcuts import render
from django.views import View

from books.helper import IsStaffPerm
from books.models import Artist


class BaseRender(View):
    template_name = None

    def render_response(self, context=None):
        if not context:
            context = {}
        assert self.template_name, 'необходимо задать шаблон'
        return render(self.request, self.template_name, context=context)


class IndexView(IsStaffPerm, BaseRender):
    template_name = 'index.html'

    def get(self, request):
        return self.render_response()


class ArtistListView(BaseRender):
    template_name = 'artist_list.html'

    def get(self, request):
        try:
            artist = Artist.objects.all()
        except ValueError:
            return f'ошибка получения данных'
        return self.render_response(context={'ar': artist})


class ArtistDetailView(BaseRender):
    template_name = 'artist_detail.html'

    def get(self, request, pk):
        try:
            artist = Artist.objects.filter(pk=pk)
            if not artist.exists():
                raise Http404
        except ValueError:
            return f'ошибка'
        return self.render_response(context={'ar': artist})
