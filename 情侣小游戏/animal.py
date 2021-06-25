# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 21:34:01 2021

@author: 刘明珠
"""

import pygame
from pygame.sprite import Sprite
import random

class Dog(Sprite):
    '''表示单个dog的类'''
    
    def __init__(self, lg_settings, screen):
        '''初始化dog并设置其起始位置'''
        super(Dog, self).__init__()
        self.screen = screen
        self.lg_settings = lg_settings
        
        #  加载dog图像，并设置其rect属性
        self.image = pygame.image.load('images/DOG.bmp')
        self.rect = self.image.get_rect()
        self.image_height = self.image.get_height()
        
        #  设置初始位置
        
        self.rect.x = random.randrange(100, lg_settings.screen_width-100, 10)
        self.rect.y = random.choice((0,lg_settings.screen_height-self.image_height))
        '''
        self.rect.x = lg_settings.screen_width / 2
        self.rect.y = lg_settings.screen_height / 2
        '''
        #  存储dog的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_d = random.randrange(-10,10,2)
        self.y_d = random.randrange(-10,10,2)
        
    def blitme(self):
        '''在指定位置绘制dog'''
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        '''如果animal位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return 1
        elif self.rect.left < screen_rect.left:
            return 2
        elif self.rect.top < screen_rect.top:
            return 3
        elif self.rect.bottom >= screen_rect.bottom:
            return 4
    
    def update(self):
        '''移动dog'''
        self.x += self.lg_settings.animal_speed_factor * self.x_d
        self.y += self.lg_settings.animal_speed_factor * self.y_d
        self.rect.x = self.x
        self.rect.y = self.y
            
class Pig(Sprite):
    '''表示单个dog的类'''
    
    def __init__(self, lg_settings, screen):
        '''初始化pig并设置其起始位置'''
        super(Pig, self).__init__()
        self.screen = screen
        self.lg_settings = lg_settings
        
        #  加载dog图像，并设置其rect属性
        self.image = pygame.image.load('images/PIG.bmp')
        self.rect = self.image.get_rect()
        self.image_height = self.image.get_height()
        
        #  设置初始位置
        
        self.rect.x = random.randrange(100, lg_settings.screen_width-100, 10)
        self.rect.y = random.choice((0,lg_settings.screen_height-self.image_height))
        '''
        self.rect.x = lg_settings.screen_width / 2
        self.rect.y = lg_settings.screen_height / 2
        '''
        #  存储pig的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_d = random.randrange(-10,10,2)
        self.y_d = random.randrange(-10,10,2)
        
    def blitme(self):
        '''在指定位置绘制pig'''
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        '''如果animal位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return 1
        elif self.rect.left < screen_rect.left:
            return 2
        elif self.rect.top < screen_rect.top:
            return 3
        elif self.rect.bottom >= screen_rect.bottom:
            return 4
    
    def update(self):
        '''移动pig'''
        self.x += self.lg_settings.animal_speed_factor * self.x_d
        self.y += self.lg_settings.animal_speed_factor * self.y_d
        self.rect.x = self.x
        self.rect.y = self.y        
        
class Cow(Sprite):
    '''表示单个cow的类'''
    
    def __init__(self, lg_settings, screen):
        '''初始化cow并设置其起始位置'''
        super(Cow, self).__init__()
        self.screen = screen
        self.lg_settings = lg_settings
        
        #  加载dog图像，并设置其rect属性
        self.image = pygame.image.load('images/COW.bmp')
        self.rect = self.image.get_rect()
        self.image_height = self.image.get_height()
        
        #  设置初始位置
        
        self.rect.x = random.randrange(100, lg_settings.screen_width-100, 10)
        self.rect.y = random.choice((0,lg_settings.screen_height-self.image_height))
        '''
        self.rect.x = lg_settings.screen_width / 2
        self.rect.y = lg_settings.screen_height / 2
        '''
        #  存储dog的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_d = random.randrange(-10,10,2)
        self.y_d = random.randrange(-10,10,2)
        
    def blitme(self):
        '''在指定位置绘制cow'''
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        '''如果animal位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return 1
        elif self.rect.left < screen_rect.left:
            return 2
        elif self.rect.top < screen_rect.top:
            return 3
        elif self.rect.bottom >= screen_rect.bottom:
            return 4
    
    def update(self):
        '''移动cow'''
        self.x += self.lg_settings.animal_speed_factor * self.x_d
        self.y += self.lg_settings.animal_speed_factor * self.y_d
        self.rect.x = self.x
        self.rect.y = self.y        
        
        
        
        
        