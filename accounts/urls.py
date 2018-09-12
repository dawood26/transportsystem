from django.urls import path
from . import views
app_name ='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('list/', views.list, name='list'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('homepage/', views.homepage, name='homepage'),

]
