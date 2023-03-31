from django.urls import path
from calculator.views import recipe_info

urlpatterns = [
    path("<_recipe>/", recipe_info)
]
