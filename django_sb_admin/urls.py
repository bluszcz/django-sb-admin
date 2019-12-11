from django.conf.urls import url
import django_sb_admin.views
from django.views.generic import TemplateView
from django.urls import path



urlpatterns = [
    url(r'^$', django_sb_admin.views.start, name='sb_admin_start'),
    path('register/', TemplateView.as_view(
        template_name="django_sb_admin/register.html"),
        name='sb_admin_register'
    ),
    path('forgot_password/', TemplateView.as_view(
        template_name="django_sb_admin/forgot_password.html"),
        name='sb_admin_forgot_password'
    ),
    path('404/', TemplateView.as_view(
        template_name="django_sb_admin/sb_admin_404.html"),
        name='sb_admin_404'
    ),
    url(r'^login/$', django_sb_admin.views.login, name='sb_admin_login'),
    url(r'^dashboard/$', django_sb_admin.views.dashboard, name='sb_admin_dashboard'),
    url(r'^charts/$', django_sb_admin.views.charts, name='sb_admin_charts'),
    url(r'^tables/$', django_sb_admin.views.tables, name='sb_admin_tables'),
    url(r'^forms/$', django_sb_admin.views.forms, name='sb_admin_forms'),
    url(r'^bootstrap-elements/$', django_sb_admin.views.bootstrap_elements, name='sb_admin_bootstrap_elements'),
    url(r'^bootstrap-grid/$', django_sb_admin.views.bootstrap_grid, name='sb_admin_bootstrap_grid'),
    url(r'^rtl-dashboard/$', django_sb_admin.views.rtl_dashboard, name='sb_admin_rtl_dashboard'),
    url(r'^blank/$', django_sb_admin.views.blank, name='sb_admin_blank'),
]