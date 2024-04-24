from django.urls import path
from .views import Homepageview, Postdetailview

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('detail/<int:pk>', Postdetailview.as_view(), name='detail'),
]


