"""app admin."""
from django import forms
from django.contrib import admin

from app.models import Article, Column


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    """ColumnAdmin"""

    list_display = ('uid', 'name', 'creation_time')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ArticleAdmin."""

    list_display = ('uid', 'title', 'creation_time')

    search_fields = ('title', 'uid')


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     """NewsAdmin."""

#     list_display = ('uid', 'title', 'creation_time')

#     search_fields = ('title', 'uid')
