'''
Last modified 6/26a/2025
Purpose: Reviewing my earlier learning re Python string methods --adding new material
See also: W3 School string methods on the web
There are 68 notes in here rather than just 47 because it includes string "tricks"
'''

# Copied from Idently 4/16/2025 and modified  https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s
# ran below ## statements and then blocked them from 2nd time run
# the blocked method vvvv (below) generates a listing of all built-in Python string methods

## def get_string_methods_list():
##    i: int = 0
##    for found_method in dir(str):
##        if '__' not in found_method:        #<-- leave out the Dunder methods
##            i += 1
##            print('#', i, found_method, sep= ': ')  #<-- a colon plus space is inserted as separator for each item
## Above function ^^^ prints out comments that enumerate the found string methods
## Below vvvv we called and thus executed the function

## get_string_methods_list()

sample_1 = 'the quick Brown fox Beat the slow turtle.'  #<-- Here is some sample text to use in trying out the methods
sample_2 = 'Every Good Boy Deserves Favor'

#C:\Users\gideon\.venv\Scripts\python.exe C:\Users\gideon\PycharmProjects\PythonProject\GG_Project-2_Strings_and-Files\Learn_String_Methods.py

## def create_example(method_name, sample):  #can't get this function to work --gave up
## Hindsight of 6/18/2025 --> the exec function must be a pure string containing executable Py code
##     run_it = """
##     do_it= sample + '.' + method_name +'()'  #<-- creates a string object followed by the target method call
##     print(do_it)
##     exec(f'cop= {do_it}')  #returns None but also supposedly creates the cop variable as result of do_it
##     """
##     exec(run_it)
##     print(cop)

## create_example('capitalize', 'sample_1')
n=0     #<-- rather than me typing each enumeration of the subject string method, I have Py calculate it
        #vvv 6/18 hindsight: use Ctrl + Shft + U to switch method name to all caps in comment

#: 1: CAPITALIZE  --> upper cases 1st letter of the string, lower cases the rest
n+=1; print(n, ':', sample_1.capitalize())   # outputs: The quick brown fox beat the slow turtle.
                    #^^^^^^^ Note that the method follows the string object being operated on

#: 2: CASEFOLD      --> lower cases the string so it can be compared with other case folded strings
n+=1; print(n, ':', sample_1.casefold())   # outputs: the quick brown fox beat the slow turtle.

#: 3: CENTER        --> pads with n fill chars and centers sample_1 in whole
n+=1; print(n, ':', sample_1.center(60, '#')) # outputs: #########the quick Brown fox beat the slow turtle.##########

#: 4: COUNT       --> counts the number of occurrences of arg in the sample_1
n+=1; print(n, ':', sample_1.count('t'))  # outputs: 5 (There are 5 T's in 'the quick Brown fox Beat the slow turtle.'

#: 5: ENCODE       --> converts sample_1 into specified alternate coding, for example UTF-8
#       ^^^^ not executed here
n+=1

#: 6: ENDSWITH      -->returns Boolean to test of whether sample_1 ends with ANY letters in supplied TUPLE
n+=1; print(n, ':', sample_1.endswith(('.', '?', '!')))  #note 3 )'s at end outputs True because ends with period

#: 7: EXPANDTABS    --> locates tabs (\t) inside sample_3 and makes them bigger
sample_3= 'hello\tthere\tmy\tpretty'    #<-- need this additional test string for below run vvvvvv
n+=1; print(n, ':', sample_3.expandtabs(10))  #outputs: hello     there     my        pretty

#: 8: FIND      --> locates arg substring in sample_1 and gives its starting index (index=0 at first spot)
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.find('\t'))  #outputs: 5 (1st place is index=0)
print(sample_3[found:])             #<-- using slice method tp print from found position to end
                                    # reminder: 'https://www.youtube.com/watch?v=bnSYeYFRCaA&t=108s'
#: 9: FORMAT    -->   inserts substitute substrings into main string
n+=1; sample_4 = 'The {subject} is {action}ing {adverb} {object}'   #<-- this is NOT an f-string
print(n, ':', sample_4.format(subject= 'elephant', action= 'work', adverb= 'very', object= 'hard' ))
sample_5 = 'The {} is {}ing {} {}'
print(n, ':', sample_5.format('elephant', 'work', 'very', 'hard' ))     #<-- same result using blank curly pairs
                        # both prints output: The elephant is working very hard

#: 10: FORMAT_MAP   --> uses a specified dictionary object and replaces in-string keys with their dictionary values
n+=1; map: dict = {'subject' : 'Elephant', 'action' : 'Work',  'adverb' : 'Very',  'object' : 'Well'}
print(n, ':', sample_4.format_map(map))   #<-- Note that map is a dictionary and keys are strings, as are their values

