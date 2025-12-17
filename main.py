questions = ("Qual é o planeta mais quente do sistema solar?", 
             "Quem é considerado o rei do futebol?", 
             "Onde fica situado a Nova Zelandia?", 
             "Qual é o animal mais grande do mundo?", 
             "Quem inventou a eletricidade?")

options = (("A. Venus", "B. Marte", "C. Terra", "D. Saturno"),
           ("A. Messi", "B. Ronaldinho", "C. Pélé", "D. Maradona"), 
           ("A. Africa", "B. Europa", "C. Asia", "D. Oceania"), 
           ("A. Gorila", "B. Baleia-Azul", "C. Girafa", "D. Elefante"), 
           ("A. Tesla", "B. Einstein", "C. Newton", "D. prof. Walter"))

answers = ("A", "C", "D", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the answer(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer!")

    question_num += 1

print("-----------------")
print("     RESULTS     ")
print("-----------------")

print("answers:", end="")

for answer in answers:
    print(answer, end="")
print()

print("guesses:", end="")

for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")