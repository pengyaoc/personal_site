from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

import hello.views
import newsletter.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', "newsletter.views.home", name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^home', newsletter.views.home, name='home'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
)
