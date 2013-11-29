from django.conf.urls import patterns, url

urlpatterns = patterns('contact.views',
    url(r'^$', 'contact_form', name="contact_form"),
)