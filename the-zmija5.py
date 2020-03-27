import pygame
import time
import random

pygame.init()

sirina=1000
visina=600
prozor=pygame.display.set_mode((sirina,visina)) #veličina prozora
pygame.display.set_caption('Zmija') #naslov prozora

ikona=pygame.image.load('snake.png')
pygame.display.set_icon(ikona)

odbrojavanje=pygame.mixer.Sound('countdown.wav')
theme=pygame.mixer.Sound('song.wav')
blip=pygame.mixer.Sound('blip.wav')
game_over=pygame.mixer.Sound('gameover.wav')
level_up=pygame.mixer.Sound('lvlup.wav')

clock=pygame.time.Clock()

crna=(0,0,0)
bijela=(255,255,255)
crvena=(159,25,25)
tamnozelena=(19,66,17)
zelena=(153,204,102)

#print(pygame.font.get_fonts)

def unos_ime(novo):
    b=True
    while b:
        for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_0 or event.key==pygame.K_KP0:
                        novo+='0'
                        b=False
                    elif event.key==pygame.K_1 or event.key==pygame.K_KP1:
                        novo+='1'
                        b=False
                    elif event.key==pygame.K_2 or event.key==pygame.K_KP2:
                        novo+='2'
                        b=False
                    elif event.key==pygame.K_3 or event.key==pygame.K_KP3:
                        novo+='3'
                        b=False
                    elif event.key==pygame.K_4 or event.key==pygame.K_KP4:
                        novo+='4'
                        b=False
                    elif event.key==pygame.K_5 or event.key==pygame.K_KP5:
                        novo+='5'
                        b=False
                    elif event.key==pygame.K_6 or event.key==pygame.K_KP6:
                        novo+='6'
                        b=False
                    elif event.key==pygame.K_7 or event.key==pygame.K_KP7:
                        novo+='7'
                        b=False
                    elif event.key==pygame.K_8 or event.key==pygame.K_KP8:
                        novo+='8'
                        b=False
                    elif event.key==pygame.K_9 or event.key==pygame.K_KP9:
                        novo+='9'
                        b=False
                    elif event.key==pygame.K_PERIOD or event.key==pygame.K_KP_PERIOD:
                        novo+='.'
                        b=False
                    elif event.key==pygame.K_COMMA:
                        novo+=','
                        b=False
                    elif event.key==pygame.K_KP_MINUS:
                        novo+='-'
                        b=False
                    elif event.key==pygame.K_KP_PLUS:
                        novo+='+'
                        b=False
                    elif event.key==pygame.K_KP_MULTIPLY:
                        novo+='*'
                        b=False
                    elif event.key==pygame.K_KP_DIVIDE:
                        novo+='/'
                        b=False
                        
                    elif event.key==pygame.K_q:
                        novo+='Q'
                        b=False
                    elif event.key==pygame.K_w:
                        novo+='W'
                        b=False
                    elif event.key==pygame.K_e:
                        novo+='E'
                        b=False
                    elif event.key==pygame.K_r:
                        novo+='R'
                        b=False
                    elif event.key==pygame.K_t:
                        novo+='T'
                        b=False
                    elif event.key==pygame.K_y:
                        novo+='Z'
                        b=False
                    elif event.key==pygame.K_u:
                        novo+='U'
                        b=False
                    elif event.key==pygame.K_i:
                        novo+='I'
                        b=False
                    elif event.key==pygame.K_o:
                        novo+='O'
                        b=False
                    elif event.key==pygame.K_p:
                        novo+='P'
                        b=False
                    elif event.key==pygame.K_a:
                        novo+='A'
                        b=False
                    elif event.key==pygame.K_s:
                        novo+='S'
                        b=False
                    elif event.key==pygame.K_d:
                        novo+='D'
                        b=False
                    elif event.key==pygame.K_f:
                        novo+='F'
                        b=False
                    elif event.key==pygame.K_g:
                        novo+='G'
                        b=False
                    elif event.key==pygame.K_h:
                        novo+='H'
                        b=False
                    elif event.key==pygame.K_j:
                        novo+='J'
                        b=False
                    elif event.key==pygame.K_k:
                        novo+='K'
                        b=False
                    elif event.key==pygame.K_l:
                        novo+='L'
                        b=False
                    elif event.key==pygame.K_z:
                        novo+='Y'
                        b=False
                    elif event.key==pygame.K_x:
                        novo+='X'
                        b=False
                    elif event.key==pygame.K_c:
                        novo+='C'
                        b=False
                    elif event.key==pygame.K_v:
                        novo+='V'
                        b=False
                    elif event.key==pygame.K_b:
                        novo+='B'
                        b=False
                    elif event.key==pygame.K_n:
                        novo+='N'
                        b=False
                    elif event.key==pygame.K_m:
                        novo+='M'
                        b=False
                    elif event.key==pygame.K_SPACE:
                        novo+=' '
                        b=False
                    elif event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                        novo+='\n'
                        b=False
                    elif event.key==pygame.K_BACKSPACE:
                        novo=novo[:-1]
                        b=False
    return(novo)

def poruka(sadrzaj,boja,vrsta,velicina,x,y):
    vrsta_fonta=pygame.font.SysFont(vrsta,velicina)
    tekst=vrsta_fonta.render(sadrzaj,True,boja)
    okvir=tekst.get_rect()
    okvir.center=(x,y)
    prozor.blit(tekst,okvir)
    pygame.display.update()
    
