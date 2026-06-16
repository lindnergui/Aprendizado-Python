class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    def get_nota(self): # Método Getter
        return self._nota

    def set_nota(self, valor): # Método Setter
        self._nota