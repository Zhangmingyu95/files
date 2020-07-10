from sys import argv
from os.path import exists
from sys import exit
from random import random
'''
prompt='>'

print("Hi %s %s" % (user_name,script))
print("do you like me %s" % user_name)
likes=input()
print("where do you live %s" % user_name)
lives=input()
print("what kind of computer do you have")
computer=input(prompt)

print("all in all ,you said you %s about me, and you lives in %s,and you have a %s" %(likes,lives,computer))



script, filename=argv

txt=open(filename,'w')

#print("here is your file %s " % filename)
#print(txt.read())
txt.truncate()
txt.write("this is the first line")
txt.write("this is the second line")
txt.write("this is the third line")
txt=open(filename,'r')
print(txt.readline())
txt.close()



script,filename,to_filename=argv
with open(filename,'r') as f1:
    txt=f1.read()
    print(txt)
    if exists(to_filename):
         print("file is exist")
         with open(to_filename,'w') as f2:
             f2.truncate()
             f2.write(txt)
with open(to_filename,'r') as f3:
            txt2=f3.read()
            print(txt2)
            print(txt2==txt)



def print_two(*args):
    arg1,arg2=args
    print("arg1:%r.arg2:%r" % (arg1,arg2))


#print_two("zed","sara")
print_two("rose")

def cheese_adn_crackers(cheese_count,boxes_of_crackers):
    print("")


script,input_file=argv

def print_all(f):

        print(f.read())

def rewind(f):
    f.seek(0)

def prin_a_line(line_count,f):
        print(line_count,f.readline())

current_file=open(input_file)

print("------1--------")

print_all(current_file)

rewind(current_file)

current_line=1

prin_a_line(current_line,current_file)

current_line=current_line+1

prin_a_line(current_line,current_file)

current_line=current_line+1

prin_a_line(current_line,current_file)



def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence ="All good things come to those who wait"
words=break_words(sentence)
print(words)
sorted_words=sort_words(words)
print(sorted_words)
print_first_word(words)
print_last_word(words)


print("you enter a dark room with two doors. do you go through door #1 or #2?")
door=input(">")
if door == "1":
    print("there is a giant bear here eating a cheese cake.what do you do")
    print("1:take the cake")
    print("2:scream at the bear")
    bear=input()
    if bear == "1":
        print("the bear eat you")
    elif bear =="2":
        print("the bear eat you too")
    else:
        print("please enter the right num")
elif door == "2":
    print("you stare into the endless abyss a Amy's retina")
else:
    print("please tell me which ddo you will step into")


i=0
while True:
   print(i)
   i+=1
   if i > 200:
       print("stop")
       break

def gold_room():
    print("this room is full of gold,How much do you take")
    next=input(">")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("man,learn to type a number")
    if how_much<50:
        print("nice you are not greedy")
    else:
        dead("you greedy bastard")
def bear_room():
    print("there is a bear here.\n the bear has bunch of honey")
    bear_moved=False
    while True:
        next=input(">")
        if next=="take money":
            dead("the bear looks at you then slaps your face off")
        elif next=="taunt bear" and not bear_moved:


cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksoncille'}

cities['NY']='New York'
cities['OR']="portland"

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "not found"

cities['_find']=find_city

while True:
    state=input(">")
    if not state:break
    city_found=cities['_find'](cities,state)
    print(city_found)



def death():
    quips=["you died. you kinda suck at this.","nice job ,you died ..jackass.","such a luser.","I have asmall puppy thatis better at this."]
    print(random(0, len(quips)-1))
    exit(1)

def central_corridor():
    print("Armory and about to pull a weapon to blast you.")
    action = input("> ")
    if action == "shoot!":
        print("you are dead. Then he eats you.")
        return 'death'
    elif action == "dodge!":
        print ("your head and eats you.")
        return 'death'
    elif action == "tell a joke":


class TheThing(object):
    def __init__(self):
        self.number=0

    def some_function(self):
        print("I got called")

    def add_me_up(self,more):
        self.number+=more
        return self.number

a=TheThing()
b=TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(20))

print(a.number)
print(b.number)
'''

class SleepingRoom(object):
    def __init__(self):
        self.name="bedroom"
