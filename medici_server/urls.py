"""medici_server URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import os
import configparser
medici_config = configparser.ConfigParser()
medici_config.read(os.path.join(settings.BASE_DIR, 'medici_system/system/medici_config/medici.ini'))

MEDICI_SYSTEM_URL = medici_config['communication']['medici_system_url']

urlpatterns = [
    path('admin', admin.site.urls),
    path(MEDICI_SYSTEM_URL, include('medici_system.urls')),
    path('', include('medici_website.urls')),
]
