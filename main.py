def new_game():
    guesses=[]
    guess=None
    opt=['A','B','C']
    correst_guesses=0
    cur_question=1
    for key in questions:
        print("-----------")
        print(key)
        for i in options[cur_question-1]:
            print(i)

        while guess not in opt:
             guess = input('enter (A,B,C): ').upper()
        guesses.append(guess)
        correst_guesses+= check_answer(questions.get(key),guess)
        cur_question+=1
        guess=None
    display_score(correst_guesses,guesses)
def check_answer(answer,guess):
    if answer==guess:
        print('correct')
        return 1
    else:
        print('wrong')
        return 0



def display_score(correct_guesses,guesses):
    print('=================')
    print('results')
    print('=================')
    print('answers:',end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print('guesses:',end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    score=int((correct_guesses/len(questions))*100)
    print('your score: '+str(score)+'%')
def play_again():

    response=None
    while response not in ['Y','N']:
        response=input('play again?(Y/N)').upper()
    if response=='Y':
        response=None
        return True
    else:
        response=None
        return False


questions = {'gdzie nocą tupta jeż?': 'A', 'czemu papież nie może zjeść burgera': 'C', 'gdie raki zimuja?': 'B'}
options = [['A. do dupy', 'B. do poznania', 'C. do burdelu'],
           ['A. bo ich nie lubi', 'B. bo je tylko kremówki', 'C. bo nie zyje'],
           ['A. w dupie', 'B. nigdzie,raki nie zimuja', 'C. w burdelu'], ]
new_game()
while play_again():
    new_game()
print('bye')