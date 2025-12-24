from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.get_item, name='item')
]
