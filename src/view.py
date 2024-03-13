def affiche_menu(): 
    print("----MENU----")
    print("1. Addition ")
    print("2. Soustraction ")
    print("3. Multiplication")
    print("4. Division ")
    print("5. Quitter ")

def get_operation(): 
    return input("Choisir une Opération :")

def get_number(): 
    return float(input("Entrer un nombre : "))

def display(result): 
    print(f"Resultat : {result}")

