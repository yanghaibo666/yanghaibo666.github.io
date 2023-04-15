import pygame, sys
import tkinter
from tkinter import ttk, StringVar
import os
from time import *
import tkinter.messagebox
import platform
from pygame.locals import *
userPlatform=platform.system()
if userPlatform == 'Darwin':
    tkinter.messagebox.showerror("Error","必须是Windows系统")
    sys.exit()
elif userPlatform == 'Linux':
    tkinter.messagebox.showerror("Error","必须是Windows系统")
    sys.exit()
else:
    pass
time_get = strftime('%Y_%m_%d_%H_%M_%S', localtime(time()))
try:
    os.mkdir('./game_log')
except:
    pass
try:
    os.mkdir('./file')
except:
    pass
with open("./game_log/" + time_get + ".txt", "w", encoding="utf-8") as file:
    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏加载\n")
try:
    with open("./file/music_number.txt", "r", encoding="utf-8") as file:
        if file.read() == "":
            with open("C:/music_number.txt", "w", encoding="utf-8") as file:
                file.write("1")
except:
    with open("./file/music_number.txt", "w", encoding="utf-8") as file:
        file.write("1")
def collide_color(aSurface,aRect,aColor):
    pixel=pygame.PixelArray(aSurface)
    aPixel=pixel[aRect.x:aRect.x+aRect.width,aRect.y:aRect.y+aRect.height]
    pygame.PixelArray.close(pixel)
    return aColor in aPixel
pygame.init()
# for i in range(701):
#     screen = pygame.display.set_mode((i, 1))
# screen = pygame.display.set_mode((700, 1))
# for j in range(501):
#     screen = pygame.display.set_mode((700, j))
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("元气大乱斗")
start = pygame.image.load("./picture/start.png")
start_rect = pygame.Rect(280, 300, 140, 50)
boss_mode_start = pygame.image.load("./picture/boss_mode.png")
boss_mode_start_rect=pygame.Rect(225,350,281,54)
game_name = pygame.image.load("./picture/game_name.png")
set_up1 = pygame.image.load("./picture/设置.png")
set_up = pygame.transform.scale(set_up1, (50, 50))
set_up_rect = pygame.Rect(650, 450, 50, 50)
sjjx1 = pygame.image.load("./picture/水晶巨蟹.png")
sjjx = pygame.transform.scale(sjjx1, (100, 70))
heLp1=pygame.image.load("./picture/帮助.png")
heLp=pygame.transform.scale(heLp1,(50,50))
help_rect=pygame.Rect(600,450,50,50)
add_blood1=pygame.image.load("./picture/add_blood.png")
add_blood=pygame.transform.scale(add_blood1,(200,32))
p1_add_blood_rect=pygame.Rect(0,200,200,32)
p2_add_blood_rect=pygame.Rect(500,200,200,32)
gift1=pygame.image.load("./picture/gift.png")
gift=pygame.transform.scale(gift1,(70,50))
gift_rect=pygame.Rect(0,450,70,50)
p1_x = 30
p1_y = 30
p1_hp = 100
p2_x = 570
p2_y = 400
game_time = 0
p1_hp = 0
p2_hp = 0
coins_p1=0
coins_p2=0
with open("./file/music_number.txt", "r", encoding="utf-8") as file:
    music_number = file.read()
bgSound = pygame.mixer.music.load("./music/" + music_number + ".mp3")
pygame.mixer.music.play(-1)
try:
    with open("./file/coin_p1.txt","r",encoding="utf-8") as file:
        coins_p1=file.read()
except:
    with open("./file/coin_p1.txt","w",encoding="utf-8") as file:
        file.write("0")
    with open("./file/coin_p1.txt","r",encoding="utf-8") as file:
        coins_p1=file.read()
try:
    with open("./file/coin_p2.txt","r",encoding="utf-8") as file:
        coins_p2=file.read()
