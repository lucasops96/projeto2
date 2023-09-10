from django.urls import path

from . import views

app_name = 'landingpage'

urlpatterns=[
    path('',views.home, name='home'),
    path('page/coffee',views.coffee, name='coffee'),
    path('page/tea',views.tea, name='tea'),
    path('page/milk',views.milk, name='milk')
]