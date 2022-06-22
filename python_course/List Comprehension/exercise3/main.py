with open("python_course/List Comprehension/exercise3/file1.txt") as file:
    file1 = [int(number) for number in file.read().split("\n") if len(number)]
with open("python_course/List Comprehension/exercise3/file2.txt") as file:
    file2 = [int(number) for number in file.read().split("\n") if len(number)]

result = [number for number in file1 if number in file2]

print(result)