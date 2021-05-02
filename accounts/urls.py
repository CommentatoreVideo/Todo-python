from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import registrazioneView

app_name = 'accounts'
urlpatterns = [
    path('registrazione/', registrazioneView, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('user/<username>/', views.userProfileView, name="user_profile"),
]