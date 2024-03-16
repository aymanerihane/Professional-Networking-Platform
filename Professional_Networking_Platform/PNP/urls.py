from django.urls import path, include
from .views import index, signUp,signUp2, firstPage,profile, messaging, room, metting, joinMetting, mettingPage, network
from django.conf import settings
from django.conf.urls.static import static

app_name = "PNP"

urlpatterns = [
    path('', index, name='index'),
    # registration
    path('signUp/', signUp, name='signUp'),
    path('signUp2/', signUp2, name='signUp2'),
    path("accounts/", include("django.contrib.auth.urls")),
    # first page after login
    path('firstPage/', firstPage , name='firstPage'),
    # messaging page
    path('messaging/', messaging , name='messaging'),
    # metting pages
    path('mettingPage/', mettingPage , name='mettingPage'), # metting choix page
    path('metting/', metting , name='metting'), # metting create page
    path('joinMetting/', joinMetting , name='joinMetting'), # metting join page
    # profile page
    path('profile/', profile , name='profile'),
    # networking
    path('network/', network, name='network'),

    # path('', views.index, name='indexOfManglib'),
    # path('room/<int:room_id>/', room, name='room')
] + static(settings.STATIC_URL)