from django.urls import path, include
from .views import loginRed,signUp,signUp2, firstPage,profile, messaging, room, metting, joinMetting, mettingPage, network, logincheck, like,classroom,comment
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
    # clasroom page
    path('classroom/', classroom , name='classroom'),
    # networking
    path('network/', network, name='network'),

    #post like
    path('like/<int:postid>/', like , name='like'),
    path('comment/<int:postid>/', comment , name='comment'),
] + static(settings.STATIC_URL)