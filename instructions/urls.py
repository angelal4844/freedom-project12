from django.urls import path
from . import views

urlpatterns = [
    path('instructions/', views.instructions_view, name='instructions'),
]