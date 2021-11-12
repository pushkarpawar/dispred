import numpy as np
import pandas as pd
import pickle
import flask
import warnings
from flask import request,redirect, url_for
warnings.filterwarnings('ignore')


data = pd.read_csv("new_test_data.csv")
diseases = data.iloc[:,-1]

symptoms_name = ["itching", "skin_rash", "nodal_skin_eruptions", "yellowish_skin", "bruising", "internal_itching", "red_spots_over_body", "dischromic _patches", "blackheads", "pus_filled_pimples", "skin_peeling", "blister", "yellow_crust_ooze","continuous_sneezing", "shivering", "chills", "cold_hands_and_feets","joint_pain", "headache", "pain_behind_the_eyes", "back_pain", "abdominal_pain", "chest_pain", "pain_during_bowel_movements", "pain_in_anal_region", "neck_pain", "knee_pain",  "hip_joint_pain", "muscle_pain", "belly_pain", "painful_walking","stomach_pain", "acidity", "indigestion", "constipation", "swelling_of_stomach", "bladder_discomfort", "stomach_bleeding", "distention_of_abdomen", "bloody_stool","ulcers_on_tongue", "patches_in_throat", "sunken_eyes", "swelled_lymph_nodes", "blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion", "puffy_face_and_eyes", "drying_and_tingling_lips", "stiff_neck", "loss_of_smell", "watering_from_eyes", "mucoid_sputum", "rusty_sputum", "visual_disturbances", "blood_in_sputum", "red_sore_around_nose", "yellowing_of_eyes","muscle_wasting", "weakness_in_limbs", "cramps", "muscle_weakness", "palpitations", "acute_liver_failure", "fast_heart_rate","vomiting", "fatigue", "weight_gain", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "cough", "high_fever", "breathlessness", "sweating", "dehydration", "nausea", "loss_of_appetite", "diarrhoea", "mild_fever", "fluid_overload", "malaise", "irritation_in_anus", "dizziness", "obesity", "swollen_legs", "swollen_blood_vessels", "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "extra_marital_contacts", "slurred_speech", "swelling_joints", "movement_stiffness", "spinning_movements", "loss_of_balance", "unsteadiness", "weakness_of_one_body_side", "passage_of_gases", "toxic_look_(typhos)", 
"abnormal_menstruation", "increased_appetite", "family_history", "receiving_blood_transfusion", "receiving_unsterile_injections", "coma", "history_of_alcohol_consumption","fluid_overload" ,"prominent_veins_on_calf", "scurring", "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails","polyuria", "burning_micturition", "spotting_ urination", "dark_urine", "yellow_urine", "foul_smell_of urine", "continuous_feel_of_urine","anxiety", "mood_swings", "excessive_hunger", "depression", "irritability", "altered_sensorium", "lack_of_concentration"]

#for col in data.columns: 
    #symptoms_name.append(col)

symptoms_dict = {}
for i in range (len(symptoms_name)):
    symptoms_dict[symptoms_name[i]]=0

symptoms_value=[0 for i in range(len(symptoms_name))]

global input_variables
global prediction
global link

usr_name_list = []
comment_list = []

 
# Use pickle to load in the pre-trained model.
with open(f'model/ml_algo_pred.pkl', 'rb') as f:
    model = pickle.load(f)
    
app = flask.Flask(__name__, template_folder='templates' )

@app.route('/')
def main():
    return(flask.render_template('opening1.html'))
if __name__ == '__main__':
    app.run()


@app.route('/symptoms', methods=['GET', 'POST'])
def main1():

    #link=''

    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':

        for i in range (132):
            symptoms_value[i] = flask.request.form[symptoms_name[i]]
            
                    
        for i in range (len(symptoms_name)):
            symptoms_dict[symptoms_name[i]] = symptoms_value[i]


        input_variables = pd.DataFrame([symptoms_value], columns = symptoms_name, dtype=int)

        prediction = model.predict(input_variables)[0]

        main1.link = prediction
        main1.link = main1.link + '.html'

                      
        return flask.render_template('main.html',len = len(symptoms_name), symptom = symptoms_name, result=prediction)
        

@app.route('/solution')
def main2():

    return(flask.render_template(main1.link))


@app.route('/solution2', methods=['GET', 'POST'])
def main22():
    if flask.request.method == 'GET':
        return(flask.render_template('solutions.html'))
    
    if flask.request.method == 'POST':
        disease22 = request.form.get("disease")

        if(disease22):
            lol = 'lol'
        else:
            disease22 = ""

        main1.link = disease22
        main1.link = main1.link + '.html'

        return flask.render_template('solutions.html',diseases = diseases ,disease=disease22)
        


