from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import signUp,signUpEntre,signUp1,signUp2, firstPage,profile, messaging, metting, joinMetting, mettingPage, network, logincheck, like,classroom,get_comment,addFriend,signUpStud,search,formProfile,accept_request,reject_request, showCommentForm, addComment,create_cours,ouvrir_pdf, rejoindre_cours, detail_cours,get_posts,add_post,deletePost,ouvrir_pdf,delete_experience,delete_education,delete_skill,delete_language,formEducation,formExperience,roomCreateForm,searchRoom,rejoindre_cours, detail_cours,get_posts,add_post,deletePost,students_page,mes_cours,create_cours,getMessages,messageForm,travaux_et_devoir,creer_devoir,creer_documentation,quitterRoom,members,chat,searchPage,accueil


app_name = "PNP"

urlpatterns = [
    path("", firstPage , name='firstPage'),

    # registration
    path("", include("django.contrib.auth.urls")),
    path('signUp/', signUp1, name='signUp'),
    path('signUpEntre/', signUpEntre, name='signUpEntre'),
    path('signUpStud/', signUpStud, name='signUpStud'),
    path('signUp1/<int:choix>', signUp, name='signUp1'),
    path('signUp2/', signUp2, name='signUp2'),
    path('logincheck/', logincheck, name='logincheck'),

    # first page after login
    path('firstPage/', firstPage , name='firstPage'),

    # messaging page
    path('messaging/', messaging , name='messaging'),
    path('roomCreateForm/<int:type>/<int:id>/', roomCreateForm , name='roomCreateForm'),
    path('searchRoom/<str:roomname>/', searchRoom , name='searchRoom'),
    path('getMessages/<int:id>/', getMessages , name='getMessages'),
    path('messageForm/<int:id>/', messageForm , name='messageForm'),
    path('quitterRoom/<int:id>/', quitterRoom , name='quitterRoom'),
    path('members/<int:id>/', members , name='members'),
    
    # metting pages
    path('mettingPage/', mettingPage , name='mettingPage'), # metting choix page
    path('metting/', metting , name='metting'), # metting create page
    path('joinMetting/', joinMetting , name='joinMetting'), # metting join page

    # profile page
    path('profile/<str:username>/', profile , name='profile'),
    path('formProfile/<int:id>/<str:username>/', formProfile , name='formProfile'),
    path('delete_experience/<int:id>/<str:username>/', delete_experience , name='delete_experience'),
    path('delete_education/<int:id>/<str:username>/', delete_education , name='delete_education'),
    path('delete_skill/<str:id>/<str:username>/', delete_skill , name='delete_skill'),
    path('delete_language/<str:id>/<str:username>/', delete_language , name='delete_language'),
    path('formEducation/<int:id>/<str:username>/', formEducation , name='formEducation'),
    path('formExperience/<int:id>/<str:username>/', formExperience , name='formExperience'),
    path('chat/<str:username>/', chat , name='chat'),

    # clasroom page
    path('classroom/', classroom , name='classroom'),
    path('classroom/accueil/', accueil, name='accueil'),
     #createcourse
    path('classroom/create/', create_cours, name='create_cours'),
    path('ouvrir_pdf/', ouvrir_pdf, name='ouvrir_pdf'),
    
   
    path('rejoindre-cours/', rejoindre_cours, name='rejoindre_cours'),
    path('detail-cours/<int:cours_id>/', detail_cours, name='detail_cours'),
    # networking
    path('network/', network, name='network'),

    #friends
    path('addFriend/<str:friend>/', addFriend, name='addFriend'),
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

   path('classroom/detail_cours/<str:code>/travaux_et_devoir/', travaux_et_devoir, name='travaux_et_devoir'),
   path('classroom/detail_cours/<str:code>/travaux_et_devoir/creer/devoir/', creer_devoir, name='creer_devoir'),
   path('classroom/detail_cours/<str:code>/travaux_et_devoir/creer/documentation/', creer_documentation, name='creer_documentation'),
    #search
    path('search/<str:username>/<int:type>/', search , name='search'),

    #search Page
    path('searchPage/', searchPage , name='searchPage'),
] + static(settings.STATIC_URL)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(settings.MEDIA_ROOT)