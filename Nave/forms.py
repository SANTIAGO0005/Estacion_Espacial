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
              fields=['nombre','modelo','fabricante','categoria','anio_fabricacion', 'peso', 'numero_motores', 'numero_tripulantes',
                      'potencia','objetivo','capacidad_carga',
                      'activo','combustible']
              labels={'nombre':'Nombre','modelo':'Modelo','fabricante':'Fabricante','categoria':'Categoria','anio_fabricacion':'Año de Fabricacion',
                      'peso': 'Peso KG', 'numero_motores': 'Numero de Motores', 'numero_tripulantes': 'Numero de Tripulantes', 'potencia': 'Potencia', 'objetivo': 'Objetivo', 'capacidad_carga': 'Capacidad de carga T', 'activo': 'Activo','combustible':'Combustible' }
              widgets={'nombre':forms.TextInput(attrs={'class':'form-control'}),'modelo':forms.TextInput(attrs={'class':'form-control'}),'fabricante':forms.TextInput(attrs={'class':'form-control'}),'categoria':forms.Select(attrs={'class':'form-control'}),'anio_fabricacion':forms.NumberInput(attrs={'class':'form-control'}),
                       'peso':forms.NumberInput(attrs={'class': 'form-control'}), 'numero_motores':forms.NumberInput(attrs={'class': 'form-control'}), 'numero_tripulantes':forms.NumberInput(attrs={'class': 'form-control'}), 'potencia':forms.NumberInput(attrs={'class': 'form-control'}), 'objetivo':forms.TextInput(attrs={'class': 'form-control'}), 'capacidad_carga':forms.NumberInput(attrs={'class': 'form-control'}), 'activo':forms.CheckboxInput(attrs={'class': 'form-control'}), 'combustible':forms.TextInput(attrs={'class': 'form-control'})}

class InventarioForm(forms.ModelForm):
      class Meta:
         model=Inventario
         fields=['nave','cantidad']
         labels={'nave':'Nave','cantidad':'Cantidad'}
         widgets={'nave':forms.Select(attrs={'class':'form-control'}),'cantidad':forms.NumberInput(attrs={'class':'form-control'})}

