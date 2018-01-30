def get_question():
    ques = input("What is your question? ")
    return ques

def check_question(ques):
    if (ques.endswith('?')):
        return True
    else:
        print("I'm sorry, I can only answer questions.")
        return False



question = get_question()

while(get_question() != "quit"):
  pass

