from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import PacienteForm, RecordForm, ConsultaForm, AntecedentesForm, SignosForm, GaleriaForm, AlbumForm
from .models import Record, Paciente, Consulta, Antecedentes, Signos, Galeria, Album

# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard3(request):
    return render(request, 'dashboard3.html')

def prueba(request):
    return render(request, 'prueba.html')

# vistas CRUD de Paciente
class PacienteListView(ListView):
    model = Paciente
    login_required = True
    template_name = 'pacientes_lista.html'
    context_object_name = 'pacientes'
    redirect_field_name = 'pacientes_lista.html'

class UploadPacienteView(CreateView):
    model = Paciente
    login_required = True
    form_class = PacienteForm
    success_url = reverse_lazy('class_upload_signos')
    template_name = 'paciente/upload_paciente.html'

class PacienteDetailView(DetailView):
    model = Paciente
    login_required = True
    template_name = 'paciente/paciente_detail.html'
    queryset = Paciente.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Paciente, id=id_)

class PacienteUpdateView(UpdateView):
    model = Paciente
    login_required = True
    template_name = 'paciente/paciente_form.html'
    fields = ['id_Expediente',
              'id_Paciente',
              'Nombre',
              'Apellido_Paterno',
              'Apellido_Materno',
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
    success_url = reverse_lazy('class_pacientes_lista')

class PacienteDeleteView(DeleteView):
    model = Paciente
    login_required = True
    template_name = 'paciente/paciente_delete.html'
    success_url = reverse_lazy('class_pacientes_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Paciente, id=id_)


#   vistas CRUD de Record
class UploadRecordView(CreateView):
    model = Record
    login_required = True
    form_class = RecordForm
    success_url = reverse_lazy('class_upload_paciente')
    template_name = 'record/upload_record.html'

class RecordDetailView(DetailView):
    model = Record
    login_required = True
    template_name = 'record/paciente_record_detail.html'
    queryset = Record.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Record, id=id_)

class RecordUpdateView(UpdateView):
    model = Record
    login_required = True
    template_name = 'record/record_form.html'
    fields = ['id_record',
              'Expediente',
            ]
    success_url = reverse_lazy('class_pacientes_lista')

#   vistas CRUD de Consultas
class ConsultaListView(ListView):
    model = Consulta
    login_required = True
    template_name = 'consulta/consulta_lista.html'
    context_object_name = 'consulta'
    redirect_field_name = 'paciente/pacientes_lista.html'

class UploadConsultaView(CreateView):
    model = Consulta
    login_required = True
    form_class = ConsultaForm
    success_url = reverse_lazy('class_consultas_lista')
    template_name = 'consulta/upload_consulta.html'

class ConsultaDetailView(DetailView):
    model = Consulta
    login_required = True
    template_name = 'consulta/consulta_detail.html'
    queryset = Consulta.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Consulta, id=id_)

class ConsultaUpdateView(UpdateView):
    model = Consulta
    login_required = True
    template_name = 'consulta/consulta_form.html'
    fields = ['id_Consulta',
              'id_Expediente',
              'Motivo',
              'Diagnostico',
            ]
    success_url = reverse_lazy('class_consultas_lista')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    login_required = True
    template_name = 'consulta/consulta_delete.html'
    success_url = reverse_lazy('class_consultas_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Consulta, id=id_)


#   vistas CRUD de Antecedentes
class UploadAntecedentesView(CreateView):
    model = Antecedentes
    login_required = True
    form_class = AntecedentesForm
    success_url = reverse_lazy('class_pacientes_lista')
    template_name = 'antecedentes/upload_antecedentes.html'

class AntecedentesDetailView(DetailView):
    model = Antecedentes
    login_required = True
    template_name = 'antecedentes/antecedentes_detail.html'
    queryset = Antecedentes.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Antecedentes, id=id_)

class AntecedentesUpdateView(UpdateView):
    model = Antecedentes
    login_required = True
    template_name = 'antecedentes/antecedentes_form.html'
    fields = ['Antecedentes_Patologicos',
              'Antecedentes_Hereditarios',
              'Antecedentes_Quirurgicos',
              'Alergias',
              'Medicamentos',
            ]
    success_url = reverse_lazy('class_pacientes_lista')


#   vistas CRUD de Signos
class UploadSignosView(CreateView):
    model = Signos
    login_required = True
    form_class = SignosForm
    success_url = reverse_lazy('class_upload_antecedentes')
    template_name = 'signos/upload_signos.html'

class SignosDetailView(DetailView):
    model = Signos
    login_required = True
    template_name = 'signos/signos_detail.html'
    queryset = Signos.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Signos, id=id_)

class SignosUpdateView(UpdateView):
    model = Signos
    login_required = True
    template_name = 'signos/signos_form.html'
    fields = ['BMI',
              'Altura',
              'Peso',
              'Temperatura',
              'Frecuencia_Cardiaca',
              'Presion',
            ]
    success_url = reverse_lazy('class_pacientes_lista')


#   vistas CRUD de Galeria
class GaleriaListView(ListView):
    model = Galeria
    login_required = True
    template_name = 'galeria/galeria_lista.html'
    context_object_name = 'galeria'
    redirect_field_name = 'home.html'

class UploadGaleriaView(CreateView):
    model = Galeria
    login_required = True
    form_class = GaleriaForm
    success_url = reverse_lazy('class_galeria_lista')
    template_name = 'galeria/upload_galeria.html'

class GaleriaUpdateView(UpdateView):
    model = Galeria
    login_required = True
    template_name = 'galeria/galeria_form.html'
    fields = ['titulo', 'owner']
    success_url = reverse_lazy('class_galeria_lista')

class GaleriaDetailView(DetailView):
    model = Galeria
    login_required = True
    template_name = 'galeria/galeria_detail.html'
    queryset = Galeria.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Galeria, id=id_)

class GaleriaDeleteView(DeleteView):
    model = Galeria
    login_required = True
    template_name = 'galeria/galeria_delete.html'
    success_url = reverse_lazy('class_galeria_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Galeria, id=id_)


#   vistas CRUD de Album
class AlbumListView(ListView):
    model = Album
    login_required = True
    template_name = 'album/album_lista.html'
    context_object_name = 'album'
    redirect_field_name = 'home.html'

class UploadAlbumView(CreateView):
    model = Album
    login_required = True
    form_class = AlbumForm
    success_url = reverse_lazy('class_album_lista')
    template_name = 'album/upload_album.html'

class AlbumDetailView(DetailView):
    model = Album
    login_required = True
    template_name = 'album/album_detail.html'
    queryset = Album.objects.all()

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Album, id=id_)

class AlbumUpdateView(UpdateView):
    model = Album
    login_required = True
    template_name = 'album/album_form.html'
    fields = ['galeria', 'titulo', 'notas', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'file_1', 'file_2']
    success_url = reverse_lazy('class_album_lista')

class AlbumDeleteView(DeleteView):
    model = Album
    login_required = True
    template_name = 'album/album_delete.html'
    success_url = reverse_lazy('class_album_lista')

    def get_objects(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Album, id=id_)
