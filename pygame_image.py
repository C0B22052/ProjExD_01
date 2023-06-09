import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    bg_imgs = pg.transform.flip(bg_img, True, False)
    #bg_img = pg.transform.scale("ex01-20230418/fig/pg_bg.jpg",(1,1))
    kokaton3 = pg.image.load("ex01-20230418/fig/3.png") #練習問題2
    kokaton3 = pg.transform.flip(kokaton3, True, False)
    kokaton3s = [kokaton3, pg.transform.rotozoom(kokaton3,10,1.0)] #練習問題3
                              #transform.rotozoom(画像,回転数,倍率)

    tmr = 0
    x = 0
    s = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x += 1 
        
        s = x%3200
              
        
        tmr += 1
        
        screen.blit(bg_img, [-s, 0]) #練習5
        screen.blit(bg_imgs, [1600-s, 0]) #バックグランドに張り付けている
        screen.blit(bg_img, [3200-s, 0])
        if tmr%160>=80:
            screen.blit(kokaton3s[0],[300,200])
        else:
            screen.blit(kokaton3s[1],[300,200])
        
        pg.display.update()
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

