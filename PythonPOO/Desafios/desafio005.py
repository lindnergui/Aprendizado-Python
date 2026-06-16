from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []
    
    def adicionar_jogo(self, jogo):
        self.jogos_favoritos.append(jogo)
    
    def jogos(self):
        lista = '\n'.join(sorted(self.jogos_favoritos))
        return Panel(f'''
Nome real: [green]{self.nome}[/]
Nickname: [green]{self.nick}[/]
Jogos favoritos: 
[blue]{lista}[/]''', title='Gamer')

c1 = Gamer(nome='Guilherme', nick='Torpedo')
c1.adicionar_jogo('🕹️  Minecraft')
c1.adicionar_jogo('🕹️  Red Dead Redemption II ')
c1.adicionar_jogo('🕹️  Outer Wilds')

print(c1.jogos())

