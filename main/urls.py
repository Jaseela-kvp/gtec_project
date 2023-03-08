from django.urls import path
from main.views import index,about,contact,shop,shopSingle

urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('shop/',shop, name='shop'),
    path('shopSingle/',shopSingle, name='shopSingle')
]