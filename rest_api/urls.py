from django.urls import path
from . import views
urlpatterns = [
    path('get_data/',views.UserGet.as_view(), name="get_data"),
    path('post_data/',views.UserCreate.as_view(), name="post_data"),
    path('put_data/<int:pk>',views.PutUser.as_view(), name="put_data"),
    path('delete_data/<int:pk>',views.DeleteUser.as_view(), name="delete_data"),
]