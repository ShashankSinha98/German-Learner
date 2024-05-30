import pandas as pd
from constants import *
from constants import *
from helper import *
import random

def start_deu_to_eng_quiz(selected_sheet):
    df = pd.read_excel(DICTIONARY_NAME, sheet_name=selected_sheet)
            
    deu_words = list(df[COL_DEUTSCH].dropna())
    eng_words = list(df[COL_ENGLISH].dropna())


    level = "A"
    if COL_LEVEL in df.columns:
        print("Input level type (E/M/H/A) : ", end = "")
        level = process_input(input())

        if level == 'A':
            print("Level ",level," selected, all words will be choosen for test")
        
        elif level in ["E", "M", "H"]:
            print("Level ",level," selected, only words from those level will be choosen for test")
            filtered_df = df[df[COL_LEVEL]==level]
            deu_words = list(filtered_df[df[COL_DEUTSCH]].dropna())
            eng_words = list(filtered_df[df[COL_ENGLISH]].dropna())

        else:
            print("Incorrect Level enetered, Default level selected: A")

    
    deu_eng_word_dict = {}
    i = 0
    while i < len(deu_words) and i < len(eng_words):

        deu_word = deu_words[i]
        eng_word = eng_words[i]
        if isinstance(deu_word, str) and isinstance(eng_word, str):
            deu_eng_word_dict[deu_word] = eng_word
        i+=1
    
    print("Total Len: ", len(deu_eng_word_dict))

    if len(deu_eng_word_dict) == 0:
        print("No words filtered. Select different options")
        print("\n\n***************************************\n")
        return

    tmp_deu_words = list(deu_words)
    random.shuffle(tmp_deu_words)

    i = 0
    score = 0
    wrong_ans = {}
    while i < len(tmp_deu_words):
        print((i+1),"/",len(tmp_deu_words), end=" ")
        print("Meaning of ", tmp_deu_words[i]," : ", end="")
        correct_ans: str = deu_eng_word_dict[tmp_deu_words[i]]

        ans:str = process_input(input(), ACTION_ANSWER_WORD)
        if ans.strip().lower() in correct_ans.strip().lower():
            print(">> Correct, ans = ",correct_ans, end="\n\n")
            score+=1
        else:
            print(">> Wrong!, ans = ", correct_ans, end="\n\n")
            wrong_ans[tmp_deu_words[i]] = correct_ans
        
        i+=1
    
    print("Score: ",score,"/",len(tmp_deu_words))
    if len(wrong_ans) > 0:
        print("Wrong Ans: ", wrong_ans)
    else:
        print("Congratulations!! Perfect score")
    
    print("\n\n***************************************\n")