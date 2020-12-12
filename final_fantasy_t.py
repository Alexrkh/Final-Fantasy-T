#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import random

import termcolor

from inventory import Item
from magic import Spell
from mechanics import Person

# Black Magic
fire = Spell("Fire", 25, 200, "black")
thunder = Spell("Thunder", 25, 200, "black")
blizzard = Spell("Blizzard", 25, 200, "black")
meteor = Spell("Meteor", 40, 500, "black")
quake = Spell("Quake", 14, 140, "black")
twister = Spell("Twister", 50, 1000, "black")

# White Magic
cura = Spell("Cura", 25, 220, "white")
recover = Spell("Recover", 32, 1500, "white")

# Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
superpotion = Item("Super Potion", "potion", "Heals 100 HP", 100)
maxpotion = Item("Max Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully Restores HP/MP Of One Party Member", 9999)
megaelixer = Item("Mega-Elixer", "elixer", "Fully Restores HP/MP Of One Party Member", 9999)
grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cura, recover]
enemy_spells = [fire, meteor, cura, twister]
player_items = [{"item": potion, "quantity": 15},
                {"item": superpotion, "quantity": 5},
                {"item": maxpotion, "quantity": 1},
                {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2},
                {"item": grenade, "quantity": 2}]

# Instantiate People
player1 = Person("Swordsman  :", 1160, 100, 300, 34, player_spells, player_items)
player2 = Person("Mage       :", 1110, 300, 100, 34, player_spells, player_items)
player3 = Person("Assassin   :", 1000, 150, 150, 34, player_spells, player_items)

