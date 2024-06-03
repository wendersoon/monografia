from django.urls import path

from .views import HomeView, AvaliaçãoView, export_avalicoes_to_csv

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('avaliacao', AvaliaçãoView.as_view(), name='avaliacao'),
    path('export/csv/', export_avalicoes_to_csv, name='export_avalicoes_to_csv'), #endpoint para exportar csv do models Avaliação

]
