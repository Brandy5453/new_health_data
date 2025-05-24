# import streamlit as st
# import mysql.connector4
# import pandas as pd
# from datetime import datetime
# import re

# # Database connection configuration
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="@Akpakli123",
#         database="screen"
#     )

# # Database setup
# def init_db():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS screening (
#         id VARCHAR(36) PRIMARY KEY,
#         first_name VARCHAR(255),
#         last_name VARCHAR(255),
#         other_name VARCHAR(255),
#         sex VARCHAR(10),
#         date_of_birth VARCHAR(10),
#         nationality VARCHAR(100),
#         area_of_residence VARCHAR(255),
#         religion VARCHAR(50),
#         contact_number VARCHAR(15),
#         religious_denomination VARCHAR(255),
#         emergency_contact_name VARCHAR(255),
#         emergency_contact_number VARCHAR(15),
#         emergency_contact_relationship VARCHAR(100),
#         marital_status VARCHAR(50),
#         occupation VARCHAR(255),
#         blood_group VARCHAR(10),
#         hepatitis_b VARCHAR(10),
#         vaccine_shots TEXT,
#         sugar_level VARCHAR(50),
#         bp_levels VARCHAR(50),
#         height VARCHAR(10),
#         weight VARCHAR(10),
#         hiv_status VARCHAR(20),
#         created_at VARCHAR(20)
#     )''')
#     conn.commit()
#     conn.close()

# # Generate custom ID (ICGChealth1, ICGChealth2, etc.)
# def generate_custom_id():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute("SELECT id FROM screening WHERE id LIKE 'ICGChealth%'")
#     ids = c.fetchall()
#     conn.close()
    
#     max_num = 0
#     for id_tuple in ids:
#         id_str = id_tuple[0]
#         num = int(id_str.replace('ICGChealth', '')) if id_str.startswith('ICGChealth') else 0
#         max_num = max(max_num, num)
    
#     return f'ICGChealth{max_num + 1}'

# # Validate phone number
# def is_valid_phone(phone):
#     pattern = r'^\+?\d{10,15}$'
#     return re.match(pattern, phone) is not None

# # Add new record
# def add_record(data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''INSERT INTO screening (
#         id, first_name, last_name, other_name, sex, date_of_birth, nationality,
#         area_of_residence, religion, contact_number, religious_denomination,
#         emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#         marital_status, occupation, blood_group, hepatitis_b, vaccine_shots,
#         sugar_level, bp_levels, height, weight, hiv_status, created_at
#     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
#     data + (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
#     conn.commit()
#     conn.close()

# # Search record by ID
# def search_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM screening WHERE id = %s', (record_id,))
#     record = c.fetchone()
#     conn.close()
#     return record

# # Delete record by ID
# def delete_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('DELETE FROM screening WHERE id = %s', (record_id,))
#     conn.commit()
#     conn.close()

# # Update lab results
# def update_lab_results(record_id, lab_data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''UPDATE screening SET
#         blood_group = %s, hepatitis_b = %s, vaccine_shots = %s,
#         sugar_level = %s, bp_levels = %s, height = %s, weight = %s, hiv_status = %s
#         WHERE id = %s''', lab_data + (record_id,))
#     conn.commit()
#     conn.close()

# # List of all countries for nationality dropdown
# countries = [
#     "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
#     "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
#     "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
#     "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
#     "Chile", "China", "Colombia", "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Croatia",
#     "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
#     "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
#     "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
#     "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
#     "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos",
#     "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
#     "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
#     "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
#     "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia",
#     "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
#     "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
#     "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
#     "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
#     "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden",
#     "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
#     "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
#     "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
#     "Yemen", "Zambia", "Zimbabwe"
# ]

# # Streamlit app
# st.set_page_config(page_title="Church Health Screening App", layout="wide")

# # Custom CSS for styling
# st.markdown("""
# <style>
#     body {
#         background-color: #FFFFFF;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 5px;
#     }
#     .stTextInput>div>input {
#         border: 2px solid #2196F3;
#         border-radius: 5px;
#     }
#     .stSelectbox>div>div {
#         border: 2px solid #2196F3;
#         border-radius: 5px;
#     }
#     .sidebar .sidebar-content {
#         background-color: #F0F8FF;
#     }
#     .stRadio > label {
#         background-color: #E0FFFF;
#         padding: 10px;
#         border-radius: 5px;
#         margin-bottom: 5px;
#     }
#     .stRadio > label:hover {
#         background-color: #B0E0E6;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Initialize database
# try:
#     init_db()
# except mysql.connector.Error as err:
#     st.error(f"Database connection failed: {err}")
#     st.stop()