#: 11: INDEX ---> similar to find except that it returns an error if substring not found as opposed to returning a -1 (False)
n+=1; found = sample_3.find('\t')
print(n, ':', sample_3.index('\t'))  #outputs: 5 as position of escape-Tab (1st place is index=0)
# print(n, ':', sample_3.index('\n'))  #outputs an error message in output window

#: 12: ISALNUM      --> Is the sample string purely Alpha-Numeric ? (Only A-Z, a-z, 0-9)
sample_6 = 'abcdefg123'
sample_7 = 'abcdefgH'
n+=1; print(n, ':', sample_5.isalnum())
print(n, ':', sample_6.isalnum())

#: 13: ISALPHA      --> Is the sample string purely Alpha (not even numbers allowed)
n+=1; print(n, ':', sample_6.isalpha())
print(n, ':', sample_7.isalpha())

#: 14: ISASCII      --> Is the sample string purely ASCII coded?
n+=1; print(n, ':', sample_6.isascii())

#: 15: ISDECIMAL    --> Is the sample string purely 0-9?

#: 16: ISDIGIT    --> Is the sample string purely numbers but in any form including funny fonts

#: 17: ISIDENTIFIER    --> Can the sample string operate as valid Python variable name?

#: 18: ISLOWER      --> Is the sample string purely lower case a-z?

#: 19: ISNUMERIC    ---> stick with is decimal

#: 20: ISPRINTABLE  --> Is the sample string usable in a one-line print() statement?

#: 21: ISSPACE      --> Only spaces

#: 22: ISTITLE      --> 1st leter of each word is capital

#: 23: ISUPPER

#: 24: JOIN      -->  join the string arguments
joiner: str = '---'   #this will be inserted between the to-be-joined args, here it is 3 dashes
n+=10; print(n, ':', joiner.join([sample_1, sample_2, sample_3]))

#: 25: LJUST    ---> pads to the right with filler
n+=1; print(n, ':', sample_6.ljust(30, '*'))  #outputs: abcdefg123********************

#: 26: LOWER    ---> converts all to LOWER case, no arg

#: 27: LSTRIP   --->  strip argument off of left side of sample
n+=2; print(n, ':', sample_6.lstrip('abc')) #outputs: defg123

#: 28: MAKETRANS --> converts text into a translation table for use with translate() function
table = sample_3.maketrans('ht', '-=') #--> plan to replace EACH h and t with RESPECTIVE chars of 2nd arg of SAME length
n+=1; print(n, ':', table)               #---> creates an ascii coded translation dictionary -can use emoji's
print(sample_3.translate(table))        #---> Translate according to pre-made Table

#: 29: PARTITION  #--> specify a partitioning substring that breaks sample into 3 LIST items with partitioner in middle
n+=1; print(n, ':', sample_6.partition('fg'))   #outputs: ('abcde', 'fg', '123')

#: 30: REMOVEPREFIX #--> remove specified opening substring
n+=1; print(n, ':', sample_5.removeprefix('Th'))

#: 31: REMOVESUFFIX     #---> same as prefix but from other end of sample
n+=1; print(n, ':', sample_5.removesuffix('{}'))

#: 32: REPLACE  #--> remplace specified substring (1st arg) with 2nd arg, optional 3rd arg is number of times to do
n+=1; print(n, ':', sample_5.replace('{}', 'BRACKS'))

#: 33: RFIND  #--> Starting from the RIGHT, find position in sample of arg text, position is counted from left !!!
n+=1; print(n, ':', sample_1.rfind('slow')) #outputs: 29 which is index of 's'  (rindex does same but returns error)

#: 34: RINDEX
n+=1; print(n, ':', sample_1.rindex('slow'))    #--> Breaks as an error if not found

#: 35: RJUST    #--> Justifies to the RIGHT, pads front with fill character
n+=1; print(n, ':', sample_1.rjust(60, '_'))

#: 36: RPARTITION    #--> same as 3-part partition but looks for middle part from the RIGHT side of sample

#: 37: RSPLIT    #--> starting from RIGHT, split into a LIST of substrings using the provided splitter upto max times
n+=2; print(n, ':', sample_1.rsplit(' ', maxsplit=4)) #outputs: ['the quick Brown fox', 'Beat', 'the', 'slow', 'turtle.']

#: 38: RSTRIP   #--> starting from RIGHT, remove just the first instance of the specified substring
n+=1; print(n, ':', sample_1.rstrip('turtle.')) #<--- requires the whole ending substring?

#: 39: SPLIT  #--> starting from LEFT, split into LIST of substrings using the provided splitter upto max times
n+=1; print(n, ':', sample_1.split(' ', maxsplit=3))

