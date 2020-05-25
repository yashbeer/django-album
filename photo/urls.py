from django.urls import path

from . import views

urlpatterns = [
    path('<int:photoid>', views.fetch, name='fetch'),
]