from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import include
from django.conf.urls import url

app_name = 'users'
urlpatterns = [
    path('register/', user_views.register, name='register'),
    #path('profile/', user_views.profile, name ='view_profile'),
    url(r'^profile/$', user_views.view_profile, name = 'view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', user_views.view_profile, name='view_profile_with_pk'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('chat.urls')),
]