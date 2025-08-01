# Date: 7/27b/2025  version 007a  <-- stripped #2, new clrj() color generator substituted in with validity check

import inspect
import sys
import os
import keyboard             #--- enable single key press inputs
import webbrowser           #--- enable opening up desired URL's for learning frames
import pyperclip            #--- enable use of clipboard
import colorama             #--- contains Fore escape codes
colorama.init()
from colorama import Fore, Back, Style      #-- see G4G here: https://www.geeksforgeeks.org/python/introduction-to-python-colorama/

W_ = 'HWb'; M_ = 'Hmb'; C_ = 'DCb'; R_ = 'HRb'; Y_ = 'HYb'  #-- Define aliases for global color combos to use inside funcs

def sl3(filler="*", times=90):   #-- separation line w \n above and an extra one below
    outp: str = cj(W_) + filler * times
    print('\n', outp, '\n')
    return None
sl = sl3('🤪')   #-- https://copychar.cc

def sl2(filler="*", times=90):   #-- bottom separation line w extra \n below
    outp: str = cj(W_) + filler * times
    print(outp, '\n')
    return None

def sl1(box_id ='(__)', filler="*", times=90):   #-- top separation line w \n above
    outp: str = f"\n{cj(W_)}{box_id}{filler * (times-4)}"
    print(outp)
    return None

def sl0(filler="*", times=40):   #-- separation line w no CRLF
    outp: str = cj(W_) + filler * times
    print(outp, end='')
    return None

def slm(mssg="MID MESSAGE GOES HERE", filler="**", times=2):   #-- mid box messages
    outpmid: str = f"{cj(W_)}{filler}{cj(M_)}{mssg.center(90-4)}{cj(W_)}{filler}"
    print(outpmid)
    return None


clr: dict = {'b':"BLACK", 'r':"RED", 'g':"GREEN", 'y':"YELLOW", 'u':"BLUE", 'm':"MAGENTA", 'c':"CYAN", 'w':"WHITE",
             'o':"RESET",
             'B':"LIGHTBLACK_EX", 'R':"LIGHTRED_EX", 'G':"LIGHTGREEN_EX", 'Y':"LIGHTYELLOW_EX", 'U':"LIGHTBLUE_EX",
             'M':"LIGHTMAGENTA_EX", 'C':"LIGHTCYAN_EX", 'W':"LIGHTWHITE_EX",
             'D':"DIM", 'N':"NORMAL", 'H':"BRIGHT", 'O':"RESET_ALL"}
#^^ in above, single letter for Fore color alone, 2 chars for Fore + Back, 3 chars for Style + Fore + Back in that order

def qif_inStr_OK(inStr, slices_list, allowed):
    for s in slices_list:
        if inStr[s] in allowed:
            continue
        else:
            print(f'Bad character {inStr[s]} found in supplied input by qif')
            return False
    return True

def cj(chars: str = W_, d: dict = clr):     #-- COLORAMA color commands generator using the clr dictionary
    numb = len(chars)
    allowed_4_Fore = 'brgyumcwoBRGYUMCW'
    allowed_4_Style = 'DNHO'
    if numb < 1:
        print(f'argument error in cj function call')
        return None

    elif numb < 2:
        if qif_inStr_OK(chars, [0], allowed_4_Fore):  #-- check for valid input String
            pass
        else:
            print(f'qif_inStr_OK found a bad input char at below breakpoint')
            breakpoint()
            return None
        sum: str = getattr(Fore, d[f'{chars[0]}'])    #-- if one char it is FORE color
        return sum

    elif numb < 3:
        if qif_inStr_OK(chars, [0, 1], allowed_4_Fore):  #-- check for valid input String
            pass
        else:
            print(f'Bad character in inputs to cj()')
            return None
        sum: str = getattr(Fore, d[f'{chars[0]}'])  + getattr(Back, d[f'{chars[1]}']) # -- if 2 chars
        return sum

    elif numb < 4:
        if qif_inStr_OK(chars, [1, 2], allowed_4_Fore):
            pass
        elif qif_inStr_OK(chars, [0], allowed_4_Style):
            pass
        else:
            print(f'Bad character in inputs to cj() found by qif at numb=3')
            return "error in numb=3"
        sum: str = getattr(Style, d[f'{chars[0]}'])  + getattr(Fore, d[f'{chars[1]}'])  + getattr(Back, d[f'{chars[2]}']) # -- if 3
        return sum
    else:
        print(f'arguments error in cj function call')
        return None

