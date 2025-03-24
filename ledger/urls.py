'''
URL configuration for the ledger app.
'''

from django.urls import path, include
from .views import recipe_list, recipe_detail, add_recipe, add_image

urlpatterns = [
    path('list', recipe_list, name="recipe_list"),
    path('<int:id>/detail', recipe_detail, name="recipe_detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recipe/add', add_recipe, name="add_recipe"),
    path('recipe/<int:id>/add_image', add_image, name="add_image")
]

app_name = "ledger"
