from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


# Create your models here.
class StatusChoice(TextChoices):
    ACTIVE = "active", "Активно"
    BLOCKED = "blocked", "Заблокировано"


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    author = models.CharField(
        max_length=50,
        null=False,
        blank=True,
        verbose_name="Автор"
    )
    text = models.TextField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Текст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    status = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=StatusChoice.choices,
        default=StatusChoice.ACTIVE,
        verbose_name="Статус"
    )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None
    )
    tags = models.ManyToManyField(
        to='webapp.Tag',
        related_name='articles',
        default=None
    )

    def __str__(self):
        return f"{self.author} - {self.title}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
