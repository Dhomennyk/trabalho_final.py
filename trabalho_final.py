class Sorteio:
    def _init_(self):
        self.alunos = []

    def add_aluno(self, nome, nota):
        self.alunos.append({"nome": nome, "nota": nota})

    def sorteio_classificatorio(self):
      if len(self.alunos) == 0:
        print("Nenhum aluno foi adicionado.")
        return

      self.aluno.sort(key=lambda x: x["nota"]
  reverse= True)

      classificacao = []
      for aluno in self.alunos:
        if aluno["nota"] >= 90:
            classificacao.append({"nome" :
 aluno["nome"], "classificacao": "A"})
        elif aluno["nota"] >= 70:
            classificacao.append({"nome":
aluno["nome"], "classicacao": "B"})
          elif aluno["nota"] >= 50:
              classificacao.append({"nome":
aluno["nome"], "classificacao": "C"})
            else:
                classificacao.append({"nome":
aluno["nome"], "classificacao": "D"})

        for aluno in classificacao:
            print(f"Aluno: {aluno['nome']}-
Classificacao: {aluno['Classificacao']}")


sorteio = Sorteio()
while True:
    nome = input("Digite o nome do aluno (ou 0 para parar): ")
    if nome == "0":
        break
      nota = float(input("Digite a nota do aluno:"))
      sorteio.add_aluno(nome, nota)
sorteio.sorteio_classificatorio()
