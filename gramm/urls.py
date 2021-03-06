from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.index,name='index'),
    url(r'^insta$',views.insta_today,name='instaToday'),
    url(r'^comment$',views.new_comment,name='new_comment'),
    url(r'^new/post', views.new_post, name='new-post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_insta,name = 'pastInsta'),
       
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
