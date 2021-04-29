import random
import os

def read(filepath = "./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words
    

def run():
    data = read(filepath = "./archivos/data.txt")
    #Uso de modulo random para seleccion de palabra
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}

    # Uso de ENUMERATE para ingresar cada letra en un 
    # diccionario con un id para ser ubicado
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("cls")
        print("Adivina la palabra")
        for element in underscores:
            print(element+" ",end="")
        print("\n")

        letter = input("Escriba una letra: ").strip().upper()
        #try
        assert letter.isalpha(), "Solo se permiten letras"
        
        #Reemplaza la letra correcta que se encuentra en el diccionario
        # en la lista de underscore a traves del id 
        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                underscores[idx] = letter
        
        if "_" not in underscores:
            os.system("cls")
            print("Ganaste!, la palabra era", chosen_word)
            break
    

if __name__ == '__main__':
    run()    