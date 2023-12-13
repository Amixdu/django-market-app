from django.urls import path

from . import views

app_name = "conversation"
urlpatterns = [
    path("", views.conversations, name="conversations"),
    path("<int:id>", views.conversation, name="conversation"),
    path("create/<int:item_id>/", views.create, name="create"),
]
