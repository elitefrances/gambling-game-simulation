# -*- coding: utf-8 -*-

import random
import pandas as pd
import time
'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
10位玩家，赌本10元，进行100轮。
'''

sample_list = []
round_num = 100
person_num = 10
for person in range(1,person_num+1):
    gambling_money = 10
    for r in range(1,round_num+1):
        coin = random.randint(0, 1) # 0为正，1为反
        if coin == 0 :
            gambling_money = gambling_money + 1
        elif coin == 1 :
            gambling_money = gambling_money - 1
        if gambling_money == 0 :
            sample_list.append([person,r,gambling_money])
            break
        else:
            pass
    sample_list.append([person,r,gambling_money])
    
sample_data1 = pd.DataFrame(sample_list,columns=['person','round','gambling_money'])
sample_data1.to_csv('./十元赌本进行100轮游戏.csv',index=0)        



'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
100位玩家，赌本10元，进行1000轮。
'''

sample_list = []
round_num = 1000
person_num = 100
for person in range(1,person_num+1):
    gambling_money = 10
    for r in range(1,round_num+1):
        coin = random.randint(0, 1) # 0为正，1为反
        if coin == 0 :
            gambling_money = gambling_money + 1
        elif coin == 1 :
            gambling_money = gambling_money - 1
        if gambling_money == 0 :
            sample_list.append([person,r,gambling_money])
            break
        else:
            pass
    sample_list.append([person,r,gambling_money])
sample_data2 = pd.DataFrame(sample_list,columns=['person','round','gambling_money'])
sample_data2.to_csv('./十元赌本进行1000轮游戏.csv',index=0)


'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
100位玩家，赌本10元，进行无限轮，直到破产。
'''

sample_list = []
person_num = 100
t1 = time.time()
for person in range(1,person_num+1):
    gambling_money = 10
    r = 0
    while gambling_money > 0 :
        r += 1
        print('进行第{}轮游戏'.format(r))
        coin = random.randint(0, 1) # 0为正，1为反
        if coin == 0 :
            gambling_money = gambling_money + 1
        elif coin == 1 :
            gambling_money = gambling_money - 1
        if gambling_money == 0 :
            sample_list.append([person,r,gambling_money])
            break
        else:
            pass
t2 = time.time()
t = round(t2 - t1,2)
print(t,'秒')    
sample_data3 = pd.DataFrame(sample_list,columns=['person','round','gambling_money'])
sample_data3.to_csv('./十元赌本进行无限轮游戏.csv',index=0)


'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
100000位玩家，赌本10元，庄家赌本10元，对赌，直到一方破产。
'''

sample_list = []
person_num = 100000
for person in range(1,person_num+1):
    gambling_money_dealer = 10
    gambling_money_player = 10
    r = 0
    while 1:
        r += 1
        print('第{}位玩家,进行第{}轮游戏'.format(person,r))
        coin = random.randint(0, 1) # 0为正，1为反
        if coin == 0 :
            gambling_money_player = gambling_money_player + 1
            gambling_money_dealer = gambling_money_dealer - 1
        elif coin == 1 :
            gambling_money_player = gambling_money_player - 1
            gambling_money_dealer = gambling_money_dealer + 1
        if (gambling_money_player == 0) or (gambling_money_dealer ==0):
            sample_list.append([person,gambling_money_dealer,gambling_money_player,r])
            break
sample_data4 = pd.DataFrame(sample_list,columns=['person','dealer','player','round'])
sample_data4.to_csv('./庄家和闲家各十元赌本对赌直到一方破产.csv',index=0)


'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
100000位玩家，赌本10元，庄家赌本20元，对赌，直到一方破产。
''' 

sample_list = []
person_num = 100000
for person in range(1,person_num+1):
    gambling_money_dealer = 20
    gambling_money_player = 10
    r = 0
    while 1:
        r += 1
        print('第{}位玩家,进行第{}轮游戏'.format(person,r))
        coin = random.randint(0, 1) # 0为正，1为反
        if coin == 0 :
            gambling_money_player = gambling_money_player + 1
            gambling_money_dealer = gambling_money_dealer - 1
        elif coin == 1 :
            gambling_money_player = gambling_money_player - 1
            gambling_money_dealer = gambling_money_dealer + 1
        if (gambling_money_player == 0) or (gambling_money_dealer ==0):
            sample_list.append([person,gambling_money_dealer,gambling_money_player,r])
            break
sample_data5 = pd.DataFrame(sample_list,columns=['person','dealer','player','round'])
sample_data5.to_csv('./庄家二十元赌本和闲家十元赌本对赌直到一方破产.csv',index=0)          


'''
抛硬币游戏：
抛硬币，正反两面概率各50%，正面你赢，反面庄家赢。
玩家获胜，庄家会抽取2%作为抽成。
模拟100W轮
'''

sample_list = []
gambling_money_dealer = 0
gambling_money_player = 0
for i in range(1,1000000+1):
    print('正在进行第{}轮游戏'.format(i))
    coin = random.randint(0, 1) # 0为正，1为反
    if coin == 0 :
        gambling_money_player = gambling_money_player + 0.98
        gambling_money_dealer = gambling_money_dealer - 0.98
    elif coin == 1 :
        gambling_money_player = gambling_money_player - 1
        gambling_money_dealer = gambling_money_dealer + 1
    sample_list.append([i,gambling_money_dealer,gambling_money_player])
sample_data6 = pd.DataFrame(sample_list,columns=['round','dealer','player'])
sample_data6.to_csv('./庄家抽取2%抽成.csv',index=0)
    
        
    
    




















        
        
