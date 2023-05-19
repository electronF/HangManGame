#-*-coding:utf8;-*-
#qpy:console

import sys
import time
import random

from typing import List, Union


class GameController:
    """ 
       This class is use to control the game flow
       and user interactions
    """
    
    def __init__(self, game_drawer:object, words:List[str], number_max_of_chances:int=5):
        self.number_of_games = 1
        self.game_lives_left = number_max_of_chances
        self.language = None
        self.words = words
        self.number_max_of_chances = number_max_of_chances
        self.game_drawer = game_drawer
        
        #start game
        self.start_game()

    def start_game(self):
        for i in range(4,-1, -1):
            self.game_drawer.clear()
            print("\n"*i)
            self.game_drawer.game_name()
            sys.stdout.flush()
            time.sleep(.5)
        time.sleep(2)
            
        if self.language == None:
            self.game_drawer.choose_language()
            while self.language == None:
                value = self.game_drawer.input_prompt()
                if value.strip() == "1":
                    self.language = "en"
                elif value.strip() == "2":
                    self.language = "fr"
                else:
                    self.game_drawer.entry_error()
                   
        self.game_drawer.set_language(self.language)
        self.new_game()
                   
    def choose_game_word(self) -> (str):
        #use letter to controls words size
        #number_of_letters = random.randint(3, 26)
        #word = words_by_lengths[number_of_letters]
           
        return random.choice(self.words)
           
    def new_game(self):
        correct_word = self.choose_game_word().lower()
        self.reset_lives_left()
        word_letters_states = [None]*len(correct_word)
       
        while self.check_game_state(word_letters_states) == 'pending':
           self.game_drawer.game_board(self.number_of_games, self.game_lives_left, word_letters_states)
          
           value = self.game_drawer.input_prompt()
           if  correct_word.find(value.lower()) != -1:
               self.show_occurences_of_letter(value.lower(), correct_word, word_letters_states) 
           else:
               self.game_lives_left -= 1
       
        if self.check_game_state(word_letters_states) == "winned":
            self.game_drawer.win_lose(True)
        else:
            self.game_drawer.win_lose(False)
        
        want_to_play_again = None
        while want_to_play_again == None:
            value = self.game_drawer.input_prompt()
            if value.strip() == "1":
                want_to_play_again = True
            elif value.strip() == "2":
                want_to_play_again = False
            else:
                self.game_drawer.entry_error()
        
     
        if want_to_play_again == True:
            self.number_of_games += 1
            self.new_game()
                   
    def reset_lives_left(self):
        self.game_lives_left = self.number_max_of_chances
   
    def show_occurences_of_letter(self, letter:str, correct_word:str, word_letters_states:List[Union[str, None]]):
        for index, letter_itr in enumerate(correct_word):
            if letter_itr == letter:
                word_letters_states[index] = letter
              
    def check_game_state(self, word_letters_states:List[Union[str, None]]) -> (str):
        if self.is_winned(word_letters_states):
            return 'winned'
        elif self.is_losed(word_letters_states):
            return 'losed'
        return 'pending'
   
    def is_winned(self, word_letters_states:List[Union[str, None]]) -> (bool):
        all_letters_has_been_founded = all([state != None for state in word_letters_states]) 
        if all_letters_has_been_founded == True and self.game_lives_left > 0:
            return True
   
    def is_losed(self, word_letters_states:List[Union[str, None]]) -> (bool):
        all_letters_has_been_founded = all([state != None for state in word_letters_states]) 
        if all_letters_has_been_founded == False and self.game_lives_left < 1:
            return True