# COLOR and func call ALIASES
x0 = w = cj(W_)  #c0 = 'HWb';  #-- color combo shortcuts ... this one for BRIGHT WHITE on Black background
x1 = x = cj('Ncb')  #c1 = 'Ncb';       #-- Normal Cyan   ... it's short since cj(cn) has no quote marks
x2 = z = cj('Dcb')  # c2 = 'Dcb';   #-- Dim Cyan
x3 = y = cj(Y_)     #c3 = 'y';      #-- Yellow
x4 = cj('Nyb')
# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w

welcome_txt_01 = f'WELCOME TO LEARNING AND REVIEWING PYTHON LISTS'
intro_01a = '(01)  <-- This is the current lesson frame number'
intro_01b = 'We will be exercising various Python list methods here'
intro_01c = 'Many other Python features are brought to light at the same time including but not limited to:'
intro_01c0 = f'(a) Using the {x3}COLORAMA{x2} module to print different colors on the console'
intro_01c1 = f'(b) Using {y}string alignment{z} (e.g., Str.center, spc:<10, more)'
intro_01c2 = f'(c) Using functions to generate indented lists like this one'
intro_01c3 = f'(d) Using the {y}Webster module{z} to open additional info in the web browser'
intro_01c4 = f'(e) Using the {y}Keyboard module{z} to detect single keystroke inputs'
intro_01c5 = f'(f) Linking to {y}my own "Back of Stage" blog{z} to provide more on-topic information'
intro_01c6 = f'(g) Opening a {x}"More to Explore"{z} informational web page ---> {y}Look in your browser -->{z}'

intro_01c_list = [intro_01c0, intro_01c1, intro_01c2, intro_01c3, intro_01c4, intro_01c5, intro_01c6 ]

intro_01d = f'For this first frame (01) we additionally {y}link to Back Stage web page explaining "aliases" -->{z}'


spc = ' '
display_id = '(00)'     #-- print initial welcome mat
sl1(display_id)
slm(welcome_txt_01)     #-- middle line uses this text message
sl2()

outp_01a: str = f'{x}{intro_01a.center(90)}'; print(outp_01a)   #-- print exercise frame (01)
outp_01b: str = f'{x}{intro_01b.center(90)}'; print(outp_01b)
outp: str = f"\n{z}{intro_01c}"; print(outp)        #-- z is alias for cj('Dcb') #--reuse "outp" variable

def outp_list(list_name = intro_01c_list, colors = 'Ncb', indent=10):
    for item in list_name:
        print(f'{cj(colors)}{spc:<10}{item}')       #-- note colon between spc and indent
    #print(f'{x4}\nend of for loop hit <--a debug notification\n')
    return

outp_list()     #-- execute above func

url_01 = "https://oldmanlearningsupport.blogspot.com/2025/07/back-stage-support-for-old-man-learns.html"
#webbrowser.open(url_01)
print("webster temporarily disabled at line 143")

url_02 = "https://steppingback269.blogspot.com/2025/07/code-beauty-trumps-that-of-display.html"
#webbrowser.open(url_02)
print("webster temporarily disabled at line 147")
print(intro_01d, '\n')

