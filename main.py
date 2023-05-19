#-*-coding:utf8;-*-
#qpy:console

import sys
import os
import random
import json

from typing import List, Union

from view import GameScreenDrawer
from controller import GameController 


def main():
    #words = ["ecouter", "happer", "sourire", "danser", "manger"]
    os.chdir(os.path.join("projects3","HangmanGame"))
    
    with open(os.path.join(".", "lang", "en_EN.json"), mode="r") as lang_en_file,\
         open(os.path.join(".", "lang", "fr_FR.json"), mode="r") as lang_fr_file,\
         open(os.path.join(".", "data", "words.txt"), mode="r") as words_file:
        lang_en = json.load(lang_en_file) 
        lang_fr = json.load(lang_fr_file)
        
        words = [word.strip() for word in words_file.readlines()]
        languages = {'en': lang_en, 'fr': lang_fr} 
        
       
        game_drawer = GameScreenDrawer(languages)
        game_controller = GameController(game_drawer, words, 5)
   

if __name__ == "__main__":
   main()
   print(os.getcwd())