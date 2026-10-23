logininfo = {
    "username": "MEK1300",
    "password": "Python"
}

total_questions = 3
question_number = 1
questions_correct = 0

wrong_answers = []

def login_info(username, password):
    if username == logininfo["username"] and password == logininfo["password"]:
        print("Login successful!")
    else:
        print("Invalid username and/or password.")
        login_info(input("Enter your username: "), input("Enter your password: "))

login_info(input("Enter your username: "), input("Enter your password: "))

def answer_check(user_answer, correct_answer):
    return user_answer == correct_answer

quiz = {
    "Question 1": {
        "question": "What is the capital of Norway?",
        "options": {
            "a": "Bergen",
            "b": "Oslo",
            "c": "Stavanger",
            "d": "Trondheim"
        },
        "answer": "b"
    },
    "Question 2": {
        "question": "What is the currency of Norway?",
        "options": {
            "a": "Euro",
            "b": "Pound",
            "c": "Krone",
            "d": "Deutsche Mark"
        },
        "answer": "c"
    },
    "Question 3": {
        "question": "What is the largest city in Norway?",
        "options": {
            "a": "Oslo",
            "b": "Stavanger",
            "c": "Bergen",
            "d": "Trondheim"
        },
        "answer": "a"
    },
    "Question 4": {
        "question": "When is constitution day (the national day) of Norway?",
        "options": {
            "a": "27th May",
            "b": "17th May",
            "c": "17th April",
            "d": "27th April"
        },
        "answer": "b"
    },
    "Question 5": {
        "question": "What color is the background of the Norwegian flag?",
        "options": {
            "a": "Red",
            "b": "White",
            "c": "Blue",
            "d": "Yellow"
        },
        "answer": "a"
    },
    "Question 6": {
        "question": "How many countries does Norway border?",
        "options": {
            "a": "1",
            "b": "2",
            "c": "3",
            "d": "4"
        },
        "answer": "c"
    },
    "Question 7": {
        "question": "What is the name of the university in Trondheim?",
        "options": {
            "a": "UiS",
            "b": "UiO",
            "c": "NMBU",
            "d": "NTNU"
        },
        "answer": "d"
    },
    "Question 8": {
        "question": "How long is the border between Norway and Russia?",
        "options": {
            "a": "96 km",
            "b": "196 km",
            "c": "296 km",
            "d": "396 km"
        },
        "answer": "b"
    },
    "Question 9": {
        "question": "Where in Norway is Stavanger?",
        "options": {
            "a": "North",
            "b": "South",
            "c": "South-west",
            "d": "South-east"
        },
        "answer": "c"
    },
    "Question 10": {
        "question": "From which Norwegian city did the world's famous composer Edvard Grieg come?",
        "options": {
            "a": "Oslo",
            "b": "Bergen",
            "c": "Stavanger",
            "d": "Tromsø"
        },
        "answer": "b"
    }
}

def print_question(quiz, question_number):
    question_key = f"Question {question_number}"
    print(f"\n{quiz[question_key]['question']}")
    print(f"a: {quiz[question_key]['options']['a']}")
    print(f"b: {quiz[question_key]['options']['b']}")
    print(f"c: {quiz[question_key]['options']['c']}")
    print(f"d: {quiz[question_key]['options']['d']}")

def print_mistakes(question_data, user_answer):     
        options = question_data["options"]
        correct_answer = question_data["answer"]
        print(f"\n{question_data['question']}")
        if user_answer in options:
            print(f"  Your answer: {user_answer}: {options[user_answer]}")
        else:
            print(f"  Your answer: {user_answer or '(blank)'} (not a listed option)")
        print(f"  Correct answer: {correct_answer}: {options[correct_answer]}")


while question_number <= total_questions:
    print_question(quiz, question_number)
    user_answer = input("Your answer (a/b/c/d): ").strip().lower()
    correct_answer = quiz[f"Question {question_number}"]["answer"]

    if answer_check(user_answer, correct_answer):
        questions_correct += 1
    else:
        wrong_answers.append((quiz[f"Question {question_number}"], user_answer))

    question_number += 1

print(f"You got {questions_correct} out of {total_questions} questions correct!")
if wrong_answers:
    print ("\nIncorrect answers:")
    while wrong_answers:
        question_data, user_answer = wrong_answers.pop()
        print_mistakes(question_data, user_answer)

    
# We could have used less functions as some of the functions are not really necessary.
# But using functions made the code more readable and easier to navigate.