enemy1 = Person("Fiend:", 1250, 90, 100, 34, enemy_spells, [])
enemy2 = Person("Chaos:", 12000, 200, 200, 50, enemy_spells, [])
enemy3 = Person("Imp  :", 1250, 100, 90, 34, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print("""
                                                  ╓<≈w                        
                                                   ╠╫µ▄╬▓                       
                                                    ▓Ñ╣▓Ñ                       
                                                    ▓▓▒╣w                       
     ,  .;,,`                         ,,,           ▓ÑH╫M                       
     ╟▐▓^*┴╫Ñ                     ║╣▓╨╙>╫─      ,▄╓;▓╣M▓▄µ,;w                   
     ╟▐╫   ⌠,,.,,  ,,       ,,,   ║▐╫   `    ,,╚▓Å"╠▓▌▓▓▓╙"╨   ,╓µ,,,,  .µ,     
     ╟▐╫   $╫▌ ▓╫w ╟▓  ▒▓▄  B╫Ñ   ║j╫   ╠╫▓  ▐▒▌ .ΦH╣╣▓█` Æ╫▌ Ä▓``╫║╙▓  j║┴     MMP""MM""YMM
     ╠▐▓▄▄▄$╫▌ ╬╜▓▄╟▌ ╓▓▐▓  b╫Γ   ║j╫╓▄µ╫▌╫░ ▐▌╣▌ ▓ ╪╫██  ╢M╫'Ü╫▄   W╫L Ñ▌      P'   MM   `7
     ╠▐▄"╙Ñ╡]▌ ╬░Γ▓▓▌ ╡▌H╫⌐ Γ╫M   ║▐▓*╙Ü╢╠╠▌ ▐▌\▀▓▓ ╟╬▓▓ ▐Φb╫H ╚▀▓w ╙J▓╓╣`           MM
     ╠j╣   L╫▌ ╢.`U╫▌ ╬▀É╫L H╫M   ║▐╫  ▐▓▀╨╫ ▐▌ )╠▓ ║░▓▌ £▌║╙▌  `Ü▀φ V╫▓M            MM
     ⌡j╫   $╫▌ ╢   @▌,╫─╞╠▓ H╫M   ║▐╫  £▌ ⌐╫H▐▌  ╠╣ ║½▓▌ M⌐"»╫'   H▓  ╨▓             MM
     ⌡j╫   P╫▌ ╢`  |▌╠▓ "]▓⌐H╫M   ▐▐╫  ╣⌐ Ü╢▌▐▌   ╢ ▐'█▌.╫  W╢▌   N▌ ⁿ]╫             MM
     ⌡]╣   ÑÅ▌~▀K  $ÑÑ▌ »Ñ▀WÑ▀▀Φ▀ ║▐╫ «▀⌐ ╧╩▀╝▌   Å ▐ ▓▌╝▀  ╩╝╝ßΦÅ╙  ╙;╫           .JMML.
     ⌡╟▓                          ║▐▓                 ▓▌             J»▓        
     ╠╟▓                          ║▐▓⌐               ▄█▌             ▐è▓        
     ▄╨`                          ║╝`                ▓█▌               ╙        
                                                     ╫▌H                                               
                                                     ╫▓                         
                                                     ║▓                         
                                                     "▀                         
""")
print(termcolor.colored(("\033[1m FINAL FANTASY T \033[0m"), "white"))
print(termcolor.colored(("\033[1m Terminal FINAL FANTASY \033[0m"), "white"))
print(termcolor.colored(("\033[1m github.com/alexrkh \033[0m"), "white"))

while running:
    print("=======================================")

    print("\n\n")
    print("CHARACTER               HP                                   MP")
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose Action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(termcolor.colored(
                ("You Attacked " + enemies[enemy].name.replace(" ", "") + " For " + str(dmg) + " Points Of Damage"),
                "green"))

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " Has Been Killed")
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(termcolor.colored(("\n Not Enough MP"), "red"))
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(termcolor.colored(("\n" + spell.name + " Heals " + str(magic_dmg) + " Points OF HP"), "blue"))
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(termcolor.colored(
                    ("\n" + spell.name + " Deals " + str(magic_dmg) + " Points Of Damage To" + enemies[enemy].name),
                    "blue"))

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " Has Been Killed")
                    del enemies[enemy]


        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1
            if player.items[item_choice]["quantity"]:
                print(termcolor.colored(("\n" + "Ran Out Of " + item.name + "s"), "red"))
                continue
            if item.type == "potion":
                player.heal(item.prop)
                print(termcolor.colored(("\n" + item.name + " Heals " + str(item.prop) + " Points of HP"), "green"))
            elif item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(termcolor.colored(("\n" + item.name + " Fully Restores HP/MP"), "green"))
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(termcolor.colored(
                    ("\n" + item.name + " Deals " + str(item.prop) + " Points of Damage To " + enemies[enemy].name),
                    "green"))

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " Has Been Killed")
                    del enemies[enemy]
    # check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
    # check if player won
    if defeated_enemies == 2:
        print(termcolor.colored(("\033[1m All Enemies Were Killed!!! You Win!!! \033[0m"), "green"))
        running = False

    print("\n")
    # check if enemy won
    if defeated_players == 2:
        print(termcolor.colored(("\033[1m You Have All Been Killed NOOBS!!! \033[0m"), "red"))
        running = False

for enemy in enemies:
    enemy_choice = random.randrange(0, 3)

    if enemy_choice == 0:
        target = random.randrange(0, 2)
        enemy_dmg = enemy.generate_damage()

        players[target].take_damage(enemy_dmg)
        print(termcolor.colored(
            (enemy.name + " Attacked " + players[target].name + " For " + str(enemy_dmg) + " Points of Damage"), "red"))

    elif enemy_choice == 1:
        spell, magic_dmg = enemy.choose_enemy_spell()
        enemy.reduce_mp(spell.cost)

        if spell.type == "white":
            enemy.heal(magic_dmg)
            print(termcolor.colored((spell.name + " Heals " + enemy.name + " For " + str(magic_dmg) + " Points OF HP"),
                                    "blue"))
        elif spell.type == "black":
            target = random.randrange(0, 3)
            players[target].take_damage(magic_dmg)
            print(termcolor.colored(
                ("\n" + enemy.name + "s " + spell.name + " Deals " + str(magic_dmg) + " Points Of Damage To " + players[
                    target].name),
                "blue"))

            if players[target].get_hp() == 0:
                print(players[target].name.replace(" ", "") + " Has Been Killed")
                del players[player]
        # print("Enemy Attacked With " + spell + " Dealing " + str(magic_dmg) + " Points of Damage " )
