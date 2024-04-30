from django.urls import path
from . import views
from django.http import HttpResponse
from django.template import loader

urlpatterns = [
    path('instructions/', views.instructions_view, name='instructions'),
]

def members(request):
  template = loader.get_template('instructions.html')
  return HttpResponse(template.render())
