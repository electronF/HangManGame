#-*-coding:utf8;-*-
#qpy:console

import os

from typing import Dict, List, Union



class GameScreenDrawer:
    """ View of the game """
    
    def __init__(self, languages:Dict[str, Dict[str, str]]):
        self.languages = languages
        self.language = 'en'
        
    def set_language(self, language:str):
        self.language = language
           
    def clear(self):        
        os.system("clear")        
    
    def game_name(self):
        print("\n\n"+"#"*27+f"\n###\t{self.languages[self.language]['title label']}\t###\n"+"#"*27)
             
    def choose_language(self):
        self.clear()
        print("\n\n") 
        print(f"{self.languages['fr']['language label']}\n{self.languages['en']['language label']}\n\n")
        print("1.English\n2.Francais")
        	   
    def part_number(self, part_number:int):
        print("\n"+"*"*5, f"{self.languages[self.language]['part label']}: {part_number}", "*"*5)
       
    def lives_left(self, lives_left:int):
        print(f"\n\n{self.languages[self.language]['live label']}: {lives_left}.")
        
    def choose_letter(self):
        print(f"\n\n{self.languages[self.language]['letter label']}:")     
    
    def win_lose(self, is_winned:bool):
        self.clear()
        print("\n\n\n"+"#"*27+f"\n###\t{self.languages[self.language]['win label' if is_winned else 'lose label']} \t###\n"+"#"*27)
        self.new_part()
    
    def new_part(self):
        print(f"\n\n{self.languages[self.language]['new part label']}")
        print(f"1. {self.languages[self.language]['yes label']}\n2. {self.languages[self.language]['no label']}")
        
    def input_prompt(self):
        print()
        return input(">>> ")
    
    def entry_error(self):
        print(f"\n{self.languages[self.language]['new entry label']}")
           	
    def game_board(self, part_number:int, lives_left:int, word_letters_states:List[Union[str, None]]):
        self.clear()
        self.game_name()
        self.part_number(part_number)
        self.lives_left(lives_left)
        
        print("\n\t", end="")
        for state in word_letters_states:
            if state != None:
                print(f"{state}", end="")
            else:
                print('-', end="") 
        self.choose_letter()