# # Sidebar navigation
# with st.sidebar:
#     st.header("Health Screening")
#     page = st.radio("Select Option", ["Bio Data", "Lab Results"])

# # Bio Data page
# if page == "Bio Data":
#     st.header("Add Bio Data")
#     with st.form("bio_data_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             first_name = st.text_input("First Name", placeholder="Enter first name")
#             last_name = st.text_input("Last Name", placeholder="Enter last name")
#             other_name = st.text_input("Other Name", placeholder="Enter other name (optional)")
#             sex = st.selectbox("Sex", ["Male", "Female"])
#             date_of_birth = st.date_input("Date of Birth")
#             nationality = st.selectbox("Nationality", countries, placeholder="Select nationality")
#             area_of_residence = st.text_input("Area of Residence", placeholder="Enter area")
#         with col2:
#             religion = st.selectbox("Religion", ["Christian", "Islamic", "Traditionalist", "Others"])
#             contact_number = st.text_input("Contact Number", placeholder="Enter phone number")
#             religious_denomination = st.text_input("Religious Denomination", placeholder="Enter denomination")
#             emergency_contact_name = st.text_input("Emergency Contact Name", placeholder="Enter name")
#             emergency_contact_number = st.text_input("Emergency Contact Number", placeholder="Enter phone number")
#             emergency_contact_relationship = st.text_input("Emergency Contact Relationship", placeholder="Enter relationship")
#             marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
#             occupation = st.text_input("Occupation", placeholder="Enter occupation")
        
#         submit = st.form_submit_button("Save Bio Data")
#         if submit:
#             if not first_name or not last_name or not contact_number or not emergency_contact_name or not emergency_contact_number:
#                 st.error("Please fill in all required bio data fields.")
#             elif not is_valid_phone(contact_number) or not is_valid_phone(emergency_contact_number):
#                 st.error("Please enter valid phone numbers (10-15 digits, optional '+' prefix).")
#             else:
#                 record_id = generate_custom_id()
#                 data = (
#                     record_id, first_name, last_name, other_name, sex, str(date_of_birth),
#                     nationality, area_of_residence, religion, contact_number, religious_denomination,
#                     emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#                     marital_status, occupation, "", "", "", "", "", "", "", ""
#                 )
#                 try:
#                     add_record(data)
#                     st.success(f"Bio data saved successfully! ID: {record_id}")
#                 except mysql.connector.Error as err:
#                     st.error(f"Error saving record: {err}")

# # Lab Results page
# elif page == "Lab Results":
#     st.header("Search and Update Lab Results")
#     search_id = st.text_input("Enter Record ID to Search", placeholder="e.g., ICGChealth1")
#     if search_id:
#         try:
#             record = search_record(search_id)
#             if record:
#                 st.subheader("Record Details")
#                 df = pd.DataFrame([record], columns=[
#                     'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                     'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                     'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                     'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                     'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#                 ])
#                 st.dataframe(df, use_container_width=True)
                
#                 with st.form("lab_results_form"):
#                     col1, col2 = st.columns(2)
#                     with col1:
#                         blood_group = st.selectbox("Blood Group", ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"].index(record[16]) if record[16] else 0)
#                         hepatitis_b = st.selectbox("Hepatitis B", ["", "Positive", "Negative"], index=["", "Positive", "Negative"].index(record[17]) if record[17] else 0)
#                         vaccine_shots = st.text_input("Vaccine Shots", value=record[18] or "", placeholder="Enter vaccine details")
#                         sugar_level = st.text_input("Sugar Level", value=record[19] or "", placeholder="Enter sugar level (mg/dL)")
#                     with col2:
#                         bp_levels = st.text_input("Blood Pressure", value=record[20] or "", placeholder="Enter BP (e.g., 120/80 mmHg)")
#                         height = st.text_input("Height", value=record[21] or "", placeholder="Enter height (cm)")
#                         weight = st.text_input("Weight", value=record[22] or "", placeholder="Enter weight (kg)")
#                         hiv_status = st.selectbox("HIV Status", ["", "Positive", "Negative", "Unknown"], index=["", "Positive", "Negative", "Unknown"].index(record[23]) if record[23] else 0)
                    
#                     col_submit, col_delete = st.columns(2)
#                     with col_submit:
#                         update = st.form_submit_button("Update Lab Results")
#                     with col_delete:
#                         delete = st.form_submit_button("Delete Record")
                    
