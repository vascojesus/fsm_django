from django.urls import path
from . import views

app_name = "tc"

urlpatterns = [
    path('', views.layout_view, name='home'),
    path('introducao/', views.intro_view, name='intro'),
    path('automatos/', views.automatos_view, name='automatos'),
    path('automatosform/', views.automatos_form_view, name='automatosform'),
    path('automatoseditar/<int:automato_id>', views.automatos_editar_view, name='automatoseditar'),
    path('automatosapagar/<int:automato_id>', views.automatos_apagar_view, name='automatosapagar'),
    path('automatosdetalhes/<int:automato_id>', views.automatos_detalhes_view, name='automatosdetalhes'),
    path('automatosseq/<int:automato_id>', views.automatos_seq_view, name='automatosseq'),
    path('maquinas/', views.maquinas_view, name='maquinas'),
    path('maquinasform/', views.maquinas_form_view, name='maquinasform'),
    path('maquinaseditar/<int:maquina_id>', views.maquinas_editar_view, name='maquinaseditar'),
    path('maquinasapagar/<int:maquina_id>', views.maquinas_apagar_view, name='maquinasapagar'),
    path('maquinasdetalhes/<int:maquina_id>', views.maquinas_detalhes_view, name='maquinasdetalhes'),
    path('maquinasseq/<int:maquina_id>', views.maquinas_seq_view, name='maquinasseq'),
]