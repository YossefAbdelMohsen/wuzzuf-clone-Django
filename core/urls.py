from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home" ),
    path('logout',views.logout,name="logout" ),
    path('register',views.register,name="register" ),
    path('explore',views.explore,name="explore" ),
    path('company-signup',views.company_signup,name="company-signUp" ),
    path('dashboard',views.dashboard,name="dashboard" ),
]