#: 40: SPLITLINES  #--> searches for \n and uses it as terminator for creating a list
sample_8 = 'Please be sure to like\nand SUBSCRIBE\nAs well as wathcing\n'
n+=1; print(n, ':', sample_8.splitlines(keepends= False)) #<-- if True, the \n terminators are included in LIST

#: 41: STARTSWITH  #--> Boolean result= True/False if sample starts with specified substring
n+=1; print(n, ':', sample_8.startswith('Please'))
print(n, ':', sample_8.startswith('please'))        #<-- and is case sensitive

#: 42: STRIP    #--> remove the specified substring
n+=1; print(n, ':', sample_8.strip('watching'))       #<-- can be in mid of sample string? NOT WORKING HERE !!!!

#: 43: SWAPCASE    #--> Changes UPPERS to lowers and vise versa, in other words, TOGGLES on per char basis

#: 44: TITLE    #--> forces 1st alpha letter of each word to be capped
n+=2; print(n, ':', sample_4.title())

#: 45: TRANSLATE    #--> See maketable above

#: 46: UPPER

#: 47: ZFILL    #--> Zero fill: prefixes the sample with n 0's (for what use, don't know)

# Process finished with exit code 0

##########  EXTRA SECTION: USEFUL f-string METHODS #####
# from https://www.youtube.com/watch?v=EoNOWVYKyo0

#: 50: Inserting commas or UNDERSCORES into large INTEGERS
biggie: int = 1000000000    #<-- lots of zeroes
n=50; print(n, ':', f'{biggie:,}')  #inserts commas for every 3 zeroes
print(n, ':', f'{biggie:_}')        #inserts underscores for every 3 zeroes, NO OTHER CHARs allowed

#: 51: Use f-string to RIGHT-ALIGN strings
short = 'Hi You'; short_2 = "Yes it's You"
n+=1; print(n, ':', f'{short:>20}')     #<--- Total string length is 20 chars
print(n, ':', f'{short_2:>20}')
print(n, ':', f'{short_2:<19}', '|')     #<--- left-aligned plus '|" as end indicator
print(n, ':', f'{short_2:^19}', '|')     #<--- CENTER-aligned plus '|" as end indicator
print(n, ':', f'{short_2:_^19}', '|')    #<--- filler char inserted after colon :

#: 52:  Date/time tricks (to be continued)
from datetime import datetime
now: datetime = datetime.now()          #<-- set this object (hinted at) to current time
print(f'\n#: 52a: Date now is: {now: %m/%d/%y}')        #<-- format the object for month first (%m), then day, then year
print(f'#: 52b: Date for Obsidian? is: {now: %Y~m%m~%d %A:} Title xxtop1')        #<-- format the output for Obsidian
# ^^^ note capital Y in above for full year, capital A for full day of week
# ^^^ also see more codes listed at: https://www.w3schools.com/python/python_datetime.asp

#: 53:  ROUNDING
long_num: float = 12345.67890123
print(f'\n#: 53a: long number originally is {long_num}')
print(f'   But when rounded is {long_num:.2f}')
print(f'   When also comma~d b4 the dot is {long_num:,.3f}  <--note rounding at 3rd decimal place')

#: 54:  Debugging with f' strings  (see as alternative the icecream module)
a = 5; b = 6; c = 2
print(f'\n#: 54: {a**c + b**c = } <--equal sign inside curly brackets causes repeat of formula')
print(f'   a = 5; b = 6; c = 2    ^^^ use above for debugging')
# ^^^ note also the space after the equal sign

#: 55:  Improve readability of Big Numbers
biggie = 1_620_000_000
print(f'\n#: 55: Original biggie is {biggie}')
print(f'   In e format  biggie is {biggie:e}')
print(f'   In dot 2 plus e format  biggie is {biggie:.2e}')

# ^^^ above is more f strings at https://www.youtube.com/watch?v=aa39jL7wdJs
breakpoint()



# (new) Indently ALL f-string tricks from https://www.youtube.com/watch?v=9saytqA0J9A

#: 60 The basic f-string usage = avoid plus signs and open/close quotes
n=60; print('\n\n\nBasic combining of strings calls for "str1" + "str2"')
my_name: str = 'Gideon'; my_age: int = 73 #<-- next want to combine string plus integer
print('NAME =' + 'Gideon ' + 'AGE = ' + str(my_age))
print(n, ':', 'Above was printed as concatenation of only strings')
print(f'NAME =  {my_name}   AGE = {my_age}')
print(n, ':', 'Above was printed as an f-string using { } for evaluating different types of objects')
n+=1; print('\n', n, ':', f" 5 + 6 = {5+6},  5*6 = {5*6}, 5^3 = {5**3}")
print('Above was printed with  an f-string using { } for evaluating different math expressions')

