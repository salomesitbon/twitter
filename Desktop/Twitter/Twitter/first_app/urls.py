from django.urls import include, path
from . import views

app_name= 'main_app'

urlpatterns = [
path('', views.index, name='index'),
path('profile/<int:user_id>/', views.profile, name='profile'),
path('profile/<int:user_id>/tweet/', views.create_tweet, name='create_tweet'),
]