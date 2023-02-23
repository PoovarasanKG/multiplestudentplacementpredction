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
                           'Placement Skillset Information Prediction',
                            'FeedBack Form Page'
                           ],
                          icons=['activity','kanban','heart'],
                          default_index=0)
    
    
# Basic Information Prediction Page
if (selected == 'Basic Information to Prediction'):
    
    # page title
    st.title('Student Placement Prediction Application')

    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Basic Information Prediction using ML - KNN Classifier </h1>
    </div>
    """
	
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
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
    st.title('Student Placement Prediction Application')

    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Placement Skillset Information Prediction using ML - KNN Classifier</h1>
    </div>
    """
	
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
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



#feedback activity
if (selected == 'FeedBack Form Page'):
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formsubmit.co/poovarasankg@gmail.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <p>Please select Prediction is Right or Wrong ?</p>
     <input type="radio" id="Right" name="pred_result" value="Right">
     <label for="Right">Right</label><br>
     <input type="radio" id="Wrong" name="pred_result" value="Wrong">
     <label for="Wrong">Wrong</label>
     <textarea name="message" placeholder="Any Suggestion Leave here..."></textarea>
     <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    
    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")


        
