from django.urls import path

from coder_course import views

urlpatterns = [
   

    path('index-2', views.index2),
    #path('cursos', views.cursos, name="Cursos"),
    path('insumos',views.insumos, name="Insumos"),
    path('tareas',views.tareas, name="Tareas"),
    path('rubros',views.rubros, name="Rubros"),
    path('familias',views.familias, name="Familias"),
    path('iniciar',views.iniciar, name="login"),
    #path('cargarFamilia',views.cargarfamilias, name="cargarFamilia"),
    path('busquedaCodigo',views.busquedaCodigo, name="BusquedaCodigo"),
    path('buscar/',views.buscar),
]