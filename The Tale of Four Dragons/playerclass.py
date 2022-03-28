##This file contains the class data for the player##

from tkinter import *
from tkinter import PhotoImage
from time import sleep

leveluprequirements = [50,200,400,600,750,1000,1500,2000,3000,10000] #10000 exists for list index

class Player():
    def __init__(self, hp = 100, maxhp = 100, magic = 100, maxmagic = 100, weapon = 'None', exp = 0, level = 1, money = 0):
        self.hp = hp
        self.maxhp = maxhp
        self.magic = magic
        self.maxmagic = maxmagic
        self.weapon = weapon
        self.exp = exp
        self.level = level
        self.money = money
    
    def addexp(self, exp):
        self.exp += exp
        for i in range(10):
            if self.exp >= leveluprequirements[self.level-1] and self.level < 10:
                self.level += 1

    def takedamage(self, basedamage):
        self.hp -= (basedamage - (5*self.level))
        if self.hp < 0:
            self.hp = 0

    def heal(self, hp):
        self.hp += hp
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def usemagic(self, magic):
        self.magic -= magic
        if self.magic < 0:
            self.magic = 0

    def magicrestore(self,magic):
        self.magic += magic
        if self.magic > self.maxmagic:
            self.magic = self.maxmagic

    def changeweapon(self, newweapon):
        self.weapon = newweapon

    def boostmaxhp(self, increase):
        self.maxhp += increase

    def boostmaxmagic(self, increase):
        self.maxmagic += increase

    def levelup(self):
        self.maxhp += 50
        player.hp += 10000
        player.magic += 10000

    def addmoney(self,money):
        self.money += money
        if self.money > 9999:
            self.money = 9999

    def spendmoney(self,money):
        self.money -= money
        if self.money < 0:
            self.money = 0