except:
    with open("./file/coin_p2.txt","w",encoding="utf-8") as file:
        file.write("0")
    with open("./file/coin_p2.txt","r",encoding="utf-8") as file:
        coins_p2=file.read()
try:
    with open("./file/p1_hp.txt","r",encoding="utf-8") as file:
        p1_hp=file.read()
except:
    with open("./file/p1_hp.txt","w",encoding="utf-8") as file:
        file.write("100")
    with open("./file/p1_hp.txt","r",encoding="utf-8") as file:
        p1_hp=file.read()
try:
    with open("./file/p2_hp.txt","r",encoding="utf-8") as file:
        p2_hp=file.read()
except:
    with open("./file/p2_hp.txt","w",encoding="utf-8") as file:
        file.write("100")
    with open("./file/p1_hp.txt","r",encoding="utf-8") as file:
        p2_hp=file.read()
aaaa=""
gift_hp_coin = "hp"
player1 = "p1"
player2 = "p1"
blue=pygame.Color("blue")
red=pygame.Color("red")
def gift_tkinter_window():
    gift_window=tkinter.Tk()
    gift_window.geometry("500x250")


    def go_player1(*args):
        player1=comvalue_player1.get()
    def go_player2(*args):
        player2=comvalue_player2.get()
    def go_gift(*args):
        gift_hp_coin=comvalue_gift.get()
        print(gift_hp_coin)
    def go_out_gift():
        if quantity_entry.get()=="":
            tkinter.messagebox.showwarning("warning","quantity不能为空")
            with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:quantity不能为空\n")
        else:
            if comvalue_gift.get()=="hp":
                if comvalue_player1.get()=="p1" and comvalue_player2.get()=="p1":
                    tkinter.messagebox.showwarning("warning","赠予人与被赠予人不能相同")
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:赠予人与被赠予人不能相同\n")
                if comvalue_player1.get()=="p2" and comvalue_player2.get()=="p2":
                    tkinter.messagebox.showwarning("warning", "赠予人与被赠予人不能相同")
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:赠予人与被赠予人不能相同\n")
                with open("./file/"+comvalue_player1.get()+"_hp.txt","r",encoding="utf-8") as file:
                    aaaaaaaaa = file.read()
                    if int(aaaaaaaaa) > int(quantity_entry.get()):
                        with open("./file/"+comvalue_player1.get()+"_hp.txt","w",encoding="utf-8") as file:
                            a111=str(int(aaaaaaaaa)-int(quantity_entry.get()))
                            file.write(a111)
                        with open("./file/"+comvalue_player2.get()+"_hp.txt","r",encoding="utf-8") as file:
                            aaaaaaaaaa=file.read()
                        with open("./file/"+comvalue_player2.get()+"_hp.txt","w",encoding="utf-8") as file:
                            a1111=str(int(aaaaaaaaaa)+int(quantity_entry.get()))
                            file.write(a1111)
                    else:
                        tkinter.messagebox.showwarning("warning", "数量不能大于赠予人的生命数量")
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:数量不能大于赠予人的生命数量\n")
            if comvalue_gift.get()=="coin":
                print(player1,player2)
                if comvalue_player1.get()=="p1" and comvalue_player2.get()=="p1":
                    tkinter.messagebox.showwarning("warning","赠予人与被赠予人不能相同")
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:赠予人与被赠予人不能相同\n")
                if comvalue_player1.get()=="p2" and comvalue_player2.get()=="p2":
                    tkinter.messagebox.showwarning("warning", "赠予人与被赠予人不能相同")
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:赠予人与被赠予人不能相同\n")
                with open("./file/coin_"+comvalue_player1.get()+".txt","r",encoding="utf-8") as file:
                    aaaaaaaa = file.read()
                    if int(aaaaaaaa) >= int(quantity_entry.get()):
                        with open("./file/coin_"+comvalue_player1.get()+".txt","w",encoding="utf-8") as file:
                            a11=str(int(aaaaaaaa)-int(quantity_entry.get()))
                            file.write(a11)
                        with open("./file/coin_"+comvalue_player2.get()+".txt","r",encoding="utf-8") as file:
                            aaaaaaaaa=file.read()
                        with open("./file/coin_"+comvalue_player2.get()+".txt","w",encoding="utf-8") as file:
                            a111=str(int(aaaaaaaaa)+int(quantity_entry.get()))
                            file.write(a111)
                    else:
                        tkinter.messagebox.showwarning("warning","数量不能大于赠予人的金币数量")
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]warning:数量不能大于赠予人的金币数量\n")
    tkinter.Label(gift_window,text="gift",font=("微软雅黑",30)).pack()
    comvalue_player1=tkinter.StringVar()
    combolist_player1=ttk.Combobox(gift_window,textvariable=comvalue_player1)
    combolist_player1["value"]=("p1","p2")
    combolist_player1.current(0)
    combolist_player1.bind("<<ComboboxSelected>>",go_player1)
    tkinter.Label(gift_window,text="to").pack()
    combolist_player1.place(x=75,y=63)
    comvalue_player2=tkinter.StringVar()
    combolist_player2=ttk.Combobox(gift_window,textvariable=comvalue_player2)
    combolist_player2.place(x=270,y=63)
    combolist_player2["value"]=("p1","p2")
    combolist_player2.current(0)
    combolist_player2.bind("<<ComboboxSelected>>",go_player2)
    tkinter.Label(gift_window,text="gift:").place(x=75,y=90)
    comvalue_gift=tkinter.StringVar()
    combolist_gift=ttk.Combobox(gift_window,textvariable=comvalue_gift)
    combolist_gift["value"]=("hp","coin")
    combolist_gift.current(0)
    combolist_gift.bind("<<ComboboxSelected>>",go_gift)
    combolist_gift.place(x=100,y=90)
    tkinter.Label(gift_window,text="quantity:").place(x=75,y=115)
    quantity_entry=tkinter.Entry(gift_window)
    quantity_entry.place(x=130, y=115)
    tkinter.Button(gift_window,text="确定",command=go_out_gift).place(x=240,y=200)
    gift_window.mainloop()
