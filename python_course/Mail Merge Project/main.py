#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("python_course/Mail Merge Project/Input/Names/invited_names.txt", "r") as f:
    data = f.read()
    names = data.split("\n")

with open("python_course/Mail Merge Project/Input/Letters/starting_letter.txt") as f:
    form = f.read()
    for name in names:
        with open(f"python_course/Mail Merge Project/Output/ReadyToSend/letter_for_{name}.txt", "w") as writer:
            writer.write(form.replace("[name]", name))