from django.urls import path
from .views import PostList, PostDetail
from home_api import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import PostList, PostDetail

app_name= 'home_api'

urlpatterns = [
    path('',views.PostList, name='home'),
    path('<int:id>', views.PostDetail, name='postdetail'),
]

