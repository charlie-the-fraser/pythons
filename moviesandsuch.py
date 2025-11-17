movies = ["IT crowd - the movie", "Guy Fawks vs Godzilla", "Thursday the 12th", "Saturday the 14th", "the dark of my souls", "the elden of my ring", "the devil that may cry", "67 - the movie"]
choice = 0
while choice != "6":
    choice = input("would you like to veiw all movies (1), add a new movie (2), remove a movie (3), find a movie (4), list assignment index out of range (5), end program (6) ")
    if choice == "1":
        input(f"movies currently showing are {movies}")
    elif choice == "2":
        movies.append(str(input("what movie would you like to add? ")))
    elif choice == "3":
        remove = str(input("which movie would you like to remove? "))
        if remove in movies:
            movies.remove(remove)
        else:
            input("movie not in list")
    elif choice == "4":
        find = str(input("which movie do you want to find? "))
        if find in movies:
            input("this movie is showing")
        else:
            input("this movie is not showing")
    elif choice == "5":
        movies[999] = "wobbly wiggly"
    elif choice == "6":
        input("bye!")
    else:
        input("invalid input")
