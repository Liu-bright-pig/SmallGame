# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:14:12 2021

@author: 刘明珠
"""

class GameStats():
    '''跟踪游戏的统计信息'''
    
    def __init__(self, lg_settings):
        '''初始化统计信息'''
        self.lg_settings = lg_settings
        self.reset_stats()
        #  游戏刚启动处于非活动状态
        self.game_active = False
        #  在任何情况下都不应重置最高得分
        self.girl_high_score = 0
        self.boy_high_score = 0
        
        
    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.girl_left = self.lg_settings.girl_limit
        self.boy_left = self.lg_settings.boy_limit
        self.girl_score = 0
        self.boy_score = 0
        self.level = 1