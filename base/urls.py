from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("archived_datasets/", views.archived_datasets, name="archived_datasets"),
  path("dataset/<int:pk>/", views.dataset, name="dataset"),
  # path("dataset/", views.dataset, name="dataset"),
  path('upload/', views.upload, name='upload'),
  path('update/<int:pk>', views.update, name='update'),
  path('archive/<int:pk>', views.archive, name='archive'),
  path('unarchive/<int:pk>', views.unarchive, name='unarchive'),
  path('download/<int:pk>/', views.download, name='download'),
]