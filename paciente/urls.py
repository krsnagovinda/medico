from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from paciente import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

        path('dashboard3/', views.dashboard3, name='dashboard3'),
        path('prueba/', views.prueba, name='prueba'),

        path('lista_general/', login_required(views.PacienteListView.as_view()), name='class_pacientes_lista'),
        path('upload_paciente/', login_required(views.UploadPacienteView.as_view()), name='class_upload_paciente'),
        path('paciente/<int:pk>/', views.PacienteDetailView.as_view(), name='class_detail'),
        path('paciente_delete/<int:pk>/', views.PacienteDeleteView.as_view(), name='class_delete'),
        path('paciente_update/<int:pk>/', views.PacienteUpdateView.as_view(), name='class_update'),

        path('upload_record/', views.UploadRecordView.as_view(), name='class_upload_record'),
        path('record/<int:pk>/', views.RecordDetailView.as_view(), name='class_detail_record'),
        path('record_update/<int:pk>/', views.RecordUpdateView.as_view(), name='class_update_record'),

        path('consultas_lista/', views.ConsultaListView.as_view(), name='class_consultas_lista'),
        path('upload_consulta', views.UploadConsultaView.as_view(), name='class_upload_consulta'),
        path('consulta/<int:pk>/', views.ConsultaDetailView.as_view(), name='class_detail_consulta'),
        path('consulta_update/<int:pk>/', views.ConsultaUpdateView.as_view(), name='class_update_consulta'),
        path('consulta_delete/<int:pk>/', views.ConsultaDeleteView.as_view(), name='class_delete_consulta'),

        path('antecedentes/<int:pk>/', views.AntecedentesDetailView.as_view(), name='class_detail_antecedentes'),
        path('antecedentes_update/<int:pk>/', views.AntecedentesUpdateView.as_view(), name='class_update_antecedentes'),
        path('upload_antecedentes', views.UploadAntecedentesView.as_view(), name='class_upload_antecedentes'),

        path('upload_signos/', views.UploadSignosView.as_view(), name='class_upload_signos'),
        path('signos/<int:pk>/', views.SignosDetailView.as_view(), name='class_detail_signos'),
        path('signos_update/<int:pk>/', views.SignosUpdateView.as_view(), name='class_update_signos'),

        path('galeria_lista/', views.GaleriaListView.as_view(), name='class_galeria_lista'),
        path('upload_galeria', views.UploadGaleriaView.as_view(), name='class_upload_galeria'),
        path('galeria/<int:pk>/', views.GaleriaDetailView.as_view(), name='class_detail_galeria'),
        path('galeria_update/<int:pk>/', views.GaleriaUpdateView.as_view(), name='class_update_galeria'),
        path('galeria_delete/<int:pk>/', views.GaleriaDeleteView.as_view(), name='class_delete_galeria'),

        path('album_lista/', views.AlbumListView.as_view(), name='class_album_lista'),
        path('upload_album', views.UploadAlbumView.as_view(), name='class_upload_album'),
        path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='class_detail_album'),
        path('album_update/<int:pk>/', views.AlbumUpdateView.as_view(), name='class_update_album'),
        path('album_delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='class_delete_album'),


        ]
