from django.conf.urls import url

from . import views

app_name = 'tagger_messages'
urlpatterns = [
    url(r'^send_message/team_message/$', views.send_team_message, name='send_team_message'),
    url(r'^send_message/global_message/$', views.send_global_message, name='send_global_message'),
    url(r'^read_message/(\d+)/$', views.read_message, name='read_message'),
    url(r'^read_message/all/$', views.read_all_messages, name='read_all_messages'),
    url(r'^delete_message/(\d+)/$', views.delete_message, name='delete_message'),
    url(r'^overview/$', views.overview_unread, name='overview'),
    url(r'^overview/unread/$', views.overview_unread, name='overview_unread'),
    url(r'^overview/all/$', views.overview_all, name='overview_all'),
    url(r'^overview/sent/$', views.overview_sent, name='overview_sent'),
    url(r'^overview/global/$', views.overview_global, name='overview_global'),
]