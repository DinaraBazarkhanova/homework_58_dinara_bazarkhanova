from django.views.generic import TemplateView, RedirectView

from webapp.forms import ArticleForm
from webapp.models import Article


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.exclude(is_deleted=True)
        context['form'] = ArticleForm()
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
