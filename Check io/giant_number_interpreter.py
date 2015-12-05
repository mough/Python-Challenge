FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    triple_humper = []
    if len(str(number)) == 1:
        space = int(number) - 1
        print (FIRST_TEN[space])
    if len(str(number)) == 2:
        if number > 19:
            number = str(number)
            space = int(number[0]) - 2
            triple_humper.append(OTHER_TENS[space])
        if int(number) % 10 != 0 and int(number) > 19:
                number = str(number)
                space = int(number[1]) - 1
                triple_humper.append(FIRST_TEN[space])
        if number in range(10, 20):
            space = int(number) - 10
            print (str(SECOND_TEN[space]))

    if len(str(number)) == 3:
        number = str(number)
        space = int(number[0]) - 1
        triple_humper.append(FIRST_TEN[space])
        triple_humper.append("hundred")
        if int(number[1]) == 0 and int(number[2]) != 0:
            space = int(number[2]) - 1
            triple_humper.append(FIRST_TEN[space])
        if int(number[1]) == 1:
            space = int(number[2])
            triple_humper.append(SECOND_TEN[space])
        if int(number[1]) > 1:
            space = int(number[1]) - 2
            triple_humper.append(OTHER_TENS[space])
            if int(number[2]) !=0:
                space = int(number[2]) - 1
                triple_humper.append(FIRST_TEN[space])

    if triple_humper:
        print(' '.join(triple_humper))


checkio(940)
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#
#     assert checkio(4) == 'four', "1st example"
#     assert checkio(133) == 'one hundred thirty three', "2nd example"
#     assert checkio(12) == 'twelve', "3rd example"
#     assert checkio(101) == 'one hundred one', "4th example"
#     assert checkio(212) == 'two hundred twelve', "5th example"
#     assert checkio(40) == 'forty', "6th example"
#     assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"


#This is better:

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
​
​
def checkio(number):
    result = ""
    while(number>0):
        if number>=100:
            result += FIRST_TEN[number//100 - 1] + " " + HUNDRED
            number = number % 100
        elif number>19:
            result += OTHER_TENS[number//10 - 2]
            number = number % 10
        elif number>9:
            result += SECOND_TEN[number%10]
            number = 0
        elif number<10:
            result += FIRST_TEN[number-1]
            number = 0
        if number!=0: result += " "
    return result
