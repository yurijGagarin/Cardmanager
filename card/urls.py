from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('generator', views.CardGenerator.as_view(), name='generator'),
    path('account/<int:pk>', views.CardInfo.as_view(), name='info'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
