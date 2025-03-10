'''
URL configuration for the ledger app.
'''

from django.urls import path, include
from .views import recipe_list, recipe_detail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('list', recipe_list, name="recipe_list"),
    path('<int:id>/detail', recipe_detail, name="recipe_detail"),
    path('accounts/', include('django.contrib.auth.urls')),
]

app_name = "ledger"
