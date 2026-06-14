from django.urls import path
from Students import views

urlpatterns = [
    path('stuDetails/<int:id>/', views.student_detail, name='student_detail'),
    path('stuList/', views.stu_List, name='stu_profile')

]
