from django.urls import path
from . import views

urlpatterns = [
    path("film_index/", views.FilmIndex.as_view(), name="filmovy_index"),
]