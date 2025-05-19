from django.urls import path

from pages import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('movies_list/', views.movies_list, name='movies_list'),
    path('movie/<int:pk>', views.movie_item, name='movie_detail'),
    path('series_list/', views.series_list, name='series_list'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