def next_frame(display_id = '(02)', intro_01x = f'{display_id} Hit "c" or "SPACE" to continue to next learning frame',
               intro_01y = 'Hit "m" to open browser to show more information re this frame'):
    outp_01x: str = cj('Hrb') + intro_01x.center(90); print(outp_01x)
    outp_01y: str = cj('Hyb') + intro_01y.center(90); print(outp_01y)
    wait_01 = True
    while wait_01 == True:
        keyrd = keyboard.read_key()  # -- do just one read opertion per while loop
        if keyrd == "c":  # if the "c" key is pressed
            wait_01 == False;
            response = 'c'
            print('You Pressed the "c" key --this is a debug notification')
            break
        elif keyrd == "space":  # if the "space" key is pressed
            wait_01 == False;
            response = ' '
            print(f'\nYou Pressed the "SPACE" key --this is a debug notification')
            break
        elif keyrd == "x":  # if the "x" key is pressed
            wait_01 == False;
            response = 'x'
            print(f'\nYou Pressed the "x" key --this is a debug notification')
            break
        elif keyrd == "m":  # if the "m" key is pressed
            wait_01 == False;
            response = 'm'
            print(f'\nYou Pressed the "m" key --this is a debug notification')
            break
        else:
            continue
    return response

user_choice = next_frame('(02)')

#def test(callback):
#    print(callback.name)

#wait_01 = True
#while wait_01 == True:
#    keyboard.hook(test)
#    keyboard.wait()
#    if callback.name == "x":  #  if the "x" key is pressed
#        wait_01 == False
#        print('You Pressed the "x" key')
#        break


# breakpoint()

if user_choice == 'c' or user_choice == ' ':
    print(f'{y}DEFINITION: A Python "list" is a mutable array of items each addressed by an index starting at i = 0\n')
    pass

if user_choice == 'm':
    outp = f'{x}Normally m will open a web browser info page'; print(outp)
    outp = f'{w}But for this frame two web browser info pages were already generated'; print(outp,'\n\n')
    pass
#webbrowser.open("https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/")

mssg_02 = f'This will be a further exercise showing COLORAMA foreground and background colors'
display_id = '(02)'     #-- print mat number 2
sl1(display_id)
slm(mssg_02)     #-- middle line uses this text message (don't insert color inside mid mssg !!)
sl2()

# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w
print(f'\n{x}TEST of cj[abc] permutations\n')

print(f'{x}bW = \t{cj("bW")}This should be plain-Black on lite-white backround {w}and then back to white/b')
print(f'{x}HbY = \t{cj("HbY")}This should be brite Black on lite yellow backround {x}and then back to normal cyan')
print(f'{x}HcW = \t{cj("HcW")}This should be brite Cyan on brite white backround {x}and then back to normal')
print(f'{x}DcW = \t{cj("DCW")}This should be dim Cyan on brite white backround {x}and then back to normal')
print(f'{x}Hbu = \t{cj("HbU")}This should be brite Black on brite blue backround {x}and then back to normal')
print(f'{x}Uw = \t{cj("Uw")}This should be brite blue on dim white backround {x}and then back to normal')
symbols_01 = "▃" * 20; symbols_02 = "▔" * 20; symbols_03 = "▚" * 20;
print(f'{x}HbY = \t{cj("HbY")}{symbols_01}{symbols_02}{symbols_03}{x}and then back to normal cyan')

print(f'\n{x}See the adjacent browser for more info from G4G re Colorama {y}and TermColor -->{x}')
print(f'{x}Also see the adjacent browser for {y}Symbol picker website -->{x}')
print(f'\nNote that not all fore and background combinations work well with text chars\n')
url_03 = "https://www.geeksforgeeks.org/python/print-colors-python-terminal/"
webbrowser.open(url_03)
url_04 = "https://fsymbols.com"
webbrowser.open(url_04)

#breakpoint()

def brk(mssg):
    print(f'\n(X): A debug {Fore.YELLOW}brk(mssg) point{Fore.WHITE} was hit at {Fore.LIGHTGREEN_EX}line '
          f'{gotten_line_numb_2back()}{Fore.LIGHTWHITE_EX}')
    print(f'(Y): Pdb debugger commands: l=LIST, c=CONTINUE, pp var= PrettyPrint the specific var')
    print(f'(Z): Additional message: {mssg}\n')
    breakpoint()

frame_current = inspect.currentframe()
frame_info = inspect.getframeinfo(frame_current)

sl3()   #-- separator line

# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w
print(f'(1): Using the {y}Inspect module {x}we can learn the line number in the main code\n\t'
      f'At current execution time it is Line Number {frame_info.lineno}')
