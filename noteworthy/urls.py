from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
    url(r"^group/(?P<name>.+)/$", "quote.views.quote_by_group"),
    url(r"^admin/", include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
)
