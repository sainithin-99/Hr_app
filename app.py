import streamlit as st

st.title('HR DASHBOARD')

txt = st.text_area(
    "Job Description",
    )


uploaded_files = st.file_uploader("Choose Resume file", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


st.button("Submit", type="primary")