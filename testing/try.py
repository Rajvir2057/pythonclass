
input("Enter Your Name :) :  ")
print("....................................................")
print("WELCOME TO RAJ.ZODIAC SIGNS.. HOPE YOU ENJOY.")
print("....................................................")

class Zodiac:
    def __init__(self,day,month):
        self.day= day
        self.month= month


class Raj_zodiac(Zodiac):

    day= int(input("Please Enter Your Birthday day only: "))

    print("Choose Your Month.")
    print("1.January")
    print("2.February")
    print("3.March")
    print("4.April")
    print("5.May")
    print("6.June")
    print("7.July")
    print("8.August")
    print("9.September")
    print("10.October")
    print("11.November")
    print("12.December")

    month= input("Please Enter Your Choice: ")

    if month == '12':
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn' 
    if month == '1':
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarias'
    if month == '2':
        astro_sign = 'Aquarias' if (day < 19) else 'Pisces'
    if month == '3':
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    if month == '4':
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    if month == '5':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    if month == '6':
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    if month == '7':
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    if month == '8':
        astro_sign = 'Leo'   if (day < 23) else 'Virgo'
    if month == '9':
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    if month == '10':
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    if month == '11':
        astro_sign = 'Scorpio' if (day< 22) else  'Sagittarius'

    print("______________________________________________________")
    print ("Your Zodiac Sign Is:  ", astro_sign)
    if astro_sign== "Sagittarius":
        file= open("try2.txt","r")
        line= file.readlines()
        print(line[0])
        print(line[1])
        print(line[2])
        print(line[3])
        print(line[4])
        print(line[5])

    else:
        print("hello")
    print("______________________________________________________")

