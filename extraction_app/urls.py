from django.urls import path
from . import views

urlpatterns = [
    path("extract/", views.extract),
    path("list/", views.list_works)
]
