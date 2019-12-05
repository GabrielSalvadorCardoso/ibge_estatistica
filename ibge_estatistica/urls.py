from django.urls import path, include

app_name = "ibge_estatistica"
urlpatterns = [
    path('api/ibge/estatistica/', include('projecoes_2018.urls', namespace="entrypoint"))#, name="entrypoint"),
]
