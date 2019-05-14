import codecs


def main():
    text = "Uryyb, jbeyq!"

    char_list = list()
    for char in text:
        char_list.append(codecs.decode(char, "rot13"))

    print("".join(char_list))


if __name__ == '__main__':
    main()
