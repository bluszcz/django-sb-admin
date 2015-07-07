from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^$', 'django_sb_admin.views.start'),

)