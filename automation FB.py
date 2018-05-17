import pyautogui as pg
import webbrowser
import time

Movie = pg.prompt(
    """
What kinda movies do you like?
a)Comidy
b)Action
c)Classics
d)Adventure
e)Horror
f)Drama

""")

if Movie == "a":
    category = pg.prompt(
        """
You might like
a)The Bee movie 
b)Space Jam


        """)
    if category == "a":
        webbrowser.open ("https://www.youtube.com/watch?v=6aJpGejQPYg")

    elif category == "b":
        webbrowser.open ("https://www.youtube.com/watch?v=O93ZjQ10gI8")

elif Movie == "b":
    category = pg.prompt(
        """
You might like?
a)Bee Movie 
b)Die Hard

""")
    if category == "a":
       webbrowser.open ("https://www.youtube.com/watch?v=6aJpGejQPYg")
    elif category == "b":
        webbrowser.open ("https://www.youtube.com/watch?v=mklnXM3LIXo")
        
elif Movie == "c":
    category = pg.prompt(
        """
You might like
a) The Bee Movie
b) The Room
        """)
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=6aJpGejQPYg")
    elif category == "b":
        webbrowser.open("https://www.youtube.com/watch?v=pKAwXLVxuZQ")

elif game== "b":
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=PA9hpOnvtCk")
    elif category == "b":
        webbrowser.open("https://www.mayoclinic.org/first-aid/first-aid-heart-attack/basics/art-20056679")
