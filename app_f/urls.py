from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from app_f import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get-my-token/', obtain_auth_token, name="api_auth_token"),
    # REST
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/crear/', views.UserCreate.as_view(), name='user-crear'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detalle'),


    path('producto/', views.ProductoList.as_view(), name='producto-list'),
    path('producto/crear/', views.ProductoCreate.as_view(), name='producto-crear'),
    path('producto/<int:pk>/', views.ProductoDetail.as_view(),
         name='producto-detalle'),

    path('foto-producto/', views.FotoProductoList.as_view(),
         name='fotoproducto-list'),
    path('foto-producto/crear/', views.FotoProductoCreate.as_view(),
         name='fotoproducto-crear'),
    path('foto-producto/<int:pk>/', views.FotoProductoDetail.as_view(),
         name='fotoproducto-detalle'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
