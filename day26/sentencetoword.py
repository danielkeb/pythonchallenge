sentence="What is the Airspeed Velocity of an Unladen Swallow?"

word_list=sentence.split()

word ={word:len(word) for word in word_list}
print(word)