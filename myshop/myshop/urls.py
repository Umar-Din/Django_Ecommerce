
from django.contrib import admin
from django.urls import path,include
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('home/', include('shop.urls')),
    path('createaccount/', include('shop.urls')),
    path('login/', include('shop.urls')),
    path('logindata/', include('shop.urls')),
    path('admin1/', include('shop.urls')),
    path('addproduct/', include('shop.urls')),
    path('registerproduct/', include('shop.urls')),
    path('showproduct/', include('shop.urls')),
    path('deletepro/', include('shop.urls')),
    path('showuser/', include('shop.urls')),
    path('logout/', include('shop.urls')),
    path('registerdata/', include('shop.urls')),
    path('user/', include('shop.urls')),
    path('deleteuser/', include('shop.urls')),
    path('myordershow/', include('shop.urls')),
    path('addoffer/', include('shop.urls')),
    path('addofferdata/', include('shop.urls')),
    path('showoffer/', include('shop.urls')),
    path('deleteoffer/', include('shop.urls')),
    path('usershowproduct/', include('shop.urls')),
    path('final/', include('shop.urls')),
    path('myorder/', include('shop.urls')),
    path('updatestatus/', include('shop.urls')),
    path('deleteorder/', include('shop.urls')),
    path('userorder/', include('shop.urls')),
    path('accountsetting/', include('shop.urls')),
    path('accountsetting1/', include('shop.urls')),
    path('showdetail/', include('shop.urls')),
    path('saverating/', include('shop.urls')),
    path('deletemyproduct/', include('shop.urls')),
]