def upute():
    uputa=True
    prozor.fill(bijela)
    pozadina=pygame.image.load('pozadina2.png')
    jabuka=pygame.image.load('jabuka.png')
    super_jabuka=pygame.image.load('superjabuka.png')
    losa_jabuka=pygame.image.load('losa jabuka.png')
    skare=pygame.image.load('scissors.png')
    lubanja=pygame.image.load('lubanja.png')
    prozor.blit(pozadina,(0,0))
    while upute:
        poruka('Upute',tamnozelena,'comicsansms',85,sirina/2,(visina/11))
        poruka('Strelicama pokreći zmijicu. Za pauzu pritisni P.',crna,'comicsansms',25,sirina/2,(visina/3)-60)
        poruka('Nemoj se zabiti u zid ili u sebe.',crna,'comicsansms',25,sirina/2,(visina*5/12)-60)
        poruka('Ako skupiš dovoljno bodova prelaziš na sljedeću razinu.',crna,'comicsansms',25,sirina/2,(visina/2)-60)
        
        prozor.blit(jabuka, (sirina*5/12,(visina*7/12)-60))
        poruka('= 1 bod',crna,'comicsansms',23,sirina*6/12,(visina*7/12)-50)
        
        prozor.blit(super_jabuka, ((sirina*5/12)-10,(visina*8/12)-65))
        poruka('= 10 bodova',crna,'comicsansms',23,(sirina*6/12)+26,(visina*8/12)-50)
        
        prozor.blit(losa_jabuka, (sirina*5/12,(visina*9/12)-55))
        poruka('= gubitak svih bodova',crna,'comicsansms',23,(sirina*6/12)+79,(visina*9/12)-40)
        
        prozor.blit(skare, ((sirina*5/12),(visina*10/12)-50))
        poruka('= smanjenje duljine na pola',crna,'comicsansms',23,(sirina*6/12)+109,(visina*10/12)-38)
        
        prozor.blit(lubanja, ((sirina*5/12),(visina*10/12)-5))
        poruka('= kraj igre',crna,'comicsansms',23,(sirina/2)+23,(visina*10/12)+7)

        poruka('Za novu igru pritisni SPACE, za povratak pritisni ESCAPE.',crna,'comicsansms',21,sirina*2/3,(visina*13/14))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                uputa=False
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    uputa=False
                    igra()
                elif event.key==pygame.K_ESCAPE:
                    uputa=False
                    pocetak_igre()
                                    
        pygame.display.update()
        clock.tick(15)
        
def naj_rezultati():
    pozadina=pygame.image.load('pozadina2.png')
    prozor.blit(pozadina,(0,0))
    najbolji=True
    dat=open('high scores.txt', 'r')
    L=dat.readlines()
    dat.close()
    while upute:
        poruka('Najbolji rezultati',tamnozelena,'comicsansms',70,sirina/2,visina/7)
        poruka('Za novu igru pritisni SPACE, za povratak pritisni ESCAPE.',crna,'comicsansms',21,sirina*2/3,(visina*11/12))
        v=visina*7/24
        for i in range(len(L)):
            mjesto=str(i+1)+'.'
            bod=L[i][:(L[i]).find('\t')]
            ime=L[i][(L[i]).find('\t')+1:L[i].find('\n')]
            poruka(mjesto, crna, 'comicsansms',18,(sirina/3)+50,v)
            poruka(ime, crna, 'comicsansms',18,(sirina/2)+50,v)
            poruka(bod, crna, 'comicsansms',18,(sirina*2/3)+50,v)
            v+=visina/18
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                najbolji=False
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    najbolji=False
                    igra()
                elif event.key==pygame.K_ESCAPE:
                    najbolji=False
                    pocetak_igre()
                    
        pygame.display.update()
        clock.tick(15)
    

def pocetak_igre():
    pozadina=pygame.image.load('pozadina.png')
    pocetak=True
    #prozor.fill(bijela)
    prozor.blit(pozadina,(0,0))
    while pocetak:
        poruka('THE ZMIJA',tamnozelena,'comicsansms',100,sirina/2,visina/6)
        poruka('Igra (SPACE)',tamnozelena,'comicsansms',50,sirina*2/3,visina*5/12)
        poruka('Upute (U)',tamnozelena,'comicsansms',50,sirina*2/3,visina*7/12)
        poruka('Najbolji rezultati (N)',tamnozelena,'comicsansms',50,sirina*2/3,visina*9/12)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pocetak=False
                    igra()
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_u:
                    pocetak=False
                    upute()
                elif event.key==pygame.K_n:
                    pocetak=False
                    naj_rezultati()
                    
        pygame.display.update()
        clock.tick(15)

def upis_dat(L):
    matrica=[]
    for i in range (len(L)):
        L1=[]
        bod=L[i][:(L[i]).find('\t')]
        L1+=[int(bod)]
        ime=L[i][(L[i]).find('\t')+1:L[i].find('\n')]
        L1+=[ime]
        matrica.append(L1)

    matrica=sorted(matrica, key=lambda i: i [0])
    del matrica[0]
    matrica.reverse()
    L=[]
    for i in range(len(matrica)):
        L1=(str(matrica[i][0])+'\t'+str(matrica[i][1])+'\n')
        L.append(L1)

    dat=open('high scores.txt', 'w')
    dat.writelines (L)
    dat.close()

