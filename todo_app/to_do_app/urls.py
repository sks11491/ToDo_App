from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    url(r'^delete/(?P<pk>\d+)/$', views.PostDelete.as_view(),
        name='entry_delete')
]