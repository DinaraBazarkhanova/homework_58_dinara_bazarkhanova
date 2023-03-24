from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    # tags = form.MultipleChoiceField(required=True, queryset=Tag.objects.all())
    class Meta:
        model = Article
        fields = ('title', 'author', 'text', 'status', 'tags')
        labels = {
            'title': 'Заголовок статьи',
            'author': 'Автор',
            'text': 'Текст',
            'status': 'Статус',
            'tags': 'Теги'
        }

    def clean_name(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Имя должно быть длинее 2 символов')
        return title