def ekran_sudar(bodovi):
    sudar=True
    prozor.fill(bijela)
    pozadina=pygame.image.load('pozadina2.png')
    prozor.blit(pozadina,(0,0))
    while sudar:
        poruka('Kraj igre',tamnozelena,'comicsansms',100,sirina/2,visina/4)
        poruka('Tvoj rezultat: '+str(bodovi),crna,'comicsansms',25,sirina*7/12,(visina/3+125))
        poruka('Za novu igru pritisni SPACE, za izlazak iz igre pritisni ESCAPE.',crna,'comicsansms',20,sirina*7/12,(visina*5/6))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    sudar=False
                    igra()
                elif event.key==pygame.K_ESCAPE:
                    sudar=False
                    pocetak_igre()
                    
        pygame.display.update()
        clock.tick(15)

def ekran_sudar_naj(bodovi):
    pozadina=pygame.image.load('pozadina2.png')
    prozor.blit(pozadina,(0,0))
    ime='i'
    dat=open('high scores.txt', 'r')
    L=dat.readlines()
    dat.close()
    provjera='p'
    
    while provjera!='\n':
        poruka('Kraj igre',tamnozelena,'comicsansms',100,sirina/2,visina/5)
        poruka('Tvoj rezultat: '+str(bodovi),crna,'comicsansms',25,sirina*7/12,(visina/2)-20)
        poruka('Upiši ime:', crna, 'comicsansms',25,(sirina*7/12),(visina*7/12))
        poruka(ime[1:], crna, 'comicsansms',25,(sirina*7/12),(visina*8/12))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        ime=unos_ime(ime)
        provjera=ime[-1]
        prozor.blit(pozadina,(0,0))
        
        pygame.display.update()
        clock.tick(15)

    L+=[(str(bodovi)+'\t'+ime[1:])]
    upis_dat(L)

    sudar=True    
    while sudar:
        poruka('Kraj igre',tamnozelena,'comicsansms',100,sirina/2,visina/5)
        poruka('Tvoj rezultat: '+str(bodovi),crna,'comicsansms',25,(sirina*7/12),(visina/2)-20)
        poruka('Upiši ime:', crna, 'comicsansms',25,(sirina*7/12),(visina*7/12))
        poruka(ime[1:-1], crna, 'comicsansms',25,(sirina*7/12),(visina*8/12))
        poruka('Za novu igru pritisni SPACE, za izlazak iz igre pritisni ESCAPE.',crna,'comicsansms',20,(sirina*7/12),(visina*5/6))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    sudar=False
                    igra()
                elif event.key==pygame.K_ESCAPE:
                    sudar=False
                    pocetak_igre()
                    
        pygame.display.update()
        clock.tick(15)
    
def sudar(bodovi):
    pygame.mixer.Sound.stop(theme)
    pygame.mixer.Sound.play(game_over)
    dat=open('high scores.txt', 'r')
    L=dat.readlines()
    dat.close()

    if bodovi<int(L[-1][:(L[-1]).find('\t')]):
        ekran_sudar(bodovi)
    else:
        ekran_sudar_naj(bodovi)
    
