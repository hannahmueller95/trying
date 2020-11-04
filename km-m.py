user_name = input('Put name here: ');
print('Hello ' + user_name + '!')

def repeating():

    kilometer = int(input('Enter kilometers (whole numbers) to convert in miles: '))
    miles = kilometer * 0.621371
    print('{0} kilometers are {1} miles'.format(kilometer, miles))

while True:
    repeating()
    s = input('Do you want to convert again? Please anwser with yes or no: ')
    if s in "Nono":
        break
