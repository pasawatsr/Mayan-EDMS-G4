from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tags.views',
    url(r'^list/$', 'tag_list', (), 'tag_list'),
    url(r'^(?P<tag_id>\d+)/remove_from_document/(?P<document_id>\d+)/$', 'tag_remove', (), 'tag_remove'),
    url(r'^add_to_document/(?P<document_id>\d+)/$', 'tag_add', (), 'tag_add'),
)
