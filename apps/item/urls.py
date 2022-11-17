from django.urls import path
from .views import (
    GetItemSessionAPIView,
    GetItemListAPIView,
    index
)


urlpatterns = [
    path('', GetItemListAPIView.as_view(), name='item-list'),
    path('buy/<int:id>/', GetItemSessionAPIView.as_view(), name='item-session'),
    path('<int:id>/', index, name='item'),
]