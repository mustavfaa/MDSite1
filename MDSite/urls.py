

from django.urls import path
from . import views

urlpatterns = [

    path("",views.MDSiteView.as_view(),name="index"),
   	path('register/',views.registerPage,name="register"),
   	path('login/',views.loginPage,name="login"),
   	path('logout/',views.logoutUser,name="logout"),
   	path('account/', views.accountSettings, name="account"),
    path("<slug:slug>/", views.post_detail ,name="base"),
    path("category/<int:id>/<slug:slug>/", views.category_alle,name="category_alle"),
    path('user/', views.userPage, name="user-page"),
    
   ]

