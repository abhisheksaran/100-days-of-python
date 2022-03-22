student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
npa_df = pandas.read_csv("nato_phonetic_alphabet.csv")
npa_dict = {row.letter: row.code for (index, row) in npa_df.iterrows()}
#print(npa_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Insert a word: ")
print(f"The phonetic code words for the {input_word} is as follows:")
for letter in input_word:
    print(letter)
phonetic_code_words = [npa_dict[letter.upper()] for letter in input_word]
print(phonetic_code_words)
