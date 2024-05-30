import pandas as pd
from constants import *
from helper import *
import random

def start_conjugation_test():
    df = pd.read_excel(DICTIONARY_NAME, sheet_name=SHEET_CONJUGATION)

    deu_words = list(df[COL_VERB].dropna())
    deu_word_conj_dict = {}
    for index, row in df.iterrows():
        
        curr_verb = None
        for col, val in row.items():
            # print(f"col: {col}, v: {val}")
            if col == "Verb":
                curr_verb = val
                deu_word_conj_dict[val] = [""]*len(CONJUGATION_FORMS)
            
            elif col in CONJUGATION_FORMS:
                conj_list = deu_word_conj_dict[curr_verb]
                conj_pos = CONJUGATION_FORMS.index(col)
                conj_list[conj_pos] = val
    
    print(f"Total words: {len(deu_words)}")
    print(f"Write conjugation of each of below words for all pronouns: {CONJUGATION_FORMS}")

    score = 0
    incorrect_ans = {}
    random.shuffle(deu_words)
    
    for deu_word in deu_words:
        incorrect_forms  = {}
        print(f"\nWrite conjugation for : {deu_word}")
        
        for i in range(len(CONJUGATION_FORMS)):
            pron = CONJUGATION_FORMS[i]
            correct_ans = deu_word_conj_dict[deu_word][i]
            simplified_ans = remove_umlaut_and_etset(correct_ans)

            print(f"\tFor {pron} ",end=" : ")
            user_ans = process_input(input(), action=ACTION_CONJUGATION_ANS)

            if user_ans == correct_ans or user_ans == simplified_ans:
                pass
            else:
                incorrect_forms[pron] = correct_ans
        
        if len(incorrect_forms) > 0:
            incorrect_ans[deu_word] = incorrect_forms
            print(f"\t>> {len(CONJUGATION_FORMS) - len(incorrect_forms)}/{len(CONJUGATION_FORMS)} were correct")
            print("\t>> Incorrect Forms: ",incorrect_forms)
        else:
            print("\t>> All correct!")
            score += 1
        

    if score == len(deu_words):
        print("Congratulations! All correct")
    else:
        print(f"Score: {score}/{len(deu_words)}")
        print(f"Incorrect conj: {incorrect_ans}")
    
    print("*"*200, end="\n")