#                     if update:
#                         lab_data = (blood_group, hepatitis_b, vaccine_shots, sugar_level, bp_levels, height, weight, hiv_status)
#                         try:
#                             update_lab_results(search_id, lab_data)
#                             # Re-fetch the record to update the DataFrame
#                             updated_record = search_record(search_id)
#                             if updated_record:
#                                 df = pd.DataFrame([updated_record], columns=[
#                                     'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                                     'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                                     'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                                     'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                                     'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#                                 ])
#                                 st.dataframe(df, use_container_width=True)
#                                 st.success("Lab results updated successfully!")
#                             else:
#                                 st.error("Error retrieving updated record.")
#                         except mysql.connector.Error as err:
#                             st.error(f"Error updating record: {err}")
                    
#                     if delete:
#                         try:
#                             delete_record(search_id)
#                             st.success("Record deleted successfully!")
#                             st.experimental_rerun()  # Refresh to clear the form
#                         except mysql.connector.Error as err:
#                             st.error(f"Error deleting record: {err}")
#             else:
#                 st.error("No record found with this ID.")
#         except mysql.connector.Error as err:
#             st.error(f"Error searching record: {err}")
#     else:
#         st.info("Please enter a valid Record ID.")



# import streamlit as st
# import sqlite3
# import pandas as pd
# from datetime import datetime
# import re

# # Database connection configuration
# def get_db_connection():
#     return sqlite3.connect("health_screening.db", check_same_thread=False)

# # Initialize database
# def init_db():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS screening (
#         id VARCHAR(36) PRIMARY KEY,
#         first_name VARCHAR(255),
#         last_name VARCHAR(255),
#         other_name VARCHAR(255),
#         sex VARCHAR(10),
#         date_of_birth VARCHAR(10),
#         nationality VARCHAR(100),
#         area_of_residence VARCHAR(255),
#         religion VARCHAR(50),
#         contact_number VARCHAR(15),
#         religious_denomination VARCHAR(255),
#         emergency_contact_name VARCHAR(255),
#         emergency_contact_number VARCHAR(15),
#         emergency_contact_relationship VARCHAR(100),
#         marital_status VARCHAR(50),
#         occupation VARCHAR(255),
#         blood_group VARCHAR(10),
#         hepatitis_b VARCHAR(10),
#         vaccine_shots TEXT,
#         sugar_level VARCHAR(50),
#         bp_levels VARCHAR(50),
#         height VARCHAR(10),
#         weight VARCHAR(10),
#         hiv_status VARCHAR(20),
#         created_at VARCHAR(20)
#     )''')
#     conn.commit()
#     conn.close()

# # Generate unique ID
# def generate_custom_id():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute("SELECT id FROM screening WHERE id LIKE 'ICGChealth%'")
#     ids = c.fetchall()
#     conn.close()
#     max_num = max([int(i[0].replace('ICGChealth', '')) for i in ids if i[0].startswith('ICGChealth')] + [0])
#     return f'ICGChealth{max_num + 1}'

# # Validate phone number
# def is_valid_phone(phone):
#     return re.match(r'^\+?\d{10,15}$', phone) is not None

# # Add record
# def add_record(data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''INSERT INTO screening (
#         id, first_name, last_name, other_name, sex, date_of_birth, nationality,
#         area_of_residence, religion, contact_number, religious_denomination,
#         emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#         marital_status, occupation, blood_group, hepatitis_b, vaccine_shots,
#         sugar_level, bp_levels, height, weight, hiv_status, created_at
#     ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#     data + (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
#     conn.commit()
#     conn.close()

# # Search record
# def search_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM screening WHERE id = ?', (record_id,))
#     record = c.fetchone()
#     conn.close()
#     return record

# # Delete record
# def delete_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('DELETE FROM screening WHERE id = ?', (record_id,))
#     conn.commit()
#     conn.close()

# # Update lab results
# def update_lab_results(record_id, lab_data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''UPDATE screening SET
#         blood_group = ?, hepatitis_b = ?, vaccine_shots = ?,
#         sugar_level = ?, bp_levels = ?, height = ?, weight = ?, hiv_status = ?
#         WHERE id = ?''', lab_data + (record_id,))
#     conn.commit()
#     conn.close()

# # Fetch all records for display
# def fetch_all_records():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM screening ORDER BY created_at DESC')
#     records = c.fetchall()
#     conn.close()
#     return records

