import random

def get_question():
    ques = input("What is your question? ")
    return ques

def check_question(ques):
    if (ques.endswith('?')):
        return True
    else:
        print("I'm sorry, I can only answer questions.")
        return False

def answers():
    response = ['It is certain', 'It is decidedly so', 'Without a doubt',
                'Yes definitely', 'You may rely on it', 'As I see it, yes','Most likely',
                'Outlook good',
                'Yes',
                'Signs point to yes',
                'Reply hazy try again',
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don\'t count on it',
                "My reply is no",
                'My sources say no',
                'Outlook not so good',
                'Very doubtful']
    return random.choice(response)


question = get_question()

while(get_question() != "quit"):
  print(answers())

