def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Erreur: Division par zéro"

while True:
    print("Options:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une opération (1/2/3/4/5): ")

    if choix == '5':
        print("Calculatrice terminée.")
        break

    if choix not in ('1', '2', '3', '4'):
        print("Choix invalide. Veuillez choisir une opération valide.")
        continue

    x = float(input("Entrez le premier nombre: "))
    y = float(input("Entrez le deuxième nombre: "))

    if choix == '1':
        print(x, "+", y, "=", addition(x, y))
    elif choix == '2':
        print(x, "-", y, "=", soustraction(x, y))
    elif choix == '3':
        print(x, "*", y, "=", multiplication(x, y))
    elif choix == '4':
        print(x, "/", y, "=", division(x, y))
