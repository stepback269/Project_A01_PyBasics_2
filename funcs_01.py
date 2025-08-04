# copy Learn Lists functions _s02 to here? 7/31/2025
# check out the Data Engineer: https://www.youtube.com/@GambillDataEngineering

from . import vars_01 as v  #-- google "python syntax of an import from statement"
from . import mssgs_01 as msg

print(f'(3) The importation of funcs_01 into Main has begun\n')

def ascii_fm_az(fm2: str = 'a-z'):
    lo_hi = fm2.split(sep ='-') #get from and to chars
    lo = lo_hi[0]; lo_ascii = ord(lo)
    hi = lo_hi[1]; hi_ascii = ord(hi)
    print(f'debug check list = {ascii_fm_az()}')  # -- verify that list contains ascii low and hi values
    return [lo_ascii-1, hi_ascii+1]


def ascii_2_str (ask = 65):
    return chr(ask)     #--^^-- use this to iterate and concatenate to varaible name

def test_iterate(lo, hi):   #use this vvv to validate the while loop outputs
    ask_value = ascii_fm_az(lo, hi)[0]
    while ask_value < ascii_fm_az(lo, hi)[1]:
        ask_value += 1
        print(ascii_2_str(ask_value))   #--check that we iterate from a to z
    return
#--^^^-- usage below
# l_01 = ascii_fm_az('a-z')


def get_dict(dict_name = 'clr'): #--returns a named dictionary
    clr: dict = {'b': "BLACK", 'r': "RED", 'g': "GREEN", 'y': "YELLOW", 'u': "BLUE", 'm': "MAGENTA", 'c': "CYAN",
                 'w': "WHITE",
                 'o': "RESET",
                 'B': "LIGHTBLACK_EX", 'R': "LIGHTRED_EX", 'G': "LIGHTGREEN_EX", 'Y': "LIGHTYELLOW_EX",
                 'U': "LIGHTBLUE_EX",
                 'M': "LIGHTMAGENTA_EX", 'C': "LIGHTCYAN_EX", 'W': "LIGHTWHITE_EX",
                 'D': "DIM", 'N': "NORMAL", 'H': "BRIGHT", 'O': "RESET_ALL"}

    clr_: dict = {'W_': 'HWb', 'M_': 'Hmb', 'C_': 'DCb', 'R_': 'HRb',
                  'Y_': 'HYb'}  # -- under score for 3 char expansions
    if dict_name == 'clr':
        f_out = clr
    elif dict_name == 'clr_':
        f_out = clr_
    return f_out  # -- func returns the whole of the dictionary; better idea= use a list or dictionary of dictionaries

def get_dict_expansion(dict_name='clr', alias = 'W_'): #-- Reverse alias is the longer equivalent of input alias string
    #clr: dict = {'b':"BLACK", 'r':"RED", 'g':"GREEN", 'y':"YELLOW", 'u':"BLUE", 'm':"MAGENTA", 'c':"CYAN", 'w':"WHITE",
#                 'o':"RESET",
#                 'B':"LIGHTBLACK_EX", 'R':"LIGHTRED_EX", 'G':"LIGHTGREEN_EX", 'Y':"LIGHTYELLOW_EX", 'U':"LIGHTBLUE_EX",
#                 'M':"LIGHTMAGENTA_EX", 'C':"LIGHTCYAN_EX", 'W':"LIGHTWHITE_EX",
#                 'D':"DIM", 'N':"NORMAL", 'H':"BRIGHT", 'O':"RESET_ALL"}
    #^^ in above, single letter will rep Fore color alone, 2 chars will rep Fore + Back,
    #^^ 3 chars will rep Style + Fore + Back in that order
    clr: dict = v.Ansii()
    clr_: dict = {'W_':'HWb', 'M_': 'Hmb', 'C_':'DCb', 'R_':'HRb', 'Y_':'HYb'}  #-- under score for 3 char expansions
    if dict_name == 'clr':
        f_out = clr[alias]
    elif dict_name == 'clr_':
        f_out = clr_[alias]
    return f_out    #-- func returns expansion from named dictionary

