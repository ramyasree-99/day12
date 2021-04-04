from django.urls import path
from Emp import views

urlpatterns=[
path('',views.home,name="hm"),
path('abt/',views.about,name="ab"),
path('con/',views.cont,name="cn"),
path('log/',views.login,name="lg"),
path('reg/',views.register,name="rg"),
path('crud/',views.crud,name="cr"),
path('delete/<str:id>',views.delete,name="delete")
]