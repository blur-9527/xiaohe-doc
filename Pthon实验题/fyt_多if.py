x = int(input())

if x > 1970 and x < 1979:
    print('after 70')
else:
    if x > 1980 and x < 1989:
        print('after 80')
    else:
        if x > 1990 and x < 1999:
            print("after 90")
        else:
            if x > 2000 and x < 2009:
                print("after 00")
            else:
                print("out of range!")


