"""
Tipos de dados primitivos
str - String
int - inteiro
float - ponto flutuante
bool - booleano
"""
# Demais tipos primitivos em Python
# str
print("Qual o tipo:", type("VB"))
print("Instancia de STR:", isinstance("VB", str))
# int
print("Qual o tipo:", type(1))
print("Instancia de INT:", isinstance(1, int))
# float
print("Qual o tipo:", type(1.25))
print("Instancia de FLOAT:", isinstance(1.25, float))
# bool
print("Qual o tipo:", type(1.25 == 0))
print("Instancia de BOOL:", isinstance(1.25 == 0, bool))
# bool
print("Qual o tipo:", type(bool([])), bool([]))
# bool
print("Qual o tipo:", type(bool([])), bool(""))
# Exemplo de conversão de tipos
print("Conversão de tipos")
print("Qual o tipo:", type(int("10")))
print("Qual o tipo:", type(str(10)))
print("Qual o tipo:", type(float("10")))
print("Qual o tipo:", type(bool("")))
print("Qual o tipo:", type(bool("0")))
print("Qual o tipo:", type(bool("1")))
print("Qual o tipo:", type(bool(0)))
print("Qual o tipo:", type(bool(1)))
print("Qual o tipo:", type(bool(-1)))
print("Qual o tipo:", type(bool("0.0")))