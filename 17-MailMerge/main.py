#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
names_list = []
with open("Input/Names/invited_names.txt", "r") as names:
    for i in names:
        names_list.append(i.strip())

for name in names_list:
    with open("Input/Letters/starting_letter.txt","r") as starting_letter:
        letter = starting_letter.readlines()
        letter[0] = letter[0].replace("[name]",name)
        with open(f"Output/ReadyToSend/{name}.txt","w") as ready_letter:
            ready_letter.writelines(letter)