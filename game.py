import random
import json


class Question:
    valid_ans = [1, 2, 3, 4]

    def __init__(self, quest, options, answer):
        self.question = quest
        self.options = options
        self.answer = answer

    def __init__(self, d):
        self.question = d["question"]
        self.options = [d["A"], d["B"], d["C"], d["D"]]
        self.answer = ord(d["answer"]) - 64

    def display_question(self):
        quest_str = self.question + "\n"
        for num, option in enumerate(self.options):
            quest_str += str(num + 1) + ". " + option + "\n"

        return quest_str

    def check_answer(self, user_ans):
        return self.answer == user_ans

    def display_result(self, right):
        if right:
            return "Correct\n"
        else:
            return "Wrong!\nThe correct answer is {}: {}\n".\
                format(self.answer, self.options[self.answer-1])


def populate_db(json_list):
    db = []
    for dt in json_list:
        q = Question(dt)
        db.append(q)

    return db


def populate_session(db):
    quest_list = set()
    while len(quest_list) < 10:
        quest_list.add(random.choice(db))
    return quest_list


# class TriviaGame:
#     def __init__(self, path):
#         self.file = open(path)
#         self.trivia_db = []
#         self.populate_db(self.file)
#
#     def start(self):
#         score = 0
#         session = self.populate_session(self.trivia_db)
#         for question in session:
#             print(question.display_question(), end="")
#             ans = int(input("Enter your answer: "))
#             correct = question.check_answer(ans)
#             score += 1 if correct else 0
#             print(question.display_result(correct))
#         return score
#
#     @staticmethod
#     def _populate_session(self, db):
#         quest_list = set()
#         while len(quest_list) < 10:
#             quest_list.add(random.choice(db))
#         return quest_list
#
#     def populate_db(self, json_list):
#         for dt in json_list:
#             q = Question(dt)
#             self.trivia_db.append(q)


with open("trivia_db.json") as f:
    trivia_db = populate_db(json.load(f))
    cont = "y"
    while cont != "n":

        score = 0
        session = populate_session(trivia_db)
        for question in session:
            print(question.display_question(), end="")
            ans = int(input("Enter your answer: "))
            correct = question.check_answer(ans)
            score += 1 if correct else 0
            print(question.display_result(correct))

        print("Your score is {}.".format(score))
        cont = input("Do you want to play again (y/n)? ")
