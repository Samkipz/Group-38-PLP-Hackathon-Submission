""" python program that takes user inputs and determines what career
the user should learn"""

print("****************************************")
print("This progrm compares what career you should pursue among:")
print("1. Medicine")
print("2. Journalism")
print("3. IT")
print("4. Teaching")
print("****************************************")
print()
print("Please answer the following questions using 'yes' or 'no' ")
print()

from random import shuffle

career_options = ['medicine','journalism','IT','Teaching']

career_advice = ['Then you should pursue a career in medicine',
                 'Then you should pursue a career in journalism',
                 'Then you should pursue a career in IT',
                 'Then you should pursue a career in teaching']

career_questions = ["Are you concerned about people's health? ",
                    "Do you like taking care of the sick? ",
                    "Do you love teaching the knowledge you have to other? ",
                    "Do you like handling students/pupils? ",
                    "Do you love working on technological devices/softwares? ",
                    "Would you like to one day work on an IT firm? ",
                    "Do you love the business of news (i.e. investigative journalism and reporting the news to others)? ",
                    "Would you one day like to work in the media, i.e. publish and broadcast news? "]

career_quiz = career_questions.copy()

shuffle(career_questions)

medicine_score = 0
Teaching_score = 0
IT_score = 0
journalism_score = 0

for quiz in career_questions:
    ans = input(quiz).lower()
    while (ans != 'yes' and ans != 'no' ):
        print("***** invalid input, please use 'yes' or 'no' ****")
        ans = input(quiz)

    if quiz == career_quiz[0] or quiz == career_quiz[1]:
        if ans == 'yes':
            medicine_score = medicine_score + 1
    if quiz == career_quiz[2] or quiz == career_quiz[3]:
        if ans == 'yes':
            Teaching_score = Teaching_score + 1
    if quiz == career_quiz[4] or quiz == career_quiz[5]:
        if ans == 'yes':
            IT_score = IT_score + 1
    if quiz == career_quiz[6] or quiz == career_quiz[7]:
        if ans == 'yes':
            journalism_score = journalism_score + 1
            

    
score = [ medicine_score, journalism_score, IT_score, Teaching_score ]

print()
maxScore = max(score)
score_tie = []

for s in range (len(score)):
    if score[s] == maxScore:
        position = score.index(score[s])
        score_tie.append(career_options[position])
        score[score.index(score[s])] = 5

print()
if score_tie != []:
    print("Your score indicates you love the following careers: ")
    for i in score_tie:
        print("-",i)
        
    print()   
    if len(score_tie)>1:
        print("Please select one of the following options to help determine your career path: ")
        for i in range( len(score_tie)):
            print(i+1,score_tie[i])
        
        x = eval(input("input selection as 1,2,3 : "))
        while(x >= len(score_tie)): 
            print("invalid selection ",x," is not among the ",len(score_tie)," options given")
            x = eval(input("input selection as 1,2,3 : "))
            
        if score_tie[x-1] in score_tie:
            print("You selected",score_tie[x-1])
            if score_tie[x-1] in career_options:
                x = career_options.index(score_tie[x-1])
                print(career_advice[x])
                
    else:
        print(career_advice[score.index(max(score))])
else:
    scoreIndex = score.index(max(score))
    print()
    print(career_advice[scoreIndex])
print()
