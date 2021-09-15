from django.urls import path
from . import views
from taskproject.settings import DEBUG, STATIC_URL
from django.conf.urls.static import static

#here you maintain your web page urls 
urlpatterns = [
	path('', views.index, name = 'index'),
	path('upload/', views.upload, name = 'upload-data'),
	path('upload1/', views.upload1, name = 'view-graph'),
	path('upload2/', views.upload2, name = 'view-file'),
	path('csv_data_upload/', views.csv_data_upload, name='csv_data_upload'),
]
