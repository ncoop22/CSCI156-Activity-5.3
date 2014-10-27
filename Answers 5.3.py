__author__ = 'Nickolas'
def KnockKnockIntro():
    print("knock, Knock")
    print("Who's There?")

def setup(a):
    print(a)
    print(a+" "+"who?")



def punchline(a,x):
    KnockKnockIntro()
    setup(a)
    print(x)

a=input("who")
x=input("punchline")
punchline(a,x)