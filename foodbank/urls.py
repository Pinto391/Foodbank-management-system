
from django.contrib import admin
from django.urls import path, include
from post import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from material.admin.sites import site


site.site_header = _('Food Bank Administration')
site.site_title = _('Online Food Bank Management System')
site.profile_name=('Almas Ali Pinto')

# site.profile_picture = staticfiles('path/to/image')
# site.profile_bg = staticfiles('path/to/image')
# site.login_logo = staticfiles('path/to/image')
# site.logout_bg = staticfiles('path/to/image')


urlpatterns = [
    
    path('', views.home, name='home'),
    path('account/', include('account.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('ngo/', include('ngo.urls')),
    path('admin/', include('material.admin.urls')),
]


urlpatterns += staticfiles_urlpatterns()