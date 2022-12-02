from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime(), '%y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo ')
            return
        
        if self.falando:
            print(f'{self.nome} ja esta falando ')
            return
        print(f'{self.nome} falou sobre {assunto}')
        self.falando = True
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

        variavel = 'valor' #não disponivel fora deste metodo
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento} ')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo ')
            return

        print(f'{self.nome} parou de comer. ')
        self.comendo = False

    def get_ano_nascimento(self):
        return  self.ano_atual - self.idade()
    

p1 = Pessoa('luiz', 29)
p2 = Pessoa('joão', 49)
print(p1.get_ano_nascimento())
p1.comer('maça')
p1.falar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
p1.comer('banana')
p1.falar('Poo')
p1.parar_comer()
p1.falar('agora consegui falar parei de comer')
p1.comer('banana')
p1.parar_falar()
p1.comer('agora consegui comer, parei de falar')
p1.parar_comer()
p1.parar_comer()

    

#git reset soft
#git reset mixed