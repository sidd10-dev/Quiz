import random

def execute_quiz(q, a):
    questions = []
    answers = []
    with open(q) as qf, open(a) as af:
        questions = qf.readlines()
        answers = af.readlines()

    question_set = []
    for i in range(len(questions)):
        question, options = questions[i].split("::")
        question_set.append((question.strip(), options.strip().split(":"), answers[i].strip()))
    
    score = 0
    random.shuffle(question_set)
    for question, options, ans in question_set:
        print(question)
        random.shuffle(options)
        for i, option in enumerate(options):
            print(f'{i+1}: {option}')
        given_ans = input("Enter answer: ")
        if given_ans == ans:
            score += 1
    
    print("Score Got in the Quiz: ", score)

        

    



if __name__ == "__main__":
    quiz = input("Enter the Quiz number you would like to take: ")
    question_file = "q" + quiz + ".txt"
    ans_file = "a" + quiz + ".txt"
    execute_quiz(question_file, ans_file)
