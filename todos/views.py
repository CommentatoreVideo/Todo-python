from django.shortcuts import render, redirect
from .models import Categoria, Todo
from rest_framework import viewsets
from .serializers import TodoSerializer
from django.contrib.auth.decorators import login_required


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('titolo')
    serializer_class = TodoSerializer
    

# Create your views here.
@login_required
def index(request):
  context={}
  context["categorie"]=getTestiCategorie()
  todos=Todo.objects.all()
  elencoTodos=[]
  for todo in todos:
    elencoTodos.append(todo)
  context["todos"]=elencoTodos
  context["autore"]=request.user
  return render(request,"index.html",context)
  
def aggiungiTodo(request):
  context={}
  context["todo"]=True
  context["categorie"]=getTestiCategorie()
  return render(request,"aggiungi.html",context)
  
def aggiungiCategoria(request):
  context={}
  context["todo"]=False
  context["categorie"]=getTestiCategorie()
  return render(request,"aggiungi.html",context)
  
def getTestiCategorie():
  categorie=Categoria.objects.all()
  elencoCategorie=[]
  for categoria in categorie:
    elencoCategorie.append(categoria.nome)
  return elencoCategorie
  
def aggiungiTodo2(request):
  titolo=request.POST.get("titolo")
  descrizione=request.POST.get("descrizione")
  categoria=request.POST.get("categoria")
  autore=request.user
  elencoCategorie=Categoria.objects.all()
  for c in elencoCategorie:
    if c.nome==categoria:
      categoria=c
      break
  t=Todo(titolo=titolo,descrizione=descrizione,autore=autore,categoria=categoria)
  t.save()
  return redirect('index')
  
def aggiungiCategoria2(request):
  nome=request.POST.get("nome")
  categorie=getTestiCategorie()
  ok=True
  for categoria in categorie:
    if categoria==nome:
      ok=False
  if ok==True:
    c=Categoria(nome=nome)
    c.save()
  return redirect('index')
  
def eliminaTodo(request):
  indice=request.POST.get("idTodo")
  todo=Todo.objects.get(id=indice)
  if todo.autore==request.user:
    todo.delete()
  return redirect('index')
  
def aggiornaTodo(request):
  indice=request.POST.get("idTodo")
  todo=Todo.objects.get(id=indice)
  print(indice)
  print(todo)
  if todo.autore!=request.user:
    return redirect("index")
  categorie=getTestiCategorie()
  context={}
  context['todo']=True
  context['categorie']=categorie
  context['titolo']=todo.titolo
  context['descrizione']=todo.descrizione
  context['indice']=indice
  context['categoriaCorrente']=todo.categoria.nome
  return render(request,"aggiorna.html",context)
  
def aggiornaTodo2(request):
  titolo=request.POST.get("titolo")
  descrizione=request.POST.get("descrizione")
  categoria=request.POST.get("categoria")
  indice=request.POST.get("indice")
  todo=Todo.objects.get(id=indice)
  if todo.autore!=request.user:
    return redirect("index")
  categoria=Categoria.objects.get(nome=categoria)
  context={}
  todo.titolo=titolo
  todo.descrizione=descrizione
  todo.categoria=categoria
  todo.save()
  return redirect("index")