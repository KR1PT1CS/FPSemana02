def char_intersection():
    phrase1 = input("Digite a primeira frase: ")
    phrase2 = input("Digite a segunda frase: ")

    
    set1 = set(phrase1.split())
    set2 = set(phrase2.split())


    intersection = set1.intersection(set2)

    
    result = " ".join(intersection)

    print(result)

if __name__ == "__main__":
    char_intersection()
