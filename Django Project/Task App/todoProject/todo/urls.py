from django.urls import path
from . import views
app_name = 'todo'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('edit/<int:task_id>/', views.edit_Task, name='editTask'),
    path('delete/<int:delete_id>/', views.delete_Task, name='deleteTask'),
    
   
 
]