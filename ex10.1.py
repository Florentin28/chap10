def nombre_max (a,b) ->int:
    if a > b:
        return a
    else:
        return b

num1 = int(input("Entrez le premier nombre entier : "))
num2 = int(input("Entrez le deuxième nombre entier : "))

print("Le nombre maximum est :", nombre_max(num1, num2))