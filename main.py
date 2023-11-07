#TODO modularization
#TODO code cleanup

import random


print("Welcome in flashterm")
test_file = open(input("What test do you want to try? (Give the filename)\n"),"r", encoding="utf-8")
task_name = test_file.read()
lines = task_name.split('\n')
print(f"There are {len(lines)*2 -2} potential tasks")
print("How many questions do you want?")
question_number = input()
print("GENERATING!!!")
print("---------------------------------------------------------------------------------------------")

questions = []
print(lines[0])
lines = lines[1:]
for line in lines:
    question_vals = line.split(',')
    questions.append(question_vals)
    #Comment the below if you don't want reverse questions
    question_vals = [question_vals[1],question_vals[0]]
    questions.append(question_vals)

question_indices = random.sample(range(0,len(questions)), int(question_number))
question_list = []
for index in question_indices:
    question_list.append(questions[index])
correct_counter = 0
def generate_test():
    questions_to_remove = []
    global correct_counter
    for question in question_list:
        answer = input(question[0] + ": ")
        if answer == question[1]:
            print("Correct\n")
            correct_counter += 1
            questions_to_remove.append(question)
        else:
            print("Wrong\n")

    for question in questions_to_remove:
        question_list.remove(question)

    print(f"Test result: {correct_counter}/{question_number}")

def main_loop():
    while True:
        generate_test()
        print("Do you want to try to solve the questions you did wrong?")
        retry = input()
        if retry.lower() == "no":
            print(question_list)
            return

main_loop()