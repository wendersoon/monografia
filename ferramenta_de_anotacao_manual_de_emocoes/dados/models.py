from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Text(models.Model):

    text = models.CharField('Texto', max_length=500)

    def __str__(self):
        return self.text
    

class Avaliação(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    alegria         = models.BooleanField('Alegria', default=False)
    raiva           = models.BooleanField('Raiva', default=False)
    tristeza        = models.BooleanField('Tristeza', default=False)
    medo            = models.BooleanField('Medo', default=False)
    nojo            = models.BooleanField('Nojo', default=False)
    surpresa        = models.BooleanField('Surpresa', default=False)
    neutro          = models.BooleanField('Neutro', default=False)
    foi_dificil     = models.BooleanField('Difícil', default=False)
    facil           = models.BooleanField('Fácil', default=False)
    nenhum_nem_outro= models.BooleanField('Mais ou Menos', default=False)

    class Meta:
        unique_together = ('user', 'text',)

    def __str__(self):
        return f'{self.text.text[:10]}'
    
    

