
from django.urls import path
from . import views


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),   
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('buyer-dashboard/', views.BuyerDashboardView.as_view(), name='buyer-dashboard'),
    path('seller-dashboard/', views.SellerDashboardView.as_view(), name='seller-dashboard'),
    path('add-property/', views.AddPropertyView.as_view(), name='add-property'),
    path('property/<int:pk>', views.PropertyView.as_view(), name='property'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
] 