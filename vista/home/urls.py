from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('login.html',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('uhome',views.uhome,name="uhome"),
    path('profile',views.profile,name="profile"),
    path('adprofile',views.adprofile,name="adprofile"),
    path('adlog',views.adlog,name="adlog"),
    path('drlog',views.drlog,name="drlog"),
    # path('drlog',views.drlog,name="rentlog"),
    path('drreg',views.drreg,name="drreg"),
    path('adhome',views.adhome,name="adhome"),
    path('drhome',views.drhome,name="drhome"),
    path('drprofile',views.drprofile,name="drprofile"),
    path('drbooking',views.drbooking,name="drbooking"),
    path('cabhome',views.cabhome,name="cabhome"),
    path('About',views.About,name="About"),
    path('cabprofile',views.cabprofile,name="cabprofile"),

    path('rentlog',views.rentlog,name="rentlog"),
    path('index.html', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('hotel.html', views.hotel, name='hotel'),
    path('single.html', views.single, name='single'),
    path('hotelsingle.html', views.hotelsingle, name='hotelsingle'),
    path('user.html', views.user, name='user'),
    path('drive.html', views.drive, name='drive'),
    path('drreg', views.drreg, name='drreg'),
    path('hotelreg.html', views.hotelreg, name='hotelreg'),
    path('reshotel.html', views.reshotel, name='reshotel'),
    path('driver.html', views.driver, name='driver'),



    # ****************************admin************************
    path('signin/', views.signin, name='signin'),
    # path('adlog',views.adlog,name="adlog"),
    path('adhome',views.adhome,name="adhome"),
    path('adprofile',views.adprofile,name="adprofile"),
    path('transport',views.transport,name="transport"),
    path('chart',views.chart,name="chart"),
    path('restaurants',views.restaurants,name="restaurants"),
    path('hotels',views.hotels,name="hotels"),


    path('rentreg',views.rentreg,name="rentreg"),
    path('renthome',views.renthome,name="renthome"),
    path('rentlog',views.rentlog,name="rentlog"),
    path('rentprofile',views.rentprofile,name="rentprofile"),
]