def qif_inStr_OK(inStr, slices_list= [0, 1, 2], allowed= 'yYesnNo'):
    #^^^-- Query if the input string chars are in the allowed_chars_string
    for s in slices_list:
        if inStr[s] in allowed:
            continue
        else:
            print(f'Bad character {inStr[s]} found in supplied input by qif')
            return False
    return True  #--if no misallowed detected, then return as true, meaning allowed

print(f'importation of funcs is about to hit the cj() func')

def cj(chars: str = 'HWb', dict_name = 'clr'):     #-- COLORAMA color commands generator using the clr dictionary
    numb = len(chars)
    allowed_4_Fore = 'brgyumcwoBRGYUMCW'
    allowed_4_Style = 'DNHO'
    dict = get_dict(dict_name) #--using above function for picking one of n dictionaries

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
        #sum: str = getattr(Fore, d[f'{chars[0]}'])  + getattr(Back, d[f'{chars[1]}']) # -- if 2 chars
        return #sum

    elif numb < 4:
        if qif_inStr_OK(chars, [1, 2], allowed_4_Fore):
            pass
        elif qif_inStr_OK(chars, [0], allowed_4_Style):
            pass
        else:
            print(f'Bad character in inputs to cj() found by qif at numb=3')
            return "error in numb=3"
        #sum: str = getattr(Style, d[f'{chars[0]}'])  + getattr(Fore, d[f'{chars[1]}'])  + getattr(Back, d[f'{chars[2]}']) # -- if 3
        return #sum
    else:
        print(f'arguments error in cj function call')
        return None


#--vv-- next are repeated char printouts for creating title boxes (sl= single line of filler char)

def sl3(filler="*", times=90):   #-- separation line w \n above and an extra one below
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print('\n', outp, '\n')
    return None
#sl = sl3('🤪')   #-- https://copychar.cc

def sl2(filler="*", times=90):   #-- bottom separation line w extra \n below
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print(outp, '\n')
    return None

def sl1(box_id ='(__)', filler="*", times=90):   #-- top separation line w \n above
    d = get_dict('clr_')
    outp: str = f"\n{v.W_}{box_id}{filler * (times-4)}"
    print(outp)
    return None

def sl0(filler="*", times=40):   #-- separation line w no CRLF
    d = get_dict('clr_')
    outp: str = v.W_ + filler * times
    print(outp, end='')
    return None

def slm(mssg="MID MESSAGE GOES HERE", filler="**", times=2):   #-- mid box messages
    d = get_dict('clr_')
    outpmid: str = f"{v.M_}{filler}{v.M_}{mssg.center(90-4)}{v.W_}{filler}"
    print(outpmid)
    return None

def outp_list(list_name = msg.intro01_list_a, color = v.C_, indent=10):  ## 137
    for item in list_name:
        print(f'{v.Y_}{spc:<10}{item}')       #-- note colon between spc and indent
    #print(f'{x4}\nend of for loop hit <--a debug notification\n')
    return

def next_frame(display_id = '(00)'): ##154
    intro_01x: str = 'Hit "c" or "SPACE" to continue to next learning frame'
    intro_01y: str = 'Hit "m" to open browser to show more information re this frame'
    outp_01x: str = f'{v.R_}{display_id}: {intro_01x.center(90)}'; print(outp_01x)
    outp_01y: str = f'{v.Y_}{intro_01y.center(90)}'; print(outp_01y)
    wait_01 = True
    while wait_01 == True:
        keyrd = keyboard.read_key()  # -- do just one read opertion per while loop
        if keyrd == "c":  # if the "c" key is pressed
            wait_01 == False;
            response = 'c'
            # print('You Pressed the "c" key --this is a debug notification')
            break
        elif keyrd == "space":  # if the "space" key is pressed
            wait_01 == False;
            response = ' '
            # print(f'\nYou Pressed the "SPACE" key --this is a debug notification')
            break
        elif keyrd == "x":  # if the "x" key is pressed
            wait_01 == False;
            response = 'x'
            # print(f'\nYou Pressed the "x" key --this is a debug notification')
            break
        elif keyrd == "m":  # if the "m" key is pressed
            wait_01 == False;
            response = 'm'
            # print(f'\nYou Pressed the "m" key --this is a debug notification')
            break
        else:
            continue
    return response

