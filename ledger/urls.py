from django.urls import path
from .views import index, recipes

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipes, name="recipes"),
]

app_name = "ledger"