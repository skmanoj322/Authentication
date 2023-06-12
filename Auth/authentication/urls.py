from django.urls import path
from . views import HomeView,Logout


urlpatterns=[
    path('home/',HomeView.as_view(),name='home'),
    path('logout/',Logout.as_view(),name='logout'),     
]