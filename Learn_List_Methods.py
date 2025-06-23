# Date: 6/23a/2025  version 001
# This Python file will be similar to the earlier Learn_String_Methods and also base don Indently's YouTube video
# located at: https://www.youtube.com/watch?v=0yySumZTxJ0&t=1s
# There are only 11 list methods according to Indently

example_list_01: list[str] = ['Adam', 'Bob', 'Calvin', 'Dario']  #<-- a type hinted list of strings, people names

#   APPEND()   = adds a new item to the specified list
n=1; method_name = 'append()'; example_list_01.append('Ernie')
print(f'{n}  {method_name}  output= {example_list_01} \n\n')

#   CLEAR()     = clears the specified list (empties it)
n+=1; method_name = 'clear()'; example_list_01.clear()
print(f'{n}  {method_name}  output= {example_list_01} \n\n')

#   COPY()      = creates a separate copy of the acted-on list if just pure strings
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
