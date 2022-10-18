from django.db import models
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(verbose_name="нНзва", max_length=255, blank=True, null=True),
        description=models.TextField(verbose_name="Опис", blank=True, null=True),
        content=HTMLField(verbose_name="Контент", blank=True, null=True),
        slug=models.SlugField(default='', blank=True, null=True, unique=True)
    )
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(User, verbose_name="автор",
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True)
    image = models.FileField(upload_to='images', default='', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост блога"
        verbose_name_plural = "Пости блога"


class HomePage(models.Model):
    pass

    class Meta:
        verbose_name = 'домашня сторінка'
        verbose_name_plural = 'домашня сторінка'

    def __str__(self):
        str_uk = 'Редагувати домашню сторінку (українська мова)'
        str_ru = 'Редагувати домашню сторінку (російська мова)'
        return mark_safe(f'<p><a href={reverse_lazy("admin:home")}?locale=uk>{str_uk}</a></p>'
                         f'<p><a href={reverse_lazy("admin:home")}?locale=ru>{str_ru}</a></p>')
