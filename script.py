#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.


# Zahl1:
z1 = input(f"Enter number 1: ")
z1 = float(z1)

# Zahl2:
z2 = input(f"Enter number 2: ")
z2 = float(z2)

op = ''
while op not in "+-*/" or len(op)!=1:
    # Operand:
    op = input(f"Enter operation [+-*/]: ")


match op:
    case '+':
        print(f"{z1} + {z2} = {z1+z2}")
    case '-':
        print(f"{z1} - {z2} = {z1-z2}")
    case '*':
        print(f"{z1} * {z2} = {z1*z2}")
    case '/':
        print(f"{z1} / {z2} = {z1/z2}")
