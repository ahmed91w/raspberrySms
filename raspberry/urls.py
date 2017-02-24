"""raspberry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from raspberry_app.views import *
from  django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^show/(?P<id>[-\w]+)$', showUser),


    url(r'^index/$', index, name="index"),
    url(r'^login/$', loginView, name="login"),
    url(r'^logout/$', costum_logout, name="logout"),
    url(r'^login_check/$', login_check, name="authentication"),
    url(r'^register/$', register_view, name="register"),
    url(r'^register_check/$', login_check, name="register_check"),
    url(r'^registeration_activation/$', login_check, name="ractivation"),
    url(r'^composeur/$', composeur, name="composeur"),
    url(r'^profile/', profil, name="profile"),
    url(r'^edit_profil/$', edit_profil_view, name="edit_profil"),
    url(r'^profil_update/$', profil_update, name="profil_update"),
    url(r'^edit_password/$', edit_password, name="edit_password"),
    url(r'^sendSMS/$', sendSMS, name='sendSMS'),
    url(r'^addContact/$', addContact, name='addContact'),
    url(r'^newContact/$', newContact, name='newContact'),
    url(r'^editContact/(?P<id>[^/]+)/$', editContact, name='editContact'),
    url(r'^updateContact/$', updateContact, name='updateContact'),
    url(r'^removeContact/(?P<id>[^/]+)/$', removeContact, name='removeContact'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^conversation/(?P<contact_num>[^/]+)/$', conversation, name="conversation"),
    url(r'^goToConversation/(?P<contact_num>[^/]+)/$', goToConversation, name="goToConversation"),
    url(r'^removeMsg/(?P<id>[^/]+)/$', removeMsg, name="removeMsg"),
    url(r'^addMsg/(?P<id_contact>[^/]+)/$', addMsg, name="addMsg"),
    url(r'^messages/$', messages, name="messages"),
    url(r'^deleteAllMessages/$', deleteAllMessages, name="deleteAllMessages"),

]
