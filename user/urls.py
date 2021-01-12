from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/<int:id>', views.change_password, name='change_password'),
    path('change_username/<int:id>', views.change_username, name='change_username'),

]
