notepad = open("notepad.txt", "w", encoding = "utf8")
notepad.write("Hello, World!")
notepad.write("Hello, World!")
notepad.close()

notepad = open("notepad.txt", "a", encoding = "utf8")
print("Hello, World!", file=notepad)
print("Hello, World!", file=notepad)
notepad.close()

notepad = open("notepad.txt", "r", encoding = "utf8")
print(notepad.readlines())
notepad.close()