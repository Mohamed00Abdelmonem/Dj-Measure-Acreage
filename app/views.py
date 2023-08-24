from django.shortcuts import render
from .models import Data_Land, Data_For_Author
from django.views.generic import ListView, DetailView
# Create your views here.

# def index(request):
#     return render(request, 'doc/index.html')
class Area_List(ListView):
    model = Data_Land
    template_name = 'app/index.html'
    context_object_name = 'objects'


class Land_Detail(DetailView):
    model = Data_Land
    template_name = 'app/land_detail.html'
    context_object_name = 'object'    