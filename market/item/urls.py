from django.urls import path

from . import views

app_name = "item"
urlpatterns = [
    path("", views.items, name="items"),
    path("<int:id>/", views.item, name="item"),
    path("create/", views.create, name="create"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/update/", views.update, name="update"),
]
