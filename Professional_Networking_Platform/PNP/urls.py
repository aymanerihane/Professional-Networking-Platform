from django.urls import path, include
from .views import index, signUp, login, firstPage,profile, messaging
from django.conf import settings
from django.conf.urls.static import static

app_name = "PNP"

urlpatterns = [
    path('', index, name='index'),
    path('signUp/', signUp, name='signUp'),
    path('login/', login , name='login'),
    path('firstPage/', firstPage , name='firstPage'),
    path('messaging/', messaging , name='messaging'),
    path('profile/', profile , name='profile'),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('', views.index, name='indexOfManglib'),
    # path('sing/<int:manga_id>/', views.show, name='show')
] + static(settings.STATIC_URL)