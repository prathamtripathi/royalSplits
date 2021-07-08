from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('page_about/',views.page_about,name='page_about'),
    path('profile_setting/',views.profile_setting,name='profile_setting'),
    path('forms/', views.formpage, name='formpage'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('tnc/', views.tnc, name='tnc'),
    path('page_404/', views.page_404, name='page_404'),
    path('page_500/', views.page_500, name='page_500'),
    path('checkout/', views.checkout, name='checkout'),
    path('maintain/', views.maintain, name='maintain'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<int:_id>/', views.BlogDetailView, name='blog_article'),
    path('page_career/', views.page_career, name='page_career'),
    path('jobA/<int:id>/', views.jobA, name='jobA'),
    path('update_item/',views.update_item,name='update_item'),
    # path('product/<slug>/', views.detail, name='detail'),
    #path('add_product/<slug>/',views.add_product,name='add_product'),
    path('findus/', views.findus, name='findus'),
    # path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    # path('remove_item_from_cart/<slug>/', views.remove_single_item_from_cart,
    #      name='remove_single_item_from_cart'),
    path('delete_account/',views.remove_account,name='remove_account'),
    # path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    path('add-coupon/', views.AddCouponView.as_view(), name='add_coupon'),
    path('color/<int:id>/',views.choose_color,name='color')
   
    
]
