# STEPS:

# 1. Divide the number by 2.

# 2. Get the integer remainder for the next iteration.

# 3. Get the quotient for the binary digit.

# 4. Repeat the steps until the remainder is equal to 0.


from datetime import datetime

from gpiozero import LED

import time

from gpiozero import LED

# sets variables to represent the different gpio pins
# seconds (blue)

ledsecond1 = LED(19)

ledsecond2 = LED(26)

ledsecond3 = LED(22)

ledsecond4 = LED(27)

ledsecond5 = LED(17)

ledsecond6 = LED(4)

# minutes (yellow)
ledminute1 = LED(24)

ledminute2 = LED(23)

ledminute3 = LED(18)

ledminute4 = LED(5)

ledminute5 = LED(6)

ledminute6 = LED(13)

# hours (red)
ledhour1 = LED(25)

ledhour2 = LED(12)

ledhour3 = LED(16)

ledhour4 = LED(20)


# function that finds binary number

def number2binary(number):

    # creates empty list for numbers digits to be stored
    bin_num = []

    # finds remainder to start while loop with

    # remainder = number % 2

    # finds quotient and new remainder

    quotient = number

    # creates base of 'times keepers' to count how many times something happens

    place = 0

    run = 0

    while run < 6:

        run += 1

        place += 1

        if quotient != 0:

            # finds remainder

            remainder = quotient % 2

            # adds remainder to list

            bin_num.insert(place, int(remainder))

            # finds quotient

            quotient = quotient - remainder

            quotient = quotient / 2



        # fills the spaces in between

        else:

            extra = 0

            bin_num.append(extra)

    # flips list so digits are in the right order

    bin_num.reverse()

    # ends function, returns number

    return bin_num


test = 12

while True:

    # gets time

    now = datetime.now()

    sec = now.second

    mins = now.minute

    hours = now.hour

    if hours > 12:
        hours -= 12

    # finds the time in binary

    binary_seconds = number2binary(sec)

    binary_minutes = number2binary(mins)

    binary_hours = number2binary(hours)

    if binary_seconds[0] == 1:

        ledsecond1.on()


    elif binary_seconds[0] == 0:

        ledsecond1.off()

    if binary_seconds[1] == 1:

        ledsecond2.on()



    elif binary_seconds[1] == 0:

        ledsecond2.off()

    if binary_seconds[2] == 1:

        ledsecond3.on()



    elif binary_seconds[2] == 0:

        ledsecond3.off()

    if binary_seconds[3] == 1:

        ledsecond4.on()



    elif binary_seconds[3] == 0:

        ledsecond4.off()

    if binary_seconds[4] == 1:

        ledsecond5.on()



    elif binary_seconds[4] == 0:

        ledsecond5.off()

    if binary_seconds[5] == 1:

        ledsecond6.on()



    elif binary_seconds[5] == 0:

        ledsecond6.off()

    if binary_minutes[0] == 1:

        ledminute1.on()



    elif binary_minutes[0] == 0:

        ledminute1.off()

    if binary_minutes[1] == 1:

        ledminute2.on()



    elif binary_minutes[1] == 0:

        ledminute2.off()

    if binary_minutes[2] == 1:

        ledminute3.on()



    elif binary_minutes[2] == 0:

        ledminute3.off()

    if binary_minutes[3] == 1:

        ledminute4.on()



    elif binary_minutes[3] == 0:

        ledminute4.off()

    if binary_minutes[4] == 1:

        ledminute5.on()



    elif binary_minutes[4] == 0:

        ledminute5.off()

    if binary_minutes[5] == 1:

        ledminute6.on()



    elif binary_minutes[5] == 0:

        ledminute6.off()

    if binary_hours[2] == 1:

        ledhour4.on()



    elif binary_hours[2] == 0:

        ledhour4.off()

    if binary_hours[3] == 1:

        ledhour3.on()


    elif binary_hours[3] == 0:

        ledhour3.off()

    if binary_hours[4] == 1:

        ledhour2.on()



    elif binary_hours[4] == 0:

        ledhour2.off()

    if binary_hours[5] == 1:

        ledhour1.on()



    elif binary_hours[5] == 0:

        ledhour1.off()
