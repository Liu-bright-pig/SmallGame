# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:53:50 2021

@author: 刘明珠
"""

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import GScoreboard
from scoreboard import BScoreboard
from button import Button
from role import Girl
from role import Boy
from animal import Dog
import game_functions as gf

def run_game():
    #  初始化pygame、设置和屏幕对象
    pygame.init()
    lg_settings = Settings()
    screen = pygame.display.set_mode(
            (lg_settings.screen_width, lg_settings.screen_height))
    pygame.display.set_caption("Lovers Games")
    
    #  创建Play按钮
    play_button = Button(lg_settings, screen, "Play")
    
    #  创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(lg_settings)
    gsb = GScoreboard(lg_settings, screen, stats)
    bsb = BScoreboard(lg_settings, screen, stats)
    
    #  设置背景色
    bg_color = (230, 230, 230)
    
    #  创建用于存储roles、animals、bullets的编组
    girl = Girl(lg_settings, screen) 
    boy = Boy(lg_settings, screen)
    
    gshits = Group()
    bshits = Group()
    ghearts = Group()
    bhearts = Group()
    
    dogs = Group()
    pigs = Group()
    cows = Group()
    
    
    #  创建animal群
    gf.create_fleet(lg_settings, screen, dogs, pigs, cows)
    
    #  开始游戏的主循环
    while True:
        
        gf.check_events(lg_settings, screen, stats, gsb, bsb, play_button, girl, boy, 
                        dogs, pigs, cows, gshits, bshits,ghearts, bhearts)
        if stats.game_active:
            girl.update()
            boy.update()        
            gf.update_bullets(lg_settings, screen, stats, gsb, bsb, girl, boy, 
                              gshits, bshits, ghearts, bhearts, dogs, pigs, cows)
            gf.update_animals(lg_settings, stats, screen, gsb, bsb, girl, boy, dogs, pigs, cows,
                               gshits, bshits, ghearts, bhearts)        
        
        gf.update_screen(lg_settings, screen, stats, gsb, bsb, girl, boy, dogs, pigs, cows,
                         gshits, bshits, ghearts, bhearts, play_button)        
        
        
run_game()