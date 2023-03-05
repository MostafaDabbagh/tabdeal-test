from django.urls import path
from . import views


app_name = 'payment'
urlpatterns = [
    path('sell/', views.ChargeSellView.as_view())
]