print(f'(2): We can also get the {cj('g')}file path + name {x}out of the frame info tuple, it is: \n\t {frame_info.filename}')
print(f'(3): We can also get the {cj('G')}name of the function {w}we are inside, at moment it is none, we get {frame_info.function}')

#^^^ above is based on https://www.youtube.com/watch?v=myTz-ZDkO6Q Professor Gerry Jenkins (https://www.youtube.com/@gjenkinsedu)
#^^^ see also Python.org documentation at https://docs.python.org/3/library/inspect.html

def get_line_numb_info_demo():
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    sl3()

    print(f'(a): ',f'current= {frame_info_current}', f'Using the Inspect module we can learn the line number in the caller"s code\n\t',
          f'At current execution time it is \tLine Number {frame_info_prior.lineno}')
    print(f'(b): We can also get the file path + name out of the frame info tuple, it is: \n\t {frame_info_current.filename}')
    print(f'(c): We can also get the name of the function we are inside, at moment we get: \t{frame_info_current.function}')

get_line_numb_info_demo()

def gotten_line_numb_1back():
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_prior.lineno}'
sl3()
print(f'\n(d): The gotten_line_numb func returned the following line number: \t{gotten_line_numb_1back()}')

def gotten_line_numb_2back():   #-- not finished see stack inspect 2 back !!!!
    frame_current = inspect.currentframe()
    frame_info_2priors_back  = sys._getframe(2)   #--get frame info from caller's caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_2priors_back.f_lineno}'    #--Google "python inspect two frames back"

brk('Used sys.getframe(2) and (dot)f_lineno to corectly point to line of brk() !!!!')


# 38:APPEND(), 39:CLEAR(),   40:COPY(), 41:COUNT(),  42:EXTEND()
# 43:INDEX(),  44:INSERT(),  45:POP(),  46:REMOVE(), 47:REVERSE(), 48:SORT()

# 01:CHOICE(), 02:SHUFFLE(), 03:RANDOMrange(), more ...

sl3()

def halt2_study(maybe, feature):
    if (maybe.lower() == 'n' or maybe.lower() == 'no' or maybe.lower() == 'not'):
        return
    else:
        print(f'The above ^^^^ printouts executed above {Fore.LIGHTGREEN_EX}line {gotten_line_numb_2back()}{Fore.LIGHTWHITE_EX} demonstrate exercise of {Fore.YELLOW}{feature}{Style.RESET_ALL} methods')
        wait = input('<Enter> to continue to next demonstartion\n')

def gen_index_templ4(numb_indices):      #--a func that prints out a template of input number of indices plus one
    skip_diz_template_create = range(numb_indices + 1)
    skip_diz_template = list(skip_diz_template_create)
    print(f'{clr["bw_"]}', end = '')
    for i in skip_diz_template: print(format(i ,"02d"), end = '__')  #-- apply the format() function one int at a time
    print(f'{clr["o"]}')
    print(f'\n{clr["Bmb_"]}Template printed out above for {numb_indices} plus one indices{clr["o"]}\n')

gen_index_templ4(6)     #-- creates an example template of 2 digits each for indices 0 to 6
gen_index_templ4(10)    #-- creates an example template of 2 digits each for indices 0 to 10

halt2_study('yes', 'Generate template of sequential, 2-digit index numbers')

sl3()

def gen_preFilled_list4(numb_indices, filler = 0):    #--func prints out a list of arg1 number of indices plus one
    skip_diz_template_A = [filler] * (numb_indices +1)    #-- and returns the gen'd list filled with the filler
    for i in skip_diz_template_A: print(format(i ,"02d"), end = ' ')  #-- no CRLF
    print(f'\nPre-filled list is printed above for {numb_indices} plus one indices\n')
    return skip_diz_template_A

skip_diz_list_a = gen_preFilled_list4(6, 0)
skip_diz_list_b = gen_preFilled_list4(10, 12)
print(skip_diz_list_a)  #-- output result a
print(skip_diz_list_b)  #-- output result b

halt2_study('yes', 'Generate pre-filled list of 2-digit filler numbers')


