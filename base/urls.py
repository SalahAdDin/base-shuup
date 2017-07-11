from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('shuup.admin.urls', namespace="shuup_admin", app_name="shuup_admin")),
    url(r'^api/', include('shuup.api.urls')),
    url(r'^', include('shuup.front.urls', namespace="shuup", app_name="shuup")),

    url(r'^robots\.txt', include('robots.urls')),
    # url(r'^sitemap\.xml$', cache_page(60)(sitemap), name='cached-sitemap'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += [
        url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico')),
    ]

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
