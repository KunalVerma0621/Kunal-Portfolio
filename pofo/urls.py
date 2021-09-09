from django.urls import path
from . import views
urlpatterns=[
    path('landing/',views.landing),
    path('contact/',views.information),
]
