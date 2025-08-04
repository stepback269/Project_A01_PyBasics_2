# Date: 8/03/2025
# This module will hold the message lines for the Learn_Lists_and_Modules main
# This module will be imported as "msg"
'''
... more to follow
'''
from . import vars_01 as v #-- we are NOT importing the primary vars because main already loaded them !!!
#from . import funcs_01 as fn

#v = vars_01() #-- because above ^^^ imports are blocked
#fn = funcs_01()

print(f'(1) The importation of mssgs_01 into Main has begun\n')


# Title Box ('00')
intro_00 = f'WELCOME TO LEARNING AND REVIEWING PYTHON LISTS'
intro_00a = '(00)  <-- This is the current lesson frame number'
intro_00aa = 'The frame number (display_id) will be incrementing as we advance thru lessons'
intro_00ab = 'At the moment this is merely an introductory first frame'
intro_00b = f'We will be exercising various {v.x3}Python list methods{v.x2} here'
intro_00c = 'Additionally, many other Python features are brought to light at the same time including but not limited to:'
intro_00c0 = f'(a) Using the {v.x3}COLORAMA{v.x2} module to print different colors on the console'
intro_00c1 = f'(b) Using {v.y_}string alignment{v.z_} (e.g., Str.center, spc:<10, more)'
intro_00c2 = f'(c) Using {v.y_}functions to repeatedly generate{v.z_} indented lists like this one'
intro_00c3 = f'(d) Using the {v.y_}Webster module{v.z_} to open additional info in the web browser'
intro_00c4 = f'(e) Using the {v.y_}Keyboard module{v.z_} to detect single keystroke inputs'
intro_00c5 = f'(f) Linking to {v.y_}my own "Back of Stage" blog{v.z_} to provide more on-topic information'
intro_00c6 = f'(g) Opening a {v.x_}"More to Explore"{v.z_} informational web page ---> {v.y_}Look in your browser -->{v.z_}'
intro_00c_list = [intro_00c0, intro_00c1, intro_00c2, intro_00c3, intro_00c4, intro_00c5, intro_00c6 ]

#--^^--usages:
#outp_01a: str = f'{x}{intro_00a.center(90)}'; print(outp_01a)   #-- print exercise frame (00)
#print(f'{intro_00aa}'); print(f'{intro_00ab}')
#outp_01b: str = f'{x}{intro_00b.center(90)}'; print(outp_01b)
#outp: str = f"\n{z}{intro_00c}"; print(outp)        #-- z is alias for cj('Dcb') #--reuse "outp" variable

intro_01d = f'For this first frame (00) we additionally {v.y_}link to Back Stage web page explaining "aliases" -->{v.z_}'

# Frame ender options
intro_01x: str = 'Hit "c" or "SPACE" to continue to next learning frame'
intro_01y: str = 'Hit "m" to open browser to show more information re this frame'

#--^^^--usages:
#outp_01x: str = f'{cj('Hrb')}{display_id}: {intro_01x.center(90)}'; print(outp_01x)
#outp_01y: str = f'{cj('Hyb')}{intro_01y.center(90)}'; print(outp_01y)

# Title Box ('01')
intro_01 = f'This will be a further exercise showing COLORAMA foreground and background colors'
#--^^^--usages:
# display_id = '(01)'     #-- print mat number 2
# sl1(display_id)
# slm(mssg_02)     #-- middle line uses this text message (don't insert color inside mid mssg !!)
# sl2()

# Colors reminder {w}=White/b, {x}=Cyan/b, {z}=dim cyan, {y}=Yellow, {cj('HBw')}= Hight Black/w
print(f'\n{v.x_}TEST of color generator function, cj[abc]\'s Style, Fore, Back permutations\n')

intro_01a = f'{v.x_}bW = \t{v.Ansii['BLACK']}{v.Ansi_['WHITE']}This should be plain-Black on lite-white backround {v.W_}and then back to white/b'
intro_01b = f'{v.x_}HbY = \t{v.Ansii['BLACK']}{v.Ansi_['YELLOW']}This should be brite Black on lite yellow backround {v.x_}and then back to normal cyan'
intro_01c = f'{v.x_}HcW = \t{v.Ansii['CYAN']}{v.Ansi_['WHITE']}This should be brite Cyan on brite white backround {v.x_}and then back to normal'
intro_01d = f'{v.x_}DcW = \t{v.Ansii['CYAN']}{v.Ansi_['WHITE']}This should be dim Cyan on brite white backround {v.x_}and then back to normal'
intro_01e = f'{v.x_}Hbu = \tThis should be brite Black on brite blue backround {v.x_}and then back to normal'
intro_01f = f'{v.x_}Uw = \tThis should be brite blue on dim white backround {v.x_}and then back to normal'
intro_01g = f'{v.x_}HbY = \t{v.symbols_01}{v.symbols_02}{v.symbols_03}{v.x_}and then back to normal cyan'
#--^^-- symbols_01 = "▃" * 20; symbols_02 = "▔" * 20; symbols_03 = "▚" * 20;
intro_01h = f'\n{v.x_}See the adjacent browser for more info from G4G re Colorama {v.y_}and TermColor -->{v.x_}'
intro_01i = f'{v.x_}Also see the adjacent browser for {v.y_}Symbol picker website -->{v.x_}'
intro_01j = f'\nNote that not all fore and background combinations work well with text chars\n'
intro01_list_a = []
intro01_list_a = []
#--^^^-- Add function to step thru lists and print them out e.g. print intro_{display_id){next_abc}

# ... to be continued
print(f'(2x) The importation of mssgs_01 into Main has finished\n')