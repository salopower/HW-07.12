def read_last(lines, file):
    if lines > 0:
        with open(file, 'r') as t:
            file_lines = t.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('The number of rows can only be a positive integer\n')


file_name = input('Enter the file name:\n')
lines_numbers = int(input('Enter the lines numbers:\n'))
print(read_last(lines_numbers, file_name))
