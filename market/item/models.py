from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self) -> str:
        return self.name
