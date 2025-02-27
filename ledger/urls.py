'''
URL configuration for the ledger app. 
'''

from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('list', recipe_list, name="recipe_list"),
    path('<int:id>/detail', recipe_detail, name="recipe_detail"),
]

app_name = "ledger"

