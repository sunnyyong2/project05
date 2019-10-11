from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),

  
    path('create/', views.create, name='create'),

    path('<int:id>/', views.detail, name ='detail'),

    path('<int:id>/update/',views.update, name='update'),

    path('<int:id>/delete/',views.delete, name='delete'),

    # path('<int:id>/delete/', views.delete ),

    # path('<int:id>/edit/', views.edit),
    # path('<int:id>/update/', views.update),

    # path('<int:id>/detail/',views.detail),
]