"""
Django views that contain the contexts for each page.
"""

from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm, ImageForm
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    """
    View function for displaying a list of recipes.
    """
    recipes = Recipe.objects.all()

    ctx = {
        'recipes': recipes,
    }
    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe_detail(request, id):
    """
    View function for displaying the details of a recipe.
    """
    ctx = {
        'recipe': Recipe.objects.get(id=id)
    }
    return render(request, 'recipe_detail.html', ctx)


@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.author = request.user
            recipe.save()
            return redirect('ledger:recipe_detail', id=recipe.id)
    ctx = {
        'form': form
    }
    return render(request, 'recipe_form.html', ctx)


@login_required
def add_image(request, id):

    recipe = Recipe.objects.get(id=id)

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_detail', id=recipe.id)
    ctx = {
        'form': form
    }
    return render(request, 'recipe_image.html', ctx)
