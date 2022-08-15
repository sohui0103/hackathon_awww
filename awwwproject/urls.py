from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import awww.views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', awww.views.home, name='home'),
    path('awww/', include('awww.urls')),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

    path('accounts/', include('allauth.urls')),

    # path('', include('socialShare.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
