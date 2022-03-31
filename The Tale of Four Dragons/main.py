##startup##
from tkinter import *
from tkinter import PhotoImage
from time import sleep
from math import *
from playerclass import Player
import json
from random import randint
print('''Do not close this window.
You may minimise it, but closing it will result in exiting the game.''')
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

##menu setup##
onmenu = True
selected = ''

##window setup##
window = Tk()
window.title('The Tale of Four Dragons')
c = Canvas(window, width = 1005, height = 690, bg = 'green')
c.pack()
window.iconbitmap('icon.ico')

##menu display##
logoimg = PhotoImage(file = 'Graphics/Logo.gif')
logoimg = logoimg.zoom(3)
logoimg = logoimg.subsample(2)
logo = c.create_image(202.5,5,image = logoimg, anchor = 'nw')

newgametext = c.create_text(330,570,fill='black',font='Times 30',text='New Game')
continuetext = c.create_text(675,570,fill='black',font='Times 30',text='Continue')

blackcursorimg = PhotoImage(file = 'Graphics/Cursor_black.gif')
blackcursor = c.create_image(195,555,image = blackcursorimg, anchor = 'nw')


##setup main screen##
overworldmapimg = PhotoImage(file = 'Graphics/OverworldMap.gif')
whitecursorgraphic = PhotoImage(file = 'Graphics/Cursor_white.gif')

def drawmainscreen():
    overworldmap = c.create_image(150,0, image = overworldmapimg, anchor = 'nw')
    c.create_rectangle(0,0,150,690,fill='black',outline='white')
    c.create_rectangle(555,0,705,690,fill='black',outline='white')
    c.create_rectangle(705,0,855,690,fill='black',outline='white')
    c.create_rectangle(855,0,1005,690,fill='black',outline='white')
    c.create_rectangle(0,540,555,615,fill='black',outline='white')
    c.create_rectangle(0,615,555,690,fill='black',outline='white')
    c.create_line(555,30,1005,30,fill='white')
    c.create_polygon(75,155,35,235,75,315,115,235,fill='black',outline='white')
    c.create_polygon(75,135,65,155,75,175,85,155,fill='black',outline='white')
    c.create_polygon(35,215,25,235,35,255,45,235,fill='black',outline='white')
    c.create_polygon(75,295,65,315,75,335,85,315,fill='black',outline='white')
    c.create_polygon(115,215,105,235,115,255,125,235,fill='black',outline='white')
    c.create_polygon(75,220,65,230,55,220,55,250,95,250,95,220,85,230,fill='black',outline='white')
    c.create_polygon(45,380,30,445,45,510,105,510,120,445,105,380,fill='black',outline='white')
    c.create_line(105,380,45,380,fill='black')
    c.create_oval(35,370,55,390,fill='black',outline='white')
    c.create_oval(20,435,40,455,fill='black',outline='white')
    c.create_oval(35,500,55,520,fill='black',outline='white')
    c.create_oval(95,500,115,520,fill='black',outline='white')
    c.create_oval(110,435,130,455,fill='black',outline='white')
    c.create_oval(95,370,115,390,fill='black',outline='white')
    c.create_polygon(70,495,80,495,80,470,85,470,90,465,80,465,80,380,75,350,70,380,70,465,60,465,65,470,70,470,fill='black',outline='white')

##run menu##
def moveblackcursor(event):
    global selected, onmenu
    blackcursorx, blackcursory = c.coords(blackcursor)
    if onmenu == True and blackcursorx == 195 and event.keysym == 'Right':
        c.coords(blackcursor, 555, 555)
    elif onmenu == True and blackcursorx == 555 and event.keysym == 'Left':
        c.coords(blackcursor, 195, 555)
    
    elif onmenu == True and blackcursorx == 195 and event.keysym == 'z':
        onmenu = False
        selected = 'New Game'
    elif onmenu == True and blackcursorx == 555 and event.keysym == 'z':
        onmenu = False
        selected = 'Continue'

c.bind_all('<Key>',moveblackcursor)

