##### Task #####
# You are given a string. Split the string n a " " (space) delimiter and join using a - hypen.

##### Input Format #####
# The first line contains a string consisting of space separated words

##### Output Format #####
# Print the formated string as explained above


if __name__ == '__main__':
    string = input()
    string = string.split(' ')
    string = '-'.join(string)
    print(string)

##### Sample Input #####
# The first line contains a string consisting of space sparated words.
##### Expected Output #####
# Print the formatted string as explained above

