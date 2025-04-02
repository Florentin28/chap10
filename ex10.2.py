def nombre_max (a,b,c) ->int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = int(input("Entrez le premier nombre entier : "))
num2 = int(input("Entrez le deuxième nombre entier : "))
num3 = int(input("Entrez le troisième nombre entier : "))


print("Le nombre maximum est :", nombre_max(num1, num2, num3))