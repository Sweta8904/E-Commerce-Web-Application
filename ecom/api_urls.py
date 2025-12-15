from django.urls import path
from .views import login_api, place_order_api

urlpatterns = [
    path('login/', login_api),
    path('place-order/', place_order_api, name='place_order_api'),
]
