from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    IndexView, ContactsView, ProductDetailView,
    CategoryDetailView, ProductUpdateView, ProductDeleteView,
    ProductCreateView, CategoryUpdateView, CategoryDeleteView,
    CategoryCreateView, VersionCreateView, VersionUpdateView,
    VersionDeleteView
)
from user.views import RegistrationView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('product/create/', ProductCreateView.as_view(), name='create'),

    path('product/version/create/', VersionCreateView.as_view(), name='create_version'),
    path('product/version/update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('product/version/delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),

    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('login/', LoginView.as_view(), name='login'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('register/', RegistrationView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
