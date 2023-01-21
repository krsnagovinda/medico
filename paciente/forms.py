from django.forms import ModelForm, Textarea, EmailInput, DateInput
from . models import Paciente, Record, Consulta, Antecedentes, Signos, Galeria, Album
from django import forms
from decimal import Decimal, DecimalException
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['id_record','Expediente']
        widgets ={'Expediente': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 3})),}
        labels = {
            'id_record' : 'Número de Ficha Clínica *',
            'Expediente' : 'Observaciones de Expediente *',
                }

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields =[
            'id_Expediente',
            'id_Paciente',
            'Apellido_Paterno',
            'Apellido_Materno',
            'Nombre',
            'Fecha_Nacimiento',
            'Edad',
            'Sexo',
            'Estado_Civil',
            'Ocupacion',
            'Nacionalidad',
            'Domicilio',
            'Ciudad',
            'Telefono',
            'Email',
            ]

        widgets ={'Domicilio': Textarea(attrs={'cols': 3, 'rows': 4 }),
                  'Email': EmailInput(),
                  'Fecha_Nacimiento': DateInput(),}
        labels = {
            'id_Expediente' : 'Numero de Ficha *',
            'id_Paciente' : 'Número Id de Paciente * ',
            'Apellido_Paterno' : 'Apellido Paterno * ',
            'Apellido_Materno' : 'Apellido Materno * ',
            'Nombre' : 'Nombre(s) * ',
            'Fecha_Nacimiento' : 'Fecha de Nacimiento (dd/mm/aaaa) * ',
            'Edad' : 'Edad *',
            'Sexo' : 'Sexo *',
            'Ocupacion' : 'Ocupación:',
            'Domicilio' : 'Domicilio * ',
            'Ciudad' : 'Ciudad * ',
            'Telefono' : 'Teléfono o Celular * ',
            'Email' : 'E-mail:',
        }

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'id_Consulta',
            'id_Expediente',
            'Motivo',
            'Diagnostico',
            ]
        widgets ={'Motivo': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),
                  'Diagnostico': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),}
        labels = {
            'id_Consulta' : 'Numero de Consulta *',
            'id_Expediente' : 'Numero de Ficha *',
            'Motivo' : 'Motivo *',
            'Diagnostico' : 'Diagnóstico',

        }

class AntecedentesForm(ModelForm):
    class Meta:
        model = Antecedentes
        fields = [
            'id_Expediente',
            'Antecedentes_Patologicos',
            'Antecedentes_Hereditarios',
            'Antecedentes_Quirurgicos',
            'Alergias',
            'Medicamentos',]

        widgets = {'Antecedentes_Patologicos': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),
                    'Antecedentes_Hereditarios': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),
                    'Antecedentes_Quirurgicos': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),
                    'Alergias': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),
                    'Medicamentos': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),}

        labels = {
            'id_Expediente' : 'Número de Ficha *',
            'Antecedentes_Patologicos' : 'Antecedentes Patológicos *',
            'Antecedentes_Quirurgicos' : 'Antecedentes Quirúrgicos',}


class SignosForm(ModelForm):
    class Meta:
        model = Signos
        fields = [
            'id_Expediente',
            'Altura',
            'Peso',
            'BMI',
            'Temperatura',
            'Frecuencia_Cardiaca',
            'Presion']

        labels = {
            'id_Expediente': 'Número de Ficha *',
            'BMI':  'Índice de masa muscular (BMI)',
            'Altura': 'Altura en cm*',
            'Peso': 'Peso en Kg *',
            'Temperatura': 'Temperatura en °C',
            'Frecuencia_Cardiaca': 'Frecuencia Cardiaca, latidos por min.',
            'Presion': 'Presión mm/Hg',
            }

        widgets = {
            ''
        }

class GaleriaForm(ModelForm):
    class Meta:
        model = Galeria
        fields = ['titulo', 'owner']

        labels = {'titulo': 'Título de Galería *',
                  'owner': 'Paciente'}

        widgets = {''}

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['galeria','titulo', 'notas', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'file_1', 'file_2']

        labels = { 'galeria': 'Nombre de Galería *',
                   'titulo': 'Título de Album *',
                   'notas': 'Notas *',
                   'image_1': 'Imágen 1',
                   'image_2': 'Imágen 2',
                   'image_3': 'Imágen 3',
                   'image_4': 'Imágen 4',
                   'image_5': 'Imágen 5',
                   'image_6': 'Imágen 6',
                   'image_7': 'Imágen 7',
                   'file_1': 'Archivo 1',
                   'file_2': 'Archivo 2',
                    }

        widgets = {'notas': forms.CharField(widget=CKEditorUploadingWidget(attrs={'cols': 3, 'rows': 4 })),}