#: 62 : Auto complete of literal plus value for DEBUGGING runs
debug_var = 125
n+=1; print('\n', n, ':', f"{debug_var = }")
print('Above was printed with  an f-string using {var=} for auto insertion of var name')

#: 63 :  Auto complete even works for Boolean function tests !!!
n+=1; print('\n', n, ':', f"{isinstance(debug_var, int) = }")
print('Above was printed with an f-string using { } for evaluating a Boolean inquiry and auto competing the result')

#: 64 :  Rounding high precision floats and converting value to percentage
multi_digit: float = 8765.4167;  compare_percent: float = 0.5678
n+=1; print('\n', n, ':', f"{multi_digit:.2f}", f"{compare_percent:.2%}")
print('Above was printed with an f-string using { } for rounding to 2 decimal places (2f) and shifting dec point 2 places')
biggie2: float = 1_234_567.8901    #<-- lots of digits (see biggie int above as reminder)
print('\n', n, ':', f"{biggie2:,.1f}")      #<-- don't forget period b4 1f !!
print(' ^^^^ Above uses f-string { } for rounding to 1 decimal place AND insering commas every 3 zeroes')

#: 65 :  Dealing with DATE-TIME issues
from datetime import datetime       #<-- this is a class (a type) that has its own methods
time_now: datetime = datetime.now()  #<-- declares var time_now as being of type, datetime
n+=1; print('\n', n, ':', f"{time_now:%X}")
print(' ^^^^ Above uses f-string { } for limit to just the short form date  (% X )') #<-- can be lower case X too
print('\n', n, ':', f"{time_now:%C}")
print(' ^^^^ Above uses f-string { } for long form date + military time  (% C )')
print('\n', n, ':', f"{time_now:%H:%M:%S}")
print(' ^^^^ Above uses f-string { } for long form time  (% H : M : S )') #<-- note colon (:) separators
print('\n', n, ':', f"{time_now:%H:%M}")
print('\n', n, ':', f"{time_now:%H military :%M time H:M}")
print('\n', '\033[96mThis should be colored blue due to the 033 escape sequence')
print('\033[91m This should be colored red  due to the 033 escape sequence')
print('\033[92m Check out Python Tutorial: Escape Sequence Explained at https://www.youtube.com/watch?v=hExrjJ_KR48')
print('\033[93m Check out Caleb Curry\'s Python Tutorial: at ..')
print('\t https://www.youtube.com/watch?v=9miLWHISMqc&list=PL_c9BZzLwBRKK8ndQBBKolg7IxrC5T6Ws&index=20')

#: 66 :  FRench Raw data specifier for f-strings (at 9:40 / 1942 in Indently video)
print('\n \033[95m This should be colored what? due to the 033 escape sequence')
print('\033[97m This should be colored what? due to the 033 [97m escape sequence, Answer: back to WHITE !!')

raw_text: str = r'Back slashes are \n treated as \b literals \t when the r-string attribute is used'
n+=1; print('\n', n, ':', raw_text)
print('\t On other hand, \t tabs and backups \bare not ignored \" if not \"raw\" ')

sample_11: str = 'My_Name'
sample_path: str = fr'\User\{sample_11}\Documents\PythonTutorials'  #<-- note fr-string !!!!!!!!! the 'f' allows {samp}
print('\nThe path to target folder is:', sample_path) #<-- the French string (fr) sample_path includes raw back slashes

#: 67:  Nested f-strings
n+=1; print('\n', n, ':', f'{5+5=}    {10 + 10=}    {10*10=}      {10**10=:,}') #<-- note also use of biggie colon-comma
print(f'{5+5=}    {10 + 10=} {r'User\Folder\Docs'}  <-- this is a nested r-string')

#: 68:  CUSTOM F-STRINGS !!!!!!!!!!
class Special_text:
    def __init__(self, text : str) -> None:
        self.text = text

    def __format__(self, format_spec: str) -> str:
        match format_spec:      #<--- test for cases of where format_spec is one thing or another
            case 'up':
                return self.text.upper()
            case 'low':
                return self.text.lower()
            case 'len':
                return str(len(self.text))      #<-- this will return the length count as a string
            case _:             #<-- all other cases default to next
                raise ValueError(f'Supplied format specifier {format_spec} is not valid')

my_sample_text_1: Special_text = Special_text('this started off as all lower case but of type: special_text')
my_sample_text_2: Special_text = Special_text('THIS STARTED OFF AS ALL UPPER CASE BUT OF TYPE: SPECIAL_TEXT')
n+=1; print('\n', n, ':', f'{my_sample_text_1:up}')
print('\t', f'{my_sample_text_2:low}')
print('\t', f'{my_sample_text_2:len} <--this is the length count')