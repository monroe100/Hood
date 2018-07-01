from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/(?P<neighbourhood_id>[0-9]+)/$', views.home, name= 'home'),
    url(r'^updateProfile/', views.create_profile, name="createProfile"),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^businesses/$', views.businesses, name= 'businesses'),
    url(r'^photo/(\d+)', views.single_photo, name='single_photo'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^createPost/', views.create_post, name="createPost"),
    url(r'^neighbourhoods/',views.neighbourhoods, name="neighbourhoods"),

]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)