@app.route('/hospitals', methods=['GET', 'POST'])
def main3():

    if flask.request.method == 'GET':
        return(flask.render_template('hospitals1.html'))
    
    if flask.request.method == 'POST':

        disease = request.form.get("disease")
        if(disease):
            lol = 'lol'
        else:
            disease = ""

        cities = ['Pune', 'Nagpur', 'Nashik']

        city = request.form.get("city")
        if(city):
            lol = 'loool'
        else:
            city = ""

        hospitals = {}

        hospitals_name = {'Pune':{'Dengue':["Gulati's Clinic : Dr. Jyoti Gulati","Surana Clinic : Dr Anuj Surana","Arogya Clinic : Dr. Manisha A Gosavi"] , 'Diabetes':["Prudent International Health Clinic : Dr. Amit Sakaria","Jupiter Hospital : Dr. Vinayak Harale","Surana Clinic : Dr Anuj Surana"], 'Malaria':["NRS Hospital : Dr. Narayan Survase","Alloveda Clinic : Dr. Abhijeet Baldota","Aaiina Clinic : Dr Vaibhav Lunkad"]},
                          'Nagpur':{'Dengue':["Sparsh Clinic : Dr. Ajit Mahant","Kalbande Nursing Home : Dr. Vinay Kalbande","Dr. Vrinda Padhye Clinic"] , 'Diabetes':["Vims : Dr Hari Gupta","Dr. Himanshu Patil","Dr Mune Psychological Health Treatment"], 'Malaria':["Wockhardt Super Speciality Hospital : Dr. Shelke Umesh Ravikant","Sawarkar Multispeciality Hospital And Mahindra's Health Retreat : Dr. Mahendra M. Sawarkar","Mother Care Nursing Home : Dr. Sunita Dhande"]},
                          'Nashik':{'Dengue':['h1','h2','h3'] , 'Diabetes':['h4','h5','h6'], 'Malaria':['h7','h8','h9']}}

        hospitals_address = {'Pune':{'Dengue':["204, Supreme Centre, ITI Road, Landmark: Above PNG Jwellers, Aundh, Pune","Surana clinic, 108 , first floor, Velstand opp. reliance mart, Bypass road, Mundhwa - Kharadi Rd, Kharadi, Pune","2, Gayatri, Ram Society, Yerwada , OFF Alandi Road, Opposite Hari Ganga Society, Next to RTO Office, Vishrantwadi, Pune"] , 'Diabetes':["C1/101, Silver Oak Society, Bishop School Road, Landmark: Above Bank of Maharashtra, Kalyani Nagar, Pune","Baner- Pimple Nilakh Road, Landmark: Near Prathamesh Park, Pune","Surana clinic, 108 , first floor, Velstand opp. reliance mart, Bypass road, Mundhwa - Kharadi Rd, Kharadi, Pune"], 'Malaria':["Solitaire Business Hub Kalewadi Phata, Opposite Ambience Hotel, Wakad, Pune","1st Floor, Lav Kush Apartments, Seasons Road, Near Hotel Season, Opposite to Chintamani Society, Near Hyundai Showroom, Aundh, Pune","162 shukrawarpeth, Near Kelkar Museum,opposite Badami Gym, Off Bajirao Road., Near Badami Houd Sangh, Shukrawar Peth, Pune"]},
                          'Nagpur':{'Dengue':["51, Falke Layout, Aakar Nagar Road, Friends Colony, Beside Ketan Medicals, On The Road To Fire College / Nisarg Lawn, Katolroad, Nagpur","Kalbande Nursing Home, #3, Sahayog Nagar, Jaripatka, Nagpur","Gokul Vaibhav Complex 179-A, Shivaji Nagar, Dharampeth, Nagpur"] , 'Diabetes':["Mohan Nagar, Kamptee Road, Sadar Bazar, Near LIC Square, Nagpur - 440001","A Wing, 2nd Floor, Niti Gaurav Complex, Ramdas Peth, Nagpur - 440010","Hypnosis Healing Foundation, Dwarkapuri Sq, Shatabdi Chowk, Nagpur - 440027, Mind Clinic"], 'Malaria':["1643, North Ambazari Road, Shankar Nagar Square, Nagpur","Khadi gramudyog Bhawan, Tilak Putla, Mahal , Gandhi sagar ., Landmark: Opp.Gandhisagar East, Nagpur","5th Floor, Midas Heights, Central Bazar Road, Landmark: Opposite Tarun Bharat Press, Nagpur"]},
                          'Nashik':{'Dengue':['a1','a2','a3'] , 'Diabetes':['a4','a5','a6'], 'Malaria':['a7','a8','a9']}}

        hospitals_contact = {'Pune':{'Dengue':['022 4893 2704','083292 44983','080 3729 6834'] , 'Diabetes':['022 4890 4353','020 4855 2640','083292 44983'], 'Malaria':['020 7117 2440','099226 68668','020 7118 8490']},
                          'Nagpur':{'Dengue':['095953 01509','099230 84612','712 2248436'] , 'Diabetes':['9890924509','07947443698','07947290522'], 'Malaria':['022 4893 3407','020 7117 7297','022 4893 3683']},
                          'Nashik':{'Dengue':['01','02','03'] , 'Diabetes':['04','05','06'], 'Malaria':['07','08','09']}}

        if(city and disease):
            final_hospitals = hospitals_name[city][disease]
            final_address = hospitals_address[city][disease]
            final_contact = hospitals_contact[city][disease]
        else:
            final_hospitals = ['']
            final_address = ['']
            final_contact = ['']
        
              

        return flask.render_template('hospitals1.html',diseases = diseases ,disease=disease, cities=cities, city=city,final_hospitals=final_hospitals, final_address= final_address,final_contact=final_contact)
        
    


@app.route('/comments', methods=['GET', 'POST'])
def main4():

    if flask.request.method == 'GET':
        return(flask.render_template('comments12.html'))
    
    if flask.request.method == 'POST':
  
        usr_name = request.form.get("usrname")

        comment = request.form.get("comment")

               
        if(usr_name):
            lol = 'lol'
        else:
            usr_name = "Unknown"

        if(comment):
            comment_list.append(comment)
        else:
            lol = 'lol'
            
        usr_name_list.append(usr_name)
               
       

        return flask.render_template('comments12.html',usr_name=usr_name, comment=comment, usr_name_list=usr_name_list, comment_list=comment_list, length=len(usr_name_list))
