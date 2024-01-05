# Read the original letter
# Read the original letter
with open("/home/daniel/Desktop/100dayscode/006 Mail-Merge-Project-Start/day24file/Input/Letters/starting_letter.txt", "r") as original_file:
    original_letter = original_file.read()

# Rest of your script...


# Read the list of names
with open("/home/daniel/Desktop/100dayscode/006 Mail-Merge-Project-Start/day24file/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

# Create and write personalized invitation letters
for name in names:
    # Remove any leading or trailing whitespace from the name
    name = name.strip()
    
    # Create a personalized letter by replacing the placeholder with the current name
    personalized_letter = original_letter.replace("[name]", name)
    
    # Write the personalized letter to a new file
    output_file_path = f"/home/daniel/Desktop/100dayscode/006 Mail-Merge-Project-Start/day24file/Output/ReadyToSend/{name}_example.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(personalized_letter)

    
