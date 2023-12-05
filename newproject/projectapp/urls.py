from.import views
from django.urls import path

urlpatterns = [
    path('registers',views.registers,name='registers'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),

]