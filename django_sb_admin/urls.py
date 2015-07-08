from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^$', 'django_sb_admin.views.start', name='sb_admin_start'),
    url(r'^dashboard/$', 'django_sb_admin.views.dashboard', name='sb_admin_dashboard'),
    url(r'^charts/$', 'django_sb_admin.views.charts', name='sb_admin_charts'),
    url(r'^tables/$', 'django_sb_admin.views.tables', name='sb_admin_tables'),
    
    

)