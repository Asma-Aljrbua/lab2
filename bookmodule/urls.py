from django.urls import path
from . import views
urlpatterns = [
 path('', views.index),
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>', views.viewbook),
 ]



#path('', views.hello_world, name='hello_world'),
 #   path('', views.hello_name, name='hello_name'),  # يجب إضافة طريقة لإدارة الأسماء
  #  path('index2/<int:value1>/', views.index2, name='index2'),



  #  path('', views.index, name='index'),
  #  path('index2/<int:val1>/', views.index2, name='index2'),
