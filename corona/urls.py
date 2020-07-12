from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='sourav'),
    path('em',views.em,name='email'),
    path('aff',views.aff,name='aff'),
    path('subb',views.subb,name='subb'),
    path('cng',views.cng,name='cng'),
    path('cngp',views.cngp,name='cngp'),
]