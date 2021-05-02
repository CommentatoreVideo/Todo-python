from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  autore = serializers.CharField(source='autore.username', read_only=True)
  # categoria = serializers.CharField(source='categoria.nome', read_only=True)
  class Meta:
      model = Todo
      fields = ['titolo', 'descrizione', 'autore', "id"]