from django.shortcuts import redirect, render

from .forms import CategoriaForm

# Create your views here.

"""  render to django admin  """

def index(request):
    return render(request, 'index.html')


def nuevaCategoria(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'categoria/nuevaCategoria.html')