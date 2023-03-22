from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('sign', views.sign,name='sign'),
    path('logi', views.logi,name='logi'),
    path('write', views.write,name='write'),
    path('home',views.home,name='home'),
    path('logou',views.logou,name='logou'),
    path('create',views.createpost,name='create'),
    path('search',views.search,name='search'),
    path('accept',views.accept, name='accept'),
    path('send',views.send, name='send'),
    path('viewpost',views.viewpost, name='viewpost'),
    path('unfollow',views.unfollow, name='unfollow'),
    path('editpro',views.editpro, name='editpro'),
    path('edipo',views.edipo, name='edipo'),
    path('like',views.like, name='like'),
    path('dislike',views.dislike, name='dislike'),
    path('about',views.about, name='about'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)