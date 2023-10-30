#from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, TemplateView
from gestioncurriculum.models import Usuario, Curriculum, SolicitudDeReemplazo, PuntuacionDeCandidato
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        is_active = request.POST['is_active']
        is_staff = request.POST['is_staff']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        usuario = Usuario(username=username, email=email, is_active=is_active, is_staff=is_staff, password1=password1, password2=password2)
        usuario.save()
        return render(request, 'registro_exitoso.html')
    else:
        return render(request, 'registro.html')
    
#class RegistroView(CreateView):
    #model = Usuario
    #form_class = UserCreationForm
    #template_name = 'registro.html'

    #def form_valid(self, form):
        #form.instance.is_staff = False
        #form.save()
        #return super().form_valid(form)



class InicioDeSesionView(LoginView):
    template_name = 'inicio_de_sesion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Agrega un mensaje de error si el usuario no está autenticado.
        if self.request.user.is_anonymous:
            context['error_login'] = True

        return context


class IndexView(TemplateView):
    template_name = 'index.html'


class SubirCurriculumView(LoginRequiredMixin, CreateView):
    model = Curriculum
    fields = ['title', 'experience', 'skills', 'education']


class SolicitudDeReemplazoView(LoginRequiredMixin, CreateView):
    model = SolicitudDeReemplazo
    fields = ['title', 'start_date', 'end_date']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)


class ListaDeCandidatosView(LoginRequiredMixin, ListView):
    model = PuntuacionDeCandidato

    def get_queryset(self):
        return PuntuacionDeCandidato.objects.filter(
            solicitud_de_reemplazo=self.kwargs['pk']
        ).order_by('-score')


#Crear un sistema de puntajes que calcule el puntaje de cada candidato tomando en cuenta la experiencia,habilidades,educacion y ubicacion
