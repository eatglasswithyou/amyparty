from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("security", views.all_attendees, name="security"),
    path("thanks", views.thanks, name="thanks")
    ]