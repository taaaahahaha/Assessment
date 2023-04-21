from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),

    path('expense/',views.expense, name='expense'),
    path('update/<int:pk>',views.update, name='update'),
    path('delete/<int:pk>',views.delete, name='delete'),
    
]
