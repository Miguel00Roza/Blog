from django.db import models

class Topico(models.Model):
    nome = models.CharField()

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.PROTECT)
    texto = models.TextField(max_length=1000)
    data_de_envio = models.DateTimeField(auto_now_add=True)
    usuario = models.TextField()

    def __str__(self):
        if len(self.texto) > 50:
            return f"{self.topico} - {self.texto[:50]}..."
        else:
            return f"{self.topico} - {self.texto}"
