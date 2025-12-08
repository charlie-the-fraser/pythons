import csv

with open("scores.csv", "a", newline="") as theoParvin:
    writer = csv.writer(theoParvin)
    writer.writerow(["hello", 67])

