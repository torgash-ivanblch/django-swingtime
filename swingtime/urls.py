from django.conf.urls import url

from django.urls import path
from swingtime import views

urlpatterns = [
    path(
        '',
        views.month_view,
        name='swingtime-month'
    ),
    path(
        'today/',
        views.today_view,
        name='swingtime-today'
        ),
#    url(
#        r'^(?:calendar/)?$',
#        views.today_view,
#        name='swingtime-today'
#    ),

    url(
        r'^calendar/(?P<year>\d{4})/$',
        views.year_view,
        name='swingtime-yearly-view'
    ),

    url(
        r'^calendar/(\d{4})/(0?[1-9]|1[012])/$',
        views.month_view,
        name='swingtime-monthly-view'
    ),

    url(
        r'^calendar/(\d{4})/(0?[1-9]|1[012])/([0-3]?\d)/$',
        views.day_view,
        name='swingtime-daily-view'
    ),

    url(
        r'^events/$',
        views.event_listing,
        name='swingtime-events'
    ),

    url(
        r'^events/add/$',
        views.add_event,
        name='swingtime-add-event'
    ),

    url(
        r'^events/(\d+)/$',
        views.event_view,
        name='swingtime-event'
    ),
    path(
        'events/delete/<int:pk>/',
        views.EventDelete.as_view(),
        name='swingtime-delete'
    ),

    url(
        r'^events/(\d+)/(\d+)/$',
        views.occurrence_view,
        name='swingtime-occurrence'
    ),
]
