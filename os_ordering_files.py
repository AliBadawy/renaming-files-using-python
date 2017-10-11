import os


# get the file path from the user and change the path

path = input('enter the file path :')

file_name = input('input file name :')

os.chdir(path)

file_counter = 1

number_of_digits=int((len(os.listdir(path))/10+1))#to organize the format using .zfill function

# list all file in the directory and renaming it
for file in os.listdir():

    old_name, file_ext = os.path.splitext(file)

    file_counter_string = str(file_counter).zfill(number_of_digits)

    new_name_format ='{}_{}{}'.format(file_counter_string, file_name, file_ext)

    print(new_name_format)

    os.rename(file, new_name_format)

    file_counter = file_counter + 1
