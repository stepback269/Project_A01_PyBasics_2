# Date: 7/02b/2025  version 004a  <-- latest edit search for: "#: 03:"  or for "#: 53:"
# (1) This Python file will be similar to the earlier Learn_String_Methods and also base don Indently's YouTube video
#   (1a) located at: https://www.youtube.com/watch?v=0yySumZTxJ0&t=1s
# (2) Emphasis is diverted here away from the target of the "learning" (e.g. List methods) and toward the
#     "LEARNING" itself.
#   (2a) According to a number of educators, stopping to ask and answer QUESTIONS about what you are studying
#       increases the effectiveness of the learning process significantly. (Because it forces your brain to
#       actively generate its own output rather than passively intaking information).
#   (2b) See "Smartest People Read Books Like This" by Python Programmer here: https://www.youtube.com/watch?v=mOJu1I57Ajc
#   (2c) See "Semantic Encoding" here: https://www.google.com/search?q=smantic+encoding&sourceid=chrome&ie=UTF-8
#   (2d) See "Prompt Engineering" here: https://www.youtube.com/watch?v=_ZvnD73m40o
#   (2e) See "Learning resources are everywhere" here: https://gilesknowledge.substack.com/p/learning-resources-are-everywhere
# (3) In the coding exercises below we will include a FOOD FOR THOUGHT questionire to improve the "LEARNING" aspects

# According to Indently, there are only 11 list methods --NOT counting Dunder methods
# 38:APPEND(), 39:CLEAR(),   40:COPY(), 41:COUNT(),  42:EXTEND()
# 43:INDEX(),  44:INSERT(),  45:POP(),  46:REMOVE(), 47:REVERSE(), 48:SORT()

# more ... code snippet exercises:
# 01:CHOICE(), 02:SHUFFLE(), 03:RANDOMrange(), more ...

# Aside from Indently, there are other worthwhile videos to cover here including:
# (4) Mosh --- How to Use Lists in Python: https://www.youtube.com/watch?v=9OeznAkyQz4
# (5) Bro Code -- Python lists, sets, and tuples explained: https://www.youtube.com/watch?v=gOMW_n2-2Mw

'''
FLOW CONTROL CHANGES:
In order to skip some coding exercises, we introduce the notion of a skip-this controler list
skip_diz_func_A = a first  list of 30 integers, each for controlling activation of tutorials #01 to #29
skip_diz_func_B = a second list of 30 integers, each for controlling activation of tutorials #30 to #59
skip_diz_func_C = a third  list of 30 integers, each for controlling activation of tutorials #60 to #99
skip_diz_template = range(0,31) = use this as a template for identifying the index of the 30 int lists
'''
def gen_index_templ4(numb_indices):      #--func prints out a template of numb number of indices plus one
    skip_diz_template_create = range(numb_indices + 1)
    skip_diz_template = list(skip_diz_template_create)
    for i in skip_diz_template: print(format(i ,"02d"), end = ' ')
    print(f'\nTemplate printed out above for {numb_indices} plus one indices\n')

gen_index_templ4(6)
gen_index_templ4(10)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# see https://www.geeksforgeeks.org/python/range-to-a-list-in-python/

def gen_preFilled_list4(numb_indices, filler = 0):    #--func prints out a list of numb number of indices plus one
    skip_diz_template_A = [filler] * (numb_indices +1)    #-- and returns the gen'd list
    for i in skip_diz_template_A: print(format(i ,"02d"), end = ' ')
    print(f'\nPre-filled list printed out above for {numb_indices} plus one indices\n')
    return skip_diz_template_A

skip_diz_list_a = gen_preFilled_list4(6, 0)
skip_diz_list_b = gen_preFilled_list4(10, 1)
print(skip_diz_list_a)
print(skip_diz_list_b)

numb_indices = 10   #--this value is internal to the last run of function above
print(f'Pre-filled strings list printed out above for {numb_indices} plus one indices\n')

# problem1: first 10 positions are 1 digit and then after it is two digits
# see https://stackoverflow.com/questions/29000613/add-leading-zeros-to-a-list-of-numbers-in-python

# problem2: how to align items on two rows of print outs (now that we're doing row1 + row2 for die dots)
# see https://labex.io/tutorials/python-how-to-align-output-in-python-printing-418802

def halt4_food(method_ID_numb = 0, method_name = 'List method', verb = 'generate', output = 'modified_list',
               original = 'original_list_example'):
    esc = '\033['; wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'
    print(f'\n#0{method_ID_numb}: Output of {method_name} is this {verb}d \t{output}')
    print(f' \t\t\t\t original list was = \t\t{original}\n')
    print(f'{yel_text}FOOD FOR THOUGHT: What applications can {method_name} be used for?{wht_text}')
    print(f'(1): {method_name} can {verb} a ____ list to produce ____ in context of ____')
    print(f'(2): {method_name} can {verb} a ____ list to produce ____ in context of ____')
    halt_02 = input(f'Do you have any more application ideas for {red_text}{method_name}{wht_text} ??__\n')

