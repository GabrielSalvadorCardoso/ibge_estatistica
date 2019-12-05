from django.urls import path, include, re_path
from .views import *

app_name = "projecoes_2018"
urlpatterns = [
    path('', APIRoot.as_view(), name="root"),
    path('projecoes/2018', ProjecaoList.as_view(), name='Projecao_list'),

    re_path('^projecoes/2018/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', ProjecaoDetail.as_view(), name='Projecao_detail_operation_or_attributes'),
    re_path('^projecoes/2018/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', ProjecaoDetail.as_view(), name='Projecao_bysigla_operation_or_attributes'),
    path('projecoes/2018/<int:pk>.<str:extension>', ProjecaoDetail.as_view(), name='Projecao_detail_extension'),
    re_path('^projecoes/2018/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', ProjecaoDetail.as_view(), name='Projecao_bysigla_extension'),
    path('projecoes/2018/<int:pk>', ProjecaoDetail.as_view(), name='Projecao_detail'),
    re_path('^projecoes/2018/(?P<sigla>[A-Za-z]{2})/?$', ProjecaoDetail.as_view(), name='Projecao_bysigla_detail'),
    path('projecoes/2018/<path:operation_or_attributes>/', ProjecaoList.as_view(), name='Projecao_list_operation_or_attributes'),
    path('projecoes/2018.<str:extension>', ProjecaoList.as_view(), name='Projecao_list_extension'),
    path('projecoes/2018', ProjecaoList.as_view(), name='Projecao_list'),
]