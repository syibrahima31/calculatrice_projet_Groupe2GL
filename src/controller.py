import view 
import model

def calculate():
    while True: 
        # affiche le menu 
        view.affiche_menu()

        # choix d'une operation 
        op = view.get_operation()

        # choix des valeurs 
        if op in "1234":
            x = view.get_number()
            y = view.get_number()

        if op == "1": 
            result = model.add(x, y)

        elif op == "2": 
            result = model.sub(x, y)

        elif op == "3": 
            result = model.mult(x, y)

        elif op == "4": 
            result = model.div(x, y)
        
        else: 
            break 

        view.display(result)
        print("-"*50)



if __name__ == "__main__": 
    calculate()