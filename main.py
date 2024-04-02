from question import Question

question_prompts=[
'1.Which programming language is best for websites?\n(a)Java\n(b)Javascript\n(C)Swift\n(d)Pandas\n',
'2.Which programming language is best for games?\n(a)Java\n(b)Javascript\n(c)C++\n(d)C language\n',
'3.Which programming language is not object oriented?\n(a)Clanguage\n(b)Javascript\n(C)Java\n(d)Python\n',
'4.Which one is not a pillar of OOP?\n(a)Encapsulation\n(b)Polymorphism\n(C)Method override\n(d)Abstraction\n',
'5.Which design pattern allows creation of only one instance of a class?\n(a)Proxy\n(b)Singleton\n(C)Facade\n(d)Decorator\n',
]

questions=[
    Question(question_prompts[0],'b'),
    Question(question_prompts[1],'c'),
    Question(question_prompts[2],'a'),
    Question(question_prompts[3],'c'),
    Question(question_prompts[4],'b')
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print('You got '+ str(score)+'/'+str(len(questions))+' correct')

run_test(questions)