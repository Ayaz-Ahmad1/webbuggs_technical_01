from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import User, ProductCategory, SubCategory, Color, Product
#from users.permissions import IsOwner, APIAuthentication
from .serializers import ProductCategorySerializer, SubCategorySerializer, NewSubCategorySerializer, ColorSerializer, ProductSerializer, GetProductSerializer, Top3SubCategorySerializer
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication ,TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Count


# ProductCategory retrieve, list and create (any authorized user).
class ProductCategoryListCreateAPIView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get(self , request, id=None):
        return self.retrieve(id) if id else self.list(request)
            
    def post(self, request):
        return self.create(request)
    
# ProductCategory update and destroy (only by admin).
class ProductCategoryUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def delete(self , request, id=None):
        return self.destroy(request,id)
    
    def put(self, request, id=None):
        return self.update(request, id)



# Product Sub-Category retrieve, list and create (any authorized user).
class SubCategoryListCreateAPIView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = NewSubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get(self , request, id=None):
        return self.retrieve(id) if id else self.list(request)
            
    def post(self, request):
        return self.create(request)

# Product-Sub-Category update and destroy (only by admin).
class SubCategoryUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def delete(self , request, id=None):
        return self.destroy(request,id)
    
    def update(self, request, id=None):
        return self.update(request, id)
    


# Product COLOR retrieve, list and create (any authorized user).
class ColorListCreateAPIView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'id'
    def get(self , request, id=None):
        return self.retrieve(id) if id else self.list(request)
            
    def post(self, request):
        return self.create(request)

# Product-Color update and destroy (only by admin).
class ColorUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'id'

    def delete(self , request, id=None):
        return self.destroy(request,id)
    
    def update(self, request, id=None):
        return self.update(request, id)
    


# PRODUCT list and create (any authorized user).
class ProductListCreateAPIView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all() 
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 15
    
    def get(self , request, id=None):
        return self.retrieve(id) if id else self.list(request)
            
    def post(self, request):
        return self.create(request)

# PRODUCT update and destroy (only by admin).
class ProductUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    #authentication_classes = [TokenAuthentication]
    lookup_field = 'id'

    def delete(self , request, id=None):
        return self.destroy(request,id)
    
    def update(self, request, id=None):
        return self.update(request, id)
    
# PRODUCT Get single Product with all details.
class GetSingleProductWithDetail(generics.ListAPIView, generics.RetrieveAPIView):
    serializer_class = GetProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]
    #authentication_classes = [TokenAuthentication]
    lookup_field = 'id'

    def get(self , request, id=None):
        return self.retrieve(id)



class TopCategoriesAPIView(GenericAPIView):
    serializer_class = Top3SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.annotate(product_count=Count('products')).order_by( '-product_count' )[:3]
    

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
