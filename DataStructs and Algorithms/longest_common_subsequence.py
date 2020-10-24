# !usr/bin/env/python3
# Longest Common Subsequence Algorithm
# Dynamic Programming Approach
# Worst Case Run Time Complexity : O(n^2)


def longest_common_subsequence(main_string, comparing_string):

    columns_length = len(main_string)  # Get the length of the first word or base word
    rows_length = len(comparing_string)  # Get the length of the second word or comparing word

    # MAKE A 2D LIST (MATRIX)
    dynamic_table = [[0] * (columns_length + 1) for i in range(rows_length + 1)]

    # rows_length = NUMBER OF ROWS
    # columns_length = NUMBER OF COLUMNS
    
    # FILL THE MATRIX FOLLOWING LCS ALGORITHM.
    for i in range(1, rows_length + 1):
        for j in range(1, columns_length + 1):
            if main_string[j - 1] == comparing_string[i - 1]:
                dynamic_table[i][j] = 1 + dynamic_table[i - 1][j - 1]

            else:
                dynamic_table[i][j] = max(dynamic_table[i - 1][j], dynamic_table[i][j - 1])

    print("MATRIX ACCORDING TO LONGEST COMMON SUBSEQUENCE ALGORITHM: \n ")

    for i in range(rows_length + 1):
        print(dynamic_table[i])

    print()
    print("LENGTH OF LONGEST COMMON SUBSEQUENCE = ", dynamic_table[rows_length][columns_length])
    print()

    i = len(comparing_string)
    j = len(main_string)

    lcs_string = str()

    # BACKTRACKING TO FIND THE LONGEST COMMON SUBSEQUENCE

    temp = True

    while temp is True:
        if dynamic_table[i][j] == 0:
            temp = False
        elif dynamic_table[i][j] == dynamic_table[i][j - 1]:
            j = j - 1

        else:
            lcs_string = main_string[j-1] + lcs_string
            i = i - 1
            j = j - 1

    return lcs_string


def main():
    main_string = "longest"  # main_string === MAIN WORD
    comparing_string = "stone"  # comparing_string === COMPARING WORD

    # CALLING THE FUNCTION
    print("THE LCS WORD IS: ", longest_common_subsequence(main_string, comparing_string))


if __name__ == '__main__':
    print("LONGEST COMMON SUBSEQUENT ALGORITHM CODE IMPLEMENTATION \n")
    main()


