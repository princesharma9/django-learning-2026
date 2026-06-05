 
from django.urls import path
from .import views

urlpatterns = [
    # path('wiudw/', views.chai_details, )
    path('', views.all_chai, name='all_chai'),
    path('details/<int:chai_id>/', views.chai_details, name='chai_details'),
    path('reviews/<int:review_id>/', views.chai_reviews, name='chai_reviews'),
    path('chai_stores/', views.chai_store_view, name='chai_store_view')
 
]
