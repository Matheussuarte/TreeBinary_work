from Tree import Tree

class Aluno:
    def __init__(self, nome, matricula, curso, nota):

        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.nota = nota

    def __str__(self):

        return (
            f"Nome: {self.nome} | "
            f"Matrícula: {self.matricula} | "
            f"Curso: {self.curso} | "
            f"Nota: {self.nota}"
        )

class Sistema:
    def __init__(self):

        # árvore por nota
        self.notas = Tree(lambda aluno: aluno.nota)


        # árvore por nome
        self.nomes = Tree(lambda aluno: aluno.nome.lower())

    def cadastrar(self):
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        curso = input("Curso: ")
        nota = float(input("Nota: "))

        aluno = Aluno(
            nome,
            matricula,
            curso,
            nota
        )

        self.notas.add(aluno)
        self.nomes.add(aluno)

    def rankingMaiorMenor(self):
        print("\nRanking:")
        self.notas.reverseOrder()


    def ordemAlfabetica(self):
        print("\nAlunos A-Z:")
        self.nomes.inOrder()


    def buscarNome(self):
        nome = input("Nome do aluno: ")
        resultado = self.nomes.search(
            nome.lower()
        )
        if resultado:
            print(resultado)
        else:
            print("Aluno não encontrado")

def menu():
    sistema = Sistema()
    while True:
        print("""
====== SISTEMA DE ALUNOS ======

1 - Cadastrar aluno
2 - Ranking de notas
3 - Lista A-Z
4 - Buscar aluno
0 - Sair
""")

        op = input("Opção: ")
        if op == "1":
            sistema.cadastrar()

        elif op == "2":
            sistema.rankingMaiorMenor()

        elif op == "3":
            sistema.ordemAlfabetica()

        elif op == "4":
            sistema.buscarNome()

        elif op == "0":
            break

menu()