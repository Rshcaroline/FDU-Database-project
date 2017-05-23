from django.conf.urls import url

from . import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.get_news, name='news_get_news'),
    url(r'^detail/(\d+)/$', views.get_detail, name='news_get_detail'),
]