# # Page config and styling
# st.set_page_config(page_title="Church Health Screening App", layout="wide")
# st.markdown("""
# <style>
#     .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
#     .stTextInput>div>input, .stSelectbox>div>div { border: 2px solid #2196F3; border-radius: 5px; }
#     .sidebar .sidebar-content { background-color: #F0F8FF; }
# </style>
# """, unsafe_allow_html=True)

# try:
#     init_db()
# except sqlite3.Error as err:
#     st.error(f"Database connection failed: {err}")
#     st.stop()

# with st.sidebar:
#     st.header("Health Screening")
#     page = st.radio("Select Option", ["Bio Data", "Lab Results"])

# # Nationalities for dropdown
# countries = ["Ghana", "Nigeria", "Kenya", "USA", "UK"]  # Trimmed for brevity

# if page == "Bio Data":
#     st.header("Add Bio Data")
#     with st.form("bio_data_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             first_name = st.text_input("First Name")
#             last_name = st.text_input("Last Name")
#             other_name = st.text_input("Other Name")
#             sex = st.selectbox("Sex", ["Male", "Female"])
#             date_of_birth = st.date_input("Date of Birth")
#             nationality = st.selectbox("Nationality", countries)
#             area_of_residence = st.text_input("Area of Residence")
#         with col2:
#             religion = st.selectbox("Religion", ["Christian", "Islamic", "Others"])
#             contact_number = st.text_input("Contact Number")
#             religious_denomination = st.text_input("Religious Denomination")
#             emergency_contact_name = st.text_input("Emergency Contact Name")
#             emergency_contact_number = st.text_input("Emergency Contact Number")
#             emergency_contact_relationship = st.text_input("Emergency Contact Relationship")
#             marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
#             occupation = st.text_input("Occupation")

#         submit = st.form_submit_button("Save Bio Data")
#         if submit:
#             if not first_name or not last_name or not contact_number:
#                 st.error("Please solve all required fields.")
#             elif not is_valid_phone(contact_number) or not is_valid_phone(emergency_contact_number):
#                 st.error("Invalid phone number.")
#             else:
#                 record_id = generate_custom_id()
#                 data = (
#                     record_id, first_name, last_name, other_name, sex, str(date_of_birth), nationality,
#                     area_of_residence, religion, contact_number, religious_denomination,
#                     emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#                     marital_status, occupation, "", "", "", "", "", "", "", ""
#                 )
#                 try:
#                     add_record(data)
#                     st.success(f"Record saved with ID: {record_id}")
#                 except sqlite3.Error as err:
#                     st.error(f"Error saving record: {err}")

# elif page == "Lab Results":
#     tab1, tab2 = st.tabs(["Update Lab Results", "All Records"])

#     with tab1:
#         st.subheader("Search and Update Lab Results")
#         search_id = st.text_input("Enter Record ID")
#         if search_id:
#             try:
#                 record = search_record(search_id)
#                 if record:
#                     st.dataframe(pd.DataFrame([record], columns=[
#                         'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                         'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                         'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                         'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                         'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#                     ]), use_container_width=True)

#                     with st.form("lab_results_form"):
#                         col1, col2 = st.columns(2)
#                         with col1:
#                             blood_group = st.selectbox("Blood Group", ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=0)
#                             hepatitis_b = st.selectbox("Hepatitis B", ["", "Positive", "Negative"], index=0)
#                             vaccine_shots = st.text_input("Vaccine Shots", value=record[18] or "")
#                             sugar_level = st.text_input("Sugar Level", value=record[19] or "")
#                         with col2:
#                             bp_levels = st.text_input("BP Levels", value=record[20] or "")
#                             height = st.text_input("Height", value=record[21] or "")
#                             weight = st.text_input("Weight", value=record[22] or "")
#                             hiv_status = st.selectbox("HIV Status", ["", "Positive", "Negative", "Unknown"], index=0)

#                         col_submit, col_delete = st.columns(2)
#                         update = col_submit.form_submit_button("Update Results")
#                         delete = col_delete.form_submit_button("Delete Record")

#                         if update:
#                             lab_data = (blood_group, hepatitis_b, vaccine_shots, sugar_level, bp_levels, height, weight, hiv_status)
#                             update_lab_results(search_id, lab_data)
#                             st.success("Lab results updated.")

#                         if delete:
#                             delete_record(search_id)
#                             st.success("Record deleted.")
#                             st.rerun()
#                 else:
#                     st.error("Record not found.")
#             except sqlite3.Error as err:
#                 st.error(f"Error: {err}")

