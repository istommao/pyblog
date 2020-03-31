"""src views."""
from django.views.generic import TemplateView

from app import services



class IndexView(TemplateView):

    template_name = 'index.html'


class DetailView(TemplateView):

    template_name = 'detail.html'


class ArticleDetailView(TemplateView):
    """Article detail view."""

    view_name = 'article_detail'

    template_name = 'app/article_detail.html'

    def get_context_data(self, uid, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = {
            'article': services.get_article_object(uid)
        }
        context.update(dataset)
        return context
