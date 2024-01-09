import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic=pandas.read_csv("nato_phonetic_alphabet.csv")
ph= pandas.DataFrame(phonetic)
#print(ph.to_dict())
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_dict={value.letter: value.code for (key, value) in  phonetic.iterrows()}
def phonet():
    word=input("enter word: ").upper()
    try:
        my_word=[new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please!")
        phonet()



    else:
        print(my_word)
phonet()