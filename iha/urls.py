from django.urls import path
from .views import createIha , updateIha , listIha , deleteIha  ,listCategory 
#brand model
from .views import listBrand , createBrand , deleteBrand
# model model
from .views import listModel , createModel , deleteModel
# category model
from .views import listCategory , createCategory , deleteCategory

urlpatterns = [
    path('add/iha/', createIha, name='createIha'),
    path('update/iha/', updateIha, name='updateIha'),
    path('get/iha/', listIha, name='listIha'),
    path('delete/iha/', deleteIha, name='deleteIha'),
    #brand url
    path('get/brand/', listBrand, name='listBrand'),
    path('add/brand/', createBrand, name='createBrand'),
    path('delete/brand/', deleteBrand, name='deleteBrand'),
    # model url 
    path('get/model/', listModel, name='listModel'),
    path('add/model/', createModel, name='createModel'),
    path('delete/model/', deleteModel, name='deleteModel'),
    # category url
    path('get/category/', listCategory, name='listCategory'),
    path('add/category/', createCategory, name='createCategory'),
    path('delete/category/', deleteCategory, name='deleteCategory'),
    
]
