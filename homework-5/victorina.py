import random
questions = ['Which country has the largest population in the world?', 'The United States consists of how many states?',
             'Which is the hottest continent on Earth?', 'Which country is also known as the Netherlands?',
             'Which country is called the Land of Rising Sun?']

answers = ['China', '50', 'Africa', 'Holland', 'Japan']

question_order = list(range(len(questions)))
random.shuffle(question_order)
points = 0
for i in question_order:
    print(questions[i])
    user_answer = input('Enter your answer: ')
    if user_answer.lower() == answers[i].lower():
        points += 1
print(points)