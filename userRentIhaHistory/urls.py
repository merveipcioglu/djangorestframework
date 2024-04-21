from django.urls import path
from .views import rentIha ,  deleteRentIha , listRentIhaByIhaId ,  updateRentIha

urlpatterns = [
    path('iha/rent/', rentIha, name='rentIha'),
    path('rent/iha/delete/', deleteRentIha, name='deleteRentIha'),
    path('rent/iha/list/', listRentIhaByIhaId, name='listRentIhaByIhaId'),
    path('rent/iha/update/<int:pk>/',  updateRentIha, name=' updateRentIha'),
]
