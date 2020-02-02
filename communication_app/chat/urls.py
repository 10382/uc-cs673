from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='chat-index'),
    path('<str:room_name>/', views.room, name='room'),
    url(r'^$', views.index, name='home'),
    path('<str:room_name>/<str:operation>/<str:pk>/', views.change_friends 
                                                    , name='change_friends')
    ]
 