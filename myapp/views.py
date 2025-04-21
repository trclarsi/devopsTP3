from django.shortcuts import render
from .models import MyModel
# Create your views here.
def my_model_list(request):
     MyModel.objects.create(name="Objet de test")
     objects = MyModel.objects.all() # Récupérer tous les objets MyModel 
     return render(request, 'myapp/my_model_list.html', {'objects': objects})