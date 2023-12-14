#FILM DICTIONARY

# Creating a dictionary with film info.
film = {
    "Title": "Aquaman",
    "Director": "James Wan",
    "Genre": "Action",
    "Release date": "December 13, 2018",
    "Rating": 6.8
}

# Displaying the info using for loop. loop is used to put in every item till finish.
print("Film Details:") # printing header
for key, value in film.items(): # defining/getting the key value items in film dictionary. For instance, Key = title || Value = Aquaman
    print(f"{key}: {value}") # printing all info 
