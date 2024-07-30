from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




from django.urls import path
from .views import product_detail

urlpatterns = [
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]