from django.urls import path

from webapp.views.articles import add_view, delete_view, confirm_delete, ArticleDetail, ArticleUpdateView
from webapp.views.base import IndexView, IndexRedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/', IndexRedirectView.as_view(), name='articles_index_redirect'),
    path('article/add/', add_view, name='article_add'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete', delete_view, name='article_delete'),
    path('article/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete'),
]
