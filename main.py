import pygame
import os

pygame.font.init()

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")


WHITE = (255,255,255)
RED = (255,0,0)
DARK_BLUE = (0,0,20)
BLACK = (0,0,0)
PURPLE = (150,0,200)

X_IMAGE = pygame.image.load(os.path.join("cross.png"))
X = pygame.transform.scale(X_IMAGE,(150,150))
O_IMAGE = pygame.image.load(os.path.join("o.png"))
O = pygame.transform.scale(O_IMAGE,(150,150))
RETRY_IMAGE = pygame.image.load(os.path.join("Retry.png"))
RETRY = pygame.transform.scale(RETRY_IMAGE,(100,100))

WELCOME_FONT = pygame.font.SysFont("comicsans", 80,bold = True)
SCORE_FONT = pygame.font.SysFont("comicsans", 100,bold = True)

FPS = 100

count = 1

def draw_window(x_list,o_list,rects):
    WIN.fill(DARK_BLUE)
    pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//3-10,0,10,HEIGHT))
    pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//3*2-10,0,10,HEIGHT))
    pygame.draw.rect(WIN,WHITE,pygame.Rect(0,HEIGHT//3-10,WIDTH,10))
    pygame.draw.rect(WIN,WHITE,pygame.Rect(0,HEIGHT//3*2-10,WIDTH,10))
    for x in x_list:
        WIN.blit(X,(rects[x].x+20,rects[x].y+20))
    for o in o_list:
        WIN.blit(O,(rects[o].x+20,rects[o].y+20))
    pygame.display.update()

def check_click(rects,x_list,o_list):
    global count
    for rect in range(9):
        if rects[rect].collidepoint(pygame.mouse.get_pos()):
            if count%2 == 0 and ((rect not in x_list) and (rect not in o_list)):
                count += 1
                o_list.append(rect)
            elif count%2 != 0 and ((rect not in x_list) and (rect not in o_list)):
                count += 1
                x_list.append(rect)
                

def check_win(x_list,o_list):
    text = ""
    if (0 in x_list and 1 in x_list and 2 in x_list) or (3 in x_list and 4 in x_list and 5 in x_list) or (6 in x_list and 7 in x_list and 8 in x_list) or (0 in x_list and 3 in x_list and 6 in x_list) or (1 in x_list and 4 in x_list and 7 in x_list) or (2 in x_list and 5 in x_list and 8 in x_list) or (0 in x_list and 4 in x_list and 8 in x_list) or (2 in x_list and 4 in x_list and 6 in x_list):
        text = "X WINS"
        return text
    if (0 in o_list and 1 in o_list and 2 in o_list) or (3 in o_list and 4 in o_list and 5 in o_list) or (6 in o_list and 7 in o_list and 8 in o_list) or (0 in o_list and 3 in o_list and 6 in o_list) or (1 in o_list and 4 in o_list and 7 in o_list) or (2 in o_list and 5 in o_list and 8 in o_list) or (0 in o_list and 4 in o_list and 8 in o_list) or (2 in o_list and 4 in o_list and 6 in o_list):
        text = "O WINS"
        return text
    if (len(x_list) + len(o_list)) == 9 and text == "":
        return "TIE" 

def start_menu():
    start = True
    clock = pygame.time.Clock()
    while start:
        clock.tick(FPS)
        WIN.fill(DARK_BLUE)
        welcome_text = WELCOME_FONT.render("TIC-TAC-TOE",1,PURPLE)
        WIN.blit(welcome_text,(WIDTH//2-pygame.Surface.get_width(welcome_text)//2,HEIGHT//2-pygame.Surface.get_height(welcome_text)//2-150))
        start_text = WELCOME_FONT.render("START",1, WHITE)
        start_rect = pygame.Rect(WIDTH//2-pygame.Surface.get_width(start_text)//2-10,HEIGHT//2-pygame.Surface.get_height(start_text)//2+50,pygame.Surface.get_width(start_text)+20,pygame.Surface.get_height(start_text)+20)
        pygame.draw.rect(WIN,(255,35,30),start_rect,border_radius = 40)
        WIN.blit(start_text,(WIDTH//2-pygame.Surface.get_width(start_text)//2,HEIGHT//2-pygame.Surface.get_height(start_text)//2+50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    start = False
                    main()
        pygame.display.update()

def end_menu(WIN_TEXT):
    clock = pygame.time.Clock()
    end = True
    while end:
        clock.tick(FPS)
        WIN.fill(DARK_BLUE)
        txt = SCORE_FONT.render(WIN_TEXT,1,PURPLE)
        WIN.blit(txt,(WIDTH//2-pygame.Surface.get_width(txt)//2,HEIGHT//2-pygame.Surface.get_height(txt)//2-100))
        WIN.blit(RETRY,(WIDTH//2-pygame.Surface.get_width(RETRY)//2,HEIGHT//2-pygame.Surface.get_height(RETRY)//2+50))
        RETRY_RECT = pygame.Rect(WIDTH//2-pygame.Surface.get_width(RETRY)//2,HEIGHT//2-pygame.Surface.get_height(RETRY)//2+50,100,100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETRY_RECT.collidepoint(pygame.mouse.get_pos()):
                    main()
        pygame.display.update()

def main():
    global count
    x_list = []
    o_list = []
    rects = []
    clock = pygame.time.Clock()
    run = True
    count = 1
    while run:
        clock.tick(FPS)
        WIN_TEXT = check_win(x_list,o_list)
        for i in range(0,HEIGHT,HEIGHT//3):
            for j in range(0,WIDTH,WIDTH//3): 
                if j == 400:
                    rects.append(pygame.Rect(j,i,WIDTH//3,HEIGHT//3-10))
                if i == 400:
                    rects.append(pygame.Rect(j,i,WIDTH//3-10,HEIGHT//3))
                if i != 400 and j!= 400:
                    rects.append(pygame.Rect(j,i,WIDTH//3-10,HEIGHT//3-10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                check_click(rects,x_list,o_list)
            if WIN_TEXT != None:
                run = False
                end_menu(WIN_TEXT)
        if run == True:
            draw_window(x_list,o_list,rects)
if __name__ == "__main__":
    start_menu()
     
