# Check if the year is leap or not
#Below is the logic behin code.
"""
is it cleanly divisible by 4?
if yes --> is it cleanly divisible by 100?
           if yes --> is it cleanly divisible by 400?
                      if yes --> Leap
                      if not --> Not Leap
           if not --> Leap
if not --> Not Leap
"""

year = int(input("Enter year: "))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap Year!")
        else:
            print("Not Leap Year!")
    else:
        print("Leap Year!")
else:
    print("Not Leap Year!")
