from django.urls import path,include
from . import views
urlpatterns = [

    
    path('signup/', views.signup,name='signup'),

    path('loging/', views.user_login,name='user_login'),
    path('logout/', views.user_logout,name='user_logout'),
    path('edit_profile', views.profile_edit,name='edit_profile'),
   
 
    path('profile/', views.profile,name='profile'),

    path('profile/edit/passwordchange', views.profile_edit_password_change,name='profile_edit_password_change'),
    path('profile/edit/pass_change', views.pass_change,name='pass_change'),
    
]

