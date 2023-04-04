from django.urls import path
from .views import verify, UserProductDetailView


urlpatterns = [
    path("verify/<str:email_token>", verify),
    path('users/<int:user_id>/', UserProductDetailView.as_view(), name='user-detail'),

]
