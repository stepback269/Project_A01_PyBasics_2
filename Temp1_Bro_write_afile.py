# ver 7/12a/2025 Bro Code tutorial on how to create, write to, append to, txt file (also json and csv)

txt_2b_saved = 'This sample text to be written to a newly created file'
file_w_path = 'Bro_test_file.txt'       #--Can be a relative path or absolute eg to Desktop

with open(file=file_w_path, mode="w") as file:   #--Insted of "w" for write mode, can use "x" to create, "a" to append
    file.write(txt_2b_saved + '\r\n')                      #-- ^^^ above createes an object named 'file' which has write method
with open(file=file_w_path, mode="a") as file:
    file.write(f'This an attempt to append a new line to the {file_w_path} file\n')   #-- need a \r before the \n ??
    file.write(f'This an attempt to append a THIRD line to the {file_w_path} file')   #-- ^^ \r makes a 2 line skip
    print(f'\nThe test file named "{file_w_path}" has been created in the .venv local directory')

txt_2b_saved_new = 'This ANOTHER sample text to be written to a newly created file on the DESKTOP'
            # ^^^ data to be written must be a string, NOT A LIST. must convert a list to strings
            # ^^^ eg. for employee in employees_listing: file.write(employee + '\n')
file_w_path2 = 'C:/Users/gideon/Desktop/Bro_test_file2.txt'  # --absolute PATH to THE Desktop use \\ or /

try:            #-- A "try BLOCK" is used to cope with exceptions like a FileExistsError
    with open(file=file_w_path2, mode="w") as file:  # --Insted of "w" for write mode, can use "x" to create, or ...
        file.write(txt_2b_saved_new + '\r\n')
    with open(file=file_w_path2, mode="x") as file:     #-- Note !!! this a "x" attempt and will cause error
                                                        #-- if we did "w" above, it would OVERWRITE the created file
        file.write(f'This an attempt to append a new line to the {file_w_path2} file on the Desktop\n')
except FileExistsError:
    print(f'That file already exists on the deskto as {file_w_path2}')


# JASON FILES
import json

employee = {
    'name': "Adam Smith",       #-- key:value pairs are separated by COMMA !!!!
    'age': 35,
    'role': "Cook"
}
file_w_path3 = 'C:/Users/gideon/Desktop/Bro_test_file2.json'  # --ext = "json" to Desktop;   use \\ or /
with open(file=file_w_path3, mode="w") as file:   #-- json extension
    json.dump(employee, file, indent=4)           # dump() method converts dictionary to string and writes to file
                                                 # ^^ indent specifies spaces between key:value pairs
    print(f'\nThe test JSON file named "{file_w_path3}" has been created on the Desktop\n'

# TO BE CONTINUED AT (10:42) in https://www.youtube.com/watch?v=1IYrmTTKOoI


#from  Learn strings:
    #: 52:  Date/time tricks (to be continued)
from datetime import datetime

now: datetime = datetime.now()  # <-- set this object (hinted at) to current time
print(f'\n#: 52a: Date now is: {now: %m/%d/%y}')  # <-- format the object for month first (%m), then day, then year
print(f'#: 52b: Date for Obsidian? is: {now: %Y~m%m~%d %A:} Title xxtop1')  # <-- format the output for Obsidian
    # ^^^ note capital Y in above for full year, capital A for full day of week
    # ^^^ also see more codes listed at: https://www.w3schools.com/python/python_datetime.asp

file_base_path4 = 'C:/Users/gideon/Python_Projects_A0/Project_A01_PyBasics_2/.venv' # --absolute PATH to THE Venv folder
Title = 'Test Run 01'
file_w_ path4 = file_base_path4 + f'{now: %Y~m%m~d%d:} {Title} xxtop1'

try:            #-- This "try BLOCK" is used to cope with exceptions like a FileExistsError
    with open(file=file_w_path4, mode="w") as file:  # --Insted of "w" for write mode, can use "x" to create, or ...
        file.write(f'{Title}' + f'{now: %Y~m%m~d%d:} for Obsidain Note \r\n')
        file.write(f'This an attempt to append new lines to the file in the VENV folder\n')
except FileExistsError:
    print(f'That file already exists on the deskto as {file_w_path4}')