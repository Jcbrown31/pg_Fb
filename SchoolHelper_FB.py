import pyautogui as pg
import webbrowser

English = ["https://classroom.google.com/u/1/c/NTA4OTEyODQ1NFpa", "https://docs.google.com/document/d/1SsZ9B7Ee2AHwMW78J3aTmV0d8y6ldprYOXHdLbOss6U/edit"]

History = ["https://docs.google.com/document/d/1YW2YCTf8d-jyC5334pd2tElmlm0jZEuz1HVYCXqMZNM/edit", "https://docs.google.com/document/d/1qPWLleVWIbwWLDamsc_pFZl8po5swtJ8tF7fC-9i1Bo/edit"]

Spanish = ["http://www.wordreference.com/"]

Science = ["https://classroom.google.com/c/NTEwNTg0Mjk1NVpa"]

Math = ["https://docs.google.com/spreadsheets/d/1bE7-_l5PTVw_cI-FmB8PsQd_k6V2r7b9gZPCZIPk0KQ/edit#gid=0"]

answer = pg.prompt (
"""
Which would you rather do
a) Do English
b) Do History
c) Do Spanish
d) Do Science
e) Do Math

"""
    )

if answer == "a":
    for i in English:
        webbrowser.open(i)

elif answer == "b":
    for i in History:
        webbrowser.open(i)
        
elif answer == "c":
    for i in Spanish:
        webbrowser.open(i)

elif answer == "d":
    for i in Science:
        webbrowser.open(i)

elif answer == "e":
    for i in Math:
        webbrowser.open(i)

