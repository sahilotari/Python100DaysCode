year = int(input("Enter year you want to check? "))

if year % 4 == 0:
    if year % 100 !=0:
        print(f"{year} is not a Leap year..")
    else:
        if year %400==0:
            print(f"{year} is a Leap year..")
        else:
            print(f"{year} is not a Leap year..")
    
else:
    print(f"{year} is not a Leap year..")
