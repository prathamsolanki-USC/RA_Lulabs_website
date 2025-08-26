from django.urls import path
from . import views

app_name = 'query_interface'

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.query_view, name='query'),
    path('api/query/', views.api_query, name='api_query'),
    path('results/', views.results_view, name='results'),
    path('documentation/', views.documentation_view, name='documentation'),
]
