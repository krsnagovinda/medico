from django.db import models
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField


class Record(models.Model):
    id_record = models.CharField(max_length=50, null=True)
    Expediente = RichTextUploadingField()

    def __str__(self):
        return self.id_record


class Paciente(models.Model):
    sexo_opciones= (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    id_Expediente = models.OneToOneField(Record, null=True, blank=True, on_delete=models.CASCADE)
    id_Paciente = models.CharField(max_length=50, null=True)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Nombre = models.CharField(max_length=50)
    Fecha_Nacimiento = models.DateField(blank=True, null=True, default='01/01/2000')
    Edad = models.PositiveSmallIntegerField(null=True, default='0')
    Sexo = models.CharField(max_length=1, choices=sexo_opciones, default="M")
    Estado_Civil = models.CharField(max_length=30, blank=True, null=True)
    Ocupacion = models.CharField(max_length=30, blank=True, null=True)
    Nacionalidad = models.CharField(max_length=30, blank=True, null=True)
    Domicilio = models.TextField(max_length=200, blank=True, null=True)
    Ciudad = models.CharField(max_length=30, blank=True, null=True, default="CDMX")
    Telefono = models.CharField(max_length=30, blank=True, null=True )
    Email = models.EmailField(null=True, blank=True)


    def get_fullname(self):
        return self.id_Paciente + ' - ' + self.Nombre + ' ' + self.Apellido_Paterno + ' ' + self.Apellido_Materno

    def __str__(self):
        return self.get_fullname()

class Consulta(models.Model):
    id_Consulta = models.CharField(max_length=20)
    id_Expediente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Fecha_consulta_creada = models.DateField(auto_now_add=True)
    Fecha_consulta_modificada = models.DateField(auto_now=True)
    Motivo = RichTextUploadingField(null=True, blank=True)
    Diagnostico = RichTextUploadingField(null=True, blank=True)

    def _str_(self):
        return self.id_Consulta + ' - ' + self.Fecha_consulta

class Antecedentes(models.Model):
    id_Expediente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    Antecedentes_Patologicos = RichTextUploadingField(blank=True, null=True)
    Antecedentes_Hereditarios = RichTextUploadingField(blank=True, null=True)
    Antecedentes_Quirurgicos = RichTextUploadingField(blank=True, null=True)
    Alergias = RichTextUploadingField(blank=True, null=True)
    Medicamentos = RichTextUploadingField(blank=True, null=True)

    def _str_(self):
        return self.id_Expediente

class Signos(models.Model):
    id_Expediente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    BMI = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Altura = models.DecimalField(max_digits=5, decimal_places=2)
    Peso = models.IntegerField()
    Temperatura = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    Frecuencia_Cardiaca = models.CharField(max_length=10, blank=True, null=True)
    Presion = models.CharField(max_length=10, blank=True, null=True)

    def _str_(self):
        return self.id_Expediente

class Galeria(models.Model):
    titulo = models.CharField(max_length=100)
    owner = models.OneToOneField(Paciente, on_delete=models.SET_NULL, blank=True, null=True)
    Fecha_galeria_creada = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

class Album(models.Model):
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    notas = RichTextUploadingField()
    image_1 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_2 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_3 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_4 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_5 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_6 = models.ImageField(null=True, blank=True, upload_to='photos')
    image_7 = models.ImageField(null=True, blank=True, upload_to='photos')
    file_1 = models.FileField(null=True, blank=True, upload_to='files')
    file_2 = models.FileField(null=True, blank=True, upload_to='files')
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        self.image_1.delete()
        self.image_2.delete()
        self.image_3.delete()
        self.image_4.delete()
        self.image_5.delete()
        self.image_6.delete()
        self.image_7.delete()
        self.file_1.delete()
        self.file_2.delete()

        super().delete(*args, **kwargs)