#     with tab2:
#         st.subheader("All Records")
#         try:
#             records = fetch_all_records()
#             df = pd.DataFrame(records, columns=[
#                 'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                 'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                 'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                 'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                 'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#             ])
#             st.dataframe(df, use_container_width=True)
#         except sqlite3.Error as err:
#             st.error(f"Failed to load records: {err}")


# import streamlit as st
# import sqlite3
# import pandas as pd
# from datetime import datetime
# import re

# # Database connection configuration
# def get_db_connection():
#     return sqlite3.connect("health_screening.db", check_same_thread=False)

# # Initialize database
# def init_db():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS screening (
#         id VARCHAR(36) PRIMARY KEY,
#         first_name VARCHAR(255),
#         last_name VARCHAR(255),
#         other_name VARCHAR(255),
#         sex VARCHAR(10),
#         date_of_birth VARCHAR(10),
#         nationality VARCHAR(100),
#         area_of_residence VARCHAR(255),
#         religion VARCHAR(50),
#         contact_number VARCHAR(15),
#         religious_denomination VARCHAR(255),
#         emergency_contact_name VARCHAR(255),
#         emergency_contact_number VARCHAR(15),
#         emergency_contact_relationship VARCHAR(100),
#         marital_status VARCHAR(50),
#         occupation VARCHAR(255),
#         blood_group VARCHAR(10),
#         hepatitis_b VARCHAR(10),
#         vaccine_shots TEXT,
#         sugar_level VARCHAR(50),
#         bp_levels VARCHAR(50),
#         height VARCHAR(10),
#         weight VARCHAR(10),
#         hiv_status VARCHAR(20),
#         created_at VARCHAR(20)
#     )''')
#     conn.commit()
#     conn.close()

# # Generate unique ID
# def generate_custom_id():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute("SELECT id FROM screening WHERE id LIKE 'ICGChealth%'")
#     ids = c.fetchall()
#     conn.close()
#     max_num = max([int(i[0].replace('ICGChealth', '')) for i in ids if i[0].startswith('ICGChealth')] + [0])
#     return f'ICGChealth{max_num + 1}'

# # Validate phone number
# def is_valid_phone(phone):
#     return re.match(r'^\+?\d{10,15}$', phone) is not None

# # Add record
# def add_record(data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''INSERT INTO screening (
#         id, first_name, last_name, other_name, sex, date_of_birth, nationality,
#         area_of_residence, religion, contact_number, religious_denomination,
#         emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#         marital_status, occupation, blood_group, hepatitis_b, vaccine_shots,
#         sugar_level, bp_levels, height, weight, hiv_status, created_at
#     ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#     data + (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
#     conn.commit()
#     conn.close()

# # Search record
# def search_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM screening WHERE id = ?', (record_id,))
#     record = c.fetchone()
#     conn.close()
#     return record

# # Delete record
# def delete_record(record_id):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('DELETE FROM screening WHERE id = ?', (record_id,))
#     conn.commit()
#     conn.close()

# # Update lab results
# def update_lab_results(record_id, lab_data):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('''UPDATE screening SET
#         blood_group = ?, hepatitis_b = ?, vaccine_shots = ?,
#         sugar_level = ?, bp_levels = ?, height = ?, weight = ?, hiv_status = ?
#         WHERE id = ?''', lab_data + (record_id,))
#     conn.commit()
#     conn.close()

# # Fetch all records for display
# def fetch_all_records():
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM screening ORDER BY created_at DESC')
#     records = c.fetchall()
#     conn.close()
#     return records

# # Page config and styling
# st.set_page_config(page_title="Church Health Screening App", layout="wide")
# st.markdown("""
# <style>
#     .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
#     .stTextInput>div>input, .stSelectbox>div>div { border: 2px solid #2196F3; border-radius: 5px; }
#     .sidebar .sidebar-content { background-color: #F0F8FF; }
# </style>
# """, unsafe_allow_html=True)

# try:
#     init_db()
# except sqlite3.Error as err:
#     st.error(f"Database connection failed: {err}")
#     st.stop()

# with st.sidebar:
#     st.header("Health Screening")
#     page = st.radio("Select Option", ["Bio Data", "Lab Results"])

# # Nationalities for dropdown
# countries = ["Ghana", "Nigeria", "Kenya", "USA", "UK"]  # Trimmed for brevity

