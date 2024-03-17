from django.urls import path, include
from .views import loginRed,signUp,signUp2, firstPage,profile, messaging, room, metting, joinMetting, mettingPage, network, logincheck, like
from django.conf import settings
from django.conf.urls.static import static

app_name = "PNP"

urlpatterns = [
    path("", loginRed , name='loginRed'),
    # registration
    path('signUp/', signUp, name='signUp'),
    path('signUp2/', signUp2, name='signUp2'),
    path("", include("django.contrib.auth.urls")),
    path('logincheck/', logincheck, name='logincheck'),
    # first page after login
    path('firstPage/', firstPage , name='firstPage'),
    # messaging page
    path('messaging/', messaging , name='messaging'),
    # metting pages
    path('mettingPage/', mettingPage , name='mettingPage'), # metting choix page
    path('metting/', metting , name='metting'), # metting create page
    path('joinMetting/', joinMetting , name='joinMetting'), # metting join page
    # profile page
    path('profile/<str:username>/', profile , name='profile'),
    # networking
    path('network/', network, name='network'),

    #post like
    path('like/<int:postid>/', like , name='like'),
] + static(settings.STATIC_URL)