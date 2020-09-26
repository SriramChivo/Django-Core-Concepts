"""CoreConcepts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from CoreApp.views import coreApp, tempalebasedview
from django.views.generic.base import TemplateView
from classBasedCoreApp.views import functionForm, loginCreateView, loginListView, loginDetailView, loginformview, loginupdateview, projectForm, tempview
# from django.views.generic.base.ContextMixin import extra_context
from usermodel.views import register, usercreation, ExtendedUser, create, get

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('First/', first),
    re_path(r'^view/(?P<id>\d+)/$', coreApp),
    re_path(r'^update/(?P<id>\d+)/$', coreApp),
    re_path(r'^delete/(?P<id>\d+)/$', coreApp),
    path('chck/', create, name='create1'),
    path('get/', get, name='get'),
    path('register/', register.as_view(), name='register'),
    path('create/', coreApp),
    path('crtform/', functionForm),
    path('home/', coreApp),
    path('One/', ExtendedUser),
    path('classview/', tempalebasedview.as_view()),
    path('temp/', tempview.as_view()),
    path('usercr/', usercreation.as_view()),
    path('classview2/',
         TemplateView.as_view(template_name='CoreApp/aboutnormalClassview.html')),  # extra_context={'title': 'Custom Title'} valid in update django 2.0 and above
    # path('update/', coreApp),
    # (?P<name>pattern) we Should use re_path()
    # re_path(r'^create/(?P<id>\d+)/$', create)
    path('createview/', loginCreateView.as_view(), name='createviewsss'),
    path('formview/', loginformview.as_view()),
    path('listview/', loginListView.as_view(), name='listview'),
    path('formproj/', projectForm.as_view()),
    re_path(r'^listview/(?P<pk>\w+)/$',
            loginDetailView.as_view(), name='detailView'),
    re_path(r'^listview/edit/(?P<pk>\w+)/$',
            loginupdateview.as_view(), name='updateview'),
]
