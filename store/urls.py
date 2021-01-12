from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('order_summary/', views.OrderSummary.as_view(), name='order_summary'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add-coupon/', views.AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart')

]
