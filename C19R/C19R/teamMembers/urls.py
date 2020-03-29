from django.urls import path
from .views import *

urlpatterns = [
    path('', teamHome, name='teamMembers-home'),
    path('add_business', AddBusiness.as_view(), name="teamMembers-addBusiness"),
    path('store_info/<str:pk>/create', AddStoreInfo.as_view(), name="teamMembers_addStoreInfo"),
    path('view_businesses', viewBusinesses, name="teamMembers_viewBusinesses"),
    path('business_detail_view/<str:pk>', BusinessDetailView.as_view(), name="teamMembers_businessDetailView"),
    path('business_update/<str:pk>/update', BusinessUpdateView.as_view(), name="teamMembers_businessUpdateView"),
    path('business_delete/<str:pk>/delete', BusinessDeleteView.as_view(), name="teamMembers_businessDelete")
]
