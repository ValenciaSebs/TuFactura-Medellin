from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("agregar_perfil/", views.nuevo_perfil_form, name="agregar_perfil"),  # Aquí está el nombre correcto
    path("nuevo_contrato/", views.nuevo_contrato, name="nuevo_contrato"),
]