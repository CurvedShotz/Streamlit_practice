import streamlit as st

st.title("USSD APP")
ussd = st.text_input('Input Ussd',)

if ussd =='*312#':
    st.markdown('''
    Welcome to the USSD PRO MAX
    Select an option:
    1. Data plan
    2. Check Balance
    3. Recharge
    4. Exit
    ''')
    ussd == ''
else:
    # st.warning("Invalid")
    
    if ussd == '1':
        st.markdown('''
        Select a data plan:
        1. 1GB for ₦100
        2. 2GB for ₦200
        3. 3.2GB for ₦300
        4. 4GB for ₦400
        5. 5GB for ₦500
        6. Exit
            ''')
        ussd = ''
        if ussd == '1':
            st.markdown("1GB Bought Successfully")
        if ussd == '6':
            exit(0)