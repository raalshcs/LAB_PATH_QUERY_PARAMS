from django.urls import path
from . import views

app_name="recommend"


urlpatterns = [
    path('',views.roundom,name='recommend')
]