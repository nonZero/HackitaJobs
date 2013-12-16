from ads import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),

    url(r'^ad/(\d+)/$', views.ad, name='ad'),

    url(r'^post-ad/$',
        views.PostAdView.as_view(),
        name='post_ad'),

    url(r'^admin/', include(admin.site.urls)),
)
