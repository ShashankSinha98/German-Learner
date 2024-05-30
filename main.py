import pandas as pd
from constants import *
from helper import *
import traceback

from deu_to_eng_quiz import start_deu_to_eng_quiz
from eng_to_deu_quiz import start_eng_to_deu_quiz
from verb_case_quiz import start_verb_case_quiz
from preposition_case_quiz import start_preposition_case_quiz
from conjugation import start_conjugation_test
from personal_pronoun_quiz import start_personal_pronoun_test

intro_page = ["\t\t >> DEUTSCHE PRAXIS  << \n", "Bitte wählen Sie den Praxistyp aus:\n", "1. Deutsch -> Englisch", "2. Englisch -> Deutsch", "3. Verb Case Quiz", "4. Conjugation", "5. Personal Pronoun", "6. Preposition Case Quiz"]

# Open the Excel file
excel_file = pd.ExcelFile(DICTIONARY_NAME)

# Get the names of all sheets
sheet_names = excel_file.sheet_names

sheet_dict = {}

idx = 0
for i in range(len(sheet_names)):
    if sheet_names[i] not in LIST_SHEET_WHITELIST:
        sheet_dict[idx] = sheet_names[i]
        idx+=1

# include DAW quiz if more than 1 verb form sheet is available
# if verb_form_cnt > 1:
#     sheet_dict[len(sheet_dict)] = ACTION_DAW_QUIZ

try:
    while True:
        print_page(intro_page)
        print("\nYour choice: ",end="")
        user_option = process_input(input(), action=ACTION_SELECTED_INTRO_OPTION)

        if user_option == OPTION_DEU_TO_ENG or user_option == OPTION_ENG_TO_DEU:
            print(sheet_dict)
            print("\nInput the sheet no. to continue: ", end = "")
            inp = process_input(input(), action=ACTION_SELECT_SHEET)

            if isinstance(inp, int) and inp in sheet_dict:
                sheet_selected = sheet_dict[inp]
                print("Option selected: ",sheet_selected)
                
                if user_option == OPTION_ENG_TO_DEU:
                    start_eng_to_deu_quiz(selected_sheet=sheet_selected)
                elif user_option == OPTION_DEU_TO_ENG:
                    start_deu_to_eng_quiz(selected_sheet=sheet_selected)
        
        elif user_option == OPTION_VERB_CASE_QUIZ:
            # check if there is more than 1 sheet of diff ver forms (Akk./Dat/Wech.)
            verb_form_cnt = 0
            verb_form_available = []
            for sheet_name in sheet_names:
                _sheet_name = sheet_name.strip().lower()
                if _sheet_name in VERB_FORMS:
                    verb_form_cnt += 1
                    verb_form_available.append(sheet_name)

            if verb_form_cnt > 1:
                start_verb_case_quiz(available_verb_forms=verb_form_available)
            else:
                print("Min verb case sheet not fulfilled")
        
        elif user_option == OPTION_CONJUGATION:
            if SHEET_CONJUGATION in sheet_names:
                start_conjugation_test()
        elif user_option == OPTION_PERSONAL_PRONOUN:
            if SHEET_PERSONAL_PRONOUNN in sheet_names:
                start_personal_pronoun_test()
        elif user_option == OPTION_PREPOSITION_CASE_QUIZ:
            # check if there is more than 1 sheet of diff ver forms (Akk./Dat/Wech.)
            prep_form_cnt = 0
            prep_form_available = []
            for sheet_name in sheet_names:
                #_sheet_name = sheet_name.strip().lower()
                if sheet_name in PREPOSITION_FORMS:
                    prep_form_cnt += 1
                    prep_form_available.append(sheet_name)

            if prep_form_cnt > 1:
                start_preposition_case_quiz(available_verb_forms=prep_form_available)
            else:
                print("Min Preposition case sheet not fulfilled")
        else:
            # user inp for sheet selection is non-int
            print("Wrong input (non-int), try again")

except Exception as e:
    print("Something went wrong")
    print(e.args[0])
    traceback.print_exc()
    sys.exit()



