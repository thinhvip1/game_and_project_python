import random

question ={"When is uncle Ho born?": "C",
           "Which is triangle square form?": "A",
           "Who create Facebook?": "A",
           "What is the capital of VietNam?": "B",
           "Which football club won the Premier League in 2022?": "D",
           "Who is king of goals in the Premier League in 2022?": "D"}
option = [["A. 2/9/1945", "B. 17/5/1890", "C. 19/5/1890", "D. 18/5/1890"],
          ["A. S = ah/2", "B. S = 2ah", "C. S = ah/3", "D. S = 3ah"],
          ["A. Mark ZuckerBerg", "B. Steve Job", "C. Crimson", "D. Steve Chen"],
          ["A. HCM city", "B. Ha Noi city", "C. Da Nang city", "D. Can Tho city"],
          ["A. Liverpool", "B. Manchester United", "C. Chelsea", "D. Manchester City"],
          ["A. Mohamed Salah", "B. Cristiano Ronaldo", "C. Son Heung-min", "D. Both A and C"]]
# ----------------------------
def new_game():
    correct_ans = 0
    question_num = 0
    for key in question:
        print("-----------------------------------")
        print(key)
        for ans in option[question_num]:
            print(ans)
        question_num += 1
        your_choice = input("Enter (A, B, C or D): ").upper()
        correct_ans += check_answer(question.get(key), your_choice)
    display_score(correct_ans)

# ----------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
# ----------------------------
def display_score(correct_ans):
    print("----------------------------")
    print("Your result:")
    num_question = len(option)
    point = 10/num_question * float(correct_ans)
    if num_question > 1:
        print(f"You got {correct_ans}/{num_question} correct answers.")
        print(f"You got {point:.{1}f} points")
    else:
        print(f"You got {correct_ans:.{1}f}/{num_question} correct answer.")
        print(f"You got {point} points")
# ----------------------------
def play_again():
    while True:
        inp = input("Do you want to play again?(Y/N): ").lower()
        if inp == "y":
            return True
        elif inp == "n":
            print("Goodbye (^.^)")
            return False
# ----------------------------

new_game()
while play_again():
    new_game()
