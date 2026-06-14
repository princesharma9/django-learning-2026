from django.urls import path
from product import views

urlpatterns = [
    path('', views.product_list_page, name='product_list_page' ),
    # path('details/<int:id>/', views.details_page, name='details_page' )
]