print('WELCOME TO LEARN LIST METHODS')
print('-' * 20)
print(f'First tutorial is number #: 01: CHOICE()')

method_name = 'CHOICE()'
method_ID_numb = 1
list_example_01 = ['Adam', 'Brad', 'Charlie', 'David', 'Ernie']
list_example_01_mod = ['Brad', 'Charlie', 'David']
halt4_food(method_ID_numb, method_name, 'Random choosing',list_example_01_mod,
               list_example_01)
# breakpoint()


#: 01:
# Indently's code for "gluing"-in a random choice function ( https://www.youtube.com/watch?v=H6Zn8MdcBwg )
method_name = 'CHOICE()'; method_ID_numb = 1; verb= 'Choosing dice roll outcome'

from random import choice       # ^^^^ above Indently URL explains advantages of the Python language
# dice_faces: int = range(1,7)    #-- generates a list of integers 1-6 (default start of range is 0)
# go_again = 'y'                  # ^^^ forinfo re random.choice, see:
#                               # https://www.google.com/search?q=python+random+choice&sourceid=chrome&ie=UTF-8
# face_imgs = ['🎲', '⛹️‍♀️', '🧑🏻‍🤝‍🧑🏻', '👪', '👨‍👨‍👧‍👦', '👪👨‍👦', '👪👪']  #<-- icons were obtained from below URL:
# face_imgs = ['🀣', '🀙', '🀚🀚', '🀛🀛🀛', '🀜🀜🀜 🀜', '🀝🀝🀝 🀝🀝', '🀞🀞🀞 🀞🀞🀞']
#face_imgs = ['🙉', '💛', '❤️❤️', '💚💚💚', '💙💙 💙💙', '💕💕❣️💕💕', '❣️❣️❣️ ❣️❣️❣️']
# ^^^^ https://copychar.cc
#   00 01 02 03 04 05 06
#   Template printed out above for 6 plus one indices

def choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a):
    if skip_diz_list_a[method_ID_numb] == 1:
        print(f'method number {method_ID_numb} has been skipped\n')
        return None     #--skip this tutorial if skip position is set to 1
    face_imgs_row1 = ['🤬', '🧐', '🤓🤓', '😲😲', '🤩🤩', '😋   🤪',   '🤠🤠🤠' ]
    face_imgs_row2 = ['☠️', ' ',   '  ',   '😲',    '🤩🤩', '😋😛🤪',   '🤠🤠🤠' ]
    print('\n\n', '-' * 20)

    dice_faces: int = range(1,7)    #-- generates a list of integers 1-6 (default start of range is 0)
    go_again = 'y'
    while go_again == 'y':
        roll_1 = choice(dice_faces)
        roll_2 = choice(dice_faces)
        print(f'\n#:00; example of random choice')
        print(f' 1st die roll gives you a \t{roll_1}\t{face_imgs_row1[roll_1]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_1]}\n')
        print(f' 2nd die roll gives you a \t{roll_2}\t{face_imgs_row1[roll_2]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_2]}\n')
        print(f' The SUM of the two rolls is \t{roll_1 + roll_2} \n')
        go_again = input('Try again? Enter y or other here__')
    halt4_food(method_ID_numb, method_name, verb, face_imgs_row1,
               face_imgs_row2)

choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a)

breakpoint()

#: 02a ANSI COLOR escape codes
esc = '\033['
wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'; grn_text = esc + '32m'
blu_text = esc + '34m'; cyan_text = esc + '36m'; magen_text = esc + '35m'
'''
from: Google prompt: "python escape codes for coloring output"
Basic Structure:
The core of an ANSI escape sequence for styling is \033[ or \x1b[, followed by one or more numerical codes separated by semicolons, and ending with m.
Common Codes:
Reset:
\033[0m resets all applied styles (color, background, effects) to default.
Background Colors:
Red Background: \033[41m  Green Background: \033[42m (Similar patterns for other colors, 
e.g., 40m for black background, 47m for white background, and 100-106m for bright background colors)
Text Effects:
Bold: \033[1m  Dim: \033[2m  Underline: \033[4m
Blink: \033[5m (Note: blinking might not be supported or desirable in all terminals)
'''

#: 02: SHUFFLE()    = Randomly shuffle a list
from random import shuffle      #<-- from Indently's learn RANDOM methods found at:
                    # https://www.youtube.com/watch?v=Ffeb5ibQDP0
list_example_01 = ['Adam', 'Brad', 'Charlie', 'David', 'Ernie']
list_example_01a = list_example_01.copy()
shuffle(list_example_01)

