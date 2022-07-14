from dataclasses import field
from pyexpat import model
from django import forms

from .models import Categoria, Inventario, Nave

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion']
        labels={'descripcion':'Descripcion'}
        widgets={'descripcion':forms.TextInput(attrs={'class':'form-control'})}
        help_texts={'descripcion':'Ingrese la descripcion de la categoria'}
        error_messages={'descripcion':{'required':'Ingrese la descripcion de la categoria'}}



class NaveForm(forms.ModelForm):
       class Meta:
              model=Nave
              fields=['nombre','modelo','fabricante','categoria','anio_fabricacion','numero_llantas','numero_motores','numero_tripulantes','numero_tripulantes_max','numero_tripulantes_min','velocidad_maxima','estado','cantidadMinima']
              labels={'nombre':'Nombre','modelo':'Modelo','fabricante':'Fabricante','categoria':'Categoria','anio_fabricacion':'Año de Fabricacion','numero_llantas':'Numero de Llantas','numero_motores':'Numero de Motores','numero_tripulantes':'Numero de Tripulantes','numero_tripulantes_max':'Numero de Tripulantes Maximo','numero_tripulantes_min':'Numero de Tripulantes Minimo','velocidad_maxima':'Velocidad Maxima','estado':'Estado','cantidadMinima':'Cantidad Minima'}
              widgets={'nombre':forms.TextInput(attrs={'class':'form-control'}),'modelo':forms.TextInput(attrs={'class':'form-control'}),'fabricante':forms.TextInput(attrs={'class':'form-control'}),'categoria':forms.Select(attrs={'class':'form-control'}),'anio_fabricacion':forms.NumberInput(attrs={'class':'form-control'}),'numero_llantas':forms.NumberInput(attrs={'class':'form-control'}),'numero_motores':forms.NumberInput(attrs={'class':'form-control'}),'numero_tripulantes':forms.NumberInput(attrs={'class':'form-control'}),'numero_tripulantes_max':forms.NumberInput(attrs={'class':'form-control'}),'numero_tripulantes_min':forms.NumberInput(attrs={'class':'form-control'}),'velocidad_maxima':forms.NumberInput(attrs={'class':'form-control'}),'estado':forms.CheckboxInput(attrs={'class':'form-control'}),'cantidadMinima':forms.NumberInput(attrs={'class':'form-control'})}

class InventarioForm(forms.ModelForm):
      class Meta:
         model=Inventario
         fields=['nave','cantidad']
         labels={'nave':'Nave','cantidad':'Cantidad'}
         widgets={'nave':forms.Select(attrs={'class':'form-control'}),'cantidad':forms.NumberInput(attrs={'class':'form-control'})}

