from django.urls import path, include
from .views import loginRed,signUp,signUpEntre,signUp1,signUp2, firstPage,profile, messaging, room, metting, joinMetting, mettingPage, network, logincheck, like,classroom,get_comment,addFriend,signUpStud,search,formProfile,accept_request,reject_request, showCommentForm, addComment
from django.conf import settings
from django.conf.urls.static import static

app_name = "PNP"

urlpatterns = [
    path("", loginRed , name='loginRed'),
    # registration
    path('signUp/', signUp1, name='signUp'),
    path('signUpEntre/', signUpEntre, name='signUpEntre'),
    path('signUpStud/', signUpStud, name='signUpStud'),
    path('signUp1/<int:choix>', signUp, name='signUp1'),
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
    path('formProfile/<int:id>/<str:username>/', formProfile , name='formProfile'),
    # clasroom page
    path('classroom/', classroom , name='classroom'),
    # networking
    path('network/', network, name='network'),

    #friends
    path('addFriend/<str:username>', addFriend, name='addFriend'),
    path('accept_request/<str:username>', accept_request , name='accept_request'),
    path('reject_request/<str:username>', reject_request , name='reject_request'),
    #post like
    path('like/<int:postid>/', like , name='like'),
    path('showCommentForm/<int:itemid>/<int:type>/', showCommentForm , name='showCommentForm'),
    path('comment/<int:itemid>/', get_comment , name='comment'),
    path('addComment/<int:itemid>/<int:type>/', addComment , name='addComment'),

    #search
    path('search/<str:username>/', search , name='search'),
] + static(settings.STATIC_URL)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)