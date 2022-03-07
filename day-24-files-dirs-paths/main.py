# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# If file doesn't exist, it will create a file for you from scratch.
# with open("my_file.txt", mode='w') as file:
#     file.write("And my last name is Saran")

with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
    for name in names:
        name = name.strip("\n")
        with open("./Input/Letters/starting_letter.txt", mode="r") as file2:
            starting_letter = file2.read()
            personalised_letter = starting_letter.replace("[name]", name)
            with open("./Output/ReadyToSend/{}.txt".format(name), mode="w") as file3:
                file3.write(personalised_letter)
print(names)
