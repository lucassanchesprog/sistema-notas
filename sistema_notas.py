print("Sistema de Verificação de Notas")

nome = input("Qual o nome do aluno? ")
nota = float(input("Qual a nota do aluno? "))

if nota >= 7:
    print(nome, "- Aprovado!")
elif nota >= 5:
    print(nome, "- Recuperação!")
else:
    print(nome, "- Reprovado!")