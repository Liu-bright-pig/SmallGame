# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:19:59 2021

@author: 刘明珠
"""

import pygame
from pygame.sprite import Sprite

class GShit(Sprite):
    '''对girl发出的shit进行管理的类'''
    
    def __init__(self, lg_settings, screen, girl):
        '''在girl所在位置创建一个shit对象'''
        super(GShit, self).__init__()
        self.screen = screen
        #  加载shit图像并获取其外接矩形
        self.image = pygame.image.load('images/shit.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #  设置位置
        self.rect.centery = girl.rect.centery
        self.rect.right = girl.rect.right
        #  存储用小数表示的位置
        self.x = float(self.rect.x)
        
        self.speed_factor = lg_settings.shit_speed_factor
        
        
    def update(self):
        '''girl向左移动子弹'''
        #  更新表示shit位置的小数值
        self.x -= self.speed_factor
        #  更新shit的位置
        self.rect.x = self.x
        
        
    def blitme(self):
        '''在指定位置绘制shit'''
        self.screen.blit(self.image, self.rect)


class BShit(Sprite):
    '''对boy发出的shit进行管理的类'''
    
    def __init__(self, lg_settings, screen, boy):
        '''在girl所在位置创建一个shit对象'''
        super(BShit, self).__init__()
        self.screen = screen
        #  加载shit图像并获取其外接矩形
        self.image = pygame.image.load('images/shit.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #  设置位置
        self.rect.centery = boy.rect.centery
        self.rect.left = boy.rect.left
        #  存储用小数表示的位置
        self.x = float(self.rect.x)
        
        self.speed_factor = lg_settings.shit_speed_factor
        
        
    def update(self):
        '''boy向右移动子弹'''
        #  更新表示shit位置的小数值
        self.x += self.speed_factor
        #  更新shit的位置
        self.rect.x = self.x
        
        
    def blitme(self):
        '''在指定位置绘制shit'''
        self.screen.blit(self.image, self.rect)    
        
class GHeart(Sprite):
    '''对girl发出的heart进行管理的类'''
    
    def __init__(self, lg_settings, screen, girl):
        '''在girl所在位置创建一个heart对象'''
        super(GHeart, self).__init__()
        self.screen = screen
        #  加载heart图像并获取其外接矩形
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #  设置位置
        self.rect.centery = girl.rect.centery
        self.rect.right = girl.rect.right
        #  存储用小数表示的位置
        self.x = float(self.rect.x)
        
        self.speed_factor = lg_settings.heart_speed_factor
        
        
    def update(self):
        '''girl向左移动子弹'''
        #  更新表示heart位置的小数值
        self.x -= self.speed_factor
        #  更新heart的位置
        self.rect.x = self.x
        
        
    def blitme(self):
        '''在指定位置绘制shit'''
        self.screen.blit(self.image, self.rect)


class BHeart(Sprite):
    '''对boy发出的heart进行管理的类'''
    
    def __init__(self, lg_settings, screen, boy):
        '''在girl所在位置创建一个shit对象'''
        super(BHeart, self).__init__()
        self.screen = screen
        #  加载heart图像并获取其外接矩形
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #  设置位置
        self.rect.centery = boy.rect.centery
        self.rect.left = boy.rect.left
        #  存储用小数表示的位置
        self.x = float(self.rect.x)
        
        self.speed_factor = lg_settings.heart_speed_factor
        
        
    def update(self):
        '''boy向右移动子弹'''
        #  更新表示heart位置的小数值
        self.x += self.speed_factor
        #  更新heart的位置
        self.rect.x = self.x
        
        
    def blitme(self):
        '''在指定位置绘制shit'''
        self.screen.blit(self.image, self.rect)