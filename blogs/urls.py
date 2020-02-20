"""learn URL Configuration

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

from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_view_list, name='blog_list'),
    path('<int:objid>/', blog_detail_view),
    path('new/', blog_create_view, name='blog_new'),
    path('<int:myid>/update/',blog_update_view, name = 'blog_update'),
    path('<int:myid>/delete/', blog_delete_view, name = 'blog_delete')
]
