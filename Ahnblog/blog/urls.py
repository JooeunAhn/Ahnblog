from django.conf.urls import include, url
from blog import views

urlpatterns = [
       url(r'^$',views.index,name="index"),
       url(r'^posts/$',views.post_list,name='post_list'),
       url(r'^posts/new/$', views.post_new, name='post_new'),
       url(r'^posts/(?P<pk>\d+)/$', views.post_detail,name='post_detail'), 
       url(r'^about-me/$', views.about_me, name='about_me'),
]
