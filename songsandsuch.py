songs = []
for i in range(0, 5):
    songs.append(str(input(f"what is your {i + 1}{"st" if i == 0 else "nd" if i == 1 else "rd" if i == 2 else "th"} favourite song? ")))
print(songs)
while songs != 4:
    choices = int(input("would you like to add a song (1), remove a song (2), view favourite song list (3), end program (4), list index out of range (5) "))
    if choices == 1:
        songs.append(str(input(f"what song would you like to add (song number {len(songs) + 1})")))
    elif choices == 2:
        byeBye = 0
        while byeBye < 1 or byeBye > len(songs) + 1: 
            byeBye = int(input("which song in the list do you want to remove? "))
            if byeBye < 1 or byeBye > len(songs) + 1:
                input("invalid input")      
        songs.remove(songs[byeBye - 1])
    elif choices == 3:
        for i in range(0, len(songs)):
            input(f"{i + 1} - {songs[i]}")
    elif choices == 4:
        input("bye! ")
    elif choices == 5:
        songs[999] = "hello world!"
    else:
        input("invalid input ")    