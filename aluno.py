
'''

oi prof, sou eu Ana do 3J 

'''
#resultado final diretora
qtdalunos = int(input("digite a quantidade de alunos"))
qtdinformados = 0
while qtdinformados < qtdalunos :
    nome = input("digite o nome do aluno:")
    nota = float(input("digite a nota"))
    if nota >= 6.0:
        aprovado = True
    else:
        aprovado = False
    if not aprovado:
        print("Infelizmente você reprovou")
    qtdinformados+1
    
print("todos os alunos informados")