# if page == "Bio Data":
#     st.header("Add Bio Data")
#     with st.form("bio_data_form"):
#         col1, col2 = st.columns(2)
#         with col1:
#             first_name = st.text_input("First Name")
#             last_name = st.text_input("Last Name")
#             other_name = st.text_input("Other Name")
#             sex = st.selectbox("Sex", ["Male", "Female"])
#             date_of_birth = st.date_input("Date of Birth")
#             nationality = st.selectbox("Nationality", countries)
#             area_of_residence = st.text_input("Area of Residence")
#         with col2:
#             religion = st.selectbox("Religion", ["Christian", "Islamic", "Others"])
#             contact_number = st.text_input("Contact Number")
#             religious_denomination = st.text_input("Religious Denomination")
#             emergency_contact_name = st.text_input("Emergency Contact Name")
#             emergency_contact_number = st.text_input("Emergency Contact Number")
#             emergency_contact_relationship = st.text_input("Emergency Contact Relationship")
#             marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
#             occupation = st.text_input("Occupation")

#         submit = st.form_submit_button("Save Bio Data")
#         if submit:
#             if not first_name or not last_name or not contact_number:
#                 st.error("Please solve all required fields.")
#             elif not is_valid_phone(contact_number) or not is_valid_phone(emergency_contact_number):
#                 st.error("Invalid phone number.")
#             else:
#                 record_id = generate_custom_id()
#                 data = (
#                     record_id, first_name, last_name, other_name, sex, str(date_of_birth), nationality,
#                     area_of_residence, religion, contact_number, religious_denomination,
#                     emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
#                     marital_status, occupation, "", "", "", "", "", "", "", ""
#                 )
#                 try:
#                     add_record(data)
#                     st.success(f"Record saved with ID: {record_id}")
#                 except sqlite3.Error as err:
#                     st.error(f"Error saving record: {err}")

# elif page == "Lab Results":
#     tab1, tab2 = st.tabs(["Update Lab Results", "All Records"])

#     with tab1:
#         st.subheader("Search and Update Lab Results")
#         search_id = st.text_input("Enter Record ID")
#         if search_id:
#             try:
#                 record = search_record(search_id)
#                 if record:
#                     st.dataframe(pd.DataFrame([record], columns=[
#                         'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                         'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                         'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                         'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                         'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#                     ]), use_container_width=True)

#                     with st.form("lab_results_form"):
#                         col1, col2 = st.columns(2)
#                         with col1:
#                             blood_group = st.selectbox("Blood Group", ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=0)
#                             hepatitis_b = st.selectbox("Hepatitis B", ["", "Positive", "Negative"], index=0)
#                             vaccine_shots = st.text_input("Vaccine Shots", value=record[18] or "")
#                             sugar_type = st.selectbox("Sugar Type", ["FBS", "RBS"], index=0)
#                             sugar_level = st.text_input("Sugar Level", value=record[19] or "")
#                         with col2:
#                             bp_levels = st.text_input("BP Levels", value=record[20] or "")
#                             height = st.text_input("Height", value=record[21] or "")
#                             weight = st.text_input("Weight", value=record[22] or "")
#                             hiv_status = st.selectbox("HIV Status", ["", "Positive", "Negative", "Unknown"], index=0)

#                         col_submit, col_delete = st.columns(2)
#                         update = col_submit.form_submit_button("Update Results")
#                         delete = col_delete.form_submit_button("Delete Record")

#                         if update:
#                             # Combine sugar type and level into the sugar_level field (e.g., "FBS: 4.3")
#                             combined_sugar = f"{sugar_type}: {sugar_level}" if sugar_level else sugar_type
#                             lab_data = (blood_group, hepatitis_b, vaccine_shots, combined_sugar, bp_levels, height, weight, hiv_status)
#                             update_lab_results(search_id, lab_data)
#                             st.success("Lab results updated.")

#                         if delete:
#                             delete_record(search_id)
#                             st.success("Record deleted.")
#                             st.rerun()
#                 else:
#                     st.error("Record not found.")
#             except sqlite3.Error as err:
#                 st.error(f"Error: {err}")

#     with tab2:
#         st.subheader("All Records")
#         try:
#             records = fetch_all_records()
#             df = pd.DataFrame(records, columns=[
#                 'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
#                 'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
#                 'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
#                 'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
#                 'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
#             ])
#             st.dataframe(df, use_container_width=True)
#         except sqlite3.Error as err:
#             st.error(f"Failed to load records: {err}")


import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, date
import re

