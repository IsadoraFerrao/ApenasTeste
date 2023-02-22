'''Crie uma classe que modele uma bola: 
Atributos: Cor, circunferência, material.
Métodos: trocaCor e mostraCor'''

class Bola:

    def __init__(self,cor,circunferencia,material):
        self.cor = str(input('Qual a cor da bola? '))
        self.circunferencia = str(input('Qual a circunferência da bola? '))
        self.material = str(input('Qual o material da bola? '))
        lista.append([self.cor,self.circunferencia,self.material])
        # lista.append(self.circunferencia)
        # lista.append(self.material)

    def ExibirInformacoesDestaBola(self):
       print(self.cor,self.circunferencia,self.material)  
    

lista = []

while True:
    bola1 = Bola('','','')
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Ss':
        pass
    else:
        if pergunta in 'Nn':
            break
print('=-'*30)
print(f'{"No.":<4}{"COR":<3}{"CIRCUNFERÊNCIA":>20}{"MATERIAL":>20}')
print('=-'*30)
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<15}{v[1]:<20}{v[2]:<30}')