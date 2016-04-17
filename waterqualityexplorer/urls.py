from django.conf.urls import include, url
from django.contrib import admin

import proposal.views 

urlpatterns = [
    # Examples:
    # url(r'^$', 'waterqualityexplorer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', proposal.views.index, name='index'),
]
