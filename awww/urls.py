from django.urls import path
from awww import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('musictalk/', views.musictalk, name='musictalk'),
    path('new/', views.new, name='new'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create_comment/<int:blog_id>',
         views.create_comment, name='create_comment'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),


    path('userplaylist/', views.userplaylist, name='userplaylist'),
    path('makeplaylist/', views.makeplaylist, name='makeplaylist'),

    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blogpost_like"),

    # path('', include('socialShare.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
