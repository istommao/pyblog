"""app urls."""
from django.urls import path

from app import views

app_name = 'app'


urlpatterns = [
    path('detail/<str:uid>/', views.ArticleDetailView.as_view(), name='app_detail_view'),
]