# Database connection configuration
def get_db_connection():
    return sqlite3.connect("health_screening.db", check_same_thread=False)

# Initialize database
def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS screening (
        id VARCHAR(36) PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        other_name VARCHAR(255),
        sex VARCHAR(10),
        date_of_birth VARCHAR(10),
        nationality VARCHAR(100),
        area_of_residence VARCHAR(255),
        religion VARCHAR(50),
        contact_number VARCHAR(15),
        religious_denomination VARCHAR(255),
        emergency_contact_name VARCHAR(255),
        emergency_contact_number VARCHAR(15),
        emergency_contact_relationship VARCHAR(100),
        marital_status VARCHAR(50),
        occupation VARCHAR(255),
        blood_group VARCHAR(10),
        hepatitis_b VARCHAR(10),
        vaccine_shots TEXT,
        sugar_level VARCHAR(50),
        bp_levels VARCHAR(50),
        height VARCHAR(10),
        weight VARCHAR(10),
        hiv_status VARCHAR(20),
        created_at VARCHAR(20)
    )''')
    conn.commit()
    # Update existing records with date_of_birth before 1940
    c.execute("UPDATE screening SET date_of_birth = '1940-01-01' WHERE date_of_birth < '1940-01-01'")
    conn.commit()
    conn.close()

# Generate unique ID
def generate_custom_id():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM screening WHERE id LIKE 'ICGChealth%'")
    ids = c.fetchall()
    conn.close()
    max_num = max([int(i[0].replace('ICGChealth', '')) for i in ids if i[0].startswith('ICGChealth')] + [0])
    return f'ICGChealth{max_num + 1}'

# Validate phone number
def is_valid_phone(phone):
    return re.match(r'^\+?\d{10,15}$', phone) is not None

# Validate date of birth format and range
def is_valid_dob(dob_str):
    # Check format: YYYY-MM-DD
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', dob_str):
        return False, "Date of Birth must be in YYYY-MM-DD format (e.g., 1940-01-01)."
    
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        min_date = date(1940, 1, 1)
        max_date = date(2025, 5, 24)
        if not (min_date <= dob <= max_date):
            return False, "Date of Birth must be between 1940-01-01 and 2025-05-24."
        return True, ""
    except ValueError:
        return False, "Invalid date format or value. Use YYYY-MM-DD (e.g., 1940-01-01)."

# Add record
def add_record(data):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO screening (
        id, first_name, last_name, other_name, sex, date_of_birth, nationality,
        area_of_residence, religion, contact_number, religious_denomination,
        emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
        marital_status, occupation, blood_group, hepatitis_b, vaccine_shots,
        sugar_level, bp_levels, height, weight, hiv_status, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    data + (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
    conn.commit()
    conn.close()

# Search record
def search_record(record_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM screening WHERE id = ?', (record_id,))
    record = c.fetchone()
    conn.close()
    return record

# Delete record
def delete_record(record_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM screening WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()

# Update lab results
def update_lab_results(record_id, lab_data):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''UPDATE screening SET
        blood_group = ?, hepatitis_b = ?, vaccine_shots = ?,
        sugar_level = ?, bp_levels = ?, height = ?, weight = ?, hiv_status = ?
        WHERE id = ?''', lab_data + (record_id,))
    conn.commit()
    conn.close()

# Fetch all records for display
def fetch_all_records():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM screening ORDER BY created_at DESC')
    records = c.fetchall()
    conn.close()
    return records

# Page config and styling
st.set_page_config(page_title="Church Health Screening App", layout="wide")
st.markdown("""
<style>
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
    .stTextInput>div>input, .stSelectbox>div>div { border: 2px solid #2196F3; border-radius: 5px; }
    .sidebar .sidebar-content { background-color: #F0F8FF; }
</style>
""", unsafe_allow_html=True)

try:
    init_db()
except sqlite3.Error as err:
    st.error(f"Database connection failed: {err}")
    st.stop()

with st.sidebar:
    st.header("Health Screening")
    page = st.radio("Select Option", ["Bio Data", "Lab Results"])

# Nationalities for dropdown
countries = ["Ghana", "Nigeria", "Kenya", "USA", "UK"]  # Trimmed for brevity

