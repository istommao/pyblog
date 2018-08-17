"""server views."""
from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = 'front/index.html'


class ArticleDetailView(TemplateView):

    template_name = 'front/detail.html'


class ColumnListView(TemplateView):

    template_name = 'front/column/index.html'


class CollectorListView(TemplateView):

    template_name = 'front/collector/index.html'


class CodeSnippetListView(TemplateView):

    template_name = 'front/codesnippet/index.html'
