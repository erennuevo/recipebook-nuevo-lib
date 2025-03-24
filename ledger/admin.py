from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
