from django.contrib import admin

from .models import Fruit, Vitamin


# Define the admin class
class FruitAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image") # Displaying these fields in the admin list view
    search_fields = ("name", "vitamins") # Allowing searching by name or vitamins
    list_filter = ("price",) # Adding a filter sidebar for price


# Register the model and the admin class.
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Vitamin)