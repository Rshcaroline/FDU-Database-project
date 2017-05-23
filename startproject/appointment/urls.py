from django.conf.urls import url

from . import views

app_name = 'appointment'
urlpatterns = [
    url(r'^acm/$', views.get_Acm, name='acm_get_acm'),
    url(r'^acm/detail/(\d+)/$', views.get_Acm_detail, name='acm_get_detail'),
    url(r'^lecture/$', views.get_Lecture, name='lecture_get_lecture'),
    url(r'^lecture/detail/(\d+)/$', views.get_Lecture_detail, name='lecture_get_detail'),
    url(r'^station/$', views.get_Station, name='station_get_station'),
    url(r'^station/detail/(\d+)/$', views.get_Station_detail, name='station_get_detail'),
]