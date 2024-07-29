from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"), 
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
]