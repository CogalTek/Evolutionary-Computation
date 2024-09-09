import sys

def processStart():
    try:
        if "-x" not in sys.argv:
            raise ValueError("L'option '-x' est manquante dans les arguments.")

        if len(sys.argv) <= (sys.argv.index("-x") + 1):
            raise IndexError("Aucun argument après '-x'.")

        index = sys.argv.index("-x") + 1

        if not sys.argv[index].isnumeric() or int(sys.argv[index]) < 1:
            raise ValueError("L'argument après '-x' doit être un entier supérieur ou égal à 1.")

        print("start")

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except IndexError as ie:
        print(f"Erreur d'index : {ie}")
    except Exception as e:
        print(f"Une exception s'est produite : {e}")
