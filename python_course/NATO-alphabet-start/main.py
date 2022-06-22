import pandas

data = pandas.read_csv("python_course/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_code = {info.letter:info.code for (idx, info) in data.iterrows()}

name = input("Enter a word : ").upper()

codes = [phonetic_code[letter] for letter in name]
print(codes)