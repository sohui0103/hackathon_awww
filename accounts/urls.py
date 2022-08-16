from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),

    path('mypage/', views.mypage, name='mypage'),

    #마이페이지
    # path('mypage/', views.userinfo, name='mypage'),
    # path('userpage/<str:writer>', views.user_select_info, name='userpage'),
    # path('profile_update', views.ProfileUpdateView.as_view(), name='profile_update'),
]