while True:
    window.update()
    if selected == 'Continue':
        window.destroy() #test
        print('You selected ' + selected) #test
    elif selected == 'New Game':
        c.itemconfig(newgametext, state = 'hidden')
        c.itemconfig(continuetext, state = 'hidden')
        c.itemconfig(blackcursor, state = 'hidden')
        nameentry = Entry(window)
        nameentry.place(x = 402.5, y = 570, width = 200, height = 20)
        window.update()
        name = ''
        def nameentered():
            global name
            name = nameentry.get()
            nameentry.destroy()
        gobutton = Button(window, activeforeground = 'lightgreen', command = nameentered, text = 'Name set, let\'s go!')
        gobutton.place(x = 452.5, y = 600, width = 100, height = 15)
        while name == '':
            sleep(0.01)
            window.update()
        gobutton.destroy()
        drawmainscreen()
        break
    sleep(0.05)

c.unbind('<Key>')

##text display functions##
textboxline1 = c.create_text(10,540,fill = 'white', font = 'Times 15', text = 'test line 1', anchor = 'nw')
textboxline2 = c.create_text(10,565,fill = 'white', font = 'Times 15', text = 'test line 2', anchor = 'nw')
textboxline3 = c.create_text(10,590,fill = 'white', font = 'Times 15', text = 'test line 3', anchor = 'nw')
def chatbox(message=['Line 1','Line 2','Line 3']):
    c.itemconfig(textboxline1,text = '')
    c.itemconfig(textboxline2,text = '')
    c.itemconfig(textboxline3,text = '')
    text = ''
    for char in str(message[0]):
        text += char
        c.itemconfig(textboxline1,text = text)
        window.update()
        sleep(0.01)
    text = ''
    for char in str(message[1]):
        text += char
        c.itemconfig(textboxline2,text = text)
        window.update()
        sleep(0.01)
    text = ''
    for char in str(message[2]):
        text += char
        c.itemconfig(textboxline3,text = text)
        window.update()
        sleep(0.01)
        
popupbox = c.create_rectangle(150,510,555,540, fill='black',outline='white',state = 'hidden')
popuptext = c.create_text(160,515,fill = 'white', font = 'Times 15', text = 'Something happened', anchor = 'nw',state = 'hidden')
def popup(displaytext):
    c.itemconfig(popupbox,state='normal')
    c.itemconfig(popuptext,state='normal')
    c.tag_raise(popupbox)
    c.tag_raise(popuptext)
    text = ''
    for char in str(displaytext):
        text += char
        c.itemconfig(popuptext,text = text)
        window.update()
        sleep(0.01)
    sleep(0.8)
    c.itemconfig(popupbox,state='hidden')
    c.itemconfig(popuptext,state='hidden')

##player setup##
player = Player()
playergroundimg = PhotoImage(file = 'Graphics/Player.gif')
playerboatimg = PhotoImage(file = 'Graphics/Player_boat.gif')
playerballoonimg = PhotoImage(file = 'Graphics/Player_balloon.gif')
playertornadoimg = PhotoImage(file = 'Graphics/Player_tornado.gif')
playergraphic = c.create_image(165,285,image = playergroundimg, anchor = 'nw')
def move_player(x,y,steps = 30,secs = 1):
    movex = x / steps
    movey = y / steps
    delay = secs / steps
    for i in range(steps):
        c.move(playergraphic,movex,movey)
        window.update()
        sleep(delay)
def change_player_graphic(image):
    c.itemconfig(playergraphic,image = image)

##stat display##
c.create_text(75,15,fill = 'white', font = 'Times 15', text = name)
c.create_text(10,30,fill = 'white', font = 'Times 10',text='LV', anchor = 'w')
c.create_text(10,50,fill = 'white', font = 'Times 10',text='HP', anchor = 'w')
c.create_text(10,70,fill = 'white', font = 'Times 10', text = 'Magic', anchor = 'w')
c.create_text(10,90,fill = 'white', font = 'Times 10', text = 'EXP', anchor = 'w')
c.create_text(630,15,fill = 'white', font = 'Times 15', text = 'Inventory')
c.create_text(780,15,fill = 'white', font = 'Times 15', text = 'Spells')
c.create_text(930,15,fill = 'white', font = 'Times 15', text = 'Weapons')
c.create_text(10,110,fill = 'white', font = 'Times 10', text = 'Weapon', anchor = 'w')
c.create_text(10,130,fill = 'white', font = 'Times 10', text = 'Money', anchor = 'w')
leveltext = c.create_text(140,25,fill = 'white',font = 'Times 10',text='1',anchor='ne')
hptext = c.create_text(140,45,fill = 'white',font = 'Times 10',text='100/100',anchor='ne')
magictext = c.create_text(140,65,fill = 'white', font = 'Times 10', text = '100/100',anchor='ne')
exptext = c.create_text(140,85,fill='white', font = 'Times 10', text = '0', anchor='ne')
weapontext = c.create_text(140,105,fill='white', font = 'Times 10', text = 'None', anchor='ne')
moneytext = c.create_text(140,125,fill='white',font='Times 10', text='0G',anchor='ne')

