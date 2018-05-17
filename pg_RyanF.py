import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
time.sleep(.5)
pg.typewrite('chrome\n',.1)
time.sleep(.2)
pg.hotkey('winleft','up')
time.sleep(1)
pg.typewrite('espn.com\n',.2)
time.sleep(5)
pg.click(1312, 173)
time.sleep(.1)
pg.typewrite('Saquon Barkley\n',.2)
time.sleep(4)
pg.click(715, 287)