def brk(mssg):      ##245
    print(f'\n(X): A debug {v.Y_}brk(mssg) point{v.W_} was hit at {v.G_}line '
          f'{gotten_line_numb_2back()}{v.W_}')
    print(f'(Y): Pdb debugger commands: l=LIST, c=CONTINUE, pp var= PrettyPrint the specific var')
    print(f'(Z): Additional message: {mssg}\n')
    breakpoint()

def get_line_numb_info_demo():      ##266
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    sl3()

    print(f'(a): ',f'current= {frame_info_current}', f'Using the Inspect module we can learn the line number in the caller"s code\n\t',
          f'At current execution time it is \tLine Number {frame_info_prior.lineno}')
    print(f'(b): We can also get the file path + name out of the frame info tuple, it is: \n\t {frame_info_current.filename}')
    print(f'(c): We can also get the name of the function we are inside, at moment we get: \t{frame_info_current.function}')
    return

def gotten_line_numb_1back():  ##279
    frame_current = inspect.currentframe()
    frame_info_prior = inspect.getframeinfo(frame_current.f_back)   #--don't get from execution of this func, get from caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_prior.lineno}'

def gotten_line_numb_2back():   ##287 #-- not finished see stack inspect 2 back !!!!
    frame_current = inspect.currentframe()
    frame_info_2priors_back  = sys._getframe(2)   #--get frame info from caller's caller
    frame_info_current = inspect.getframeinfo(frame_current)
    return f'{frame_info_2priors_back.f_lineno}'    #--Google "python inspect two frames back"

def halt2_study(maybe, feature):    ##303
    if (maybe.lower() == 'n' or maybe.lower() == 'no' or maybe.lower() == 'not'):
        return
    else:
        print(f'The above ^^^^ printouts executed above {v.G_}line {gotten_line_numb_2back()}{v.W_} demonstrate exercise of {v.Y_}{feature}{v.W_} methods')
        wait = input('<Enter> to continue to next demonstartion\n')
    return

def gen_index_templ4(numb_indices):     ##310 #--a func that prints out a template of input number of indices plus one
    skip_diz_template_create = range(numb_indices + 1)
    skip_diz_template = list(skip_diz_template_create)
    print(f'{v.G_}', end = '')
    for i in skip_diz_template: print(format(i ,"02d"), end = '__')  #-- apply the format() function one int at a time
    print(f'{v.W_}')
    print(f'\n{v.M_}Template printed out above for {numb_indices} plus one indices{v.W_}\n')

def gen_preFilled_list4(numb_indices, filler = 0):   ##325 #--func prints out a list of arg1 number of indices plus one
    skip_diz_template_A = [filler] * (numb_indices +1)    #-- and returns the gen'd list filled with the filler
    for i in skip_diz_template_A: print(format(i ,"02d"), end = ' ')  #-- no CRLF
    print(f'\nPre-filled list is printed above for {numb_indices} plus one indices\n')
    return skip_diz_template_A

def halt4_ideas(halt4_IDs_params):      ##354
    p = halt4_IDs_params         #-- shallow assign creates a shorter var name for the input dictionary
    original = p['tute_input_var1']     #-- get the original list example
    result = p['tute_output1']
    esc = '\033['; wht_text = esc + '37m'; yel_text = esc + '33m'; red_text = esc + '31m'  #-- import colorama
    print(f'\n#0{p['tute_ID']}: Output of {p['tute_name']} {p['tute_actions']} to produce \t{p['tute_output1']}')
    print(f' \t\t\t\t original input was = \t\t{original}\n')
    print(f'{yel_text}FOOD FOR THOUGHT: ({v.G_}Halted at {gotten_line_numb_2back()}{v.W_}) '
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


def choice_of_die_outcomes(method_ID_numb, method_name, verb, skip_diz_list_a): ##416    #-- last arg is a skip control
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

# Indently's code for printing out all the methods is as follows
def gen_list_of_methods(): ##499
    i: int =0
    for method in dir(list):    #<-- how do we set the path for directory? Don't have to. We're executing inside Py!
        i += 1
        print(i, method, sep=': ')
        if i > 100:
            break
        else:
            pass
    return

print(f'import of funcs has finished')