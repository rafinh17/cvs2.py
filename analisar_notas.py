import csv

# Lista para armazenar as notas
notas = []

# Abrindo o arquivo CSV
with open('alunos.csv', mode='r', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
   
    print("Alunos com nota maior ou igual a 7:")
   
    for linha in leitor:
        nome = linha['nome']
        nota = float(linha['nota'])  # Convertendo para número
        notas.append(nota)  # Salvando nota para média depois
       
        if nota >= 7:
            print(f"- {nome}")

# Calculando média das notas
media = sum(notas) / len(notas)
print(f"\nMédia da turma: {media:.2f}")