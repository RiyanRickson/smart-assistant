# Modules:A file contain codes you want to include in your program
# use 'import' to include a module (built-in or create your own)
# useful to break up a large program reuasable seperate files

# print(help("modules"))     # To see all tBhe modules in python

# print(help("math"))        # To see the given module in python
  
# import math 
# print(math.pi)

# # or

# import math as m             # preffered
# print(m.pi)

# from math import pi          # from <module_name> import <something_specific>
# print(pi)


# 1) random modules: To get random values for a game , to get random number/values ,  shuffle values

import random as r
# print(r.random())            # To get values b/w (0 and 1)

# print(r.uniform(1 , 10))     # To get values b/w (1 and 10)

# print(r.randint(5 , 10))     # To get random integers of range [5 , 10]

# greeting = ["Hey" , "Yo" , "Hi" , "Hola" , "Howdy", "Hey"]
# print(r.choice(greeting))    # To get. a random value from a given dataype

# print(r.choices(greeting , k = 10))
# To get k no. of values from a given datatype 
# 2 arguments datatype name and k value
# Gives output in list

# colors = ['Black' , 'Blue' , 'Green']
# result = r.choices(colors , weights = [18 , 18 , 2] , k = 38)

# print(result.count("Green"))
# print(result.count("Black"))
# print(result.count("Blue"))

# deck = list(range(1, 53))
# r.shuffle(deck)      # this shuffles the list
# print(deck)          # now print the shuffled list

# shuffled_deck = r.sample(deck, len(deck))
# print(shuffled_deck)


# •	shuffle() → changes your existing list , returns None.
# •	sample() → returns a new shuffled list , leaves the original intact.

# To get a list of random sample of 5 cards from our 52 deck of cards (we did not use choices methord as it won't give us distinct values)
# deck = list(range(1, 53))
# hand = r.sample(deck , k = 5)
# print(hand)

# • random()
# • uniform()
# • randint()
# • choice()
# • choices()
# • shuffle()
# • sample()

# 2) math module:

# before that lets do built in functions that don't require import of it:

# x = 3.141516
# y = -4
# z = 5

# result = round(x)
# print(result)
# 3

# result = round(x , 2)
# print(result)
# 3.14

# result = abs(y)      # Here abs() --> is the absolute value function ie modulus function.
# print(result)
# 4

# result = pow( y , 3)
# print(result)
# -64

# result = max(x , y , z)
# print(result)
# 5

# # result = min(x , y , z)
# print(result)
# -4
 
# Therefore:
# max
# min
# pow
# round
# abs
# sum

# for more:

import math

# basic:

# print(math.pi)
# 3.141592653589793
# print(round(math.pi , 2))
# 3.14

# print(math.e)
# 2.718281828459045

# x = 9
# print(math.sqrt(x))
# 3.0        #gives ans in floating points

#  Rounding and Truncation:

# print(round(math.e , 2))
# 2.72

# result = math.ceil(9.1)         
# print(result)
# 10        # it's like a GIF

# result = math.floor(9.9)    
# print(result)
# 9         # it's like a LIF

# math.trunc(x):Removes decimal (toward zero)
# print(math.trunc(-4.8))
# -4                                  -4.8  --> -4  -->  0
# print(math.trunc(4.8))
# 4                                    0  <--  4  <--  4.8

# log func:
# print(math.log(10))
# 2.302585092994046
# print(math.log10(10))
# 1.0
# print(math.log2(1))
# 0.0

# exponential func:
# print(math.exp(1))
# 2.718281828459045
# print(math.exp(2))
# 7.38905609893065
# pow() discussed

# Trigonometric Functions:
# print(math.sin(math.pi/2))
# 1.0
# print(math.asin(1))
# 1.5707963267948966
# print(math.sinh(1))
# 1.1752011936438014

# Factorials and Combinatorics:

# math.factorial(n):n! (only for non-negative ints)
# print(math.factorial(5))
# 120

# math.comb(n, k):Number of combinations (n choose k)
# print(math.comb(5, 2))
# 10           ncr = (n!/((n-r)!*r!))

# math.perm(n, k):Number of permutations
# print(math.perm(5, 2))
# 20

# THEREFORE:

# pi
# e 
# sqrt
# ceil , floor , round , trunc
# math.pow(x, y) , math.exp(x) , 
# math.log(x)  # natural log , math.log10(x) , math.log2(x)
# math.factorial(n)
# math.sin(x), math.cos(x), math.tan(x) math.asin(x) , matj.acos(x) , math.atan() , math.sin(h) , math.cos(h) , math.tanh(h) —  trig functions


# 3 calendar module
import calendar

# calendar(year , month) function:
# print(calendar.calendar(2025))
#                                   2025

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2                      1  2
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
# 27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
#                                                     31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                1  2  3  4                         1
#  7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
# 14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
# 21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
# 28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
#                                                     30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
#  7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 28 29 30 31               25 26 27 28 29 30 31      29 30

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
# 27 28 29 30 31            24 25 26 27 28 29 30      29 30 31

# print(calendar.month(2025, 11))
#    November 2025
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30









# month(year , month) function
# print(calendar.month(2000 , 4))
#      April 2000
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

# print(calendar.month(2025, 11))
#    November 2025
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

# weekday(year,month,day) function: Day of week (0–6)
# print(calendar.weekday(2025,11,4))
# 1     # becouse tuesday
# print(calendar.isoweekday(2025,11,4))
# no isoweekday unlike datetime

# isleap(year) function:True if leap year
# print(calendar.isleap(2024))
# True

# leapdays(year1,year2) function:Count of leap years
# print(calendar.leapdays(2000,2025))   
# 7       #here  it is not inclusive of y2 , It counts leap years from y1 up to but not including y2.

# monthrange(year,month):(weekday, days)
# print(calendar.monthrange(2025, 11))
# # Output: (5, 30)


# monthcalendar(year,month):List of weeks
# cal = calendar.monthcalendar(2025, 11)
# for week in cal:
#     print(week)















# 4 datetime module:

import datetime as t

# d = t.date(2016 , 7 , 24)
# print(d)
# 2016-07-24

# tday = t.date.today()
# print(tday)
# 2025-11-04

# print(tday.weekday())          # Monday -> 0 , Tuesday -> 1 , ... , Sunday --> 6
# 1
# print(tday.isoweekday())
# 2                              # Monday -> 1 , Tuesday -> 2 , ... , Sunday --> 7

# delta_t = t.timedelta(days = 7)  # To check date from + / - n days
# print(tday + delta_t)
# print(tday - delta_t)

# time = t.time(12 , 30 ,0)
# print(time)

# now = t.datetime.now()
# print(now)
