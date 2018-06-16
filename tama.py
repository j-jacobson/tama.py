# -*- coding: utf-8 -*-
#has a list of all the tamagotchis, with the last thingy being "create new"

#you pick ur tamagotchi and it has an ascii animal. there are different pictures for what it should be (fat, sleepy, awake, healthy)

#then it says what do you want to do

#then you pick and it says what happened (kinda)

#then you log out, the system checks what time you logged out
#when you log in again, it changes the values of your animal so it looked like time passed when you weren't there

#it should also adjust for how long you are looking at your tamagotchi (so you cant keep it open all day to keep it from dying)

sleep = 100
food = 100
health = 100
fat = 0
emo = 100

name = raw_input('Name your tamagotchi!!!!!: ')
print name, "? Wow what a stupid name!"


def pic():
  print(name)
  print("\n")
  print("""
  
        /`·..
       /,...,`:·
   ¸.·´  ¸   `·.¸.·´)
  : 0 ):´;      ¸  {
   `·.¸ `·  ¸.·´\`·¸)
       `\\´´\¸.·´
  
  
  
  """)
  
 
def stats():

  global food
  global fat
  global sleep
  global health
  global emo
  
  if sleep < 0:
    sleep = 0
    health = health - 10
    
  if food < 0:
    food = 0
    health = health - 10
    fat = fat - 15
    
  if emo < 0:
    emo = 0
    health = health - 10
    fat = fat + 5
  
  if food > 100:
    fat = fat + 5
    health = health - 3
    
  if fat > 80:
    health = health - 5
  
  if fat < 0:
    fat = 0
    health = health - 5
    
  if emo > 100:
    health = health + 1
    
  if sleep > 100:
    health = health - 5
    
  print "Your tamagotchis stats are: \n"
  print "Sleep:",sleep
  print "Food:",food
  print "Healthy:",health
  print "Fat:",fat
  print "Emotion:",emo


def checkup(): 

  if (sleep < 40):
    print("Your tamagotchi is sleepy")
    
  if (food < 40):
    print("Your tamagotchi is hungry")
    
  if (health < 30):
    print("Your tamagotchi is not healthy")
    
  if (fat > 60):
    print("Your tamagotchi is fat.")
    
  if (emo < 40):
    print ("Your tamagotchi is sad.")
  
def do():
  do = raw_input(">>")
  
  global food
  global fat
  global sleep
  global health
  global emo
  
  if(do == "feed"):
    food = food + 15
    fat = fat + 10
    sleep = sleep - 5
    health = health - 2
    
  if(do == "sleep"):
    sleep = sleep + 15
    health = health + 1
    
  if(do == "play"):
    health = health + 12
    fat = fat - 10
    emo = emo + 7
    food = food - 5
    sleep = sleep - 10
    
  else:
    print("no")
    
  health = health - 5
  food = food - 5
  sleep = sleep - 5
  emo = emo - 2
  

while(health > 0):
  pic()
  stats()
  checkup()
  do()
  print("\033[H\033[J")
  

print "Your tamagotchi is dead.\n"
raw_input(">>")
