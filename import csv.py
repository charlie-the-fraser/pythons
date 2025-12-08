import csv

FILENAME = "scores.csv"

def add_score(username, score):
    with open("scores.csv", "a" ,newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])
    

def show_scores():
    total = 0
    scoring = []
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
            total = total + int(line[1])
            scoring.append(int(line[1]))
    print(f"the average score is {total / len(scoring)}")


def main():
    while True:
        print("1. add a score")
        print("2. Show all scores")
        print("3. Quit")
        print("4. list assignment index out of range")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            penar = ["67"]
            penar[420] = ["69"]
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()