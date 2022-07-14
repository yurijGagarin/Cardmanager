from django.urls import path
from . import views

urlpatterns = [

    path('list', views.list, name='list'),
    path('generator', views.CardGenerator.as_view(), name='generator'),
    path('account/<str:pk>', views.account, name='account'),
]