# Note: Upgraded below method to input a Dictionary full of parameters including prompts for AI models
example_list_A = ['🤬', '🧐', '🤓🤓', '😲😲', '🤩🤩', '😋   🤪',   '🤠🤠🤠' ]
example_list_B = ['🙉', '💛', '❤️❤️', '💚💚💚', '💙💙 💙💙', '💕💕❣️💕💕', '❣️❣️❣️ ❣️❣️❣️']
result_list1 = ['🀣', '🀙', '🀚🀚', '🀛🀛🀛', '🀜🀜🀜 🀜', '🀝🀝🀝 🀝🀝', '🀞🀞🀞 🀞🀞🀞']
result_list2 = ['🎲', '⛹️‍♀️', '🧑🏻‍🤝‍🧑🏻', '👪', '👨‍👨‍👧‍👦', '👪👨‍👦', '👪👪']

from datetime import datetime
halt4_IDs_params: dict = {'tute_ID':'00a', 'tute_name':'Indently_01a',
                          'tute_actions':'producing example output as follows: ',
                          'tute_input_var1':example_list_A, 'tute_input_var2':example_list_B,
                          'tute_output1':result_list1, 'tute_output2':result_list2,
                          'tute_suggest1':f'Random choosing of elements of an interrogatory (Why/Where/When/)',
                          'tute_suggest2':f'Try applying actions in a different context'}


def halt4_ideas(halt4_IDs_params):
    p = halt4_IDs_params         #-- shallow assign creates a shorter var name for the input dictionary
    original = p['tute_input_var1']     #-- get the original list example
    result = p['tute_output1']
    esc = '\033['; wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'  #-- import colorama
    print(f'\n#0{p['tute_ID']}: Output of {p['tute_name']} {p['tute_actions']} to produce \t{p['tute_output1']}')
    print(f' \t\t\t\t original input was = \t\t{original}\n')
    print(f'{yel_text}FOOD FOR THOUGHT: ({Fore.LIGHTGREEN_EX}Halted at {gotten_line_numb_2back()}{Fore.LIGHTWHITE_EX}) '
          f'What other applications can {p['tute_name']} be used for?{wht_text}')
    print(f'(1): {p['tute_name']} used for {p['tute_actions']} {p['tute_suggest1']} ____ in context of ____')
    print(f'(2): {p['tute_name']} used for {p['tute_actions']} {p['tute_suggest2']}____ in context of ____')
    print(f'(3):', end= " ")
    halt_02 = input(f'Do you have any more application ideas for {red_text}{p['tute_name']}{wht_text} ??__\n'
                    f'type xx to exit\n')
    idea_numb = 1
    now: datetime = datetime.now()  # <-- set this (hinted at) object to current time
    file_base_path4 = 'C:/Users/gideon/Python_Projects_A0/Project_A01_PyBasics_2/.venv/'  # --absolute PATH to THE Venv folder
    Title = f'Test Run for saving numbered ideas of more uses of {p['tute_name']}'
    file_w_path4 = file_base_path4 + f'{now: %Y~m%m~d%d}.txt'   #--file name follows my Obsidian notes

    try:  # -- This "try BLOCK" is used to cope with exceptions like a FileExistsError
        with open(file=file_w_path4, mode="wt") as file:  # --"w" for initial write mode
            file.write(f'{Title}' + f'{now: %Y~m%m~d%d:} for example Obsidian Note \r\n')
            file.write(f'({idea_numb}) {halt_02}\n')  #<--- save idea 01 into the file
    except FileExistsError:
        print(f'That file already exists in the target folder as {file_w_path4}')

# repeat for more ideas in below while loop  which is still part of the func VVVVVVV

    while halt_02 != 'xx':
        idea_numb += 1
        file_base_path4 = 'C:/Users/gideon/Python_Projects_A0/Project_A01_PyBasics_2/.venv/'
        Title = f'Save user input for idea number {idea_numb}'
        file_w_path4 = file_base_path4 + f'{now: %Y~m%m~d%d}.txt'

        try:  # -- This "try BLOCK" is used to cope with exceptions like a FileExistsError
            with open(file=file_w_path4, mode="a") as file:  # --"a" is append
                file.write(f'{Title}' + f'{now: %Y~m%m~d%d:} for Obsidian Note \r\n')
                file.write(f'({idea_numb}): {halt_02}\n')
        except FileExistsError:
            print(f'That file already exists on the deskto as {file_w_path4}')

        halt_02 = input(f'Do you have any more application ideas for use of {red_text}{p['tute_name']}{wht_text} ??__\n'
                        f'type xx to exit\n')

