'''

oi prof, sou eu Ana do 3J 

'''
try:
    valor = float(input("Digite o valor do produto"))
    if valor > 100.00:
       print("valor não permitido")
       print("Bom dia")
except ValueError:
    print("Digitar somente números sem símbulos")
except floatingPaintError:
    print("Digitar número com . e não vírgula")
except Exception as Celia:
    mensagem = str (Celia)
    print("Ocorreu erro", mensagem)