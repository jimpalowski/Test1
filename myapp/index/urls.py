from django.conf.urls import url
from . import views


#def index(request):
    #print ("testing")



urlpatterns =[
    url(r'^$', views.index)
]