#Importing required libraries

import streamlit as st
import pandas as pd
import numpy as np
from util import test

#Training the model with training dataset
t = test("training_data.csv")
t.train()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "home_page"

# Define functions for each page
def home():
    # st.title("Chronic Disease Predictor")
    st.markdown("<h1 style='text-align:center;'>Chronic Disease Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align:center;margin-bottom:30px;'>Disclaimer: Not for Medical Use!!</h1>", unsafe_allow_html=True)
    
    st.markdown("__Go through a complete body analysis to find your problem__")
    if st.button("Complete Analysis"):
        st.session_state.page = "comp_analysis"

    st.markdown("<h3 margin-top:30px;>Particular Analysis</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Skin Analysis"):
            st.session_state.page = "skin_analysis"

        if st.button("Heart Analysis"):
            st.session_state.page = "heart_analysis"

        if st.button("Vision Analysis"):
            st.session_state.page = "eye_analysis"

        if st.button("Mental Analysis"):
            st.session_state.page = "mental_analysis"

        if st.button("Excretary Analysis"):
            st.session_state.page = "exec_analysis"

    with col2:
        if st.button("Digestive Analysis"):
            st.session_state.page = "diges_analysis"

        if st.button("Bone, Muscle, Joint Analysis"):
            st.session_state.page = "BMJ_analysis"

        if st.button("Oral Analysis"):
            st.session_state.page = "oral_analysis"

        if st.button("Nasal Analysis"):
            st.session_state.page = "nose_analysis"

        if st.button("Body and Fever Analysis"):
            st.session_state.page = "body_analysis"

    

def comp_analysis():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Complete Analysis")
    st.write("A Thorough examination of your body.")
    col1, col2, col3, col4, col5 = st.columns(5)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    # val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    val = []
    col1, col2, col3 = st.columns(3)
    for i in col:
        if col.index(i) < 44:
            with col1:
                check = st.checkbox(i)
                if check:
                    val.append(1)
                else:
                    val.append(0)
        elif col.index(i) >= 44 and col.index(i) < 89:
            with col2:
                check = st.checkbox(i)
                if check:
                    val.append(1)
                else:
                    val.append(0)
        else:
            with col3:
                check = st.checkbox(i)
                if check:
                    val.append(1)
                else:
                    val.append(0)


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        result(t.predict_test(df_test), "comp_analysis")



