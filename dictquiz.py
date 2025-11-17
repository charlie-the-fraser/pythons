quiz = {"who is dante dmc's brother: urizen, vergil, V, nelo angelo" : "all of the above", "in demon slayer, how many people did akaza kill before becoming a demon" : "67", "in chainsaw man, which devil is the first devil we see denji fight? tomato, eggplant, bat, testicle" : "tomato" , "which of the following elden ring characters is an empyrean: radahn, godfrey, ranni, alexander" : "ranii", "in Steel Ball Run, how long is the steel ball run in km" : "6000", "in demon slayer, who holds the title of upper rank 6: Daki, Gyuttaro, Kaigaku" : "all of the above", "in jujutsu kaisen, what species is panda's older brother? " : "gorilla" }
correct = 0
quiztime = list(quiz.keys())
for i in range(0, len(quiztime)):
    answer = str(input(f"{quiztime[i]} "))
    if quiz[quiztime[i]] == answer:
        input("correct")
        correct = correct + 1
    else:
        input(f"incorrect! the answer was {quiz[quiztime[i]]}")
input(f"you got {correct} out of {len(quiztime)} correct! ")