def set_window_main():
    set_up_window = tkinter.Tk()
    set_up_window.title("元气大乱斗 set up")
    set_up_window.geometry("300x700")
    label_title = tkinter.Label(set_up_window, text="set up", font=("微软雅黑", 20, "bold"))
    label_title.pack()
    label_title1 = tkinter.Label(set_up_window, text="music:", font=("微软雅黑", 15))
    label_title1.place(x=0, y=30)
    var = tkinter.StringVar()

    def set_music_dingyi():
        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]设置背景音乐为:" + str(var.get()) + ".mp3\n")
        with open("./file/music_number.txt", "w", encoding="utf-8") as file:
            file.write(var.get())

    tkinter.Radiobutton(set_up_window, text="冰风暴", variable=var, value="1", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="超星际旅行", variable=var, value="2", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="春天的礼物", variable=var, value="3", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="地表下的秘密", variable=var, value="4", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="翻滚的岩浆", variable=var, value="5", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="钢铁破浪者永不沉没", variable=var, value="6", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="劲敌", variable=var, value="7", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="决战", variable=var, value="8", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="漆黑地牢", variable=var, value="9", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="强手", variable=var, value="10", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="英雄荟萃", variable=var, value="11", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="溶洞神秘大碟", variable=var, value="12", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="树沼神秘大碟", variable=var, value="13", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="万圣节幽影", variable=var, value="14", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="小心坠落", variable=var, value="15", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="新年新气象", variable=var, value="16", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="遗迹神秘大碟", variable=var, value="17", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="英雄的化身", variable=var, value="18", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="勇闯密林深处", variable=var, value="19", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="元气满满", variable=var, value="20", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="远眺那辉煌的神庙", variable=var, value="21", command=set_music_dingyi).pack()
    tkinter.Radiobutton(set_up_window, text="直到黎明的尽头", variable=var, value="22", command=set_music_dingyi).pack()
    aaaa=""
    def ok_music():
        pygame.mixer.music.stop()
        with open("./file/music_number.txt", "r", encoding="utf-8") as file:
            aaaa=file.read()
            BgSound = pygame.mixer.music.load("./music/" + str(aaaa) + ".mp3")
            with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file1:
                file1.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]将背景音乐改为" + str(aaaa) + ".mp3\n")
        pygame.mixer.music.play(-1)

    tkinter.Button(set_up_window, text="确定", command=ok_music).pack()
    set_up_window.mainloop()

