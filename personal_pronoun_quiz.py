import pandas as pd
from constants import *
from helper import *
import random

def start_personal_pronoun_test():
    df = pd.read_excel(DICTIONARY_NAME, sheet_name=SHEET_PERSONAL_PRONOUNN)
    nomm_pronouns = list(df[COL_NOMMINATIV].dropna())
    akk_pronouns = list(df[COL_AKKUSATIV].dropna())
    dat_pronouns = list(df[COL_DATIV].dropna())

    pron_nomm_dict = {}
    for i in range(len(nomm_pronouns)):
        pron_nomm_dict[nomm_pronouns[i]] = (akk_pronouns[i], dat_pronouns[i])
    
    random.shuffle(nomm_pronouns)
    print("*"*100)
    print("\nAnswer Akkusativ and dativ form of below pronouns:\n\n")

    score = 0
    wrong_ans = []
    for nomm_pron in nomm_pronouns:
        akk_pron, dat_pron = pron_nomm_dict[nomm_pron]
        print(f"\nPronoun is '{nomm_pron}'")
        print("Akkusativ form: ",end="")
        user_akk_ans = process_input(input(), action=ACTION_PERSONAL_PRONOUN_ANS)
        print("Dativ form: ",end="")
        user_dat_ans = process_input(input(), action=ACTION_PERSONAL_PRONOUN_ANS)

        if user_akk_ans != akk_pron or dat_pron != user_dat_ans:
            print(f">> Incorrect ans. Correct ans is: pron: {nomm_pron}, Akk: {akk_pron}, Dat: {dat_pron}")
            wrong_ans.append(nomm_pron)
        else:
            print(">> Correct!")
            score+=1
    
    if score == len(nomm_pronouns):
        print("Congrats! Perfect score")
    else:
        print(f"Pronouns for which you gave wrong ans: {wrong_ans}")
