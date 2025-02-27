"""
Django views that contain the contexts for each page.
"""

from django.shortcuts import render

def recipes(request):
    """View function for displaying a list of recipes."""
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {"name": "tomato", "quantity": "3pcs"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "pork", "quantity": "1kg"},
                    {"name": "water", "quantity": "1L"},
                    {"name": "sinigang mix", "quantity": "1 packet"}
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {"name": "garlic", "quantity": "1 head"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "vinegar", "quantity": "1/2 cup"},
                    {"name": "water", "quantity": "1 cup"},
                    {"name": "salt", "quantity": "1 tablespoon"},
                    {"name": "whole black peppers", "quantity": "1 tablespoon"},
                    {"name": "pork", "quantity": "1 kilo"}
                ],
                "link": "/recipe/2"
            }
        ]
    }
    return render(request, "recipes.html", ctx)

def recipe1(request):
    """View function for displaying details of Recipe 1."""
    ctx = {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ],
        "link": "/recipe/1"
    }
    return render(request, "recipe.html", ctx)

def recipe2(request):
    """View function for displaying details of Recipe 2."""
    ctx = {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "vinegar", "quantity": "1/2 cup"},
            {"name": "water", "quantity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilo"}
        ],
        "link": "/recipe/2"
    }
    return render(request, "recipe.html", ctx)
