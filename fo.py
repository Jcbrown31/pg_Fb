import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name")
answer = pg.prompt("Enter your name")

speak.Speak("Hello " + answer + ". " "Nice to meet you.")



color = pg.prompt("Enter in your favorite color.")


if color == "Blue":
    speak.Speak("I like blue too.")

elif color == "Black":
    speak.Speak(color + " is the worst of all the colors.")

else:
    speak.Speak("I really enjoy " + color + " also. ")


speak.Speak("What video would you like to watch.")
video = pg.prompt("Enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)
