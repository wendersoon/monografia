from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from .models import Text, Avaliação
import csv
from django.http import HttpResponse

#Leitura do arquivo para o banco de dados
# import csv

# def add_csv_to_db(csv_file_path):
#     with open(csv_file_path, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             text = row['tweet_text'] 
#             Text.objects.create(text=text)

# add_csv_to_db('/home/wendersom/Desktop/monografia/monografia/dados/tweets_pre_avalicao.csv')

class HomeView(TemplateView):
    template_name = 'home.html'


class AvaliaçãoView(View):
    template_name = 'avaliacao.html'

    def get(self, request, *args, **kwargs):
        text = Text.objects.exclude(avaliação__user=request.user).first()
        if not text:
            return render(request, 'fim.html')  # Renderiza a página de fim
        return render(request, self.template_name, {'text': text})


    def post(self, request, *args, **kwargs):
        print(request.POST)
        text_id = request.POST.get('text_id')
        text = Text.objects.get(id=text_id)
        avaliacao = Avaliação.objects.create(user=request.user, text=text)
       
        # Obtém a emoção selecionada no formulário
        selected_emotion = request.POST.get('gridRadios')
        
        # Atualiza a instância de Avaliação com a emoção selecionada
        if selected_emotion:
            if selected_emotion == 'alegria':
                avaliacao.alegria = True
            elif selected_emotion == 'raiva':
                avaliacao.raiva = True
            elif selected_emotion == 'tristeza':
                avaliacao.tristeza = True
            elif selected_emotion == 'medo':
                avaliacao.medo = True
            elif selected_emotion == 'nojo':
                avaliacao.nojo = True
            elif selected_emotion == 'surpresa':
                avaliacao.surpresa = True
            elif selected_emotion == 'neutro':
                avaliacao.neutro = True
        
        # Verifica se a tarefa foi difícil
        dificuldade = request.POST.get('gridRadios2')
        if dificuldade:
            if dificuldade == 'dificil':
                avaliacao.foi_dificil = True            
            elif dificuldade == 'facil':
                avaliacao.facil = True
            elif dificuldade == 'nenhum':
                avaliacao.nenhum_nem_outro = True
        
        # Salva a instância de Avaliação
        avaliacao.save()
        return redirect('avaliacao')
    

def export_avalicoes_to_csv(request):
    # Define o nome do arquivo e o tipo de conteúdo
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="avaliacoes.csv"'

    # Cria o writer CSV
    writer = csv.writer(response)
    
    # Escreve o cabeçalho do CSV
    writer.writerow([
        'User', 'Text', 'Alegria', 'Raiva', 'Tristeza', 'Medo',
        'Nojo', 'Surpresa', 'Neutro', 'Foi Dificil', 'Facil', 'Nenhum nem Outro'
    ])

    # Consulta todos os registros de Avaliação e escreve as linhas no CSV
    avaliacoes = Avaliação.objects.all()
    for avaliacao in avaliacoes:
        writer.writerow([
            avaliacao.user, avaliacao.text, avaliacao.alegria, avaliacao.raiva,
            avaliacao.tristeza, avaliacao.medo, avaliacao.nojo, avaliacao.surpresa,
            avaliacao.neutro, avaliacao.foi_dificil, avaliacao.facil, avaliacao.nenhum_nem_outro
        ])

    return response
