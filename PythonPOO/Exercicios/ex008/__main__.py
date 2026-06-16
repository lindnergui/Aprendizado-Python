from PythonPOO.Exercícios.ex008 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("João", "Matemática", 8.5)
    av1.nota = 9.0
    inspect(av1, private=True)

if __name__ == "__main__":
    main()