n=2; method_name = 'shuffle()'
print('\n')
print(f'#0{n}  method = {method_name}  shuffled output= \t{list_example_01}')
print(f' \t\t\t\t original list was = \t\t{list_example_01a}\n')
print(f'{yel_text}FOOD for THOUGHT: What applications can SHUFFLE() be used for?{wht_text}')
print(f'(1): Shuffle 52 playing cards e.g. Poker, then pick a random index in range of 0 to 51-5, then pick 5 cards')
print(f'(2): Shuffle a list of N nouns and also M verbs, then generate random sentences for new ideas')
halt_02 = input(f'Do you have any more application ideas for {red_text}SHUFFLE(){wht_text} ??__\n')


#: 03: RANDOMrange()    = more random functions
n += 1; method_name = 'random()'
from random import random, randint, randrange      #<-- from Indently's learn RANDOM methods
rand_02one: float = random()

print('\n')
print(f'#0{n}a  method = {method_name}  generated output= \t{rand_02one} \n')
print(f'{yel_text}FOOD for THOUGHT: What applications can RANDOM() be used for?{wht_text}')
print(f'(1): Pick a random member of a list of N words (e.g., nouns, verbs, adverbs, adjectives, more ...?')
print(f'(2): Pick a random member of a list of code snippets, then exec the picked snippet= genetic code create')
halt_02 = input(f'Do you have any more application ideas for {red_text}RANDOM(){wht_text} ??__\n')

n += 0; method_name = 'randint(arg1, arg2)'       #<-- creates a list in range of arg1 to arg2 inclusive
rand_a2b: list[int] = randint(10, 20)
print(f'#0{n}b  method = {method_name}  generated list= \t{rand_a2b}')

rand_a2b: list[int] = [randint(10, 20) for _ in range(5)]
print(f' \t\t\t\t expanded list is = \t\t{rand_a2b}\n')
print(f'{yel_text}FOOD for THOUGHT: What applications can RANDINT() be used for?{wht_text}')
print(f'(1): Pick a random member of a list of N indexes (e.g., point to nouns, verbs, adverbs, adjectives, more ...?')
print(f'(2): Pick a random member of a list of N identifiers of code snippets, then exec the picked snippet= genetic code create')
halt_02b = input(f'Do you have any more application ideas for {red_text}RANDOMINT(){wht_text} ??__\n')


breakpoint()        #<-- halted at 2:44 of https://www.youtube.com/watch?v=Ffeb5ibQDP0

# Indently's code for printing out all the methods is as follows
def gen_list_of_methods():
    i: int =0
    for method in dir(list):    #<-- how do we set the path for directory? Don't have to. We're executing inside Py!
        i += 1
        print(i, method, sep=': ')
        if i > 100:
            break
        else:
            pass
gen_list_of_methods()
print('*' *20, '\n')

# Let's start with an example list of string objects:
example_list_01: list[str] = ['Adam', 'Bob', 'Calvin', 'Dario']  #<-- a type hinted list of strings, people names

#: 38:   APPEND()   = adds a new item to the specified list (append is number 38 in the gen_list output)
n=38; method_name = 'append()'; example_list_01.append('Ernie')
print(f'{n}  {method_name}  output= {example_list_01} \n\n')

#: 39:   CLEAR()     = clears the specified list (empties it)
n+=1; method_name = 'clear()'; example_list_01.clear()
print(f'{n}  {method_name}  output= {example_list_01} \n\n')

#: 40:   COPY()      = creates a separate copy of the acted-on list if just pure strings
n+=1; method_name = 'copy()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario']
example_list_02 = example_list_01.copy()
print(f'{n} \t{method_name} \toutput1= {example_list_01}')
print(f' \t\t\t output2= {example_list_02}\n\n')
example_list_02.remove('Dario')
print(f'{n}a \t{method_name} \toutput1= {example_list_01}  no change here')
print(f' \t\t\t output2.removed= {example_list_02}\n\n')

example_list_03 = ['Adam', 'Bob', ['Calvin', 'Frank']]  #<-- this list contains a nested list
example_list_04 = example_list_03.copy()
example_list_04[2][1] = 'George'    #<-- this replacement action supposedly puts in George in place of Frank in #4
print(f'{n}b \t{method_name} \toutput3= {example_list_03}  also CHANGED!')     #<-- but NO !! the mod affects both lists
print(f' \t\t\t output4.modified= {example_list_04}\n\n')

#: 41:   COUNT()   = COUNTS HOW MANY TIMES an item exists in the list
n+=1; method_name = 'count()'; example_list_01 = ['Adam', 'Bob', 'Bob', 'Calvin', 'Calvin', 'Calvin', 'Dario']
numb_Bobs = example_list_01.count('Bob')
numb_Cals = example_list_01.count('Calvin')

