from sympy import symbols, Eq, solve, sympify

numerosEquacao = input("Insira a equação do primeiro grau (ex: 2*x - 50 + 90 = 0): ")

x = symbols('x')

expressao = sympify(numerosEquacao.split('=')[0])

equacao = Eq(expressao, int(numerosEquacao.split('=')[1]))

solucao = solve(equacao, x)

print(solucao)
