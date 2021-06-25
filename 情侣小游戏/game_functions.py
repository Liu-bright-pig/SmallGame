# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:08:07 2021

@author: 刘明珠
"""

import sys
import pygame
from time import sleep

from bullet import GShit
from bullet import BShit
from bullet import GHeart
from bullet import BHeart

from animal import Dog
from animal import Pig
from animal import Cow


def check_keydown_events(event, lg_settings, screen, girl, boy, gshits, bshits,
                         ghearts, bhearts):
    '''响应按键'''
    if event.key == pygame.K_UP:
        girl.moving_up = True
    elif event.key == pygame.K_w:
        boy.moving_up = True
    elif event.key == pygame.K_DOWN:
        girl.moving_down = True
    elif event.key == pygame.K_s:
        boy.moving_down = True
    elif event.key == pygame.K_LEFT:
        #  创建一个gshit，并将其加入到编组gshits中
        if len(gshits) < lg_settings.bullets_allowed:
            new_gshit = GShit(lg_settings, screen, girl)
            gshits.add(new_gshit)
    elif event.key == pygame.K_a:
        #  创建一个bshit，并将其加入到编组bshits中
        if len(bshits) < lg_settings.bullets_allowed:
            new_bshit = BShit(lg_settings, screen, boy)
            bshits.add(new_bshit)
    elif event.key == pygame.K_RIGHT:
        #  创建一个gheart，并将其加入到编组gshits中
        if len(ghearts) < lg_settings.bullets_allowed:
            new_gheart = GHeart(lg_settings, screen, girl)
            ghearts.add(new_gheart)
    elif event.key == pygame.K_d:
        #  创建一个bheart，并将其加入到编组bhearts中
        if len(bhearts) < lg_settings.bullets_allowed:
            new_bheart = BHeart(lg_settings, screen, boy)
            bhearts.add(new_bheart)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, girl, boy):
    if event.key == pygame.K_UP:
        girl.moving_up = False
    elif event.key == pygame.K_w:
        boy.moving_up = False
    elif event.key == pygame.K_DOWN:
        girl.moving_down = False
    elif event.key == pygame.K_s:
        boy.moving_down = False

def check_events(lg_settings, screen, stats, gsb, bsb, play_button, girl, boy,
                 dogs, pigs, cows, gshits, bshits,ghearts, bhearts):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, lg_settings, screen, girl, boy,
                                 gshits, bshits, ghearts, bhearts)                    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, girl, boy)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(lg_settings, screen, stats, gsb, bsb, play_button,
                              girl, boy, dogs, pigs, cows, gshits, bshits,
                              ghearts, bhearts, mouse_x, mouse_y)
            
def check_play_button(lg_settings, screen, stats, gsb, bsb, play_button, girl, boy, 
                      dogs, pigs, cows, gshits, bshits, ghearts, bhearts,
                      mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #  重置游戏统计信息
        lg_settings.initialize_dynamic_settings()
        #  隐藏光标
        pygame.mouse.set_visible(False)
        #  重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #  重置记分牌图像
        gsb.prep_score()
        gsb.prep_high_score()
        gsb.prep_level()
        gsb.prep_energy()
        bsb.prep_score()
        bsb.prep_high_score()
        bsb.prep_energy()
        #  清空animal和bullet
        dogs.empty()
        pigs.empty()
        cows.empty()
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        
        #  创建一群新的animal，并让role居中
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        girl.center_girl()
        boy.center_boy()
                
def update_screen(lg_settings, screen, stats, gsb, bsb, girl, boy, dogs, pigs, cows, 
                  gshits, bshits, ghearts, bhearts, play_button):
    '''更新屏幕上的图像，切换到新屏幕'''
    #  每次循环时都重绘屏幕
    screen.fill(lg_settings.bg_color)    
    #  在角色和动物后面重绘所有shit和heart
    for gshit in gshits.sprites():
        gshit.blitme()
    for bshit in bshits.sprites():
        bshit.blitme()
    for gheart in ghearts.sprites():
        gheart.blitme()
    for bheart in bhearts.sprites():
        bheart.blitme()
    girl.blitme()
    boy.blitme()
    dogs.draw(screen)
    pigs.draw(screen)
    cows.draw(screen)
    
    #  显示得分
    gsb.show_score()
    bsb.show_score()
    
    #  如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    #  让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(lg_settings, screen, stats, gsb, bsb, girl, boy,
                   gshits, bshits, ghearts, bhearts, dogs, pigs, cows):
    #  更新子弹位置
    gshits.update()
    bshits.update()
    ghearts.update()
    bhearts.update()
    #  删除已消失的shit
    for gshit in gshits.copy():
         if gshit.rect.left < 0 :
             gshits.remove(gshit)                
    for bshit in bshits.copy():
        if bshit.rect.right > lg_settings.screen_width:
            bshits.remove(bshit)          
    #  删除已消失的heart
    for gheart in ghearts.copy():
        if gheart.rect.left < 0 :
            ghearts.remove(gheart)            
    for bheart in bhearts.copy():
        if bheart.rect.right > lg_settings.screen_width:
            bhearts.remove(bheart)
    check_bullet_animal_collisions(lg_settings, screen, stats, gsb, bsb, 
                                   girl, boy, gshits, bshits, ghearts, bhearts,
                                   dogs, pigs, cows)

def check_high_score(stats, gsb, bsb):
    '''检查是否产生了最高得分'''
    if stats.girl_score > stats.girl_high_score:
        stats.girl_high_score = stats.girl_score
        gsb.prep_high_score()
    if stats.boy_score > stats.boy_high_score:
        stats.boy_high_score = stats.boy_score
        bsb.prep_high_score()

def check_bullet_animal_collisions(lg_settings, screen, stats, gsb, bsb, 
                                   girl, boy, gshits, bshits, ghearts, bhearts,
                                   dogs, pigs, cows):            
    #  检查是否有bullet击中animal
    #  如果是这样，就删除相应的bullet和animal
    gs_d_collisions = pygame.sprite.groupcollide(gshits, dogs, True, True)
    bs_d_collisions = pygame.sprite.groupcollide(bshits, dogs, True, True)
    gs_p_collisions = pygame.sprite.groupcollide(gshits, pigs, True, True)
    bs_p_collisions = pygame.sprite.groupcollide(bshits, pigs, True, True)
    gs_c_collisions = pygame.sprite.groupcollide(gshits, cows, True, True)
    bs_c_collisions = pygame.sprite.groupcollide(bshits, cows, True, True)
    '''
    gh_d_collisions = pygame.sprite.groupcollide(ghearts, dogs, False, True)
    bh_d_collisions = pygame.sprite.groupcollide(bhearts, dogs, False, True)
    gh_p_collisions = pygame.sprite.groupcollide(ghearts, pigs, False, True)
    bh_p_collisions = pygame.sprite.groupcollide(bhearts, pigs, False, True)
    gh_c_collisions = pygame.sprite.groupcollide(ghearts, cows, False, True)
    bh_c_collisions = pygame.sprite.groupcollide(bhearts, cows, False, True)
    '''
    gh_b_collisions = pygame.sprite.spritecollideany(boy, ghearts)
    bh_g_collisions = pygame.sprite.spritecollideany(girl, bhearts)
    
    if gs_d_collisions:
        stats.girl_score += lg_settings.dog_points
        gsb.prep_score()
        check_high_score(stats, gsb, bsb)
    if bs_d_collisions:
        stats.boy_score += lg_settings.dog_points
        bsb.prep_score()
    if gs_p_collisions:
        stats.girl_score += lg_settings.pig_points
        gsb.prep_score()
    if bs_p_collisions:
        stats.boy_score += lg_settings.pig_points
        bsb.prep_score()
    if gs_c_collisions:
        stats.girl_score += lg_settings.cow_points
        gsb.prep_score()
    if bs_c_collisions:
        stats.boy_score += lg_settings.cow_points
        bsb.prep_score()
    '''
    if gh_d_collisions:
        stats.girl_score += lg_settings.dog_points
        gsb.prep_score()
        check_high_score(stats, gsb, bsb)
    if bh_d_collisions:
        stats.boy_score += lg_settings.dog_points
        bsb.prep_score()
    if gh_p_collisions:
        stats.girl_score += lg_settings.pig_points
        gsb.prep_score()
    if bh_p_collisions:
        stats.boy_score += lg_settings.pig_points
        bsb.prep_score()
    if gh_c_collisions:
        stats.girl_score += lg_settings.cow_points
        gsb.prep_score()
    if bh_c_collisions:
        stats.boy_score += lg_settings.cow_points
        bsb.prep_score()
    '''
    
    if gh_b_collisions:
        if pygame.sprite.collide_circle_ratio(0.65)(boy,gh_b_collisions):
                stats.girl_left += lg_settings.heart_points
                ghearts.remove(gh_b_collisions)
        if stats.girl_left > 100:
            stats.girl_left = 100
        gsb.prep_energy()
    if bh_g_collisions:
        if pygame.sprite.collide_circle_ratio(0.65)(girl,bh_g_collisions):
                stats.boy_left += lg_settings.heart_points
                bhearts.remove(bh_g_collisions)
        if stats.boy_left > 100:
            stats.boy_left = 100
        bsb.prep_energy()
    
    if len(dogs)==0 and len(pigs)==0 and len(cows)==0:
        #  如果整群animal都消灭，就提高一个等级
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        lg_settings.increase_speed()
        
        #  提高等级
        stats.level += 1
        gsb.prep_level()
        
        create_fleet(lg_settings, screen, dogs, pigs, cows)
    
    
def create_fleet(lg_settings, screen, dogs, pigs, cows):
    '''创建animal群'''
    #  随机创建animal
    dog = Dog(lg_settings, screen)
    pig = Pig(lg_settings, screen)
    cow = Cow(lg_settings, screen)
    #  创建animal群
    for dog_number in range(lg_settings.dog_total):
        dog = Dog(lg_settings, screen)
        dogs.add(dog)
    for pig_number in range(lg_settings.pig_total):
        pig = Pig(lg_settings, screen)
        pigs.add(pig)
    for cow_number in range(lg_settings.cow_total):
        cow = Cow(lg_settings, screen)
        cows.add(cow)


def check_fleet_edges(lg_settings, dogs, pigs, cows):
    '''animal到达边缘时应采取相应措施'''
    for dog in dogs.sprites():
        if dog.check_edges()==1 or dog.check_edges()==2:
            dog.x_d *= -1
        elif dog.check_edges()==3 or dog.check_edges()==4:
            dog.y_d *= -1
    for pig in pigs.sprites():
        if pig.check_edges()==1 or pig.check_edges()==2:
            pig.x_d *= -1
        elif pig.check_edges()==3 or pig.check_edges()==4:
            pig.y_d *= -1
    for cow in cows.sprites():
        if cow.check_edges()==1 or cow.check_edges()==2:
            cow.x_d *= -1
        elif cow.check_edges()==3 or cow.check_edges()==4:
            cow.y_d *= -1


def girl_dog_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被dog撞到的girl'''
    if stats.girl_left > 0:
        #  将girl_left减10
        stats.girl_left -= lg_settings.dog_points
        gsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        dogs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        girl.center_girl()
        girl.update()
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def boy_dog_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被dog撞到的boy'''
    if stats.boy_left > 0:
        #  将girl_left减10
        stats.boy_left -= lg_settings.dog_points
        bsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        dogs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        boy.center_boy()
        boy.update()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def girl_pig_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被pig撞到的girl'''
    if stats.girl_left > 0:
        #  将girl_left减20
        stats.girl_left -= lg_settings.pig_points
        gsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        pigs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        girl.center_girl()
        girl.update()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def boy_pig_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被pig撞到的boy'''
    if stats.boy_left > 0:
        #  将boy_left减20
        stats.boy_left -= lg_settings.pig_points
        bsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        dogs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        boy.center_boy()
        boy.update()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def girl_cow_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被cow撞到的girl'''
    if stats.girl_left > 0:
        #  将girl_left减30
        stats.girl_left -= lg_settings.cow_points
        gsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        dogs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        girl.center_girl()
        girl.update()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def boy_cow_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts):
    '''响应被cow撞到的boy'''
    if stats.boy_left > 0:
        #  将boy_left减10
        stats.boy_left -= lg_settings.cow_points
        bsb.prep_energy()
        #  清空bullet和animal
        gshits.empty()
        bshits.empty()
        ghearts.empty()
        bhearts.empty()
        dogs.empty()
        #  创建新的animal,并将role放到中间
        create_fleet(lg_settings, screen, dogs, pigs, cows)
        boy.center_boy()
        boy.update()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def update_animals(lg_settings,stats, screen, gsb, bsb, girl, boy, dogs, pigs, cows,
                   gshits, bshits, ghearts, bhearts):
    '''检查是否有animal位于屏幕边缘，更新animal位置''' 
    #dogs.update()
    check_fleet_edges(lg_settings, dogs, pigs, cows)
    dogs.update()
    pigs.update()
    cows.update()
    
    #  检测animal和role之间的碰撞
    if pygame.sprite.spritecollideany(girl, dogs):
        print(stats.girl_left)
        girl_dog_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)
    elif pygame.sprite.spritecollideany(boy, dogs):
        print(stats.boy_left)
        boy_dog_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)
    elif pygame.sprite.spritecollideany(girl, pigs):
        print(stats.girl_left)
        girl_pig_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)
    elif pygame.sprite.spritecollideany(boy, pigs):
        print(stats.boy_left)
        boy_pig_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)
    elif pygame.sprite.spritecollideany(girl, cows):
        print(stats.girl_left)
        girl_cow_hit(lg_settings, stats, screen, gsb, girl, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)
    elif pygame.sprite.spritecollideany(boy, cows):
        print(stats.boy_left)
        boy_cow_hit(lg_settings, stats, screen, bsb, boy, dogs, pigs, cows,
                 gshits, bshits, ghearts, bhearts)


        
    
    
    
    
    
    