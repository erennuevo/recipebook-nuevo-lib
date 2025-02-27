"""
Django views that contain the contexts for each page.
"""

from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    """
    View function for displaying a list of recipes.
    """
    recipes = Recipe.objects.all()

    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, id):
    """
    View function for displaying the details of a recipe.
    """
    ctx = { 
        'recipe': Recipe.objects.get(id=id) 
    }
    return render(request, 'recipe_detail.html', ctx)
