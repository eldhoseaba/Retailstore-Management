from django.urls import path
from.import views

urlpatterns=[
path('',views.home,name="home"),
path('add',views.add),
path('delete',views.delete),
path('Nameupdation',views.Nameupdation),
path('PhNoupdation',views.PhNoupdation),
path('display',views.display),

]