# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:54:48 2021

@author: 刘明珠
"""

import pygame.font

class GScoreboard():
    '''显示得分信息的类'''
    
    def __init__(self, lg_settings, screen, stats):
        '''初始化得分信息涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.lg_settings = lg_settings
        self.stats = stats
        
        #  显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #  准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_energy()
        
    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = int(round(self.stats.girl_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.lg_settings.bg_color)
        
        #  将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        '''将最高得分转换为一幅渲染的图像'''
        high_score = int(round(self.stats.girl_high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color,self.lg_settings.bg_color)
        
        #  将最高分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 200
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        '''将等级转换为渲染的图像'''
        self.level_image = self.font.render(str(self.stats.level), True,
                                self.text_color, self.lg_settings.bg_color)
        #  将等级放在中间
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_energy(self):
        '''将体力值转换为一幅渲染的图像'''
        energy_left = int(round(self.stats.girl_left, -1))
        energy_str = "{:,}".format(energy_left)
        self.energy_image = self.font.render(energy_str, True, self.text_color,
                                            self.lg_settings.bg_color)
        
        #  将体力值放在屏幕右下角
        self.energy_rect = self.energy_image.get_rect()
        self.energy_rect.right = self.screen_rect.right - 20
        self.energy_rect.bottom = self.screen_rect.bottom - 20
    
    def show_score(self):
        '''在屏幕上显示得分和最高得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.energy_image, self.energy_rect)

        
class BScoreboard():
    '''显示得分信息的类'''
    
    def __init__(self, lg_settings, screen, stats):
        '''初始化得分信息涉及的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.lg_settings = lg_settings
        self.stats = stats
        
        #  显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #  准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_energy()
        
    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = int(round(self.stats.boy_score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.lg_settings.bg_color)
        
        #  将得分放在屏幕左上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20
     
    def prep_high_score(self):
        '''将最高得分转换为一幅渲染的图像'''
        high_score = int(round(self.stats.boy_high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color,self.lg_settings.bg_color)
        
        #  将最高分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 200
        self.high_score_rect.top = self.score_rect.top    
    
    def prep_energy(self):
        '''将体力值转换为一幅渲染的图像'''
        energy_left = int(round(self.stats.boy_left, -1))
        energy_str = "{:,}".format(energy_left)
        self.energy_image = self.font.render(energy_str, True, self.text_color,
                                            self.lg_settings.bg_color)
        
        #  将体力值放在屏幕左下角
        self.energy_rect = self.energy_image.get_rect()
        self.energy_rect.left = self.screen_rect.left + 20
        self.energy_rect.bottom = self.screen_rect.bottom - 20
    
    def show_score(self):
        '''在屏幕上显示得分和最高得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.energy_image, self.energy_rect)