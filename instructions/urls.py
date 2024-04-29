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

# above is used to render what is inside the html and then transfer used the data from python
# back into the work branch of django and back into print out in webpage.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]

