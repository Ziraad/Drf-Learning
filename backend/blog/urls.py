from django.urls import path
from .views import AtricleList, ArticleDetail

app_name = 'blog'

urlpatterns = [
    path('', AtricleList.as_view(), name='list'),
    path('<int:pk>', ArticleDetail.as_view(), name='detail'),
]