print(f'{n}a \t{method_name} \toutput1= There are {numb_Bobs} Bobs in the list')
print(f' \t\t\t output2= There are {numb_Cals} Calvins in the list \n')

#: 42:   EXTEND()    = extends a first list by appending a second list
n+=1; method_name = 'extend()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario']
example_list_02 = ['Ernie', 'Frank']
example_list_01.extend(example_list_02)
print(f'{n} \t{method_name} \toutput= {example_list_01} as extended \n')

#: 43:   INDEX()   = Finds the index number of the specified item within the list
n+=1; method_name = 'index()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario']
locate= example_list_01.index('Calvin')
print(f'{n} \t{method_name} \toutput= {locate} is index location of arg1 \n')

#: 44:   INSERT()  = inserts into the specified locationof arg1, the given element specified by arg2
n+=1; method_name = 'insert()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario']
example_list_01.insert(1, 'George')
print(f'{n} \t{method_name} \toutput= {example_list_01} with its insert included \n')

#: 45:   POP() = pops an indexed item off the acted-on list and returns the popped item, i= -1 by default
n+=1; method_name = 'pop()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario', 'Ernie', 'Frank']
original = example_list_01.copy()
last = example_list_01.pop()
first= example_list_01.pop(0)
print(f'{n} \t{method_name} \toutput1= {last} = popped off from end of list')
print(f' \t\t\t output2= {first} = popped off from front of list')
print(f' \t\t\t original list = {original} ')
print(f' \t\t\t current list = {example_list_01} = after two pop offs \n')

#: 46:   REMOVE()  = similar to POP except it does not return the removed item AND arg1 must be supplied as a member of the list
n+=1; method_name = 'remove()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario', 'Ernie', 'Frank']
original = example_list_01.copy()
end = len(example_list_01)-1
pop_off_item = example_list_01[-1]
example_list_01.remove(pop_off_item)
print(f'{n} \t{method_name} \toutput1= {example_list_01} = current after removal from end of list')
pop_off_item = example_list_01[0]
example_list_01.remove(pop_off_item)
print(f' \t\t\t output2= {example_list_01} = current after removal from front of list')
print(f' \t\t\t original list = {original} \n')

#: 47:   REVERSE() =  reverses the order in the list
n+=1; method_name = 'remove()'; example_list_01 = ['Adam', 'Bob', 'Calvin', 'Dario', 'Ernie', 'Frank']
flipped = example_list_01.reverse()
print(f'{n} \t{method_name} \toutput1= {example_list_01} = current after reversal of the list \n')

#: 48:   SORT()    = sorts the items in the list according to a key, default is alphabetic but case sensitive
n+=1; method_name = 'sort()'
example_list_01.sort()
print(f'{n} \t{method_name} \toutput1= {example_list_01} = current after reversal and sorting')
example_list_01.sort(key = lambda name: len(name))      #<-- sorting according to length of the item name
print(f' \t\t\t resorted list = {example_list_01} = by len of name \n')

#: 50:  Mosh's string tricks at https://www.youtube.com/watch?v=9OeznAkyQz4
n=50; method_name = 'nested lists'
example_list_50 = [[0, 1, 2], [3, 4, 5], [6, 7, 8],]
print(f'{n} \t{method_name} \toutput1= {example_list_50} = 3x3 matrix')
print(f' \t\t\t first  row = {example_list_50[0]}')
print(f' \t\t\t second row = {example_list_50[1]}')
print(f' \t\t\t third  row = {example_list_50[2]}\n')

#: 51: plural lists, concatenated lists
n+= 1; method_name = 'concat-ed lists'
example_list_51a = [0] * 10
example_list_51b = example_list_50[0:2]         #<-- reminder: slice stop is not included
example_list_51c = example_list_51a + example_list_51b
print(f'{n} \t{method_name} \toutput1= {example_list_51c} = sum of a + b\n')

#: 52: generating lists with the range function
n+= 1; method_name = 'using the range function'
example_list_52a = list(range(1,11))            #<-- reminder: stopper index is not included
example_list_52b = list(map(str, example_list_52a))    #<-- str() can only do one int at a time, map applies it that way
# ^^^ for converting list of ints to str's see different methods described in:
#       https://www.geeksforgeeks.org/python/python-program-to-convert-list-of-integer-to-list-of-string/
print(f'{n} \t{method_name} \toutput1= {example_list_52a} = list of integers')
print(f' \t\t\t output2= {example_list_52b} = list of strings \n')
example_string_52c = "Hello World"
list_52c = list(example_string_52c)
print(f' \t\t\t output3= {list_52c} = list function applied to a string \n')

#: 53: counting items in a list with the len() function  # Mosh at (3:45)
n+= 1; method_name = 'counting items in a list'
print(f'{n} \t{method_name} \toutput4= {len(list_52c)} = count of items in list form of "Hello World \n')
