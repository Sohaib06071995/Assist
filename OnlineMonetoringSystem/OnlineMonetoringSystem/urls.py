"""OnlineMonetoringSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from Activity import views
from Dictionary import views
from UserAccount import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.login_redirect,name='login_redirect'),
    url(r'^action/',include('Dictionary.urls')),
    url(r'^activities/',include('Activity.urls')),
    # url(r'^dictionary/',include('Dictionary.urls')),
    url(r'^account/',include('UserAccount.urls')),
    url(r'^select2/', include('select2.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = _("Assit Administration")
admin.site.site_title = _("Assist Site Admin")
