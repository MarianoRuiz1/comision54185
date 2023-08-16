from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Curso, Entregable, Profesor, Estudiante, Post
from .forms import EntregableForm, ProfesorForm, EstudianteForm, CursoSearchForm, PostForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

# Vistas para el modelo Curso
class CursoListView(ListView):
    model = Curso
    template_name = 'curso_list.html'
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    fields = ['nombre', 'numero_comision']
    template_name = 'curso_create.html'
    success_url = reverse_lazy('app1:curso_list')

# Vistas para el modelo Entregable
class EntregableCreateView(CreateView):
    model = Entregable
    form_class = EntregableForm
    template_name = 'entregable_form.html'
    success_url = reverse_lazy('app1:index')

class EntregableListView(ListView):
    model = Entregable
    template_name = 'entregable_list.html'
    context_object_name = 'entregables'

# Vistas para el modelo Profesor
class ProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor_form.html'
    success_url = reverse_lazy('app1:index')

class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesor_list.html'
    context_object_name = 'profesores'

# Vistas para el modelo Estudiante
class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiante_form.html'
    success_url = reverse_lazy('app1:index')

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante_list.html'
    context_object_name = 'estudiantes'

# Vista para buscar cursos por nombre
class CursoSearchView(FormView):
    template_name = 'buscar_cursos.html'
    form_class = CursoSearchForm

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return self.render_to_response({'form': form, 'cursos': cursos})

# Vistas para el modelo Curso
class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nombre', 'numero_comision']
    template_name = 'curso_update.html'
    success_url = reverse_lazy('app1:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'curso_confirm_delete.html'
    success_url = reverse_lazy('app1:curso_list')

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('app1:post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('app1:post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('app1:post_list')

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('app1:login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
            return redirect('app1:index')  
        return response

class CustomLogoutView(LogoutView):
    next_page = 'app1:login'