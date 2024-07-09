from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *
from . import views
app_name="singer"
urlpatterns = [
    path('singer', views.singer_list_create),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:singer_id>/song/<int:song_id>', views.song_patch),
    path('<int:singer_id>/song', views.song_read_create),
    path('tags/<str:tag_name>', views.find_tag),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)