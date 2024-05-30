from django.urls import path

from .views import HomeView, AvaliaçãoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('avaliacao', AvaliaçãoView.as_view(), name='avaliacao')
]
