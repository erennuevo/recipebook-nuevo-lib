from django import forms
from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['recipe_image', 'description']
