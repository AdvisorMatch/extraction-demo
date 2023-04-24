from django.urls import path
from . import views

urlpatterns = [
    path("extract/", views.extract, name='extract'),
    path("", views.list_works, name='work_list'),
    path("<int:id>/", views.work_detail, name='work_detail'),
]
