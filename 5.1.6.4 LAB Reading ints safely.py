def readint(prompt, min, max):
    cycle=True
    while cycle:
        try:
            num=int(input(prompt))
            if(num > min and num < max):
                cycle=False
                return num
            else: 
                assert num < min and num > max
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (",min,"..",max,")")
        except KeyboardInterrupt:
            print("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)