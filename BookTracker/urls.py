from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'BookTracker.book.views.home', name='home'),
    url(r'^book/add/$', 'BookTracker.book.views.book_new', name='book_new'),
    url(r'^book/list$', 'BookTracker.book.views.book_list', name='book_list'),
    url(r'^book/search$', 'BookTracker.book.views.book_search', name='book_search'),
    url(r'^book/delete$', 'BookTracker.book.views.book_delete', name='book_delete'),
    url(r'^book/update$', 'BookTracker.book.views.book_update', name='book_update'),
    # url(r'^BookTracker/', include('BookTracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
