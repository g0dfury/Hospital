from django.urls import path

from . import views


urlpatterns = [
    path('spec/', views.ListCreateSpecAPIView.as_view(), name='spec_list_create'), # ототбражение + показывает всех
    path('spec/one/<int:pk>/', views.RetrieveSpecAPIView.as_view(), name='spec_one'), # выбирает одного
    path('spec/delete/<int:pk>/', views.DestroySpecAPIView.as_view(), name='spec_delete'), # удаляет одного
    path('spec/update/<int:pk>/', views.UpdateSpecAPIView.as_view(), name='spec_update'), #обновляет полностью или частично
]