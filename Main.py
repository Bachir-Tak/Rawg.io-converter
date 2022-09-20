from dis import Instruction
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
import time


def send_games(user,mdp) :
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get('https://rawg.io/login');


  time.sleep(2)
  window_before=driver.window_handles[0]
  driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/main/div/div[2]/div[2]/div/div[3]').click()
  time.sleep(3)
  window_after=driver.window_handles[1]
  driver.switch_to.window(window_after)
  elem=driver.find_element(By.XPATH,'//*[@id="username_or_email"]')
  elem.send_keys(user)
  elem=driver.find_element(By.XPATH,'//*[@id="password"]')
  elem.send_keys(mdp)
  driver.find_element(By.XPATH,'//*[@id="allow"]').click()
  driver.switch_to.window(window_before)
  time.sleep(1)
  driver.get('https://rawg.io');
  time.sleep(5)
  game=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/header/div/div[2]/div/form/div[1]/input')
  game.send_keys('te')
  game.submit()
  time.sleep(1)
  game=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/main/div/div/div[1]/div/div[1]/div/input')





  f = open("Games.txt", "r")
  d = open ("Not_Found.txt","a")
  for gm in f:
    game.clear()
    time.sleep(1)
    game.send_keys(gm)
    game.send_keys(Keys.ENTER)
    time.sleep(1)
    try :
      driver.find_element(By.XPATH,'//*[@id="load-more-button"]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button[2]').click()
    except :
      d.write(gm)
    time.sleep(2)

  driver.quit()




root=tk.Tk()
canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=12,rowspan=5)

Instru=tk.Label(root,text="Enter credentials to enter your account : ")
Instru.grid(columnspan=12,column=0,row=0)

text1=tk.Label(root,text="Username : ")
text1.grid(column=5,row=1)
user=tk.Entry(root)
user.grid(column=6,row=1)

text2=tk.Label(root,text="Password : ")
text2.grid(column=5,row=2)
mdp=tk.Entry(root)
mdp.grid(column=6,row=2)

btn=tk.Button(root,text="Connect",bg="#4681f4", fg="white", height=2, width=10, command=lambda:send_games(user.get(),mdp.get()))
btn.grid(columnspan=12,column=0,row=3)

tk.mainloop()