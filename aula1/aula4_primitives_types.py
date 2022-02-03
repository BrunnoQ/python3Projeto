"""
Tipos de dados
str - String
int - inteiro
float - ponto flutuante
bool - booleano
"""
# utilizando a função type
print("Qual o tipo:", type("VB"))
print("Qual o tipo:", type(1))
print("Qual o tipo:", type(1.25))
print("Qual o tipo:", type(1.25 == 0))
# Esta função faz um casting para boolean, e ela considera tudo que eh VAZIO como false
print("Qual o tipo:", type(bool([])), bool([]))
print("Qual o tipo:", type(bool([])), bool(""))
