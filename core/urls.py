from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),

    path('admin/', include('admin_honeypot.urls')),
    path('inside/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='500.html')),
        url(r'^email/$', TemplateView.as_view(template_name='email.html')),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
