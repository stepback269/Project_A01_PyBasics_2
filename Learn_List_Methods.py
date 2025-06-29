# Date: 6/28c/2025  version 002  <-- latest edit search for "#: 53:"
# This Python file will be similar to the earlier Learn_String_Methods and also base don Indently's YouTube video
# (1) located at: https://www.youtube.com/watch?v=0yySumZTxJ0&t=1s
# There are only 11 list methods according to Indently --NOT counting Dunder methods
# 38:APPEND(), 39:CLEAR(),   40:COPY(), 41:COUNT(),  42:EXTEND()
# 43:INDEX(),  44:INSERT(),  45:POP(),  46:REMOVE(), 47:REVERSE(), 48:SORT()

# Aside from Indently, there are other worthwhile videos to cover here including:
# (2) Mosh --- How to Use Lists in Python: https://www.youtube.com/watch?v=9OeznAkyQz4
# (3) Bro Code -- Python lists, sets, and tuples explained: https://www.youtube.com/watch?v=gOMW_n2-2Mw

# Indently's code for "gluing"-in a random choice function ( https://www.youtube.com/watch?v=H6Zn8MdcBwg )
from random import choice       # ^^^^ above URL explains advantages of the Python language
dice_faces: int = range(1,7)    #<-- generates a list of integers 1-6 (default start of range is 0)
go_again = 'y'                  # ^^^ forinfo re random.choice, see:
#                               # https://www.google.com/search?q=python+random+choice&sourceid=chrome&ie=UTF-8
face_imgs = ['🎲', '⛹️‍♀️', '🧑🏻‍🤝‍🧑🏻', '👪', '👨‍👨‍👧‍👦', '👪👨‍👦', '👪👪']  #<-- icons were obtained from below URL:
                        # ^^^^ https://copychar.cc
while go_again == 'y':
    roll_1 = choice(dice_faces)
    roll_2 = choice(dice_faces)
    print(f'\n#:00; example of random choice')
    print(f' 1st die roll gives you a {roll_1}   {face_imgs[roll_1]}')
    print(f' 2nd die roll gives you a {roll_2}   {face_imgs[roll_2]}')
    print(f' the SUM of the two rolls is {roll_1 + roll_2} \n')
    go_again = input('Try again? Enter y/n here__')

# breakpoint()

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
