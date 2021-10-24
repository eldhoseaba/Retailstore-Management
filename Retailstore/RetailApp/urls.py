from django.urls import path
from.import views

urlpatterns=[
path('',views.home,name="home"),
path('addproduct',views.addproduct,name="addproduct"),
path('addcustomer',views.addcustomer,name="addcustomer"),
path('addcmpny',views.addcmpny,name="addcompany"),
path('addorder',views.orderprdct,name="orderproduct"),
path('addsales',views.addsales,name="sales"),
path('addcart',views.addcart,name="addcart"),
path('displaycart',views.displaycart,name="displaycart"),
path('displayorder',views.displayorder,name="vieworder"),
path('displayorder',views.displayproduct,name="viewproduct"),
path('displayorder',views.displaysales,name="viewsales"),
path('accounts/login/',views.loginview,name="login"),
path('accounts/sign_up/',views.sign_up,name="signup"),
path('logout',views.logout_view,name="logout")
]