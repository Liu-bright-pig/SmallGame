# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:11:23 2021

@author: 刘明珠
"""

class Settings():
    '''存储《情侣小游戏》里所有设置的类'''
    
    def __init__(self):
        '''初始化游戏的设置'''
        #  屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        #  girl的设置
        self.girl_speed_factor = 1.5
        self.boy_speed_factor = 1.5
        #  role的初始体力值
        self.girl_limit = 100
        self.boy_limit = 100
        #  heart的恢复体力值设置
        self.heart_points = 10
        #  animal的体力削减值
        self.dog_points = 5
        self.pig_points = 10
        self.cow_points = 15
        
        #  子弹设置
        self.shit_speed_factor = 5
        self.heart_speed_factor = 5
        self.bullets_allowed = 3
        
        #  animal设置
        self.dog_total = 5
        self.pig_total = 3
        self.cow_total = 2
        self.animal_speed_factor = 0.03
        self.fleet_drop_speed = 10
        
        #  加快游戏节奏
        self.speedup_scale = 1.1
        #  animal点数提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.girl_speed_factor = 1.5
        self.boy_speed_factor = 1.5
        self.shit_speed_factor = 3
        self.heart_speed_factor = 3
        self.animal_speed_factor = 0.03
        
        #  记分
        self.dog_points = 10
        self.pig_points = 20
        self.cow_points = 30
        
        
    def increase_speed(self):
        '''提高速度设置'''
        self.girl_speed_factor *= self.speedup_scale
        self.boy_speed_factor *= self.speedup_scale
        self.shit_speed_factor *= self.speedup_scale
        self.heart_speed_factor *= self.speedup_scale
        self.animal_speed_factor *= self.speedup_scale
        
        self.dog_points = int (self.dog_points * self.score_scale)
        self.pig_points = int (self.pig_points * self.score_scale)
        self.cow_points = int (self.cow_points * self.score_scale)
        
        
        