from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

menu_item_routes = SimpleRouter(trailing_slash=False)
menu_item_routes.register('menu-items', views.MenuItemViewSet, basename='menu-items')
categories_routes = SimpleRouter(trailing_slash=False)
categories_routes.register('categories', views.CategoryViewSet, basename='categories')
orders_routes = SimpleRouter(trailing_slash=False)
orders_routes.register('orders', views.OrderViewSet, basename='orders')


urlpatterns = [
    path('', views.index),
    path('', include(menu_item_routes.urls)),
    path('', include(categories_routes.urls)),
    path('', include(orders_routes.urls)),
    path('cart/', include(orders_routes.urls)),
    path('groups/manager/users', views.ManagerUsersAPIView.as_view(),  name='manager-users'),
    path('groups/manager/users/<int:user_id>', views.ManagerUserDeleteAPIView.as_view(),  name='manager-users-delete'),
    path('groups/delivery-crew/users', views.DeliveryCrewUsersAPIView.as_view(),  name='delivery-crew-users'),
    path('groups/delivery-crew/users/<int:user_id>', views.DeliveryCrewDeleteAPIView.as_view(),  name='delivery-crew-users-delete'),
    path('cart/menu-items', views.CartAPIView.as_view(),  name='cart'),
    
] 