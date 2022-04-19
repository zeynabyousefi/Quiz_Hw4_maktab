import csv
import random


class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def chek(self, input_answer):
        for d in range(len(self.answer)):
            if input_answer.upper() == self.answer[d]:
                return True
            else:
                return False

    def __str__(self):
        print(f'{self.question} answer is {self.answer}')


class Multiple_choice(Quiz):
    def __init__(self, question, answer, choice):
        super().__init__(question, answer)
        self.choice = choice

    def __str__(self):
        for k in range(2):
            print(f'{self.question[k]}\n{self.choice[k]}')


class TrueFalse(Quiz):
    def __init__(self, question, answer, choice):
        super().__init__(question, answer)
        self.choice = choice

    def __str__(self):
        for k in range(2):
            return print(f'{self.question[k]}\n{self.choice[k]}')


class Shoretanswer(Quiz):
    def __init__(self, question, answer, choicse):
        super(Shoretanswer, self).__init__(question, answer)
        self.question = question
        self.answer = answer
        self.choicse = choicse

    def __str__(self):
        return print(f'{self.question}\n')


class Point:

    def __init__(self, point):
        self.point = point

    def __str__(self):
        return f"{self.point}"

    def __add__(self, other):
        self.point = self.point + other.point
        return self.point

    def __sub__(self, other):
        self.point = self.point - other.point
        return self.point

    def result(self):
        if self.point >= 40:
            print("winner!")
        else:
            print("failed!")
        return self.point


result_list = []

with open("C:/Users/ASUS/pythonProject/open file/all questions.csv") as datafile:
    reader = csv.DictReader(datafile, delimiter=',')
    for row in reader:
        result_list.append(dict(row))
tf_questions = []
tf_answer = []
tf_choice = []
score = 0
correct = 0
wrong = 0
Q = 0
for l in range(2):
    tf_type = random.choices(result_list[2:6], k=2)
    tf_questions.append(tf_type[l]['question'])
    tf_answer.append(tf_type[l]['answer'])
    tf_choice.append(tf_type[l]['choices'])
    print(f'#Question:{tf_questions[l]}')
    print(f'#choices are:{tf_choice[l]}')
    input_answer = input("Enter your answer>>>")
    tf_quize = TrueFalse(tf_questions, tf_answer, tf_choice)
    Q += 1
    if tf_quize.chek((input_answer)):
        print("True!")
        point = Point(score)  # self
        plus = Point(10)  # other
        score = point.__add__(plus)
        correct += 1

    elif input_answer == '':
        print("0 score")
        wrong += 1
    else:
        print("False")
        point = Point(score)
        sub = Point(3)
        score = point.__sub__(sub)
        wrong += 1

    print(f'Q:\t\tcorrect:\t\twrong:\t\tscore:\t\tRemaining:\n  '
f'\r{Q}\t\t\t {correct}\t\t\t {wrong}\t\t\t {score}\t\t\t {5 - Q}')


mu_questions = []
mu_answer = []
mu_choice = []
for l in range(2):
    Q += 1
    mu_type = random.choices(result_list[7:11], k=2)
    mu_questions.append(mu_type[l]['question'])
    mu_answer.append(mu_type[l]['answer'])
    mu_choice.append(mu_type[l]['choices'])
    print(f'#Question:{mu_questions[l]}')
    print(f'#choices are:{mu_choice[l]}')
    input_answer = input("Enter your answer>>>")
    mu_quize = Multiple_choice(mu_questions, mu_answer, mu_choice)
    if mu_quize.chek(input_answer):
        print("True!")
        point = Point(score)
        # plus = Point(10)
        score = point.__add__(Point(10))
        correct += 1

    elif input_answer == '':
        print("0 score")
        wrong += 1

    else:
        print("False")
        point = Point(score)
        sub = Point(3)
        score = point.__sub__(sub)
        wrong += 1

    print(f'Q:\t\tcorrect:\t\twrong:\t\tscore:\t\tRemaining:\n  '
          f'\r{Q}\t\t\t {correct}\t\t\t {wrong}\t\t\t {score}\t\t\t {5 - Q}')

sh_questions = []
sh_answer = []
sh_choice = []

sh_type = random.choices(result_list[12:16], k=1)
sh_questions.append(sh_type[0]['question'])
sh_answer.append(sh_type[0]['answer'])
sh_choice.append(sh_type[0]['choices'])
print(f'#Question:{sh_questions[0]}')
input_answer = input("Enter your answer>>>")
sh_quize = Multiple_choice(sh_questions, sh_answer, sh_choice)
Q += 1
if sh_quize.chek((input_answer)):
    print("True!")
    point = Point(score)
    plus = Point(10)
    score = point.__add__(plus)
    correct += 1

elif input_answer == '':
    print("0 score")
    wrong += 1

else:
    print("False")
    point = Point(score)
    sub = Point(3)
    score = point.__sub__(sub)
    wrong += 1

print(f'Q:\t\tcorrect:\t\twrong:\t\tscore:\t\tRemaining:\n  '
      f'\r{Q}\t\t\t {correct}\t\t\t {wrong}\t\t\t {score}\t\t\t {5 - Q}')


print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
point =  Point(score)
point.result()
print("hi")
