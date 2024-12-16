from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('uhome',views.uhome,name="uhome"),
    path('profile',views.profile,name="profile"),
    path('adprofile',views.adprofile,name="adprofile"),
    path('adlog',views.adlog,name="adlog"),
    path('drlog',views.drlog,name="drlog"),
    path('drreg',views.drreg,name="drreg"),
    path('adhome',views.adhome,name="adhome"),
    path('drhome',views.drhome,name="drhome"),
    path('drprofile',views.drprofile,name="drprofile"),
    path('drbooking',views.drbooking,name="drbooking"),
    path('cabhome',views.cabhome,name="cabhome"),
    path('About',views.About,name="About"),
]