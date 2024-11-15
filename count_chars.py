from collections import OrderedDict

def count_chars():
    phrase = input("Digite uma frase: ")
    char_count = OrderedDict()

    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(dict(char_count))

if __name__ == "__main__":
    count_chars()
