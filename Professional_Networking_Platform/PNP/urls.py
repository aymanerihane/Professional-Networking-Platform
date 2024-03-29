from django.urls import path, include
from .views import loginRed,signUp,signUpEntre,signUp1,signUp2, firstPage,profile, messaging, room, metting, joinMetting, mettingPage, network, logincheck, like,classroom,get_comment,addFriend,signUpStud,search,formProfile,accept_request,reject_request, showCommentForm, addComment,create_cours,ouvrir_pdf, rejoindre_cours, detail_cours,get_posts,add_post,deletePost,students_page,mes_cours
from django.conf import settings
from django.conf.urls.static import static


app_name = "PNP"

urlpatterns = [
    path("", firstPage , name='firstPage'),
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
     #createcourse
    path('classroom/create/', create_cours, name='create_cours'),
   
    path('rejoindre-cours/', rejoindre_cours, name='rejoindre_cours'),
    path('detail-cours/<int:cours_id>/', detail_cours, name='detail_cours'),
    # networking
    path('network/', network, name='network'),

    #friends
    path('addFriend/<str:username>', addFriend, name='addFriend'),
    path('accept_request/<str:username>', accept_request , name='accept_request'),
    path('reject_request/<str:username>', reject_request , name='reject_request'),
    
    #post
    path('posts/', get_posts , name='posts'),
    path('addPost/', add_post , name='addPost'),
    path('deletePost/<int:id>/', deletePost , name='deletePost'),
    path('like/<int:postid>/', like , name='like'),
    path('showCommentForm/<int:itemid>/<int:type>/', showCommentForm , name='showCommentForm'),
    path('comment/<int:itemid>/', get_comment , name='comment'),
    path('addComment/<int:itemid>/<int:type>/', addComment , name='addComment'),
    
    #pdf calendrier classroom
    #path('ouvrir-pdf/', ouvrir_pdf, name='ouvrir-pdf'),
    
    path('classroom/rejoindre_cours/', rejoindre_cours, name='rejoindre_cours'),  # Route pour rejoindre un cours
    path('classroom/detail_cours/<str:code>/', detail_cours, name='detail_cours'),
    path('classroom/detail_cours/<str:code>/students/', students_page, name='students_page'),
   
   path('mes_cours/', mes_cours, name='mes_cours'),
    #search
    path('search/<str:username>/', search , name='search'),
] + static(settings.STATIC_URL)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)