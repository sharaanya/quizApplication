from tkinter import *
import time


class quiz:

    def __init__(self, questions, answers, correct_answer):
        self.questions=questions
        self.answers=answers
        self.correct_answer=correct_answer
        # self.display_question( )



def m(check):
    if check==1:
        qstn=open('history.txt', 'r')
        answ=open('history_answers.txt', 'r')
        qq=qstn.readlines( )
        aa=answ.readlines( )
        j=0
        run=[]
        for i in range(0, len(qq), 6):
            qt=qq[i]
            ans=[qq[i + 1], qq[i + 2], qq[i + 3], qq[i + 4]]
            c_a=aa[j]
            j+=1
            run.append(quiz(qt, ans, c_a))
    elif check==2:
        qstn=open('GK.txt', 'r')
        answ=open('GKanswers.txt', 'r')
        qq=qstn.readlines( )
        aa=answ.readlines( )

        j=0
        run=[]
        for i in range(0, len(qq), 6):
            qt=qq[i]
            ans=[qq[i + 1], qq[i + 2], qq[i + 3], qq[i + 4]]
            c_a=aa[j]
            j+=1
            run.append(quiz(qt, ans, c_a))

    return run