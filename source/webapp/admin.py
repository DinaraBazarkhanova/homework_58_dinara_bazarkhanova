from django.contrib import admin

from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'text']
    list_filter = ['id', 'title', 'status', 'text']
    search_fields = ['name', 'status']
    fields = ['title', 'status', 'text', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
