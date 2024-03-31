
print("""
1 - translation from latin language to Morse code
2 - translation from Morse code language to latin language
      """)

translte_mode = input("Choose the option: ")

alfabet_Morse = {
    "A": "•-",
    "B": "-•••",
    "C": "-•-•",
    "D": "-••",
    "E": "•",
    "F": "••-•",
    "G": "--•",
    "H": "••••",
    "I": "••",
    "J": "•----",
    "K": "-•-",
    "L": "•-••",
    "M": "--",
    "N": "-•",
    "O": "---",
    "P": "•--•",
    "Q": "--•-",
    "R": "•-•",
    "S": "•••",
    "T": "-",
    "U": "••-",
    "V": "•••-",
    "W": "•--",
    "X": "-••-",
    "Y": "-•--",
    "Z": "--••",
    ".": "•-•-•-",      #punctuation marks
    ",": "--••--",
    "?": "••--••",
    ":": "---•••",
    ";": "-•-•-•",
    "-": "-••••-",
    "/": "-••-•",
    '"': "•-••-•",
    "'": "•----•",
    "(": "-•--•",
    ")": "-•--•-",
    "=": "-••-",
    "+": "•-•-•",
    "$": "•••--••-",
    "_": "••--•-",
    "0": "-----",       #numbers
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    " ": "  ",
}

if translte_mode == "1":
    user_file = input("Enter name of file with text: ")

    file_l = open(user_file, "r")
    word = file_l.read()

    word = word.upper()

    i = 0;
    for i in range(len(word)):
        if word[i] == "A":
            word_Morse = alfabet_Morse["A"]
        elif word[i] == "B":
            word_Morse = alfabet_Morse["B"]
        elif word[i] == "C":
            word_Morse = alfabet_Morse["C"]
        elif word[i] == "D":
            word_Morse = alfabet_Morse["D"]
        elif word[i] == "E":
            word_Morse = alfabet_Morse["E"]
        elif word[i] == "F":
            word_Morse = alfabet_Morse["F"]
        elif word[i] == "G":
            word_Morse = alfabet_Morse["G"]
        elif word[i] == "H":
            word_Morse = alfabet_Morse["H"]
        elif word[i] == "I":
            word_Morse = alfabet_Morse["I"]
        elif word[i] == "J":
            word_Morse = alfabet_Morse["J"]
        elif word[i] == "K":
            word_Morse = alfabet_Morse["K"]
        elif word[i] == "L":
            word_Morse = alfabet_Morse["L"]
        elif word[i] == "M":
            word_Morse = alfabet_Morse["M"]
        elif word[i] == "N":
            word_Morse = alfabet_Morse["N"]
        elif word[i] == "O":
            word_Morse = alfabet_Morse["O"]
        elif word[i] == "P":
            word_Morse = alfabet_Morse["P"]
        elif word[i] == "Q":
            word_Morse = alfabet_Morse["Q"]
        elif word[i] == "R":
            word_Morse = alfabet_Morse["R"]
        elif word[i] == "S":
            word_Morse = alfabet_Morse["S"]
        elif word[i] == "T":
            word_Morse = alfabet_Morse["T"]
        elif word[i] == "U":
            word_Morse = alfabet_Morse["U"]
        elif word[i] == "V":
            word_Morse = alfabet_Morse["V"]
        elif word[i] == "W":
            word_Morse = alfabet_Morse["W"]
        elif word[i] == "X":
            word_Morse = alfabet_Morse["X"]
        elif word[i] == "Y":
            word_Morse = alfabet_Morse["Y"]
        elif word[i] == "Z":
            word_Morse = alfabet_Morse["Z"]
        elif word[i] == ".":
            word_Morse = alfabet_Morse["."]
        elif word[i] == ",":
            word_Morse = alfabet_Morse[","]
        elif word[i] == "?":
            word_Morse = alfabet_Morse["?"]
        elif word[i] == ":":
            word_Morse = alfabet_Morse[":"]
        elif word[i] == ";":
            word_Morse = alfabet_Morse[";"]
        elif word[i] == "-":
            word_Morse = alfabet_Morse["/"]
        elif word[i] == '"':
            word_Morse = alfabet_Morse['"']
        elif word[i] == "'":
            word_Morse = alfabet_Morse["'"]
        elif word[i] == "(":
            word_Morse = alfabet_Morse["("]
        elif word[i] == ")":
            word_Morse = alfabet_Morse[")"]
        elif word[i] == "=":
            word_Morse = alfabet_Morse["="]
        elif word[i] == "+":
            word_Morse = alfabet_Morse["+"]
        elif word[i] == "$":
            word_Morse = alafbet_Morse["$"]
        elif word[i] == "_":
            word_Morse = alfabet_Morse["_"]
        elif word[i] == "0":
            word_Morse = alfabet_Morse["0"]
        elif word[i] == "1":
            word_Morse = alfabet_Morse["1"]
        elif word[i] == "2":
            word_Morse = alfabet_Morse["2"]
        elif word[i] == "3":
            word_Morse = alfabet_Morse["3"]
        elif word[i] == "4":
            word_Morse = alfabet_Morse["4"]
        elif word[i] == "5":
            word_Morse = alfabet_Morse["5"]
        elif word[i] == "6":
            word_Morse = alfabet_Morse["6"]
        elif word[i] == "7":
            word_Morse = alfabet_Morse["7"]
        elif word[i] == "8":
            word_Morse = alfabet_Morse["8"]
        elif word[i] == "9":
            word_Morse = alfabet_Morse["9"]
        elif word[i] == " ":
            word_Morse = alfabet_Morse[" "]

        with open("translate.txt", "a") as tr:
            tr.write(word_Morse)

        print(word_Morse, end=' ')
        i += 1;


# don't working
elif translte_mode == "2":
    user_Morse_file = input("Enter the name of file with Morse code: ")
    file_M = open(user_Morse_file, "r")
    word = file_M.read()

    print(word)

    word = word.upper()
    word = list(word)

    i = 0
    for i in range(len(word)):
        if word[i] == "-":
            word_latin = alfabet_Morse_m1[""]
        elif word[i] == "":
            word_latin = alfabet_Morse_m1[""]

        with open("translate.txt", "a") as tr:
            tr.write(word_latin)

        print(word_latin, end=" ")
        i += 1;