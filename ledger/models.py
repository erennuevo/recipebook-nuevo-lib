"""
Defines Ingredient, Recipe, and RecipeIngredient models.
"""

from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    """Model for an ingredient with name field."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Returns the URL to access the detail view of this ingredient."""
        return reverse('ledger:ingredient_detail', args=[str(self.pk)])

class Recipe(models.Model):
    """Model for a recipe with name field."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Returns the URL to access the detail view of this recipe."""
        return reverse('ledger:recipe_detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    """Model for a recipe ingredient, with quantity and keys to a recipe and ingredient."""
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
