"""
-> Considera uma turma de alunos e as suas respectivas notas. Cria um programa em Python que armazena essas informações em listas e dicionários.

1. Cria uma lista chamada "alunos" que armazena os nomes dos alunos.
2. Cria uma lista chamada "notas" que armazena as notas correspondentes aos alunos na mesma ordem.
3. Cria um dicionário chamado "turma" que associa cada aluno à sua respectiva nota
4. Adiciona mais dois alunos e as suas notas à lista e ao dicionário.
5. Acede a nota do primeiro aluno na lista de notas.
6. Modifica a nota do segundo aluno na lista e no dicionário.
7. Remove o terceiro aluno da lista e do dicionário.
8. Imprime a lista de alunos.
9. Imprime o dicionário "turma" completo.
"""

print("")
print("VERSION 1")
print("")

# VERSION 1
# Este código usa a funçãpo zip para criar de forma dinâmica um dicionário baseado
# nas nossas duas listas 'studentes' e 'grades'

# Create lists "students" and "grades"
students = ["Hugo", "Luís", "Pedro"]
grades = [90, 80, 95]

# Print the initial "students" and "grades" lists
print("Initial 'students' list:", students)
print("Initial 'grades' list:", grades)
print("")

# Add Tânia and André to the "students" list
students.extend(["Tânia", "André"]) # append also works but only for single records, i want multiple

# Add grades for Tânia and André to the "grades" list
grades.extend([87, 89]) # append also works but only for single records, i want multiple

# Print the extended "students" list
print("Extended 'students' list:", students)
print("")

# Print the extended "grades" list
print("Extended 'grades' list:", grades)
print("")

# Create a dictionary "class_dict" using zip to pair names with grades
class_dict = dict(zip(students, grades))

# Print the initial "class_dict" dictionary
print("Initial 'class_dict' dictionary:", class_dict)
print("")

# Access the grade of the first student in the "class_dict" and also in the list 'grades'
hugo_grade = class_dict["Hugo"]
print(f"The grade of Hugo in the 'class_dict' is: {hugo_grade}")

hugo_grade_list = grades[0]
print(f"The grade of Hugo in the 'grades' list is: {hugo_grade_list}")
print ("")

# Modify the grade of the second student ("Luís") in the "class_dict"
class_dict[students[1]] = 95

# Print the "class_dict" dictionary after modifying Luís's grade
print("Updated 'class_dict' dictionary after modifying Luís's grade:", class_dict)
print("")

# Remove the third student ("Pedro") from the "students" list, the "grades" list, and the "class_dict" dictionary
students.pop(2)
grades.pop(2)
del class_dict["Pedro"] #Key on our dict

# Print the final "students" list
print("Final 'students' list:", students)
print("")

# Print the final "class_dict" dictionary
print("Final 'class_dict' dictionary:", class_dict)



print("")
print("")
print("VERSION 2")
print("")



# VERSION 2

# Create lists "students" and "grades"
studentsv2 = ["Hugo", "Luís", "Pedro"]
gradesv2 = [90, 80, 95]

# Print the initial "students" and "grades" lists
print("Initial 'studentsv2' list:", studentsv2)
print("Initial 'gradesv2' list:", gradesv2)
print("")

# Add Tânia and André to the "students" list
studentsv2.extend(["Tânia", "André"]) # append also works but only for single records, i want multiple

# Add grades for Tânia and André to the "grades" list
gradesv2.extend([87, 89]) # append also works but only for single records, i want multiple

# Print the extended "students" list
print("Extended 'studentsv2' list:", studentsv2)
print("")

# Print the extended "grades" list
print("Extended 'gradesv2' list:", gradesv2)
print("")

# Create a dictionary "class_dictv2" using hardcoded key-value pairs for names and grades
class_dictv2 = {
    "Hugo": 90,
    "Luís": 80,
    "Pedro": 95,
    "Tânia": 87,
    "André": 89
}


# Print the initial "class_dict" dictionary
print("Initial 'class_dictv2' dictionary:", class_dictv2)
print("")

# Access the grade of the first student in the "class_dict" and also in the list 'grades'
hugo_grade = class_dictv2["Hugo"]
print(f"The grade of Hugo in the 'class_dictv2' is: {hugo_grade}")

hugo_grade_listv2 = gradesv2[0]
print(f"The grade of Hugo in the 'gradesv2' list is: {hugo_grade_listv2}")
print ("")

# Modify the grade of the second student ("Luís") in the "class_dict"
class_dictv2[studentsv2[1]] = 95

# Print the "class_dict" dictionary after modifying Luís's grade
print("Updated 'class_dictv2' dictionary after modifying Luís's grade:", class_dictv2)
print("")

# Remove the third student ("Pedro") from the "students" list, the "grades" list, and the "class_dict" dictionary
studentsv2.pop(2)
gradesv2.pop(2)
del class_dictv2["Pedro"] #Key on our dict

# Print the final "students" list
print("Final 'studentsv2' list:", studentsv2)
print("")

# Print the final "class_dict" dictionary
print("Final 'class_dictv2' dictionary:", class_dictv2)