def skin_analysis():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Skin Analysis")
    st.write("Examine your body if you have any Skin Problems.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    skin = {'itching':1,'skin_rash':2,'nodal_skin_eruptions':3,'yellowish_skin':4,'bruising':5,'internal_itching':6,'typhos(toxic look)':7,'dischromic_patches':8,'blackheads':9,'scurring':10}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in skin.keys():
            check = st.checkbox(i)
            if check:
                skin[i] = 1
            else:
                skin[i] = 0
                
    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in skin.keys():
            if i == j:
                val[d[i]] = skin[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def heart_analysis():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Heart Analysis")
    st.write("Examine your body if you have any Heart Related Problems.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    heart = {'chest pain': 1, 'fast heart rate': 2, 'palpitation': 3}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in heart.keys():
            check = st.checkbox(i)
            if check:
                heart[i] = 1
            else:
                heart[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in heart.keys():
            if i == j:
                val[d[i]] = heart[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def eyes():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Vision Analysis")
    st.write("Examine your eye if you have any Problem.")
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    eyes = {'sunken_eyes':1,'pain_behind_the_eye': 2,'yellowish_eyes': 3,'blurred_and_distorted_vision':4, 'redness_of_eyes':5, 'puffy_face_and_eyes':6, 'watering_from_eyes':7,'visual_disturbance':8}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    col1, col2 = st.columns(2)
    with col1:
        for i in eyes.keys():
            check = st.checkbox(i)
            if check:
                eyes[i] = 1
            else:
                eyes[i] = 0
    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in eyes.keys():
            if i == j:
                val[d[i]] = eyes[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]

    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def mental():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Mental Health Analysis")
    st.write("Know your mental health and behavioral impacts.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    mental = {'anxiety':1,'mood_swings':2, 'restlessness':3, 'lethargy':4, 'malaise':5, 'dizziness':6, 'irritability':7, 'altered_sensorium':8, 'lack_of_concentration':9}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in mental.keys():
            check = st.checkbox(i)
            if check:
                mental[i] = 1
            else:
                mental[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in mental.keys():
            if i == j:
                val[d[i]] = mental[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def excretary():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Excretary and Urinary track Analysis")
    st.write("Examine your excretary and urinary track problem.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    excretary = {'burning_mictrurition':1, 'spotting_ urination':2, 'dark_urine':3, 'diarrhoea':4, 'yellow_urine':5, 'fluid_overload.1':6, 'pain_during_bowel_movements':7, 'pain_in_anal_region':8, 'bloody_stool':9, 'irritation_in_anus':10, 'bladder_discomfort':11,'foul_smell_in_urine':12, 'continous_feel_in_urination':13, 'passage_of_gas':14, 'poluria':15, 'receving_blood_transfusion':16, 'receving_unsterile_infection':17}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in excretary.keys():
            check = st.checkbox(i)
            if check:
                excretary[i] = 1
            else:
                excretary[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in excretary.keys():
            if i == j:
                val[d[i]] = excretary[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def digestive():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Stomach and Digestive Analysis")
    st.write("Examine your digestive track if you are facing problem.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    stomach = {'acidity':1, 'stomach_pain':2, 'vomiting':3, 'irregular_sugar_level':4, 'indigestion':5, 'loss_of_appetiate':6, 'constipation':7, 'abdominal_pain':8, 'swelling_of_stomach':9, 'obesity':10, 'excessive_hunger':11, 'belly_pain':12, 'increases_appetite':13, 'stomach_bleeding':14, 'distention_of_abdomen':15}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in stomach.keys():
            check = st.checkbox(i)
            if check:
                stomach[i] = 1
            else:
                stomach[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in stomach.keys():
            if i == j:
                val[d[i]] = stomach[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def bones_muscles_joints():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Bones, Joints and Muscles Analysis")
    st.write("Examine Bones, Joints and Muscles if you are facing problem.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    bones_muscles_joints = {'join_pain':1, 'muscle_wasting':2, 'back_pain':3, 'weakness_in_limbs':4, 'cramps':5, 'swollen_legs':6, 'knee_pain':7, 'hip_joint_pain':8, 'muscle_weakness':9, 'stiff_neck':10, 'swelling_in_joints':11, 'movements_stiffness':12, 'spinning_movements':13, 'muscle_pain':14, 'painful_walks':15}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in bones_muscles_joints.keys():
            check = st.checkbox(i)
            if check:
                bones_muscles_joints[i] = 1
            else:
                bones_muscles_joints[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in bones_muscles_joints.keys():
            if i == j:
                val[d[i]] = bones_muscles_joints[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def oral():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Oral Problem Analysis")
    st.write("Examine your oral health if you have any Problem.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    oral = {'ulcers_on_tongue':1, 'nausea':2, 'drying_and_tingling_lips':3, 'slurred_tongue':4, 'mucoid_sputum':5, 'rusty_sputum':6, 'blood_in_sputum':7, 'cough':8, 'swelled_lymph_nodes':9, 'phelgm':10, 'throat_irritation':11, 'enlarged_thyroid':12}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in oral.keys():
            check = st.checkbox(i)
            if check:
                oral[i] = 1
            else:
                oral[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in oral.keys():
            if i == j:
                val[d[i]] = oral[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def nasal():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Nasal and Allergic Problem Analysis")
    st.write("Examine your nasal or respiratory track if you have any Problem.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    nose = {'continous_sneezing':1, 'breathlessness':2, 'sinus_infection':3, 'runny_nose':4, 'congestions':5, 'loss_of_smell':6, 'red_sore_around_nose':7}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in nose.keys():
            check = st.checkbox(i)
            if check:
                nose[i] = 1
            else:
                nose[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in nose.keys():
            if i == j:
                val[d[i]] = nose[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def body():
    if st.button("Go to Home Page"):
        st.session_state.page = "home_page"

    st.title("Body Problem Analysis")
    st.write("Examine your body if you have fever, tiredness or other problems.")
    col1, col2 = st.columns(2)
    col = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload.1','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
    d = dict()
    for i in range(len(col)):
        d[col[i]] = i

    body = {'shivering':1, 'chills':2, 'fatigue':3, 'weight_gain':4, 'cold_hands_and_feets':5, 'weight_loss':6, 'high_fever':7, 'dehydration':8, 'sweating':9, 'headache':10, 'mild_fever':11, 'neck_pain':12, 'swollen_extremeties':13, 'brittle_nails':14, 'loss_of_balance':15, 'unsteadiness':16, 'weakness_of_one_body_side':17, 'red_spots_over_body':18, 'prominent_veins_on_calf':19, 'pus_filled_pimples':20, 'silver_like_dusting':21, 'skin_peeling':22, 'small_dents_in_nails':23, 'inflammatory_nails':24, 'blisters':25}
    others = {'acute_liver_failure': 1, 'swollen_blood_vessels': 2, 'external_marital_contact':3,'abdominal_menstruation': 4, 'family_history': 5, 'history_of_alcohol_consumption':6, 'yellow_crust_ooze': 7 }
    with col1:
        for i in body.keys():
            check = st.checkbox(i)
            if check:
                body[i] = 1
            else:
                body[i] = 0

    with col2:
        st.write("__Miscellaneous Symptoms:__")
        for i in others.keys():
            check = st.checkbox(i)
            if check:
                others[i] = 1
            else:
                others[i] = 0

    val = []
    for i in d.keys():
        val.append(0)
        for j in body.keys():
            if i == j:
                val[d[i]] = body[j]
    for i in d.keys():
        for j in others.keys():
            if i == j:
                val[d[i]] = others[j]


    df_test = pd.DataFrame(columns=col)
    df_test.loc[0] = np.array(val)

    if st.button("Check"):
        print(val)
        st.write(t.predict_test(df_test))



def result(res, state):
    st.title("RESULT")
    st.write(res)

    if st.button("Close"):
        st.session_state.page = state



# Conditionally render the selected page
if st.session_state.page == "home_page":
    home()
elif st.session_state.page == "comp_analysis":
    comp_analysis()
elif st.session_state.page == "skin_analysis":
    skin_analysis()
elif st.session_state.page == "heart_analysis":
    heart_analysis()
elif st.session_state.page == "eye_analysis":
    eyes()
elif st.session_state.page == "mental_analysis":
    mental()
elif st.session_state.page == "exec_analysis":
    excretary()
elif st.session_state.page == "diges_analysis":
    digestive()
elif st.session_state.page == "BMJ_analysis":
    bones_muscles_joints()
elif st.session_state.page == "oral_analysis":
    oral()
elif st.session_state.page == "nose_analysis":
    nasal()
elif st.session_state.page == "body_analysis":
    body()