from django.urls import path
from . import views
urlpatterns = [
    path('home', views.index),
    path('learnmore', views.learnpage),
    path('veryniceprod', views.clothingpage),
    path('static/css/images/resume.pdf', views.resumepage),
    path('createmessage', views.createmess),
    path('veryniceproducts', views.cspage),
    # path('', views.displaymessages),
]
