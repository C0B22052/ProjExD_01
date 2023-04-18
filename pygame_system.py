import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600)) #画面の大きさを設定
    clock  = pg.time.Clock()
    fonto  = pg.font.Font(None, 280) #文字の大きさを決定
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        txt = fonto.render(str(tmr), True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(txt, [300, 200])
        pg.display.update()
        clock.tick(1)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()