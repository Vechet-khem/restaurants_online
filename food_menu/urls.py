from django.urls import path
from .views import *

urlpatterns = [
    # address
    path('address/village/', village),
    path('address/village/<str:uniqid>', villageDetail),
    path('address/district/', district),
    path('address/district/<str:uniqid>', districtDetail),
    path('address/communce/', communce),
    path('address/communce/<str:uniqid>', communceDetail),
    path('address/province/', province),
    path('address/province/<str:uniqid>', provinceDetail),

    # supplyer
    path('supplyer/', supplyer),
    path('supplyer/<str:search>', supplyerDetail),

    # path('food/', food),
    # path('food/category/', category),
]
