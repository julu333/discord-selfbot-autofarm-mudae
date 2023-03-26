import discum    
bot = discum.Client(token='token', log=True)

import time
import random

SalonAFarm = SAF = '930144477891428422'

while True:
    for _ in range(10):
    
        options = [7231, 7348, 7412, 7563, 7301] # Liste des options
        choix = random.choice(options)
    
        bot.sendMessage("SAF", "$p")
        time.sleep(choix)
        
        
    options2 = [1, 3, 6]
    choix2 = random.choice(options2)
    
    bot.sendMessage("SAF", "$dk")
    time.sleep(choix2)
    
    
    options3 = [65, 94, 140]
    choix3 = random.choice(options3)
    
    bot.sendMessage("SAF", "$daily")
    time.sleep(choix3)