def update_stats():
    c.itemconfig(leveltext, text = player.level)
    c.itemconfig(hptext, text = str(player.hp) + '/' + str(player.maxhp))
    c.itemconfig(magictext, text = str(player.magic) + '/' + str(player.maxmagic))
    c.itemconfig(exptext, text = player.exp)
    c.itemconfig(weapontext, text = player.weapon)
    c.itemconfig(moneytext, text = str(player.money) + 'G')


##inventory##
inventory = []
spells = []
spellcosts = []
weapons = []

def addtoinv(item):
    if item not in inventory:
        inventory.append(item)
        c.create_text(650, (len(inventory)*30)+10, fill = 'white', font = 'Times 10', text = item, anchor = 'n')
        update_stats()
    else:
        popup('You already have this!')

def addtospells(item, itemcost):
    if item not in spells:
        spells.append(item)
        spellcosts.append(itemcost)
        c.create_text(800, (len(spells)*30)+10, fill = 'white', font = 'Times 10', text = item + ' - ' + str(itemcost), anchor = 'n')
        update_stats()
    else:
        popup('You already have this!')

def addtoweapons(item):
    if item not in weapons:
        weapons.append(item)
        c.create_text(950, (len(weapons)*30)+10, fill = 'white', font = 'Times 10', text = item, anchor = 'n')
        update_stats()
    else:
        popup('You already have this!')
        

def equipweapon(item):
    if item in weapons:
        player.changeweapon(item)
        update_stats()
        popup('You equipped the ' + item + '.')

##get player choice##
option = 0
chosen = ''
row = 0
column = 0
def getplayerchoice(options = ['---','---','---','---','---','---']):
    global option, chosen, row, column
    op1text = c.create_text(40,625, fill='white',font = 'Times 20',text = options[0], anchor = 'nw')
    op2text = c.create_text(40,650, fill='white', font = 'Times 20', text = options[1], anchor = 'nw')
    op3text = c.create_text(277.5, 625, fill='white',font='Times 20', text = options[2], anchor = 'n')
    op4text = c.create_text(277.5, 650, fill='white', font = 'Times 20', text = options[3], anchor = 'n')
    op5text = c.create_text(545, 625, fill='white', font = 'Times 20', text = options[4], anchor = 'ne')
    op6text = c.create_text(545, 650, fill='white', font = 'Times 20', text = options[5], anchor = 'ne')
    cursor = c.create_image(10, 625, image = whitecursorgraphic, anchor = 'nw')
    window.update()
    option = 0
    row = 0
    column = 0
    def movecursor(event):
        global option, chosen
        if event.keysym == 'Right' and option < 4:
            c.move(cursor, 200, 0)
            option += 2
        elif event.keysym == 'Left' and option > 1:
            c.move(cursor, -200, 0)
            option -= 2
        elif event.keysym == 'Up' and option % 2 == 1:
            c.move(cursor, 0, -25)
            option -= 1
        elif event.keysym == 'Down' and option % 2 == 0:
            c.move(cursor, 0, 25)
            option += 1
        elif event.keysym == 'z' and options[option] != '---':
            chosen = options[option]
    c.bind_all('<Key>', movecursor)
    chosen = ''
    while chosen == '':
        sleep(0.01)
        window.update()
    if chosen == 'Items':
        c.coords(cursor, 575, 40)
        c.unbind('<Key>')
        def movecursorininventory(event):
            global chosen, row, column
            if event.keysym == 'Right' and ((column == 0 and row+1 <= len(spells)) or (column == 1 and row+1 <= len(weapons))):
                c.move(cursor, 150, 0)
                column += 1
            elif event.keysym == 'Left' and ((column == 1 and row+1 <= len(inventory)) or (column == 2 and row+1 <= len(spells))):
                c.move(cursor, -150, 0)
                column -= 1
            elif event.keysym == 'Left' and column == 0:
                chosen = 'backtomain'
            elif event.keysym == 'Up' and row != 0:
                c.move(cursor, 0, -30)
                row -= 1
            elif event.keysym == 'Down' and ((column == 0 and row+2 <= len(inventory)) or (column == 1 and row+2 <= len(spells)) or (column == 2 and row+2 <= len(weapons))):
                c.move(cursor, 0, 30)
                row += 1
            elif event.keysym == 'Right' and column == 0 and len(spells) == 0 and len(weapons) > 0:
                c.coords(cursor, 875, 40)
                column = 2
                row = 0
            elif event.keysym == 'Left' and column == 2 and len(spells) == 0:
                c.coords(cursor, 575, 40)
                column = 0
                row = 0
            elif event.keysym == 'z':
                if column == 0 and inventory[row][-1] != '0':
                    chosen = inventory[row]
                elif column == 1:
                    chosen = spells[row]
                elif column == 2:
                    chosen = weapons[row]
        c.bind_all('<Key>',movecursorininventory)
        chosen = ''
        while chosen == '':
            sleep(0.01)
            window.update()
    c.delete(op1text)
    c.delete(op2text)
    c.delete(op3text)
    c.delete(op4text)
    c.delete(op5text)
    c.delete(op6text)
    c.unbind('<Key>')
    c.delete(cursor)
    option = 0
    row = 0
    column = 0
    if chosen == 'backtomain':
         chosen = getplayerchoice(options)
    option = 0
    row = 0
    column = 0
    return chosen

