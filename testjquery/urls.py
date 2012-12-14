from django.conf.urls import patterns, url

urlpatterns = patterns('testjquery.views',
	url(r'^$', 'index', name="index"),
	url(r'^guardar-user/$', 'guardar_user', name="guardar-user"),
	url(r'^buscar-user/$', 'buscar_user', name="buscar-user"),
)

