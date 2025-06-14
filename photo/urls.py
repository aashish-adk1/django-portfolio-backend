from django.urls import path
from .views import (PhotoListView,VideoListView,PhotoCreateView,VideoCreateView,PhotoDeleteView,VideoDeleteView,PhotoUpdateView,VideoUpdateView)

urlpatterns=[
    path('photos/',PhotoListView.as_view(),name='photo-list'),
    path('Photos/create/',PhotoCreateView.as_view(),name='photo-create'),
    path('photos/<int:id>/update/',PhotoUpdateView.as_view(),name='photo-update'),
    path('photos/<int:id>/delete/',PhotoDeleteView.as_view(),name='photo-delete'),
    
    
    path('videos/',VideoListView.as_view(),name='video-list'),
    path('videos/create/',VideoCreateView.as_view(),name='video-create'),
    path('videos/<int:id>/update/',VideoUpdateView.as_view(),name='video-update'),
    path('videos/<int:id>/delete/',VideoDeleteView.as_view(),name='video-delete'),
]