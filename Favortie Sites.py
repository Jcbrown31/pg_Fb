import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=p3gZi62iefo", "https://www.youtube.com/watch?v=qZHycHI3F1Q"]

teams = ["http://www.espn.com/nba/team/_/name/ny/new-york-knicks", "http://www.espn.com/"]

answer = pg.prompt (
"""
Which would you rather do
a) Watch videos
b) Check sports

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in teams:
        webbrowser.open(i)
