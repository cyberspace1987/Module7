"""
Program: file_input_output_file.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/11/2020
In this assignment you will tie together the seemingly unrelated tuple
and arbitrary argument list to perform file input and output.
"""


def write_to_file(tuple_pupil):
    """
    Use reST style.
    :param parameter_1: converting tuple_pupil str to a new character
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    file = open("student_info.txt",'a')
    file.write(str(tuple_pupil)+'\n')
    file.close()


def get_student_info(name):
    """
    Use reST style.
    :param parameter_1: will take input from user until user enter's a new line.
    :param parameter_2:
    :returns: makes name and scores list
    :raises keyError: raises an exception
    """
    input("Press any key to start and end")
    print("Enter test scores",name)
    scores = []
    while True:
        score = input()
        if score == "":
            break
            scores.append(float(score))


    tuble_pupil = (name, scores)
    write_to_file(tuble_pupil)


def read_from_file():
    """
    Use reST style.
    :param parameter_1: reads all lines
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises keyError: raises an exception
    """
    file = open("student_info.txt",'r')
    lines = file.readlines()
    for line in lines:
            print(line)

def main():
    open("student_info.txt",'w').close()
    names = ["Janeway","B'Elanna","Tom", "Harry"]
    for i in range(0,len(names)):
        get_student_info(names[i])
        read_from_file()

if __name__ == '__main__':
    main()
