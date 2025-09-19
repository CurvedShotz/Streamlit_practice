#USSD Streamlit

import streamlit  as st

with st.sidebar:
    st.header('SIde Bar')
    st.Page('./ussd_streamlit.py',title="Registration Page" )   
    st.Page('pages/ussd2.py',title="USSD PAGE")
    st.Page('pages/visuals.py',title="Visualization")
    

st.markdown('''
 
<h1 style="text-align: center;">Registration Form</h1>


''',unsafe_allow_html=True)

with st.form("Registration Form"):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("First Name:")
    l_name = col2.text_input("Last Name:")
    email = st.text_input("Email:")
    age = st.number_input("Age:")
    col1,col2, col3 = st.columns(3)
    day = col1.text_input("Day:")
    month = col2.text_input("Month:")
    year = col3.text_input("Year:")
    password = st.text_input("Password:")
    confirm_password = st.text_input("Confirm Password")
    if confirm_password != password:
        st.warning("Error Passwords Must Match")
    submit_btn = st.form_submit_button("Submittt")

    if submit_btn:
        if confirm_password != password:
            st.warning("Error Passwords Must Match")
    
#SESSION STATE COUNTER
if "registration" not in st.session_state:
    st.session_state.registration = []

CAPACITY = 5

st.title("Ticket Booking")

if len(st.session_state.registration) >= CAPACITY:
    st.error("Registration Closed - 5 people have already registered.")
    st.write("### Current Registration")
    st.table(st.session_state.registration)

else:
    with st.form("booking_form"):
        st.text_input("Enter your name", key="name")
        st.selectbox("Select your destination: ", options=['New York','London','Tokyo'], key="destination")
        st.date_input("Select your travel date:", key="travel_date")

        if st.form_submit_button("Book Now"):
            booking = {
                "Name": st.session_state.name,
                "Destination": st.session_state.destination,
                "Travel Date": st.session_state.travel_date
            }
            st.session_state.registration.append(booking)

            st.success("Ticket booked successfully")
            st.write("Name:" ,st.session_state.name)
            st.write("Destination",st.session_state.destination)
            st.write("Travel Date", st.session_state.travel_date)

        elif st.form_submit_button("Reset"):
            st.info("Form reset.")

        else:
            st.write("Please fill out the form to book your ticket.")

        st.write("### Current Registration")
        if st.session_state.registration:
            st.table(st.session_state.registration)