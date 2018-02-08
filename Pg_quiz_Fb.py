import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1

answer = pg.prompt (
"""
Do you like the flash

a) Yes
b) Its ok 
c) No
d) Never watched it
"""
    )
# Give points

if answer == "a":
    points += 0
elif answer == "b":
    points += 10
elif answer == "c":
    points += 100
elif answer == "d":
    points += 25

# Question 2

answer = pg.prompt (
"""
Do you like the Arrow

a) Yes
b) Its ok 
c) No
d) Never watched it
"""
    )
# Give points

if answer == "a":
    points += 0
elif answer == "b":
    points += 3
elif answer == "c":
    points += 25
elif answer == "d":
    points += 7

    # Question 3

answer = pg.prompt (
"""
Do you like the Black Lightning

a) Yes
b) Its ok 
c) No
d) Never watched it
"""
    )
# Give points

if answer == "a":
    points += 0
elif answer == "b":
    points += 0
elif answer == "c":
    points += 15
elif answer == "d":
    points += 1

# Question 4

answer = pg.prompt (
"""
Do you like the office

a) Yes
b) Its ok 
c) No
d) Never watched any part of any episode
"""
    )
# Give points

if answer == "a":
    points += 0
elif answer == "b":
    points += 20
elif answer == "c":
    points += 100
elif answer == "d":
    points += 200


# Question 5

answer = pg.prompt (
"""
Do you like the Knicks

a) Yes
b) No
c) Don't watch basketball
"""
    )
# Give points

if answer == "a":
    points += 0
elif answer == "b":
    points += 50
elif answer == "c":
    points += 10

# Question 6

answer = pg.prompt (

"""
Who is your favorite

a) Lebron James
b) Stephen Curry
c) Russel Westbrook
d) Kristaps Porzingus
e) Don't care
"""
    )
# Give points

if answer == "a":
    points += 30
elif answer == "b":
    points += 30
elif answer == "c":
    points += 20
elif answer == "d":
    points += 0
elif answer == "e":
    points += 10


# END OF SURVEY

pg.alert("You are...")

# Perfect
if points <= 0:
    pg.alert("Perfect")
    webbrowser.open("https://www.qsleap.com/content/wp-content/uploads/2016/10/perfect-1300767_960_720-715x315.png")

# Ok
elif points <= 100 and points > 0:
    pg.alert("ok")
    webbrowser.open("http://www.todayifoundout.com/wp-content/uploads/2010/04/ok.gif")

# A Horrible Human 
elif points > 100:
    pg.alert("A horrible human")
    webbrowser.open("http://clipground.com/images/bad-mood-clipart-1.jpg")



