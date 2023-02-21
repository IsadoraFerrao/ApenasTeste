'''Crie uma classe que modele uma bola: 
Atributos: Cor, circunferência, material.
Métodos: trocaCor e mostraCor'''

class Bola:

    def __init__(self,cor,circunferencia,material):
        self.cor = str(input('Qual a cor da bola? '))
        self.circunferencia = str(input('Qual a circunferência da bola? '))
        self.material = str(input('Qual o material da bola? '))

    def ExibirInformacoesDestaBola(self):
       print(self.cor,self.circunferencia,self.material)  



while True:

    bola1 = Bola('','','')
    bola1.ExibirInformacoesDestaBola()
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
