file = open("text.txt", "r+")

if file.readable():
    text = file.readlines();

for i in text:
    sentence = i;
    for j in sentence:
        if (j != ' ' and j != '\n'):
            signs = open("letters/" + j + ".txt", "r+")
            if signs.readable():
                braille_sign = signs.readlines()

            save = open("braille_alphabet.txt", "a+")

            for i in braille_sign:
                save.write(i)

        save.write('\n\n')
        print(j, end = ' ')