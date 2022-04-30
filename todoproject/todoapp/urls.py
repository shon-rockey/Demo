from . import views
from django.urls import path

urlpatterns = [
    path('', views.add, name="add"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('edit/<int:taskid>/', views.edit, name="edit"),
    path('home1/', views.TasklistView.as_view(), name="home1"),
    path('detail1/<int:pk>/', views.TaskDetailView.as_view(), name="detail1"),
    path('homePageUpdate/<int:pk>/', views.TaskUpdateView.as_view(), name='homePageUpdate'),
    path('deletePage/<int:pk>/', views.TaskDeleteView.as_view(), name='deletePage'),

]
