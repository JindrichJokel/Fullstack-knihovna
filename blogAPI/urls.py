from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogAPI import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)