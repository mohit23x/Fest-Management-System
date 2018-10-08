from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#localhost/v/
urlpatterns = [

    path('maindashboard', views.maindashboard, name='maindashboard'),
    path('logout', auth_views.logout, name='logout'),
    path('allevents', views.allevents, name='allevents'),
    path('addevent', views.addevent, name='addevent'),
    path('addcoordin', views.addcoordin, name='addcoordin'),
    path('allcoordinators', views.allcoordinators, name='allcoordinators'),
    path('addcoordinators', views.addcoordinator.as_view(), name='addcoordinators'),
    path('eventdelete/<int:pk>', views.eventdelete, name='eventdelete'),
    path('addcoordinatortoevennt/<int:pk>', views.addcoordinatortoevennt, name='addcoordinatortoevennt'),
    path('sponsers', views.sponsers, name='sponsers'),
    path('addsponser', views.addsponser, name='addsponser'),
    path('positive/<int:pk>', views.positive, name='positive'),
    path('negative/<int:pk>', views.negative, name='negative'),
    path('final/<int:pk>', views.final, name='final'),
    path('removesponser/<int:pk>', views.removesponser, name='removesponser')
]