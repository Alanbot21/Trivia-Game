
#---------------PLAN----------------#
# List of questions 
# store the answers
# randomly pick questions
# ask the questions see if they are correct
# keep track of the score
# tell the user their score
#-----------------------------------#

import random

questions = {
    "How to print hello?": "print('hello')",
    
    "Make a variable x = 10?": "x = 10",
    
    "Make a list with 1,2,3?": "my_list = [1, 2, 3]",
    
    "Make a dictionary with name: John?": "my_dict = {'name': 'John'}",
    
    "Make a function called greet?": "def greet():",
    
    "Make a for loop 5 times?": "for i in range(5):",
    
    "Check if x is greater than 5?": "if x > 5:",
    
    "Add two numbers a and b?": "a + b",
    
    "Get user input?": "input('Enter: ')",
    
    "Convert string to number?": "int('5')"
}

def trivia_game():
    question_list = list(questions.keys())
    total_questions = 10
    score = 0
    selected_questions = random.sample(question_list, total_questions)

    for idx, question in enumerate(selected_questions):  # it will give both index and value
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer : ").lower().strip()
        correct_answers = questions[question]
        if user_answer == correct_answers.lower():
            print("Correct Answer ! \n")
            score += 1
        else:
            print(f"Wrong ! The correct answer is: {correct_answers}.\n")
    
    print(f"Your score is: {score}/{total_questions}")

        
 
trivia_game()