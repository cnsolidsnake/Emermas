from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('solicitar_cita/', views.solicitar_cita, name='solicitar_cita'),
    path('cancelar_cita/<int:cita_id>/', views.cancelar_cita, name='cancelar_cita'),
    path('ver_citas/', views.ver_citas, name='ver_citas'),
    path('historial_medico/', views.historial_medico, name='historial_medico'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home')),  # Redirige la raíz a la vista 'home'
    path('registro/', include('app_name.urls')),
]
