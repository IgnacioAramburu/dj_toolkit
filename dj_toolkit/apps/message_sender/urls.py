from django.urls import path
from . import views

urlpatterns=[
    path("",views.message_sender,name="message_sender")
]