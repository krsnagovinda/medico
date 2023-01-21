from django.contrib import admin
from .models import Paciente, Record, Consulta, Antecedentes, Signos, Galeria, Album

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    fields= ['id_record', 'Expediente']
    list_display = ['id_record']
    list_filter = ['id_record']
    search_fields = ['id_record']

class PacienteAdmin(admin.ModelAdmin):
    fields =['id_Expediente', 'id_Paciente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Fecha_Nacimiento', 'Edad', 'Sexo', 'Estado_Civil', 'Ocupacion', 'Nacionalidad', 'Domicilio', 'Ciudad', 'Telefono', 'Email']
    list_display =['id_Expediente', 'id_Paciente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']
    list_filter =[]
    search_fields =['id_Expediente', 'Nombre', 'Apellido_Paterno', 'Apellido_Materno']

class ConsultaAdmin(admin.ModelAdmin):
    fields =['id_Consulta', 'id_Expediente', 'Motivo', 'Diagnostico']
    list_display =['id_Consulta', 'id_Expediente', 'Fecha_consulta_creada', 'Fecha_consulta_modificada', 'Motivo' ]
    list_filter =[ 'id_Consulta', 'id_Expediente', 'Fecha_consulta_creada', 'Fecha_consulta_modificada']
    search_fields =['id_Consulta', 'id_Expediente',]

class AntecedentesAdmin(admin.ModelAdmin):
    fields= ['id_Expediente', 'Antecedentes_Patologicos', 'Antecedentes_Hereditarios', 'Antecedentes_Quirurgicos', 'Alergias', 'Medicamentos']
    list_display = ['id_Expediente', 'Alergias', 'Medicamentos']
    list_filter = ['id_Expediente']
    search_fields = ['id_Expediente']

class SignosAdmin(admin.ModelAdmin):
    fields= ['id_Expediente', 'BMI', 'Altura', 'Peso', 'Temperatura', 'Frecuencia_Cardiaca']
    list_display = ['id_Expediente', 'Altura', 'Peso', 'BMI']
    list_filter = ['id_Expediente']
    search_fields = ['id_Expediente', 'Altura', 'Peso', 'BMI']

class GaleriaAdmin(admin.ModelAdmin):
    fields= ['titulo', 'owner']
    list_display = ['titulo', 'owner']
    list_filter = ['titulo', 'owner']
    search_fields = ['titulo', 'owner']

class AlbumAdmin(admin.ModelAdmin):
    fields= ['galeria', 'titulo', 'notas', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'file_1', 'file_2']
    list_display = ['titulo', 'galeria']
    list_filter = ['titulo', 'galeria']
    search_fields = ['titulo', 'galeria']


admin.site.register(Record, RecordAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Antecedentes, AntecedentesAdmin)
admin.site.register(Signos, SignosAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Album, AlbumAdmin)
