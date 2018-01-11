import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft',)
pg.typewrite('crome\n',.3)
pg.hotkey('winleft','up')
pg.typewrite('http://www.espn.com/nba/team/_/name/ny/new-york-knicks\n',.001)
time.sleep(30)
pg.hotkey('alt','f4')
pg.hotkey('ctrl','winleft','f4')
pg.hotkey('winleft')
pg.typewrite('crome\n',.1)
pg.typewrite('netflix.com\n',.1)

