from django.urls import path
from.import views

urlpatterns=[
path('',views.home,name="home"),
path('add',views.add),
path('update',views.update),
path('display',views.display),
path('display2',views.display2)
]