##collectible display##
firegem = PhotoImage(file = 'Graphics/firegem.gif')
watergem = PhotoImage(file = 'Graphics/watergem.gif')
icegem = PhotoImage(file = 'Graphics/icegem.gif')
stormgem = PhotoImage(file = 'Graphics/stormgem.gif')
crown = PhotoImage(file = 'Graphics/crown.gif')

def addgem(gemvalue = 5):
    if gemvalue == 1:
        c.create_image(115,235, image = icegem)
    elif gemvalue == 2:
        c.create_image(35,235, image = watergem)
    elif gemvalue == 3:
        c.create_image(75,315, image = firegem)
    elif gemvalue == 4:
        c.create_image(75,155, image = stormgem)
    else:
        c.create_image(75,235, image = crown)
    window.update()

pearl1 = PhotoImage(file = 'Graphics/forestpearl.gif')
pearl2 = PhotoImage(file = 'Graphics/grasspearl.gif')
pearl3 = PhotoImage(file = 'Graphics/mountainpearl.gif')
pearl4 = PhotoImage(file = 'Graphics/waterpearl.gif')
pearl5 = PhotoImage(file = 'Graphics/desertpearl.gif')
pearl6 = PhotoImage(file = 'Graphics/skypearl.gif')
sword = PhotoImage(file = 'Graphics/swordofcourage.gif')

def addpearl(value = 7):
    if value == 1:
        c.create_image(45,380,image = pearl1)
    elif value == 2:
        c.create_image(30,445,image = pearl2)
    elif value == 3:
        c.create_image(45,510,image = pearl3)
    elif value == 4:
        c.create_image(105,510,image = pearl4)
    elif value == 5:
        c.create_image(120,445,image = pearl5)
    elif value == 6:
        c.create_image(105,380,image = pearl6)
    else:
        c.create_image(75,495,image = sword, anchor = 's')

##initialise enemy graphics##
enemygraphics = {
        'First_Goblit' : PhotoImage(file = 'Graphics/Enemy/First_Goblit.gif')
    }

##other images##
slashimg = PhotoImage(file = 'Graphics/slash.gif')

