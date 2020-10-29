one  = [ [' ',' ','#'],[' ',' ','#'],[' ',' ','#'],[' ',' ','#'],[' ',' ','#']]
two  = [ ['#','#','#'],[' ',' ','#'],['#','#','#'],['#',' ',' '],['#','#','#']]
three= [ ['#','#','#'],[' ',' ','#'],['#','#','#'],[' ',' ','#'],['#','#','#']]
four = [ ['#',' ','#'],['#',' ','#'],['#','#','#'],[' ',' ','#'],[' ',' ','#']]
five = [ ['#','#','#'],['#',' ',' '],['#','#','#'],[' ',' ','#'],['#','#','#']]
six  = [ ['#','#','#'],['#',' ',' '],['#','#','#'],['#',' ','#'],['#','#','#']]
seven= [ ['#','#','#'],[' ',' ','#'],[' ',' ','#'],[' ',' ','#'],[' ',' ','#']]
eight= [ ['#','#','#'],['#',' ','#'],['#','#','#'],['#',' ','#'],['#','#','#']]
nine = [ ['#','#','#'],['#',' ','#'],['#','#','#'],[' ',' ','#'],['#','#','#']]
zero = [ ['#','#','#'],['#',' ','#'],['#',' ','#'],['#',' ','#'],['#','#','#']]

def ledDisplay(numberList):
    for y in range(5):
        for x in range(len(numberList)):
            for i in range(3):
                if numberList[x] == '0': print(zero[y][i]   ,end=' ')
                if numberList[x] == '1': print(one[y][i]    ,end=' ')
                if numberList[x] == '2': print(two[y][i]    ,end=' ')
                if numberList[x] == '3': print(three[y][i]  ,end=' ')
                if numberList[x] == '4': print(four[y][i]   ,end=' ')
                if numberList[x] == '5': print(five[y][i]   ,end=' ')
                if numberList[x] == '6': print(six[y][i]    ,end=' ')
                if numberList[x] == '7': print(seven[y][i]  ,end=' ')
                if numberList[x] == '8': print(eight[y][i]  ,end=' ')
                if numberList[x] == '9': print(nine[y][i]   ,end=' ')
            print('  ',end='')
        print("")

# Main
number=input("Number to display:")
while number.isdigit() == False:
    number=input("Only numbers:")
numberList=list(number)
ledDisplay(numberList)