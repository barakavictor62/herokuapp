"""popeyeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from popeye import views
from popeye.forms import LoginForm, resetForm, PasswordChange
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset,{'template_name': 'password_reset.html','password_reset_form': resetForm}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name': 'popeye/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$',auth_views.password_reset_complete,{'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name='logout'),
    url(r'^password/$', auth_views.password_change,{'template_name':'password_change.html', 'password_change_form': PasswordChange}, name='password_change'),
    url(r'^password_change_done$', auth_views.password_change_done, name='password_change_done'),
    url(r'^myprofile$', views.myprofile),
    url(r'^signup$', views.signup),
    url(r'^edit_profile$', views.edit_profile),
    url(r'^mywallet$', views.mywallet),
    url(r'^pricing$', views.pricing),
    url(r'^passwordchange$', views.passwordchange),
    url(r'^articles$', views.articles),
    url(r'^web$', views.web),
    url(r'^contact$', views.contact),
    url(r'^edit_request$', views.edit_request),
    url(r'^articles_request$', views.articles_request),
    ]
