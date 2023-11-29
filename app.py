import streamlit as st
from sqlalchemy import text

list_courses = ['', 'General English', 'Business English', 'TOEFL Preparation', 'IELTS Preparation']
list_gender = ['', 'Male', 'Female']

conn = st.connection("postgresql", type="sql", 
                     url="your_postgresql_connection_url_here")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS REGISTRATION (id serial, full_name varchar, gender char(25), \
                                                       course varchar, email varchar, phone_number varchar, address text, registration_date date);')
    session.execute(query)

st.header('KAMPUNG INGGRIS PARE REGISTRATION SYSTEM')
page = st.sidebar.selectbox("Choose Menu", ["View Data", "Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM registration ORDER BY id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Add Data'):
        with conn.session as session:
            query = text('INSERT INTO registration (full_name, gender, course, email, phone_number, address, registration_date) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':'', '6':'', '7':None})
            session.commit()

    data = conn.query('SELECT * FROM registration ORDER BY id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        full_name_lama = result["full_name"]
        gender_lama = result["gender"]
        course_lama = result["course"]
        email_lama = result["email"]
        phone_number_lama = result["phone_number"]
        address_lama = result["address"]
        registration_date_lama = result["registration_date"]

        with st.expander(f'a.n. {full_name_lama}'):
            with st.form(f'data-{id}'):
                full_name_baru = st.text_input("Full Name", full_name_lama)
                gender_baru = st.selectbox("Gender", list_gender, list_gender.index(gender_lama))
                course_baru = st.selectbox("Course", list_courses, list_courses.index(course_lama))
                email_baru = st.text_input("Email", email_lama)
                phone_number_baru = st.text_input("Phone Number", phone_number_lama)
                address_baru = st.text_input("Address", address_lama)
                registration_date_baru = st.date_input("Registration Date", registration_date_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE registration \
                                          SET full_name=:1, gender=:2, course=:3, email=:4, \
                                          phone_number=:5, address=:6, registration_date=:7 \
                                          WHERE id=:8;')
                            session.execute(query, {'1':full_name_baru, '2':gender_baru, '3':course_baru, '4':email_baru, 
                                                    '5':phone_number_baru, '6':address_baru, '7':registration_date_baru, '8':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM registration WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