def game_help():
    game_help_window=tkinter.Tk()
    game_help_window.title("game help")
    game_help_window.geometry("330x260")
    tkinter.Label(game_help_window,text="游戏帮助",font=("微软雅黑",30,"bold")).pack()
    tkinter.Label(game_help_window,text="1.p1移动:上w 下s 左a 右d").pack()
    tkinter.Label(game_help_window,text="2.p2移动:上↑ 下↓ 左← 右→").pack()
    tkinter.Label(game_help_window,text="3.普通攻击:p1空格 p2Enter").pack()
    tkinter.Label(game_help_window,text="4.技能攻击(共3次 无CD):p1 m  p2 Backspace").pack()
    tkinter.Label(game_help_window,text="5.普通攻击范围:红框碰到红框").pack()
    tkinter.Label(game_help_window,text="6.技能攻击范围:绿框碰到绿框").pack()
    tkinter.Label(game_help_window, text="7.p1地震波:按r").pack()
    tkinter.Label(game_help_window, text="8.p2地震波:按p").pack()
    tkinter.Label(game_help_window,text="注:如果技能红框未碰到对方绿框,会减技能数,但对方不会减血").pack()
    tkinter.Label(game_help_window,text="注:gift需关闭赠与才能生效").pack()
    tkinter.Label(game_help_window,text="注:仅支持windows系统")
    game_help_window.mainloop()
