"""
Escreve um programa em python que pede ao utilizador o seu nome, 
e sobrenome, e depois imprime essas informações na tela separadas por um espaço.

-> Este exercício contém código que não foi ensinado nas aulas ainda.
"""

# Ask the user for their name
nome = input("Insert your name: ")

# Check if the input contains any digits, loop each char to check if there are digits in 'nome'
if any(char.isdigit() for char in nome):
    raise ValueError("You cannot insert numbers, only text!")
else:
    print(f"Your name is: {nome}")


# Ask the user for their surname
surname = input("Insert your surname: ")

# Check if the input contains any digits, loop each char to check if their are digits in 'surname'
if any(char.isdigit() for char in surname):
    raise ValueError("You cannot insert numbers, only text!")
else:
    print(f"Your surname is: {surname}")


# Ask the user for their age
num = input("Please enter your age: ")

# Check if the input can be converted to an integer
if num.isdigit():
    num = int(num)
    print(f"You entered: {num}")
else:
    raise ValueError("You need to insert a number!")
print("")

print(f"Your name is {nome} {surname}, and you are {num} years old.")
