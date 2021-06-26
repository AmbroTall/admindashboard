from django.urls import path
from .views import DashBoardView, ProductsView,RegisterPageView,LoginPageView, CustomerDetailView,DeleteProductView, CustomerCreateView, OrderCreateView, DeleteCustomer, UpdateCustomer, UpdateOrder,DeleteOrder,ProductCreateView,ProductUpdateView, CustomerDetailViewTrial,AllCustomersView,AllOrdersView
from django.contrib.auth.views import LogoutView

app_name = 'dashboard'
urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login' ),
    path('register/', RegisterPageView.as_view(), name='register' ),
    path('logout/', LogoutView.as_view(next_page='dashboard:login'), name='logout' ),
    path('', DashBoardView.as_view(), name='homepage' ),
    path('customers/', AllCustomersView.as_view(), name='allcustomerspage' ),
    path('orders/', AllOrdersView.as_view(), name='allorderspage' ),
    path('products/', ProductsView.as_view(), name='productpage' ),
    path('productcreate/', ProductCreateView.as_view(), name='productcreatepage' ),
    path('<str:slug>/updateproduct', ProductUpdateView.as_view(), name='productupdatepage' ),
    path('<str:slug>/deleteproduct', DeleteProductView.as_view(), name='productdelete' ),
    path('create_order/', OrderCreateView.as_view(), name='ordercreatepage'),
    path('<str:slug>/delete', DeleteOrder.as_view(), name='deleteorderpage' ),
    path('<str:slug>/update', UpdateOrder.as_view(), name='updateorderpage' ),
    path('create_customer/', CustomerCreateView.as_view(), name='customercreatepage' ),
    path('<str:slug>/', CustomerDetailView.as_view(), name='customerpage'),
    path('<str:slug>/', CustomerDetailViewTrial.as_view(), name='customerpagetrial'),
    path('<str:slug>/Delete_customer', DeleteCustomer.as_view(), name='deletecustomerpage' ),
    path('<str:slug>/Update_customer', UpdateCustomer.as_view(), name='updatecustomerpage' ),
]
