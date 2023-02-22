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
        print('=-'*30)
        print(f'{"No.":<4}{"COR":<3}{"CIRCUNFERÊNCIA":>20}{"MATERIAL":>20}')
        print(self.cor,self.circunferencia,self.material)  
        print('=-'*30)
        for i, v in enumerate(lista):
            print(f'{i:<4}{v[0]:<15}{v[1]:<20}{v[2]:<30}')
        
    def MudarInformacoesBola(self):
        self.cor = str(input('Qual a cor da bola? '))
        self.circunferencia = str(input('Qual a circunferência da bola? '))
        self.material = str(input('Qual o material da bola? '))
        lista.append([self.cor,self.circunferencia,self.material])

lista = []
bola1 = Bola('','','')

while True:
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Ss':
        opcao = input('Digite a opção desejada: \n1-Exibir informações\n2-Alterar bola\n->')
        if opcao == '1':
            bola1.ExibirInformacoesDestaBola()
            # chamar aqui o metodo de exibir informacoes
        else:
            bola1.MudarInformacoesBola()
            # chamar aqui o metodo de alteracao
    else:
        if pergunta in 'Nn':
            break
        
#for i, v in enumerate(lista):
    #print(f'{i:<4}{v[0]:<15}{v[1]:<20}{v[2]:<30}')
