from Code.Controller import Controller

if __name__ == "__main__":
    file = open("../automatador/micodigo.txt", "r")
    for line in file:
        print(line)
        Controller.reconocedor(line)
