'''Crie um classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
métodos: envelhecer, engordar, emagrecer, crescer.
obs: por padrao, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, 
ela deve crescer 0,5cm.'''

lista = []
class pessoa:
    
    def __init__(self,nome,idade,peso,altura):
        self.nome = input('Digite seu nome: ').capitalize()
        self.idade = int(input('Qual a sua idade: '))
        self.peso = float(input('Qual o seu peso: '))
        self.altura = float(input('Qual a sua altura: '))
        lista.append([self.nome,self.idade,self.peso,self.altura])
        
    def ExibirInformacoesLista(self):
        print('-='*30)
        print(f'{"No.":<4}{"NOME":<13}{"IDADE":<10}{"PESO":<10}{"ALTURA"}')
        print('-='*30)
        for i, v in enumerate(lista):
            print(f'{i:<4}{v[0]:<13}{v[1]:<10}{v[2]:<10}{v[3]}')
        print('-='*30)

    def envelhecer(self):
        crescimento = 21 - self.idade
        if self.idade <= 21:
            print(f'\033[36mAté completar 21 anos, você cresce {crescimento*0.5}cm.\033[m')
        else:
            print('\033[34mVocê ja passou dos 21 anos, portanto, não crescerá mais...\033[m')
    def engordar_emagrecer(self):
        self.IMC = self.peso / (self.altura * self.altura)
        if self.IMC < 18.5:
            print(f'\033[33mSeu Índice de Massa Corporal é {self.IMC:.2f}Kg/m² e vc está magro(a), procure um nutricionista.\033[m')
        if self.IMC >= 18.50 and self.IMC <= 24.99:
            print(f'\033[32mSeu Índice de Massa Corporal é {self.IMC:.2f}Kg/m² e você está dentro do ideal.\033[m')
        else:
            if self.IMC > 24.99 and self.IMC <= 34.9:
                print(f'\033[33mSeu Índice de Massa Corporal é {self.IMC:.2f}Kg/m² e você está com obesidade grau 1.\033[m')
            if self.IMC > 34.9 and self.IMC <= 39.9:
                print(f'\033[35mSeu Índice de Massa Corporal é {self.IMC:.2f}Kg/m² e você está com obesidade grau 2.\033[m')
            if self.IMC > 39.9:
                print(f'\033[31mSeu Índice de Massa Corporal é {self.IMC:.2f}Kg/m² e você está com obesidade grau 3.\033[m')
    def MudarInformacoesPessoas(self):
        self.nome = input('Digite seu nome: ').capitalize()
        self.idade = int(input('Qual a sua idade: '))
        self.peso = float(input('Qual o seu peso: '))
        self.altura = float(input('Qual a sua altura: '))
        lista.append([self.nome,self.idade,self.peso,self.altura])
pessoas1 = pessoa('','','','')
#pessoas1.ExibirInformacoesLista()
# pessoas1.envelhecer()
# pessoas1.engordar_emagrecer()

while True:
    pessoas1.ExibirInformacoesLista()
    opcao = input('Digite a opção desejada: \n1-Alterar pessoa\n2-Informações IMC\n3-Calculo sobre crescimento\n4-Deseja sair\n->')
    if opcao == '1':
        pessoas1.MudarInformacoesPessoas()
    if opcao == '2':
        pessoas1.engordar_emagrecer()
    if opcao == '3':
        pessoas1.envelhecer()
    if opcao == '4':
        break

