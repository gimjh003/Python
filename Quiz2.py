import random
words = ['apple', 'banana', 'orange', 'coffee']
word = random.choice(words)
current = list('_' for i in range(len(word)))
while True:
    for i in current:
        print(i, end=' ')
    if '_' not in current:
        break
    alpha = input("\nalphabet : ")
    if alpha in word:
        print("Correct")
        for idx, val in enumerate(word):
            if word[idx] == alpha:
                current[idx] = alpha
    else:
        print("Wrong")
print('\nSUCCESS')