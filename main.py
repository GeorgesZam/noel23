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

# Initialisation du session state pour les souvenirs
if 'souvenirs' not in st.session_state:
    st.session_state['souvenirs'] = []

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

        st.title("Album de famille")

        # Téléchargement des photos
        uploaded_files = st.file_uploader("Téléchargez vos photos de famille", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.image(bytes_data, caption=uploaded_file.name, use_column_width=True)

        # Souvenirs et histoires
        st.write("Partagez vos souvenirs et histoires de famille ici :")
        user_memory = st.text_area("Votre souvenir ou histoire", height=150)

        if st.button('Partager le souvenir'):
            st.session_state['souvenirs'].append(user_memory)
            st.success("Souvenir partagé !")

        # Afficher tous les souvenirs
        if st.session_state['souvenirs']:
            st.write("Souvenirs partagés :")
            for souvenir in st.session_state['souvenirs']:
                st.text_area("Souvenir", value=souvenir, height=100, key=souvenir)

    else:
        st.error('Incorrect username or password')

# If not logged in, show nothing (or you can customize this part)
else:
    st.info('Please enter your username and password')
