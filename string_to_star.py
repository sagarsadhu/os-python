stars ={
    15 : '*   *',
    12345: '*****',
    123: '***  ',
    3: '  *  ',
    24:' * * ',
    14: '*  * ',
    2345: ' ****',
    1: '*    ',
    1345: '* ***',
    1234: '**** ',
    13: '* *  ',
    135: '* * *',
    125: '**  *',
    145: '*  **',
    234: ' *** ',
    5: '    *',
    2: ' *   ',
    4: '   * ',
    1245: '** **'
}

letters = {
    'A': [3,24,12345,15,15],
    'B': [1234, 15, 1234, 15, 1234],
    'C' : [2345, 1, 1,1, 2345],
    'D' : [1234, 15, 15, 15, 1234],
    'E': [12345, 1, 12345, 1, 12345],
    'F': [12345, 1, 12345, 1, 1],
    'G': [12345, 1, 1345, 15, 12345],
    'H': [15,15, 12345, 15, 15],
    'I': [12345, 3,3,3,12345],
    'J': [12345, 3, 3, 13, 2],
    'K': [15, 14, 123, 14, 15],
    'L': [1,1,1,1,12345],
    'M': [15, 1245, 135, 15, 15],
    'N': [15, 125, 135, 145, 15],
    'O': [234, 15, 15, 15, 234],
    'P': [1234, 15, 1234, 1, 1],
    'Q': [234, 15, 135, 145, 2345],
    'R': [1234, 15, 1234, 14, 15],
    'S': [234, 1, 234, 5, 234],
    'T': [12345, 3, 3, 3, 3],
    'U': [15,15, 15, 15, 234],
    'V': [15, 15, 15, 24, 3],
    'W': [15, 15, 135, 1245, 15],
    'X': [15, 24, 3, 24, 15],
    'Y': [15, 24, 3, 3, 3],
    'Z': [12345, 4, 3, 2, 12345]
}

input_str = input('Please enter a string that needs conversion : ')
print('\n')
print('\n')
words = input_str.split()

for word in words:
    first_line = '  '
    second_line = '  '
    third_line = '  '
    fourth_line = '  '
    fifth_line = '  '

    for letter in word.upper():
        first_line += stars[letters[letter][0]] + ' '
        second_line += stars[letters[letter][1]] + ' '
        third_line += stars[letters[letter][2]] + ' '
        fourth_line += stars[letters[letter][3]] + ' '
        fifth_line += stars[letters[letter][4]] + ' '

    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)

    print('\n')
    print('\n')

    