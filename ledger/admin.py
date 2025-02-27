from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

admin.site.register(Recipe, RecipeAdmin)
