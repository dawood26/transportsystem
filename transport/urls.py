from django.urls import path,include
from . import views
app_name ='transport'
urlpatterns = [

    path('create', views.index, name='create'),
    path('list', views.list, name='list'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('detail/<int:id>/', views.detail, name='detail'),

]
