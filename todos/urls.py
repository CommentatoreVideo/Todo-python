from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)
urlpatterns = [
    path('', views.index, name="index"),
    path('aggiungi/todo', views.aggiungiTodo,name="aggiungiTodo"),
    path('aggiungi/categoria', views.aggiungiCategoria, name="aggiungiCategoria"),
    path('aggiungiTodo',views.aggiungiTodo2, name="creaTodo"),
    path('aggiungiCategoria',views.aggiungiCategoria2, name="creaCategoria"),
    path('eliminaTodo',views.eliminaTodo,name="eliminaTodo"),
    path('aggiornaTodo',views.aggiornaTodo,name="aggiornaTodo"),
    path('aggiornaTodo2',views.aggiornaTodo2,name="aggiornaTodo2"),
    path('aggiornaCategoria',views.aggiornaCategorie,name="aggiornaCategoria"),
    path('aggiornaCategoria2',views.aggiornaCategorie2,name="aggiornaCategoria2"),
    path('eliminaCategoria',views.eliminaCategoria,name="eliminaCategoria"),
    path('api/',include(router.urls))
]