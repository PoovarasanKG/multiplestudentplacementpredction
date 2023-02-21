import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

basic_model = pickle.load(open('model.pkl', 'rb'))

place_model = pickle.load(open('model_place.pkl', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Student Placement Prediction System',
                          
                          ['Basic Information to Prediction',
                           'Placement Skillset Information Prediction'],
                          icons=['activity','kanban'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Basic Information to Prediction'):
    
    # page title
    st.title('Basic Information Prediction using ML - KNN Classifier')
    
    
    gender = st.number_input("Enter Gender(Female=0, Male=1)", step=1, value=0)
    stream = st.number_input("Enter Stream(Civil=0, CSE=1, Electronics=2,EnTC=3, IT=4, Mechanical=5)",step=1, value=0)
    intern = st.number_input("Enter Previous Internships",step=1, value=0)
    cgpa = st.number_input("Enter CGPA",step=1, value=0)
    backlogs = st.number_input("Enter backlogs",step=1, value=0)	

    
    
    # code for Prediction
    result_baisc =""
    
    # creating a button for Prediction
    
    if st.button('Predict The Result'):
        basic_pred = basic_model.predict([[gender, stream, intern, cgpa, backlogs]])
        
        if (basic_pred[0] == 1):
          result_baisc = "You're Placed"
          st.success(result_baisc)
          st.success("Good luck, and your studies will continue to prepare you for your future career...")

        else:
          result_baisc = "You're Not Placed"
          st.success(result_baisc)
          st.success("Better luck next time, and your studies will focus on your CGPA and clearing your backlogs for future career advancement...")

    #st.success(result_baisc)




# Placement In.fo Prediction Page
if (selected == 'Placement Skillset Information Prediction'):
    
    # page title
    st.title('Placement Information Prediction using ML - KNN Classifier')
    
    quants = st.number_input("Enter Quants(Please Enter 1 to 25 of Score)", step=1, value=0)
    logical = st.number_input("Enter LogicalReasoning (Please Enter 1 to 25 of Score)",step=1, value=0)
    verbal = st.number_input("Enter Verbal (Pleace Enter 1 to 25 of Score)",step=1, value=0)
    program = st.number_input("Enter Programming (Please Enter 1 to 25 of Score)",step=1, value=0)
    cgpa = st.number_input("Enter CGPA (Please Enter 1 to 10 of Grade)",step=1, value=0)	
     
    # code for Prediction
    result_place =""     
    
    # creating a button for Prediction
    
    if st.button('Predict The Result'):
        place_pred = place_model.predict([[quants, logical, verbal, program, cgpa]])                          
        
        if (place_pred[0] == 1):
          result_place = "You're Selected"
          st.success(result_place)
          st.success("Congratulations on being placed Keep in touch with your abilities and progress. Learn new technologies...")

        else:
          result_place = "You're Not Selected"
          st.success(result_place)
          st.success("Sorry for conveying this, please concentrate on your programming skills and aptidudes!")
        
