from django.urls import path
from apps.newProducts.addProducts.views import product_view, product_list, product_edit, product_delete

urlpatterns = [
    path('addProducts/', product_view),
    path('listProducts/', product_list, name="listProducts"),
    path('editProducts/<int:id_product>/', product_edit, name='editProduct'),
    path('deleteProducts/<int:id_product>/',
         product_delete, name='deleteProduct'),
]
