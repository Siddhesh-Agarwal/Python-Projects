import streamlit as st
from random import choice
 
st.title('Password Generator')
requirements = st.multiselect(label='Please choose the requirements of your new password:', 
                              options=['Small letters', 'Capital letters', 'Numbers', 'Special characters'],
                              default='Small letters',
                              help='The types of characters present in the generated password. More the types of characters, the safer the pasword.')
length = st.slider(label='Password length', 
                   min_value=8, 
                   max_value=32, 
                   value=12, 
                   help='Length of the password generated. Longer passwords are more secure.')

if st.button('Generate Password'):
    dataset = []
    password = ''
    allowed_types = 0
    if 'Small letters' in requirements:
        dataset.append('abcdefghijklmnopqrstuvwxyz')
        allowed_types += 1
    if 'Capital letters' in requirements:
        dataset.append('ABCDEFGHIJKLMNOPQRSTUVWXY')
        allowed_types += 1
    if 'Numbers' in requirements:
        dataset.append('0123456789')
        allowed_types += 1
    if 'Special characters' in requirements:
        dataset.append('!@#$%^&*.?-_+')
        allowed_types += 1
    if allowed_types == 0:
        st.warning('Choosing atleast one options from requirements is necessary.')

    if len(dataset) > 0:
        for _ in range(length):
            password += choice(choice(dataset))
        st.info(password)