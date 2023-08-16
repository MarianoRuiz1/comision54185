from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('curso_list/', views.CursoListView.as_view(), name='curso_list'),
    path('curso_create/', views.CursoCreateView.as_view(), name='curso_create'),
    path('entregables/', views.EntregableListView.as_view(), name='lista_entregables'),
    path('profesores/', views.ProfesorListView.as_view(), name='lista_profesores'),
    path('alumnos/', views.EstudianteListView.as_view(), name='lista_alumnos'),
    path('entregable/create/', views.EntregableCreateView.as_view(), name='entregable-create'),
    path('profesor/create/', views.ProfesorCreateView.as_view(), name='profesor-create'),
    path('estudiante/create/', views.EstudianteCreateView.as_view(), name='estudiante-create'),
    path('buscar-por-nombre/', views.CursoSearchView.as_view(), name='buscar_cursos_por_nombre'),
    path('curso_update/<int:pk>/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('curso_delete/<int:pk>/', views.CursoDeleteView.as_view(), name='curso_delete'),
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

