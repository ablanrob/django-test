from django.conf.urls import url, include
from basic_app import views

# Template tagging
app_name = 'basic_app'

# Url patterns
urlpatterns = [
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^other/$', views.other,name='other'),
]
