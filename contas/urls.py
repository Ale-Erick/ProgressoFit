from django.urls import path 
from . import views 


app_name = "contas" 
urlpatterns = [    
    path("", views.home_view, name="home"),  
    path("login/", views.login_view, name="login"),
    path("cadastro/", views.cadastro_view, name="cadastro"),
    path("perfil/", views.perfil_view, name="perfil"), 
    path("perfil/editar/", views.perfil_editar_view, name="perfil_editar"),    
    path("especialista/verificacao/", views.verificacao_view, name="verificacao"),]