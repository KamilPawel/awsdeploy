from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.TimeRecordCreateView.as_view()),
    path("RUD/", views.TimeRecordRUDView.as_view()),
]
