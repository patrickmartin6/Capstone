from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'), #creating the views for the website, which refrences the index and attaches the url to be just the standard for the notifications tab
    path('about/',views.about, name='about'),
    path('registration/',views.registration, name='registration'),#creating the view and url extension for the help page
    path('websocket/',views.websocket, name='websocket'),#creating the view and url extension for the websocket test page
    path('passwordreset/',views.passwordreset, name='passwordreset')#creating the view and url extension for the passwordreset
]