import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic=pandas.read_csv("nato_phonetic_alphabet.csv")
ph= pandas.DataFrame(phonetic)
#print(ph.to_dict())
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_dict={value.letter: value.code for (key, value) in  ph.iterrows()}

word=input("enter word: ").upper()
my_word=[new_dict[letter] for letter in word]

print(new_dict)

print(my_word)