##fight system##
def enemy_encounter(enemy):
    global player
    enemyfile = open('Areas/Enemies/'+enemy+'.json')
    enemyjson = json.load(enemyfile)
    enemyfile.close()
    victory = False
    fled = False
    sprite = enemygraphics[enemy]
    background = c.create_image(150,-540, image = sprite, anchor = 'nw')
    for i in range(54):
        c.move(background,0,10)
        window.update()
        sleep(0.01)
    popup('The ' + enemyjson['Name'] + ' appears!')
    while player.hp > 0 and victory == False and not fled:
        ##player turn##
        texttodisplay = enemyjson['Text'][randint(0,len(enemyjson['Text'])-1)]
        chatbox(texttodisplay)
        choice = getplayerchoice(['Bash','Block','Flee','---','---','Items'])
        ###add here choice effects###
        defence = 1 #defence works as a damage multiplier - 0.5 means you take 50% damage for example
        if choice == 'Bash':
            slash0 = c.create_image(250,180,image = slashimg, anchor = 'nw',state='hidden')
            slash1 = c.create_image(240,170,image = slashimg, anchor = 'nw',state='hidden')
            slash2 = c.create_image(230,160,image = slashimg, anchor = 'nw',state='hidden')
            slash3 = c.create_image(220,150,image = slashimg, anchor = 'nw',state='hidden')
            slash4 = c.create_image(210,140,image = slashimg, anchor = 'nw',state='hidden')
            slash5 = c.create_image(200,130,image = slashimg, anchor = 'nw',state='hidden')
            slash = [slash0,slash1,slash2,slash3,slash4,slash5]
            for j in range(47):
                for i in range(6):
                    c.move(slash[i],5,5)
                    window.update()
                    if j % 2 == 0 and j <= 10:
                        indexvalue = j / 2
                        c.itemconfig(slash[int(indexvalue)],state='normal')
                        window.update()
                    if j % 2 == 0 and j >= 36:
                        indexvalue = (j - 36) / 2
                        c.itemconfig(slash[int(indexvalue)],state='hidden')
                        window.update()
                window.update()
                sleep(0.01)
            if player.weapon == 'None':
                mindmg = 6
                maxdmg = 10
            elif player.weapon == 'Knife':
                mindmg = 9
                maxdmg = 14
            damage_dealt = randint(mindmg,maxdmg)
            popup('The ' + enemyjson['Name'] + ' takes ' + str(damage_dealt) + ' damage!')
            enemyjson['Health'] -= damage_dealt

        elif choice == 'Block':
            popup('You brace for impact.')
            defence = 0.75
        
        elif choice == 'Flee':
            if enemyjson['FleeChance'] == 0:
                popup('Cannot run!')
            elif randint(1,100) <= enemyjson['FleeChance']:
                popup('Got away successfully!')
                fled = True
            

        if enemyjson['Health'] <= 0:
                popup('The ' + enemyjson['Name'] + ' was defeated.')
                victory = True
                break


        ##enemy turn##
        chatbox(['','',''])
        sleep(1)
        attackoptions = enemyjson['Attacks']['options']
        attackused = attackoptions[randint(0,len(attackoptions)-1)]
        popup('The ' + enemyjson['Name'] + attackused)
        attackdata = enemyjson['Attacks'][attackused]
        damage = int(round(randint(attackdata['MinDmg'],attackdata['MaxDmg']) * defence, 0))
        lines = []
        for i in range(540):
            if i % 2 == 0:
                lines.append(c.create_line(150,i,555,i,fill='black'))
        window.update()
        sleep(0.1)
        for i in range(270):
            c.delete(lines[0])
            del lines[0]
        player.takedamage(damage)
        update_stats()
        popup('You take ' + str(damage) + ' damage.')

    ##rewards##
    if victory:
        expgain = randint(enemyjson['Rewards']['MinExp'],enemyjson['Rewards']['MaxExp'])
        goldgain = randint(enemyjson['Rewards']['MinGold'],enemyjson['Rewards']['MaxGold'])
        chatbox(['You win!', 'You gain ' + str(expgain) + ' EXP and ' + str(goldgain) + ' gold.', ''])
        player.addexp(expgain)
        player.addmoney(goldgain)
        sleep(1)
        try:
            flags[enemyjson['Rewards']['flag']] = 1
        except:
            pass
    
    elif player.hp <= 0:
        popup('You lose...')
    
    update_stats()
    c.delete(background)
            
                    
##mainloop##
addtoinv('Health Potion - x 0')
addtoinv('Magic Potion - x 0')
oldlevel = 1

