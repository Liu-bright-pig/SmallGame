# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:15:21 2021

@author: 刘明珠
"""

import pygame
class Girl():
    
    def __init__(self, lg_settings, screen):
        '''初始化girl并设置其初始位置'''
        self.screen = screen
        self.lg_settings = lg_settings
        
        #  加载girl图像并获取其外接矩形
        self.image = pygame.image.load('images/girl.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #  将girl放在屏幕右边中央
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        
        
        #  在girl的属性center中存储小数值
        self.center = float(self.rect.centery)
        
        #  移动标志
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        '''根据移动标志调整girl的位置'''
        #  更新girl的center值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.center -= self.lg_settings.girl_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.lg_settings.girl_speed_factor
            
        #  根据self.center更新rect对象
        self.rect.centery = self.center
        
    def center_girl(self):
        '''girl在屏幕居中'''
        self.center = self.screen_rect.centery
        
        
    def blitme(self):
        '''在指定位置绘制girl'''
        self.screen.blit(self.image, self.rect)
        
        
class Boy():
    
    def __init__(self, lg_settings, screen):
        '''初始化girl并设置其初始位置'''
        self.screen = screen
        self.lg_settings = lg_settings
        
        #  加载girl图像并获取其外接矩形
        self.image = pygame.image.load('images/boy.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #  将boy放在屏幕左边中央
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        
        
        #  在boy的属性center中存储小数值
        self.center = float(self.rect.centery)
        
        #  移动标志
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        '''根据移动标志调整boy的位置'''
        #  更新boy的center值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.center -= self.lg_settings.boy_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.lg_settings.boy_speed_factor
            
        #  根据self.center更新rect对象
        self.rect.centery = self.center
     
    def center_boy(self):
        '''boy在屏幕居中'''
        self.center = self.screen_rect.centery
        
    def blitme(self):
        '''在指定位置绘制boy'''
        self.screen.blit(self.image, self.rect)