halt4_ideas(halt4_IDs_params)    #-- EXECUTE THE ABOVE FUNC HERE !!!!

print('-' * 20)
print('WELCOME TO LEARN LIST METHODS')
print('-' * 20)
print(f'First tutorial should be number #: 01: CHOICE() unless the skip_diz list says otherwise')


#: 01:
method_name = 'CHOICE()'; method_ID_numb = 1; verb= 'Choosing dice roll outcome'

from random import choice
# face_imgs = ['🎲', '⛹️‍♀️', '🧑🏻‍🤝‍🧑🏻', '👪', '👨‍👨‍👧‍👦', '👪👨‍👦', '👪👪']  #<-- icons were obtained from below URL:
# face_imgs = ['🀣', '🀙', '🀚🀚', '🀛🀛🀛', '🀜🀜🀜 🀜', '🀝🀝🀝 🀝🀝', '🀞🀞🀞 🀞🀞🀞']
#face_imgs = ['🙉', '💛', '❤️❤️', '💚💚💚', '💙💙 💙💙', '💕💕❣️💕💕', '❣️❣️❣️ ❣️❣️❣️']
# ^^^^ https://copychar.cc

def choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a):     #-- last arg is a skip control
    if skip_diz_list_a[method_ID_numb] == 1:
        print(f'method number {method_ID_numb} has been skipped\n')
        return None                               #--skip this tutorial if skip position for tutorial 01 is set to 1
    face_imgs_row1 = ['🤬', '🧐', '🤓🤓', '😲😲', '🤩🤩', '😋   🤪',   '🤠🤠🤠' ]
    face_imgs_row2 = ['☠️', ' ',   '  ',   '😲',    '🤩🤩', '😋😛🤪',   '🤠🤠🤠' ]
    print('\n\n', '#' * 20)

    dice_faces: int = range(1,7)    #-- generates a sequence (not list) of integers 1-6 (default start of range is 0)
    go_again = 'y'
    while go_again == 'y':
        roll_1 = choice(dice_faces)
        roll_2 = choice(dice_faces)
        print(f'\n#:00; example of random choice made with the CHOICE() function')
        print(f' 1st die roll gives you a \t{roll_1}\t{face_imgs_row1[roll_1]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_1]}\n')
        print(f' 2nd die roll gives you a \t{roll_2}\t{face_imgs_row1[roll_2]}')
        print(f' \t\t\t\t\t\t\t\t{face_imgs_row2[roll_2]}\n')
        print(f' The SUM of the two rolls is \t{roll_1 + roll_2} \n')
        go_again = input('Try again? Enter y or other here__')

    halt4_IDs_params: dict = {'tute_ID': '01a', 'tute_name': 'CHOICE()',
                         'tute_actions': 'producing example output as follows: ',
                         'tute_input_var1': example_list_A, 'tute_input_var2': example_list_B,
                         'tute_output1': result_list1, 'tute_output2': result_list2,
                         'tute_suggest1': f'Random choosing of elements of an interrogatory (Why/Where/When/)',
                         'tute_suggest2': f'Try applying actions in a different context'}

    halt4_ideas(halt4_IDs_params)    #--save user ideas for the choice() example

choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a)  #-- EXECUTE the above function here

breakpoint()

#: 02a ANSI COLOR escape codes (Can these be imported from an existing module?)
esc = '\033['
wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'; grn_text = esc + '32m'
blu_text = esc + '34m'; cyan_text = esc + '36m'; magen_text = esc + '35m'


#: 02: SHUFFLE()    = Randomly shuffle a list
from random import shuffle      #-- from Indently's learn RANDOM methods found at:
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


breakpoint()        #-- halted at 2:44 of https://www.youtube.com/watch?v=Ffeb5ibQDP0

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
