import sys
from constants import *

def remove_umlaut_and_etset(inp: str) -> str:
    replace_with = {"ü": "u", "ö": "o", "ä": "a", "ß": "s"}

    for key, value in replace_with.items():
        if key in inp:
            inp = inp.replace(key, value)
    return inp

def process_input(inp: any, action=None) -> any:
    if isinstance(inp, str):
        tmp_inp = inp.strip().lower()
        
        if tmp_inp == "cls" or tmp_inp == "exit":
            print("Successfully Terminated")
            sys.exit()
        
        if action == ACTION_SELECT_SHEET or action == ACTION_SELECTED_INTRO_OPTION:
            return int(inp)
        
        if action == ACTION_ANSWER_WORD or action == ACTION_SELECT_LEVEL or action == ACTION_DAW_QUIZ_ANS or action == ACTION_CONJUGATION_ANS or action == ACTION_PERSONAL_PRONOUN_ANS:
            return str(inp)

    return inp

def print_page(page: list[str]):
    for line in page:
        print(line)
