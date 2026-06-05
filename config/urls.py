"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static 


from django.conf.urls.i18n import i18n_patterns  # for multi languages


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # language switch endpoint
]


# for multi languages 
urlpatterns += i18n_patterns(
    path('dj-admin/', admin.site.urls),
    path('admin/', include('accounts.urls')),
    path('', include('core.urls')),
    path('', include('about_us.urls')),
    path('', include('accounts.urls')),
    path('', include('admin_panel.urls')),
    path('', include('contact.urls')),
    path('', include('rider.urls')),
    path('', include('service.urls')),
    path('', include('translation.urls')),
    path('', include('vendor.urls')),
)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('core.urls')),
#     path('', include('about_us.urls')),
#     path('', include('accounts.urls')),
#     path('', include('admin_panel.urls')),
#     path('', include('contact.urls')),
#     path('', include('rider.urls')),
#     path('', include('service.urls')),
#     path('', include('translation.urls')),
#     path('', include('vendor.urls')),
# ]


#for media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    