from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin.site.urls),
    url(r'^awarie/$', 'failure.views.awarie'),
    url(r'^awarie/new/$', 'failure.views.awarie_new'),

    url(r'^login/$', 'service.views.login'),
    url(r'^auth/$', 'service.views.auth_view'),
    url(r'^loggedin/$', 'service.views.loggedin'),
    url(r'^logout/$', 'service.views.logout'),
    url(r'^invalid/$', 'service.views.invalid_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
