from django.urls import path
from .views import HomeListViev

urlpatterns=[
     path('',HomeListViev.as_view(),name='home'),
]