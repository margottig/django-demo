from django.urls import path
from . import views

urlpatterns = [
    path('', views.raiz ),
    path('crearBanda', views.crearBanda),
    path('showBand/<int:id_banda>', views.showBanda),
    path('crearFan', views.crearFan),
    path('agregarFan/<int:id_banda>', views.agregarFan)
]
