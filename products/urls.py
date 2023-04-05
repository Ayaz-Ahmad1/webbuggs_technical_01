from django.urls import path
from .views import ProductSearchAPIView, TopCategoriesAPIView, ProductCategoryListCreateAPIView, ProductCategoryUpdateDestroyAPIView, SubCategoryListCreateAPIView, SubCategoryUpdateDestroyAPIView, ColorListCreateAPIView, ColorUpdateDestroyAPIView, ProductListCreateAPIView, ProductUpdateDestroyAPIView,GetSingleProductWithDetail

urlpatterns = [

#Categories URLs 
path('categories/', ProductCategoryListCreateAPIView.as_view(), name='category_list_create'),
path('categories/get/<int:id>/', ProductCategoryListCreateAPIView.as_view(), name='category_get'),

path('categories/update-delete/<int:id>/', ProductCategoryUpdateDestroyAPIView.as_view(), name='category_update-delete'),


#Sub-Category URLs
path('subcategories/', SubCategoryListCreateAPIView.as_view(), name='subcategory_list_create'),
path('subcategories/get/<int:id>/', SubCategoryListCreateAPIView.as_view(), name='subcategory_get'),

path('subcategories/update-delete/<int:id>/', SubCategoryUpdateDestroyAPIView.as_view(),name='subcategory-update_destroy'),


#Colors URLs
path('colors/', ColorListCreateAPIView.as_view(), name='color_list_create'),
path('colors/get/<int:id>/', ColorListCreateAPIView.as_view(), name='color_get'),

path('colors/update-delete/<int:id>/', ColorUpdateDestroyAPIView.as_view(), name='color_update_destroy'),


#PRODUCTS  URLs
path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
path('products/get/<int:id>/', GetSingleProductWithDetail.as_view(), name='product_retrieve_update_destroy'),

path('products/update-delete/<int:id>/', ProductUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),



path('top-categories/', TopCategoriesAPIView.as_view(), name='top_categories'),
path('search/', ProductSearchAPIView.as_view(), name='search'),

]
