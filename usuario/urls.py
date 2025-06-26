from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('inicio/', views.inicio_view, name='inicio_page'),

    path('', views.dashboard, name='dashboard'),

    ########################################################################
    # **REPORTES**
    #######################################################################

    path('reportes/', views.reportes_view, name='reportes_page'),

    # **URL PARA EGRESADOS**#############################################################################
    path('reportes/egresados/', views.egresados_report, name='egresados_report'),

    # **URL PARA EXPORTAR EGRESADOS (URL separada)**
    path('reportes/egresados/export/excel/', views.export_egresados_excel, name='export_egresados_excel'),
    ######################################################################################################
    # **FIN EGRESADOS REPORTES**
    ######################################################################################################

     # **URL PARA EXAMENES**
    path('reportes/examenes/', views.examenes_report, name='examenes_report'),

    # **URL PARA EXPORTAR EXAMENES (URL separada)**
    path('reportes/examenes/export/excel/', views.export_examenes_excel, name='export_examenes_excel'),
    ######################################################################################################
    # **FIN EXAMENES REPORTES**
    ######################################################################################################

    # **NUEVA URL PARA CURSADAS**
    path('reportes/cursadas/', views.cursadas_report, name='cursadas_report'),

    # **NUEVA URL PARA EXPORTAR CURSADAS (URL separada)**
    path('reportes/cursadas/export/excel/', views.export_cursadas_excel, name='export_cursadas_excel'),
    ######################################################################################################
    # **FIN CURSADAS REPORTES**
    ######################################################################################################

    # **NUEVA URL PARA PROMEDIOS**
    path('reportes/promedio_historico/', views.promedio_historico_report, name='promedio_historico_report'),

    # **NUEVA URL PARA EXPORTAR PROMEDIOS (URL separada)**
    path('reportes/promedio_historico/export/excel/', views.export_promedio_historico_excel, name='export_promedio_historico_excel'),
    ######################################################################################################
    # **FIN PROMEDIOS REPORTES**
    ######################################################################################################

    # **NUEVA URL PARA RESULTADO DE CURSADAS**
    path('reportes/resultado_cursada/', views.resultado_cursadas_report, name='resultado_cursada_report'),


    #**NUEVA URL PARA EXPORTAR RESULTADO DE CURSADAS (URL separada)**
    path('reportes/resultado_cursada/export/excel/', views.export_resultado_cursadas_excel, name='export_resultado_cursadas_excel'),
    ######################################################################################################
    # **FIN RESULTADO DE CURSADAS REPORTES**
    ######################################################################################################

    # **NUEVA URL PARA DOCENTES POR COMISION**
    path('reportes/docentes/', views.docentes_x_comision_report, name='docentes_x_comision_report'),

    #**NUEVA URL PARA EXPORTAR RESULTADO DE CURSADAS (URL separada)**
    path('reportes/docentes/export/excel/', views.export_docentes_x_comision_excel, name='export_docentes_x_comision_excel'),

    ######################################################################################################
    # **FIN RDOCENTES POR COMISION**
    ######################################################################################################

    ########################################################################
    # **ESTADISTICAS**
    #######################################################################

    path('estadisticas/', views.estadisticas_view, name='estadisticas_page'),

    ########################################################################
    # **NUEVAS URLS PARA ESTADISTICAS**
    #######################################################################


    # **NUEVA URL PARA INGRESANTES X CARRERA**
    path('estadisticas/ingresantes/', views.ingresantes_por_carrera_view, name='ingresantes_por_carrera'),

    # **NUEVA URL PARA EXPORTAR INGRESANTES (URL separada)**
    path('estadisticas/ingresantes/export/excel/', views.export_ingresantes_excel, name='export_ingresantes_excel'),

    # **NUEVA URL PARA DOCENTES CANTIDAD**
    path('estadisticas/docentes/', views.docentes_x_carrera_dpto_view, name='docentes_x_carrera_dpto'),

    # **NNUEVA URL PARA EXPORTAR DONCENTES  CANTIDAD (URL separada) **
    path('estadisticas/docentes/export/excel/', views.export_docentes_cardpto_excel, name='export_docentes_cardpto_excel'),

    # **NUEVA URL PARA RETENIDOS PRIMER AÑO**
    path('estadisticas/retenidos/', views.retenidos_por_carrera_view, name='retenidos_por_carrera'),

    # **NNUEVA URL PARA EXPORTAR RETENIDOS PRIMER AÑO **
    path('estadisticas/retenidos/export/excel/', views.export_retenidos_por_carrera_view, name='export_retenidos_por_carrera_view'),

    # **NUEVA URL PARA Rango Etario**
    path('estadisticas/etarios/', views.rango_etario_view, name='rango_etario_view'),

    # **NNUEVA URL PARA RANGO ETARIO EXCEL **
    path('estadisticas/etarios/export/excel/', views.export_rango_etario_excel, name='export_rango_etario_excel'),

     # **NUEVA URL PARA EGRESADOS POR ANIO DE INGRESO**
    path('estadisticas/egresados/', views.egresados_x_anio_view, name='egresados_x_anio_view'),




]

