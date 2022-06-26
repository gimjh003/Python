import pandas

data = pandas.read_csv("python_course/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_code = {info.letter:info.code for (idx, info) in data.iterrows()}

while True:
    name = input("Enter a word : ").upper()
    try:
        codes = [phonetic_code[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(codes)
        break