p_yes = 0
now_game_time = 0
p1_s_to_p2_p = 0
p2_s_to_p1_p = 0
p1_jinen = 3
p2_jinen = 3
a = 0
a1 = 0
r=50
rtf=0
ftr=0
dzb2_p2_x=0
dzb2_p2_y=0
dzb2_p2_tf=0
r1=50
rtf1=0
ftr1=0
dzb1_p1_tf=0
dzb1_p1_x=0
dzb1_p1_y=0
clock = pygame.time.Clock()
with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏初始化\n")
while True:
    if game_time == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if set_up_rect.collidepoint(event.pos):
                    set_window_main()
                if start_rect.collidepoint(event.pos):
                    game_time = 2
                if help_rect.collidepoint(event.pos):
                    game_help()
                if boss_mode_start_rect.collidepoint(event.pos):
                    game_time = 3
        screen.fill((255, 255, 255))
        screen.blit(game_name, (120, 100))
        screen.blit(start, (280, 300))
        screen.blit(boss_mode_start,(225,350))
        screen.blit(set_up, (650, 450))
        screen.blit(heLp,(600,450))
        pygame.display.update()
    if game_time == 1:
        screen.fill((255, 255, 255))
        clock.tick(60)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if a1 == 0:
                            if p_yes == 1:
                                p2_hp=int(p2_hp)
                                p2_hp -= 1
                                p2_hp=str(p2_hp)
                                with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2减1滴血\n")
                    elif event.key == pygame.K_RETURN:
                        if a1 == 0:
                            if p_yes == 1:
                                p1_hp = int(p1_hp)
                                p1_hp -= 1
                                p1_hp = str(p1_hp)
                                with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1减1滴血\n")
                    elif event.key == pygame.K_m:
                        if a1 == 0:
                            if p1_jinen >= 1:
                                p1_jinen -= 1
                                with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1使用技能\n")
                                if p1_s_to_p2_p == 1:
                                    p2_hp = int(p2_hp)
                                    p2_hp -= 10
                                    p2_hp = str(p2_hp)
                                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                        file.write(
                                            "[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2减10滴血\n")
                    elif event.key == pygame.K_BACKSPACE:
                        if a1 == 0:
                            if p2_jinen >= 1:
                                p2_jinen -= 1
                                with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                    file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2使用技能\n")
                                if p2_s_to_p1_p == 1:
                                    if a1 == 0:
                                        p1_hp = int(p1_hp)
                                        p1_hp -= 10
                                        p1_hp = str(p1_hp)
                                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                                            file.write(
                                                "[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1减10滴血\n")
                    elif event.key == pygame.K_p:
                        if dzb2_p2_tf==0:
                            ftr = 1
                            rtf = 1
                            dzb2_p2_x=p2_x+50
                            dzb2_p2_y=p2_y+35
                            dzb2_p2_tf=1
                    elif event.key == pygame.K_r:
                        if dzb1_p1_tf==0:
                            ftr1 = 1
                            rtf1 = 1
                            dzb1_p1_x=p1_x+50
                            dzb1_p1_y=p1_y+35
                            dzb1_p1_tf=1
                if p1_hero_p.colliderect(p2_hero_p):
                    p_yes = 1
                else:
                    p_yes = 0
                if p1_hero_s.colliderect(p2_hero_p):
                    p1_s_to_p2_p = 1
                else:
                    p1_s_to_p2_p = 0
                if p2_hero_s.colliderect(p1_hero_p):
                    p2_s_to_p1_p = 1
                else:
                    p2_s_to_p1_p = 0
            key_pressed_is=pygame.key.get_pressed()
            if key_pressed_is[K_UP]:
                if a1 == 0:
                    if p2_y != 30:
                        p2_y -= 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2上移动\n")
            if key_pressed_is[K_DOWN]:
                if a1 == 0:
                    if p2_y != 400:
                        p2_y += 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2下移动\n")
            if key_pressed_is[K_LEFT]:
                if a1 == 0:
                    if p2_x != 30:
                        p2_x -= 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2左移动\n")
            if key_pressed_is[K_RIGHT]:
                if a1 == 0:
                    if p2_x != 570:
                        p2_x += 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2右移动\n")
            if key_pressed_is[K_w]:
                if a1 == 0:
                    if p1_y != 30:
                        p1_y -= 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1上移动\n")
            if key_pressed_is[K_s]:
                if a1 == 0:
                    if p1_y != 400:
                        p1_y += 5
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1下移动\n")
            if key_pressed_is[K_a]:
                if a1 == 0:
                    if p1_x != 30:
                        p1_x -= 5
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1左移动\n")
            if key_pressed_is[K_d]:
                if a1 == 0:
                    if p1_x != 570:
                        p1_x += 5
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1右移动\n")

            p1_skills_word = "p1 skills:" + str(p1_jinen)
            p2_skills_word = "p2 skills:" + str(p2_jinen)
            p1_skills_font = pygame.font.SysFont(None, 30)
            p2_skills_font = pygame.font.SysFont(None, 30)
            p1_skills_text = p1_skills_font.render(p1_skills_word, True, (0, 0, 0))
            p2_skills_text = p2_skills_font.render(p2_skills_word, True, (0, 0, 0))
            p1_win_word = "p1 is a winner!"
            p2_win_word = "p2 is a winner!"
            p1_win_font = pygame.font.SysFont(None, 100)
            p2_win_font = pygame.font.SysFont(None, 100)
            p1_win_text = p1_win_font.render(p1_win_word, True, (0, 0, 0))
            p2_win_text = p2_win_font.render(p2_win_word, True, (0, 0, 0))
            if now_game_time == 0:

                p1_hp_word = "p1 hp:" + str(p1_hp)
                p2_hp_word = "p2 hp:" + str(p2_hp)
                p1_hp_font = pygame.font.SysFont(None, 30)
                p2_hp_font = pygame.font.SysFont(None, 30)
                p1_hp_text = p1_hp_font.render(p1_hp_word, True, (0, 0, 0))
                p2_hp_text = p2_hp_font.render(p2_hp_word, True, (0, 0, 0))

                p1_hero_p = pygame.Rect(p1_x, p1_y, 100, 70)
                p2_hero_p = pygame.Rect(p2_x, p2_y, 100, 70)
                p1_hero_s = pygame.Rect(p1_x - 30, p1_y - 30, 160, 130)
                p2_hero_s = pygame.Rect(p2_x - 30, p2_y - 30, 160, 130)
                screen.fill((255, 255, 255))
                clock = pygame.time.Clock()
                time_passed = clock.tick()
                time_passed = clock.tick(100)
                if ftr == 1:
                    pygame.draw.circle(screen, (0, 0, 255), (dzb2_p2_x, dzb2_p2_y), r, 5)
                if rtf == 1:
                    r += 1
                if r== 250:
                    ftr = 0
                    rtf= 0
                    r = 5
                    dzb2_p2_tf=0
                if ftr1 == 1:
                    pygame.draw.circle(screen, (255, 0,0), (dzb1_p1_x, dzb1_p1_y), r1, 5)
                if rtf1 == 1:
                    r1 += 1
                if r1 == 250:
                    ftr1 = 0
                    rtf1 = 0
                    r1 = 5
                    dzb1_p1_tf=0
                if collide_color(screen, p1_hero_p, blue):
                    p1_hp=int(p1_hp)
                    p1_hp-=1
                    p1_hp=str(p1_hp)
                if collide_color(screen, p2_hero_p, red):
                    p2_hp=int(p2_hp)
                    p2_hp-=1
                    p2_hp=str(p2_hp)
                screen.blit(sjjx, (p1_x, p1_y))
                screen.blit(sjjx, (p2_x, p2_y))
                screen.blit(p1_hp_text, (50, 0))
                screen.blit(p2_hp_text, (550, 0))
                screen.blit(p1_skills_text, (50, 470))
                screen.blit(p2_skills_text, (550, 470))
                pygame.draw.rect(screen, (255, 0, 0), p1_hero_p, 1)
                pygame.draw.rect(screen, (255, 0, 0), p2_hero_p, 1)
                pygame.draw.rect(screen, (0, 255, 0), p1_hero_s, 1)
                pygame.draw.rect(screen, (0, 255, 0), p2_hero_s, 1)
                if int(p1_hp) <= 0:
                    if a1 == 0:
                        p1_hp = 0
                        now_game_time = 1
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                        a1 = 1
                elif int(p2_hp) <= 0:
                    if a1 == 0:
                        p2_hp = 0
                        now_game_time = 2
                        with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                            file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                        a1 = 1
            elif now_game_time == 1:
                if a == 0:
                    screen.fill((255, 255, 255))
                    screen.blit(p2_win_text, (100, 10))
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p2赢了\n")
                    a = 1
                    then_coins_p2=0
                    with open("./file/coin_p2.txt","r",encoding="utf-8") as file:
                        then_coins_p2=file.read()
                        coins_p211 = str(int(then_coins_p2) +100)
                    with open("./file/coin_p2.txt","w",encoding="utf-8") as file:
                        file.write(coins_p211)
            else:
                if a == 0:
                    screen.fill((255, 255, 255))
                    screen.blit(p1_win_text, (100, 10))
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]p1赢了\n")
                    a = 1
                    then_coins_p1=0
                    with open("./file/coin_p1.txt","r",encoding="utf-8") as file:
                        then_coins_p1=file.read()
                        coins_p111=str(int(then_coins_p1)+100)
                    with open("./file/coin_p1.txt","w",encoding="utf-8") as file:
                        file.write(coins_p111)
            pygame.display.update()
    if game_time==2:
        screen.fill((255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect1.collidepoint(event.pos):
                        game_time=1
                        break
                    if p1_add_blood_rect.collidepoint(event.pos):
                        if int(coins_p11)>=100:
                            with open("./file/coin_p1.txt","r",encoding="utf-8") as file:
                                aaaaaa=file.read()
                            with open("./file/coin_p1.txt","w",encoding="utf-8") as file:
                                file.write(str(int(aaaaaa)-100))
                            with open("./file/p1_hp.txt","r",encoding="utf-8") as file:
                                aa=file.read()
                            with open("./file/p1_hp.txt","w",encoding="utf-8") as file:
                                file.write(str(int(aa)+1))
                    if p2_add_blood_rect.collidepoint(event.pos):
                        if int(coins_p21)>=100:
                            with open("./file/coin_p2.txt","r",encoding="utf-8") as file:
                                aaa=file.read()
                            with open("./file/coin_p2.txt","w",encoding="utf-8") as file:
                                file.write(str(int(aaa)-100))
                            with open("./file/p2_hp.txt","r",encoding="utf-8") as file:
                                aaaaaaa=file.read()
                            with open("./file/p2_hp.txt","w",encoding="utf-8") as file:
                                file.write(str(int(aaaaaaa)+1))
                    if gift_rect.collidepoint(event.pos):
                        gift_tkinter_window()
            if game_time==1:
                break
            screen.fill((255, 255, 255))
            with open("./file/p1_hp.txt", "r", encoding="utf-8") as file:
                p1_hp = file.read()
            with open("./file/p2_hp.txt", "r", encoding="utf-8") as file:
                p2_hp = file.read()
            with open("./file/coin_p1.txt", "r", encoding="utf-8") as file:
                coins_p11 = file.read()
            with open("./file/coin_p2.txt", "r", encoding="utf-8") as file:
                coins_p21 = file.read()
            start_rect1 = pygame.Rect(560, 450, 140, 50)
            p1_word="p1"
            p2_word="p2"
            p2_font=pygame.font.SysFont(None,30)
            p2_text=p2_font.render(p2_word,True,(0,0,0))
            p1_coins_word="p1 coins:"+str(coins_p11)
            p2_coins_word="p2 coins:"+str(coins_p21)
            p1_hp_word="p1 hp:"+p1_hp
            p2_hp_word="p2 hp:"+p2_hp
            p1_hp_font=pygame.font.SysFont(None,50)
            p2_hp_font=pygame.font.SysFont(None,50)
            p1_hp_text=p1_hp_font.render(p1_hp_word,True,(0,0,0))
            p2_hp_text=p2_hp_font.render(p2_hp_word,True,(0,0,0))
            p1_coins_font=pygame.font.SysFont(None,40)
            p2_coins_font=pygame.font.SysFont(None,40)
            p1_font = pygame.font.SysFont(None, 30)
            p1_coins_text=p1_coins_font.render(p1_coins_word,True,(0,0,0))
            p2_coins_text=p2_coins_font.render(p2_coins_word,True,(0,0,0))
            p1_text=p1_font.render(p1_word,True,(0,0,0))
            screen.blit(start,(560,450))
            screen.blit(p1_text,(0,0))
            screen.blit(p2_text,(650,0))
            screen.blit(p1_coins_text,(0,30))
            screen.blit(p2_coins_text,(500,30))
            screen.blit(p1_hp_text,(0,60))
            screen.blit(p2_hp_text,(500,60))
            screen.blit(sjjx,(10,120))
            screen.blit(sjjx,(500,120))
            screen.blit(add_blood,(0,200))
            screen.blit(add_blood, (500, 200))
            screen.blit(gift,(0,450))
            pygame.display.update()
    if game_time == 3:
        screen.fill((255,255,255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open("./game_log/" + time_get + ".txt", "a", encoding="utf-8") as file:
                        file.write("[" + strftime('%Y-%m-%d_%H:%M:%S', localtime(time())) + "]游戏结束\n")
                    pygame.quit()
                    sys.exit()
            pygame.display.update()