import streamlit as st
from PIL import Image

# Hardcoded user credentials
users = {
    "papa": "papa",
    "tara": "tara"
}

# Login function
def check_login(username, password):
    return username in users and users[username] == password

# Login form
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button('Login'):
    if check_login(username, password):
        st.success('Logged in as {}'.format(username))

        # Votre application Streamlit ici
        st.title(f"Merry Christmas Papa and Tara!")

        # message
        st.subheader("A Special Christmas Message")
        st.write("Merry Christmas! I am happy and grateful to have you as my family. "
                 "I am fulfilled because of you, and living with you every day is a joy for me. "
                 "I love you, and Merry Christmas!!!")

        # Image upload section
        uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)

    else:
        st.error('Incorrect username or password')

# If not logged in, show nothing (or you can customize this part)
else:
    st.info('Please enter your username and password')
