from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

import hello.views
import newsletter.views

urlpatterns = patterns('',
    url(r'^$', newsletter.views.home, name='home'),
    url(r'^home', newsletter.views.home, name='home'),
    url(r'^payment', newsletter.views.payment, name='payment'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
)