flags = {
    'whistlegot': 0,
    'knifegot': 0,
    'livingroomhatchopen': 0,
    'unclerescued': 0,
    'forestpearlgot': 0,
    'fieldpearlgot' : 0,
    'mountainpearlgot': 0,
    'oceanpearlgot': 0,
    'desertpearlgot': 0,
    'skypearlgot': 0,
    'allpearlsgot': 0,
    'swordcouragegot': 0
    }

file = open('Areas/Rooms/Game_Entry.json')
room = json.load(file)
file.close()
room_name = 'Game_Entry'
room_folder = 'Rooms'

while True:
    if room_folder == 'Rooms':
        try:
           if flags['swordcouragegot'] == 1 and ('Pearls' in room['flag']['optionsif1']):
                room['flag']['optionsif1'][4] = '---'
                
        except:
            pass
        
        if randint(1,100) <= room['Enemies']['Chance']:
            popup('Look out!')
            enemy_encounter(room['Enemies']['Enemy'])
        
        try:
            related_flag = room['flag']['name']
            if flags[related_flag] == 0:
                chatbox(room['flag']['maintextif0'])
                choice = getplayerchoice(room['flag']['optionsif0'])
            else:
                chatbox(room['flag']['maintextif1'])
                choice = getplayerchoice(room['flag']['optionsif1'])
        except:
            chatbox(room['maintext'])
            choice = getplayerchoice(room['options'])


        if choice in room.keys():
            try:
                flags[room[choice]['flagtoupdate']] = 1
            except:
                pass
            
            try:
                if room[choice]['section'] == "inventory":
                    addtoinv(room[choice]['additem'])
                elif room[choice]['section'] == 'spells':
                    addtospells(room[choice]['additem'],room[choice]['cost'])
                elif room[choice]['section'] == 'weapons':
                    addtoweapons(room[choice]['additem'])
            except:
                pass
            
            if room[choice]['startgraphicswap'] == 'Player':
                change_player_graphic(playergroundimg)
            elif room[choice]['startgraphicswap'] == 'Boat':
                change_player_graphic(playerboatimg)
            elif room[choice]['startgraphicswap'] == 'Balloon':
                change_player_graphic(playerballoonimg)
            
            if room[choice]['popup'] != 'None':
                popup(room[choice]['popup'])

            try:
                chatbox(room[choice]['maintextupdate'])
            except:
                pass

            try:
                enemy_encounter(room[choice]['forcedencounter'])
            except:
                h = 0/0
                    
            move_player(room[choice]['move1'][0],room[choice]['move1'][1],room[choice]['move1'][2],room[choice]['move1'][3])
            if room[choice]['move2'][0] != 'None':
                move_player(room[choice]['move2'][0],room[choice]['move2'][1],room[choice]['move2'][2],room[choice]['move2'][3])
            if room[choice]['move3'][0] != 'None':
                move_player(room[choice]['move3'][0],room[choice]['move3'][1],room[choice]['move3'][2],room[choice]['move3'][3])

            if room[choice]['endgraphicswap'] == 'Player':
                change_player_graphic(playergroundimg)
            elif room[choice]['endgraphicswap'] == 'Boat':
                change_player_graphic(playerboatimg)
            elif room[choice]['endgraphicswap'] == 'Balloon':
                change_player_graphic(playerballoonimg)

            if choice == 'Rest':
                player.heal(999999)
                player.magicrestore(999999)
                popup('Your HP and magic are maxed out.')
                update_stats()

            room_name = room[choice]['NewRoom']
            room_folder = room[choice]['NewRoomFolder']
            file = open('Areas/' + room_folder + '/' + room_name + '.json')
            room = json.load(file)
            file.close()
            
        else:
            whistleused = False
            try:
                a = room['Whistle_Disabled']
            except:
                if choice == 'Whistle':
                    x,y = c.coords(playergraphic)
                    movex = 165 - x
                    movey = 285 - y
                    change_player_graphic(playertornadoimg)
                    move_player(movex,movey,50,1)
                    change_player_graphic(playergroundimg)
                    file = open('Areas/Rooms/Player_Bedroom.json')
                    room = json.load(file)
                    file.close()
                    whistleused = True
            if choice in weapons:
                equipweapon(choice)
            elif whistleused == True:
                pass
            else:
                popup('Nothing happened.')
        option = 0
        chosen = ''
        row = 0
        column = 0