def pauza():
    veca_pozadina=pygame.image.load('trava2.png')
    pauza=True
    prozor.blit(veca_pozadina,(0,0))
    while pauza:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pauza=False
                elif event.key==pygame.K_ESCAPE:
                    pauza=False
                    pocetak_igre()
        
        poruka('Pauza',crna,'comicsansms',100,sirina/2,visina/2)
        poruka('Pritisni SPACE za povratak u igru.',crna,'comicsansms',50,sirina/2,visina*2/3)
        pygame.display.update()
        clock.tick(3)
    pygame.mixer.Sound.play(odbrojavanje)
    prozor.blit(veca_pozadina,(0,0))
    poruka('3',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('2',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('1',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)

def provjera(x,y,x2,y2,x3,y3,x4,y4):
    if x==200 and 200<=y<400 or x==780 and 200<=y<400:
        x=round(random.randrange(40,sirina-40,20))
        y=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4=provjera(x,y,x2,y2,x3,y3,x4,y4)
    if 180<=x2<220 and 1180<=y2<400 or 760<=x2<800 and 180<=y2<400:
        x2=round(random.randrange(40,sirina-40,20))
        y2=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4=provjera(x,y,x2,y2,x3,y3,x4,y4)
    if x3==200 and 180<=y3<400 or x3==780 and 180<=y3<400:
        x3=round(random.randrange(40,sirina-40,20))
        y3=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4=provjera(x,y,x2,y2,x3,y3,x4,y4)
    if x4==200 and 200<=y4<400 or x4==780 and 200<=y4<400:
        x4=round(random.randrange(40,sirina-40,20))
        y4=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4=provjera(x,y,x2,y2,x3,y3,x4,y4)
    return(x,y,x2,y2,x3,y3,x4,y4)

def provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5):
    if x==200 and 140<=y<240 or x==200 and 400<=y<500 or x==780 and 140<=y<240 or x==780 and 400<=y<500 or 220<=x<420 and y==140 or 580<=x<780 and y==140 or 580<=x<780 and y==480 or 220<=x<420 and y==480:
        x=round(random.randrange(40,sirina-40,20))
        y=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
    if 180<=x2<220 and 120<=y2<240 or 180<=x2<220 and 380<=y2<500 or 760<=x2<800 and 120<=y2<240 or 760<=x2<800 and 380<=y2<500 or 200<=x2<420 and 120<=y2<160 or 560<=x2<780 and 120<=y2<160 or 560<=x2<780 and 460<=y2<500 or 200<=x2<420 and 460<=y2<500:
        x2=round(random.randrange(40,sirina-40,20))
        y2=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
    if x3==200 and 120<=y3<240 or x3==200 and 380<=y3<500 or x3==780 and 120<=y3<240 or x3==780 and 380<=y3<500 or 220<=x3<420 and y3==120 or 580<=x3<780 and y3==120 or 580<=x3<780 and y3==460 or 220<=x3<420 and y3==460:
        x3=round(random.randrange(40,sirina-40,20))
        y3=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
    if x4==200 and 140<=y4<240 or x4==200 and 400<=y4<500 or x4==780 and 140<=y4<240 or x4==780 and 400<=y4<500 or 220<=x4<420 and y4==140 or 580<=x4<780 and y4==140 or 580<=x4<780 and y4==480 or 220<=x4<420 and y4==480:
        x4=round(random.randrange(40,sirina-40,20))
        y4=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
    if x5==200 and 140<=y5<240 or x5==200 and 400<=y5<500 or x5==780 and 140<=y5<240 or x5==780 and 400<=y5<500 or 220<=x5<420 and y5==140 or 580<=x5<780 and y5==140 or 580<=x5<780 and y5==480 or 220<=x5<420 and y5==480:
        x5=round(random.randrange(40,sirina-40,20))
        y5=round(random.randrange(40,visina-40,20))
        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
    return(x,y,x2,y2,x3,y3,x4,y4,x5,y5)

def hrana(x,y,jabuka):
    prozor.blit(jabuka,(x,y))
    
def pokupljena_jabuka(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
    if zmija_x+zmija_s>x and zmija_x<(x+20) and zmija_y+zmija_v>y and zmija_y<(y+20):
        pygame.mixer.Sound.play(blip)
        return True
    else:
        return False

def pokupljena_superjabuka(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
    if zmija_x+zmija_s>x and zmija_x<(x+40) and zmija_y+zmija_v>y and zmija_y<(y+40):
        pygame.mixer.Sound.play(blip)
        return True
    else:
        return False

def pokupljena_losa(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
    if zmija_x+zmija_s>x and zmija_x<(x+20) and zmija_y+zmija_v>y and zmija_y<(y+29):
        pygame.mixer.Sound.play(blip)
        return True
    else:
        return False

def pokupljene_skare(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
    if zmija_x+zmija_s>x and zmija_x<(x+20) and zmija_y+zmija_v>y and zmija_y<(y+20):
        pygame.mixer.Sound.play(blip)
        return True
    else:
        return False

def pokupljena_smrt(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
    if zmija_x+zmija_s>x and zmija_x<(x+20) and zmija_y+zmija_v>y and zmija_y<(y+20):
        return True
    else:
        return False
        
def rezultat(bodovi):
    vrsta_fonta=pygame.font.SysFont('comicsansms',20)
    tekst=vrsta_fonta.render('Rezultat: '+str(bodovi),True,tamnozelena)
    prozor.blit(tekst,(10,0))

def najbolje(high_score):
    vrsta_fonta=pygame.font.SysFont('comicsansms',20)
    tekst=vrsta_fonta.render('Najbolji postignuti rezultat: '+str(high_score),True,tamnozelena)
    prozor.blit(tekst,(sirina/2,0))

def zmija(smjer,lista,zmija_s,zmija_v):
    boja=tamnozelena
    for i in lista:
        pygame.draw.rect(prozor, boja, [i[0],i[1],zmija_s,zmija_v])
           
def igra():
    pygame.mixer.Sound.play(theme)
    zmija_x=300
    zmija_y=400
    zmija_s=20
    zmija_v=20
    duljina=3
    smjer=2
    x=round(random.randrange(40,sirina-40,20))
    y=round(random.randrange(40,visina-40,20))
    x2=round(random.randrange(40,sirina-40,20))
    y2=round(random.randrange(40,visina-40,20))
    x3=round(random.randrange(40,sirina-40,20))
    y3=round(random.randrange(40,visina-40,20))
    bodovi=0
    uvjet_super=round(random.randrange(1,20))
    uvjet_losa=round(random.randrange(1,20))
    timer_start_super=time.time()
    timer_start_losa=time.time()
    brzina=5
    lista=[]
    jabuka=pygame.image.load('jabuka.png')
    super_jabuka=pygame.image.load('superjabuka.png')
    losa_jabuka=pygame.image.load('losa jabuka.png')
    trava=pygame.image.load('trava.png')

    dat=open('high scores.txt', 'r')
    popis=dat.readlines()
    prvi=popis[0]
    tab=prvi.find('\t')
    high_score=prvi[:tab]
    dat.close()
    
    kraj=False
    while not kraj:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and smjer!=3:
                    smjer=1
                elif event.key==pygame.K_DOWN and smjer!=1:
                    smjer=3
                elif event.key==pygame.K_LEFT and smjer!=2:
                    smjer=0
                elif event.key==pygame.K_RIGHT and smjer!=0:
                    smjer=2
                elif event.key==pygame.K_p:
                    pygame.mixer.Sound.stop(theme)
                    pauza()
                    pygame.mixer.Sound.play(theme)
                elif event.key==pygame.K_ESCAPE:
                    pygame.mixer.Sound.stop(theme)
                    pocetak_igre()
               
        prozor.fill(bijela)
        prozor.blit(trava,(0,40))
              
        if uvjet_super==7:
            hrana(x2,y2,super_jabuka)
        if uvjet_losa==7:
            hrana(x3,y3,losa_jabuka)
        hrana(x,y,jabuka)
            
        pygame.draw.line(prozor, crna, (0,40),(sirina,40))

        if smjer==0:
            zmija_x-=zmija_s
        elif smjer==1:
            zmija_y-=zmija_v
        elif smjer==2:
            zmija_x+=zmija_s
        elif smjer==3:
            zmija_y+=zmija_v

        glava=[]
        glava.append(zmija_x)
        glava.append(zmija_y)
        lista.append(glava)
        if len(lista)>duljina:
            del lista[0]

        zmija(smjer,lista,zmija_s,zmija_v)
        rezultat(bodovi)
                        
        if zmija_x==-zmija_s or zmija_x==sirina:
            sudar(bodovi)
        elif zmija_y==zmija_v or zmija_y==visina:
            sudar(bodovi)

        for svaki in lista[:-1]:
            if svaki==glava:
                sudar(bodovi)

        if uvjet_super==7:
            if pokupljena_superjabuka(zmija_x,zmija_y,zmija_s,zmija_v,x2,y2):
                bodovi+=10
                duljina+=1
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_super=time.time()
        if uvjet_losa==7:
            if pokupljena_losa(zmija_x,zmija_y,zmija_s,zmija_v,x3,y3):
                bodovi-=bodovi
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_losa=time.time()
        if pokupljena_jabuka(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
                if uvjet_losa==7 or uvjet_super==7:
                    if uvjet_super!=7:
                        uvjet_super=round(random.randrange(1,20))
                        timer_start_super=time.time()
                    if uvjet_losa!=7:
                        uvjet_losa=round(random.randrange(1,20))
                        timer_start_losa=time.time()
                    bodovi+=1
                    duljina+=1
                    x=round(random.randrange(40,sirina-40,20))
                    y=round(random.randrange(40,visina-40,20))
                    brzina+=0.2
                else:
                    bodovi+=1
                    duljina+=1
                    x=round(random.randrange(40,sirina-40,20))
                    y=round(random.randrange(40,visina-40,20))
                    uvjet_super=round(random.randrange(1,20))
                    uvjet_losa=round(random.randrange(1,20))
                    brzina+=0.2
                    timer_start_super=time.time()
                    timer_start_losa=time.time()
        timer_end_super=time.time()
        timer_end_losa=time.time()
        #print(timer_end-timer_start)

        if uvjet_super==7:
            if timer_end_super-timer_start_super>8:
                timer_start_super=time.time()
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
        if uvjet_losa==7:
            if timer_end_losa-timer_start_losa>15:
                timer_start_losa=time.time()
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
                                        
        if bodovi!='':
            if int(bodovi)>int(high_score):
                high_score=bodovi
        najbolje(high_score)

        if bodovi>=50:
            kraj=True
            pygame.mixer.Sound.stop(theme)
            pygame.mixer.Sound.play(level_up)
                    
        print(uvjet_super,uvjet_losa)
        pygame.display.update()
        clock.tick(brzina)

    pygame.time.wait(1000)
    igra2(bodovi,duljina)

def igra2(bodovi,duljina):
    veca_pozadina=pygame.image.load('trava2.png')
    prozor.blit(veca_pozadina,(0,0))
    poruka('Level 2',crna,'comicsansms',100,sirina/2,visina/2)
    poruka('Nemoj se zabiti u crvene zidove.',crna,'comicsansms',40,sirina/2,visina*3/4)
    pygame.time.wait(2000)
    pygame.mixer.Sound.play(odbrojavanje)
    prozor.blit(veca_pozadina,(0,0))
    poruka('3',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('2',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('1',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    
    pygame.mixer.Sound.play(theme)
    zmija_x=300
    zmija_y=400
    zmija_s=20
    zmija_v=20
    smjer=2
    x=round(random.randrange(40,sirina-40,20))
    y=round(random.randrange(40,visina-40,20))
    x2=round(random.randrange(40,sirina-40,20))
    y2=round(random.randrange(40,visina-40,20))
    x3=round(random.randrange(40,sirina-40,20))
    y3=round(random.randrange(40,visina-40,20))
    x4=round(random.randrange(40,sirina-40,20))
    y4=round(random.randrange(40,visina-40,20))
    uvjet_super=round(random.randrange(1,20))
    uvjet_losa=round(random.randrange(1,20))
    uvjet_skare=round(random.randrange(1,20))
    timer_start_super=time.time()
    timer_start_losa=time.time()
    timer_start_skare=time.time()
    brzina=5
    lista=[]
    jabuka=pygame.image.load('jabuka.png')
    super_jabuka=pygame.image.load('superjabuka.png')
    losa_jabuka=pygame.image.load('losa jabuka.png')
    skare=pygame.image.load('scissors.png')
    trava=pygame.image.load('trava.png')

    dat=open('high scores.txt', 'r')
    popis=dat.readlines()
    prvi=popis[0]
    tab=prvi.find('\t')
    high_score=prvi[:tab]
    dat.close()
    
    kraj=False
    while not kraj:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and smjer!=3:
                    smjer=1
                elif event.key==pygame.K_DOWN and smjer!=1:
                    smjer=3
                elif event.key==pygame.K_LEFT and smjer!=2:
                    smjer=0
                elif event.key==pygame.K_RIGHT and smjer!=0:
                    smjer=2
                elif event.key==pygame.K_p:
                    pygame.mixer.Sound.stop(theme)
                    pauza()
                    pygame.mixer.Sound.play(theme)
                elif event.key==pygame.K_ESCAPE:
                    pygame.mixer.Sound.stop(theme)
                    pocetak_igre()
               
        prozor.fill(bijela)
        prozor.blit(trava,(0,40))

        x,y,x2,y2,x3,y3,x4,y4=provjera(x,y,x2,y2,x3,y3,x4,y4)
         
        pygame.draw.rect(prozor, crvena, [200,200,20,200])
        pygame.draw.rect(prozor, crvena, [780,200,20,200])
              
        if uvjet_super==7:
            hrana(x2,y2,super_jabuka)
        if uvjet_losa==7:
            hrana(x3,y3,losa_jabuka)
        if uvjet_skare==7:
            hrana(x4,y4,skare)
        hrana(x,y,jabuka)
            
        pygame.draw.line(prozor, crna, (0,40),(sirina,40))
        
        if smjer==0:
            zmija_x-=zmija_s
        elif smjer==1:
            zmija_y-=zmija_v
        elif smjer==2:
            zmija_x+=zmija_s
        elif smjer==3:
            zmija_y+=zmija_v

        glava=[]
        glava.append(zmija_x)
        glava.append(zmija_y)
        lista.append(glava)
        if len(lista)>duljina:
            n=len(lista)-duljina
            for i in range (n):
                del lista[0]

        zmija(smjer,lista,zmija_s,zmija_v)
        rezultat(bodovi)
                        
        if zmija_x==-zmija_s or zmija_x==sirina:
            sudar(bodovi)
        elif zmija_y==zmija_v or zmija_y==visina:
            sudar(bodovi)
        elif zmija_x+zmija_s>200 and zmija_x<220 and zmija_y+zmija_v>200 and zmija_y<400:
            sudar(bodovi)
        elif zmija_x+zmija_s>780 and zmija_x<800 and zmija_y+zmija_v>200 and zmija_y<400:
            sudar(bodovi)

        for svaki in lista[:-1]:
            if svaki==glava:
                sudar(bodovi)

        if uvjet_super==7:
            if pokupljena_superjabuka(zmija_x,zmija_y,zmija_s,zmija_v,x2,y2):
                bodovi+=10
                duljina+=1
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_super=time.time()
        if uvjet_losa==7:
            if pokupljena_losa(zmija_x,zmija_y,zmija_s,zmija_v,x3,y3):
                bodovi-=bodovi
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_losa=time.time()
        if uvjet_skare==7:
            if pokupljene_skare(zmija_x,zmija_y,zmija_s,zmija_v,x4,y4):
                duljina-=duljina//2
                x4=round(random.randrange(40,sirina-40,20))
                y4=round(random.randrange(40,visina-40,20))
                uvjet_skare=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_skare=time.time()
        if pokupljena_jabuka(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
            if uvjet_losa==7 or uvjet_super==7 or uvjet_skare==7:
                if uvjet_losa!=7:
                    uvjet_losa=round(random.randrange(1,20))
                    timer_start_losa=time.time()
                if uvjet_super!=7:
                    uvjet_super=round(random.randrange(1,20))
                    timer_start_super=time.time()
                if uvjet_skare!=7:                    
                    uvjet_skare=round(random.randrange(1,20))
                    timer_start_skare=time.time()
                bodovi+=1
                duljina+=1
                x=round(random.randrange(40,sirina-40,20))
                y=round(random.randrange(40,visina-40,20))
                brzina+=0.2
            else:
                bodovi+=1
                duljina+=1
                x=round(random.randrange(40,sirina-40,20))
                y=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
                uvjet_losa=round(random.randrange(1,20))
                uvjet_skare=round(random.randrange(1,20))
                timer_start_super=time.time()
                timer_start_losa=time.time()
                timer_start_skare=time.time()
                brzina+=0.2
            
        timer_end_super=time.time()
        timer_end_losa=time.time()
        timer_end_skare=time.time()

        if uvjet_super==7:
            if timer_end_super-timer_start_super>8:
                timer_start_super=time.time()
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
        if uvjet_losa==7:
            if timer_end_losa-timer_start_losa>15:
                timer_start_losa=time.time()
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
        if uvjet_skare==7:
            if timer_end_skare-timer_start_skare>10:
                timer_start_skare=time.time()
                x4=round(random.randrange(40,sirina-40,20))
                y4=round(random.randrange(40,visina-40,20))
                uvjet_skare=round(random.randrange(1,20))
                        
        if bodovi!='':
            if int(bodovi)>int(high_score):
                high_score=bodovi
        najbolje(high_score)

        if bodovi>=100:
            kraj=True
            pygame.mixer.Sound.stop(theme)
            pygame.mixer.Sound.play(level_up)

        print(uvjet_super,uvjet_losa,uvjet_skare)
        pygame.display.update()
        clock.tick(brzina)

    pygame.time.wait(1000)
    igra3(bodovi,duljina,brzina)

def igra3(bodovi,duljina,brzina):
    veca_pozadina=pygame.image.load('trava2.png')
    prozor.blit(veca_pozadina,(0,0))
    poruka('Level 3',crna,'comicsansms',100,sirina/2,visina/2)
    poruka('Nemoj se zabiti u crvene zidove.',crna,'comicsansms',40,sirina/2,visina*3/4)
    pygame.time.wait(2000)
    pygame.mixer.Sound.play(odbrojavanje)
    prozor.blit(veca_pozadina,(0,0))
    poruka('3',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('2',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    prozor.blit(veca_pozadina,(0,0))
    poruka('1',crna,'comicsansms',100,sirina/2,visina/2)
    pygame.time.wait(1000)
    
    pygame.mixer.Sound.play(theme)
    zmija_x=300
    zmija_y=400
    zmija_s=20
    zmija_v=20
    smjer=2
    x=round(random.randrange(40,sirina-40,20))
    y=round(random.randrange(40,visina-40,20))
    x2=round(random.randrange(40,sirina-40,20))
    y2=round(random.randrange(40,visina-40,20))
    x3=round(random.randrange(40,sirina-40,20))
    y3=round(random.randrange(40,visina-40,20))
    x4=round(random.randrange(40,sirina-40,20))
    y4=round(random.randrange(40,visina-40,20))
    x5=round(random.randrange(40,sirina-40,20))
    y5=round(random.randrange(40,visina-40,20))
    uvjet_super=round(random.randrange(1,20))
    uvjet_losa=round(random.randrange(1,20))
    uvjet_skare=round(random.randrange(1,20))
    uvjet_smrt=round(random.randrange(1,20))
    timer_start_super=time.time()
    timer_start_losa=time.time()
    timer_start_skare=time.time()
    timer_start_smrt=time.time()
    lista=[]
    jabuka=pygame.image.load('jabuka.png')
    super_jabuka=pygame.image.load('superjabuka.png')
    losa_jabuka=pygame.image.load('losa jabuka.png')
    skare=pygame.image.load('scissors.png')
    smrt=pygame.image.load('lubanja.png')
    trava=pygame.image.load('trava.png')

    dat=open('high scores.txt', 'r')
    popis=dat.readlines()
    prvi=popis[0]
    tab=prvi.find('\t')
    high_score=prvi[:tab]
    dat.close()
    
    kraj=False
    while not kraj:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and smjer!=3:
                    smjer=1
                elif event.key==pygame.K_DOWN and smjer!=1:
                    smjer=3
                elif event.key==pygame.K_LEFT and smjer!=2:
                    smjer=0
                elif event.key==pygame.K_RIGHT and smjer!=0:
                    smjer=2
                elif event.key==pygame.K_p:
                    pygame.mixer.Sound.stop(theme)
                    pauza()
                    pygame.mixer.Sound.play(theme)
                elif event.key==pygame.K_ESCAPE:
                    pygame.mixer.Sound.stop(theme)
                    pocetak_igre()
               
        prozor.fill(bijela)
        prozor.blit(trava,(0,40))

        x,y,x2,y2,x3,y3,x4,y4,x5,y5=provjera2(x,y,x2,y2,x3,y3,x4,y4,x5,y5)
         
        pygame.draw.rect(prozor, crvena, [220,140,200,20])
        pygame.draw.rect(prozor, crvena, [200,140,20,100])
        pygame.draw.rect(prozor, crvena, [220,480,200,20])
        pygame.draw.rect(prozor, crvena, [200,400,20,100])
        pygame.draw.rect(prozor, crvena, [580,140,200,20])
        pygame.draw.rect(prozor, crvena, [780,140,20,100])
        pygame.draw.rect(prozor, crvena, [580,480,200,20])
        pygame.draw.rect(prozor, crvena, [780,400,20,100])
                      
        if uvjet_super==7:
            hrana(x2,y2,super_jabuka)
        if uvjet_losa==7:
            hrana(x3,y3,losa_jabuka)
        if uvjet_skare==7:
            hrana(x4,y4,skare)
        if uvjet_smrt==7:
            hrana(x5,y5,smrt)
        hrana(x,y,jabuka)
            
        pygame.draw.line(prozor, tamnozelena, (0,40),(sirina,40))
        
        if smjer==0:
            zmija_x-=zmija_s
        elif smjer==1:
            zmija_y-=zmija_v
        elif smjer==2:
            zmija_x+=zmija_s
        elif smjer==3:
            zmija_y+=zmija_v

        glava=[]
        glava.append(zmija_x)
        glava.append(zmija_y)
        lista.append(glava)
        if len(lista)>duljina:
            n=len(lista)-duljina
            for i in range (n):
                del lista[0]

        zmija(smjer,lista,zmija_s,zmija_v)
        rezultat(bodovi)
                        
        if zmija_x==-zmija_s or zmija_x==sirina:
            sudar(bodovi)
        elif zmija_y==zmija_v or zmija_y==visina:
            sudar(bodovi)
        elif zmija_x+zmija_s>200 and zmija_x<420 and zmija_y+zmija_v>140 and zmija_y<160:
            sudar(bodovi)
        elif zmija_x+zmija_s>200 and zmija_x<220 and zmija_y+zmija_v>140 and zmija_y<240:
            sudar(bodovi)
        elif zmija_x+zmija_s>200 and zmija_x<220 and zmija_y+zmija_v>400 and zmija_y<500:
            sudar(bodovi)
        elif zmija_x+zmija_s>200 and zmija_x<420 and zmija_y+zmija_v>480 and zmija_y<500:
            sudar(bodovi)
        elif zmija_x+zmija_s>580 and zmija_x<800 and zmija_y+zmija_v>140 and zmija_y<160:
            sudar(bodovi)
        elif zmija_x+zmija_s>780 and zmija_x<800 and zmija_y+zmija_v>140 and zmija_y<240:
            sudar(bodovi)
        elif zmija_x+zmija_s>780 and zmija_x<800 and zmija_y+zmija_v>400 and zmija_y<500:
            sudar(bodovi)
        elif zmija_x+zmija_s>580 and zmija_x<800 and zmija_y+zmija_v>480 and zmija_y<500:
            sudar(bodovi)

        for svaki in lista[:-1]:
            if svaki==glava:
                sudar(bodovi)

        if uvjet_super==7:
            if pokupljena_superjabuka(zmija_x,zmija_y,zmija_s,zmija_v,x2,y2):
                bodovi+=10
                duljina+=1
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_super=time.time()
        if uvjet_losa==7:
            if pokupljena_losa(zmija_x,zmija_y,zmija_s,zmija_v,x3,y3):
                bodovi-=bodovi
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_losa=time.time()
        if uvjet_skare==7:
            if pokupljene_skare(zmija_x,zmija_y,zmija_s,zmija_v,x4,y4):
                duljina-=duljina//2
                x4=round(random.randrange(40,sirina-40,20))
                y4=round(random.randrange(40,visina-40,20))
                uvjet_skare=round(random.randrange(1,20))
                brzina+=0.2
                timer_start_skare=time.time()
        if uvjet_smrt==7:
            if pokupljena_smrt(zmija_x,zmija_y,zmija_s,zmija_v,x5,y5):
                sudar(bodovi)
        if pokupljena_jabuka(zmija_x,zmija_y,zmija_s,zmija_v,x,y):
            if uvjet_losa==7 or uvjet_super==7 or uvjet_skare==7 or uvjet_smrt==7:
                if uvjet_losa!=7:
                    uvjet_losa=round(random.randrange(1,20))
                    timer_start_losa=time.time()
                if uvjet_super!=7:
                    uvjet_super=round(random.randrange(1,20))
                    timer_start_super=time.time()
                if uvjet_skare!=7:                    
                    uvjet_skare=round(random.randrange(1,20))
                    timer_start_skare=time.time()
                if uvjet_smrt!=7:
                    uvjet_smrt=round(random.randrange(1,20))
                    timer_start_smrt==time.time()
                bodovi+=1
                duljina+=1
                x=round(random.randrange(40,sirina-40,20))
                y=round(random.randrange(40,visina-40,20))
                brzina+=0.2
            else:
                bodovi+=1
                duljina+=1
                x=round(random.randrange(40,sirina-40,20))
                y=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
                uvjet_losa=round(random.randrange(1,20))
                uvjet_skare=round(random.randrange(1,20))
                uvjet_smrt=round(random.randrange(1,20))
                timer_start_super=time.time()
                timer_start_losa=time.time()
                timer_start_skare=time.time()
                timer_start_smrt=time.time()
                brzina+=0.2
            
        timer_end_super=time.time()
        timer_end_losa=time.time()
        timer_end_skare=time.time()
        timer_end_smrt=time.time()

        if uvjet_super==7:
            if timer_end_super-timer_start_super>8:
                timer_start_super=time.time()
                x2=round(random.randrange(40,sirina-40,20))
                y2=round(random.randrange(40,visina-40,20))
                uvjet_super=round(random.randrange(1,20))
        if uvjet_losa==7:
            if timer_end_losa-timer_start_losa>15:
                timer_start_losa=time.time()
                x3=round(random.randrange(40,sirina-40,20))
                y3=round(random.randrange(40,visina-40,20))
                uvjet_losa=round(random.randrange(1,20))
        if uvjet_skare==7:
            if timer_end_skare-timer_start_skare>10:
                timer_start_skare=time.time()
                x4=round(random.randrange(40,sirina-40,20))
                y4=round(random.randrange(40,visina-40,20))
                uvjet_skare=round(random.randrange(1,20))
        if uvjet_smrt==7:
            if timer_end_smrt-timer_start_smrt>20:
                timer_start_smrt=time.time()
                x5=round(random.randrange(40,sirina-40,20))
                y5=round(random.randrange(40,visina-40,20))
                uvjet_smrt=round(random.randrange(1,20))
                        
        if bodovi!='':
            if int(bodovi)>int(high_score):
                high_score=bodovi
        najbolje(high_score)

        print(uvjet_super,uvjet_losa,uvjet_skare,uvjet_smrt)
        pygame.display.update()
        clock.tick(brzina)

pocetak_igre()