if page == "Bio Data":
    st.header("Add Bio Data")
    with st.form("bio_data_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            other_name = st.text_input("Other Name")
            sex = st.selectbox("Sex", ["Male", "Female"])
            date_of_birth = st.text_input("Date of Birth (YYYY-MM-DD)", placeholder="e.g., 1940-01-01")
            nationality = st.selectbox("Nationality", countries)
            area_of_residence = st.text_input("Area of Residence")
        with col2:
            religion = st.selectbox("Religion", ["Christian", "Islamic", "Others"])
            contact_number = st.text_input("Contact Number")
            religious_denomination = st.text_input("Religious Denomination")
            emergency_contact_name = st.text_input("Emergency Contact Name")
            emergency_contact_number = st.text_input("Emergency Contact Number")
            emergency_contact_relationship = st.text_input("Emergency Contact Relationship")
            marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widow", "Widower"])
            occupation = st.text_input("Occupation")

        submit = st.form_submit_button("Save Bio Data")
        if submit:
            if not first_name or not last_name or not contact_number:
                st.error("Please fill all required fields.")
            elif not is_valid_phone(contact_number) or not is_valid_phone(emergency_contact_number):
                st.error("Invalid phone number.")
            else:
                # Validate date of birth
                is_valid, error_message = is_valid_dob(date_of_birth)
                if not is_valid:
                    st.error(error_message)
                else:
                    record_id = generate_custom_id()
                    data = (
                        record_id, first_name, last_name, other_name, sex, date_of_birth, nationality,
                        area_of_residence, religion, contact_number, religious_denomination,
                        emergency_contact_name, emergency_contact_number, emergency_contact_relationship,
                        marital_status, occupation, "", "", "", "", "", "", "", ""
                    )
                    try:
                        add_record(data)
                        st.success(f"Record saved with ID: {record_id}")
                    except sqlite3.Error as err:
                        st.error(f"Error saving record: {err}")

elif page == "Lab Results":
    tab1, tab2 = st.tabs(["Update Lab Results", "All Records"])

    with tab1:
        st.subheader("Search and Update Lab Results")
        search_id = st.text_input("Enter Record ID")
        if search_id:
            try:
                record = search_record(search_id)
                if record:
                    st.dataframe(pd.DataFrame([record], columns=[
                        'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
                        'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
                        'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
                        'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
                        'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
                    ]), use_container_width=True)

                    with st.form("lab_results_form"):
                        col1, col2 = st.columns(2)
                        with col1:
                            blood_group = st.selectbox("Blood Group", ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], index=0)
                            hepatitis_b = st.selectbox("Hepatitis B", ["", "Positive", "Negative"], index=0)
                            vaccine_shots = st.text_input("Vaccine Shots", value=record[18] or "")
                            sugar_type = st.selectbox("Sugar Type", ["FBS", "RBS"], index=0)
                            sugar_level = st.text_input("Sugar Level", value=record[19] or "")
                        with col2:
                            bp_levels = st.text_input("BP Levels", value=record[20] or "")
                            height = st.text_input("Height", value=record[21] or "")
                            weight = st.text_input("Weight", value=record[22] or "")
                            hiv_status = st.selectbox("HIV Status", ["", "Positive", "Negative", "Unknown"], index=0)

                        col_submit, col_delete = st.columns(2)
                        update = col_submit.form_submit_button("Update Results")
                        delete = col_delete.form_submit_button("Delete Record")

                        if update:
                            combined_sugar = f"{sugar_type}: {sugar_level}" if sugar_level else sugar_type
                            lab_data = (blood_group, hepatitis_b, vaccine_shots, combined_sugar, bp_levels, height, weight, hiv_status)
                            update_lab_results(search_id, lab_data)
                            st.success("Lab results updated.")

                        if delete:
                            delete_record(search_id)
                            st.success("Record deleted.")
                            st.rerun()
                else:
                    st.error("Record not found.")
            except sqlite3.Error as err:
                st.error(f"Error: {err}")

    with tab2:
        st.subheader("All Records")
        try:
            records = fetch_all_records()
            df = pd.DataFrame(records, columns=[
                'ID', 'First Name', 'Last Name', 'Other Name', 'Sex', 'Date of Birth', 'Nationality',
                'Area of Residence', 'Religion', 'Contact Number', 'Religious Denomination',
                'Emergency Contact Name', 'Emergency Contact Number', 'Emergency Contact Relationship',
                'Marital Status', 'Occupation', 'Blood Group', 'Hepatitis B', 'Vaccine Shots',
                'Sugar Level', 'BP Levels', 'Height', 'Weight', 'HIV Status', 'Created At'
            ])
            st.dataframe(df, use_container_width=True)
        except sqlite3.Error as err:
            st.error(f"Failed to load records: {err}")
