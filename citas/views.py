from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm, IngresoForm, SolicitarCitaForm, CancelarCitaForm
from .models import Cita, HistorialMedico

# Vista de registro de usuario
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = RegistroForm()
    return render(request, 'citas/registro.html', {'form': form})

# Vista de ingreso de usuario
def login_view(request):
    if request.method == 'POST':
        form = IngresoForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')  # Redirige a la página principal
            else:
                print("Autenticación fallida")  # Esto es solo para depuración
    else:
        form = IngresoForm()
    return render(request, 'citas/login.html', {'form': form})

# Vista de cierre de sesión
def logout_view(request):
    logout(request)
    return redirect('login')

# Vista para solicitar una cita
def solicitar_cita(request):
    if request.method == 'POST':
        form = SolicitarCitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            cita.estado = 'Pendiente'
            cita.save()
            return redirect('ver_citas')  # Redirige a la lista de citas
    else:
        form = SolicitarCitaForm()
    return render(request, 'citas/solicitar_cita.html', {'form': form})

# Vista para cancelar una cita
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, usuario=request.user)
    if request.method == 'POST':
        cita.estado = 'Cancelada'
        cita.save()
        return redirect('ver_citas')  # Redirige a la lista de citas después de la cancelación
    return render(request, 'citas/cancelar_cita.html', {'cita': cita})

# Vista para ver todas las citas del usuario
def ver_citas(request):
    citas = Cita.objects.filter(usuario=request.user)
    return render(request, 'citas/ver_citas.html', {'citas': citas})

# Vista para ver el historial médico del usuario
def historial_medico(request):
    historial = HistorialMedico.objects.filter(usuario=request.user)
    return render(request, 'citas/historial_medico.html', {'historial': historial})


from django.shortcuts import render

def home(request):
    return render(request, 'citas/home.html')
