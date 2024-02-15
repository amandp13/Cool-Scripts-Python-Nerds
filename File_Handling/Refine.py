"""
i/p: pass file with list of words 
o/p: list of words which are valid
"""

import os


def check(line):
    """Checks for Validity letter by letter"""

    for (
        letter
    ) in (
        line
    ):  # this loop checks every word and if that word are in uppercase then return false

        if not "z" >= letter >= "a":

            return False

    return True


input_file = input("Enter the path to the input file")  # get input path from the user
output_file = input(
    "Enter the path to the output file"
)  # get output path from the user

if not os.path.exists(input_file):  # handling exception if the input file does not exit
    print("input file not found")
    exit()

if not os.path.exists(
    output_file
):  # handling exception if the output file does not exit
    print("output file not found")
    exit()


with open(input_file) as file:

    data = file.readlines()
    with open(output_file, "w") as wr:

        for line in data:
            line = line.strip()

            if len(line) > 1 and check(line):

                wr.write(line + "\n")


# eof
