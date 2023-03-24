from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from webapp.forms import ArticleForm
from webapp.models import Article
from webapp.models.articles import StatusChoice


class ArticleDetail(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs['pk'])
        return context


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices, 'form': form})
    form = ArticleForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices, 'form': form})
    else:
        article = form.save()
        return redirect('article_detail', pk=article.pk)


class ArticleUpdateView(TemplateView):
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs['pk'])
        context['form'] = ArticleForm(instance=context['article'])
        return context

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
        return render(request, 'article_update.html',
                      context={'form': form, 'article': article})


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'article': article})


def confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')
