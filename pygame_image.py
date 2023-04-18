import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    kokaton3 = pg.image.load("ex01-20230418/fig/3.png") #練習問題2
    kokaton3 = pg.transform.flip(kokaton3, True, False)
    kokaton3s = [kokaton3,pg.transform.rotozoom(kokaton3,10,1.0)] #練習問題3

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        screen.blit(bg_img, [0, 0]) #バックグランドに張り付けている
        screen.blit(kokaton3,[0,0])
        pg.display.update()
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
