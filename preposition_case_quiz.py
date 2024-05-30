import pandas as pd
import random
from constants import *
from helper import *

def start_preposition_case_quiz(available_verb_forms):
    print("\n\n***************************************************\n")
    print("\t\t >> START PREPOSITION CASE QUIZ <<\n")
    
    sheet_dict = pd.read_excel(DICTIONARY_NAME, sheet_name=available_verb_forms)
    deuword_to_case_dict = {}
    deuword_to_eng_dict = {}

    all_deu_words = []

    for sheet_name, sheet_df in sheet_dict.items():
        deu_words = list(sheet_df[COL_DEUTSCH].dropna())
        eng_words = list(sheet_df[COL_ENGLISH].dropna())

        all_deu_words.extend(deu_words)
        verb_case = str(sheet_name[12]).lower()

        for i in range(len(deu_words)):
            deu_word = deu_words[i]
            deuword_to_case_dict[deu_word] = verb_case
            deuword_to_eng_dict[deu_word] = eng_words[i]
    
    random.shuffle(all_deu_words)
    
    print("Cases available for quiz: ", available_verb_forms, "/n Total words: ", len(all_deu_words))
    print("Enter the case of German words (A-Akkusativ / D-Dativ / W-Wechel): \n")

    incorrect_ans = {}
    incorrect_case_words = {'a':[], 'd':[], 'w':[]}
    score = 0
    for i in range(len(all_deu_words)):
        ques_no = f"({i+1}/{len(all_deu_words)})"
        deu_word = all_deu_words[i]
        print(ques_no, " Case of ",deu_word,end=" : ")
        user_ans: str = process_input(input())
        correct_case = deuword_to_case_dict[deu_word]


        if user_ans.strip().lower() == correct_case:
            print(">> Correct, Meaning: ",deuword_to_eng_dict[deu_word],"\n")
            score+=1
        else:
            print(">> Incorrect, correct case: ",correct_case," Meaning: ",deuword_to_eng_dict[deu_word],"\n")
            incorrect_ans[deu_word] = correct_case
            incorrect_case_words[correct_case].append(deu_word)
        
    if len(incorrect_ans) == 0:
        print("Congrats! Perfect score")
    else:
        print(f"{score}/{len(all_deu_words)}")
        print("Incorrect ans: ", incorrect_ans)
        print("\nIncorrect cases answered: ", incorrect_case_words)
    
    print("***************************************************\n\n")



    

