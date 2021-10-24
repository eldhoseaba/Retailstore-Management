from django.urls import path
from.import views

urlpatterns=[
path('',views.home,name="home"),
path('add',views.add),
path('display',views.display),
path('delete',views.delete),
path('update',views.update),
path('accounts/login/',views.loginview,name="login"),
path('accounts/sign_up/',views.sign_up,name="signup"),
path('logout',views.logout_view)
]