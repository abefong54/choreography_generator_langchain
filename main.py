import langchain_helper as lch
import streamlit as strlit 




dance_types = ("Bachata", "Salsa On 2", "Zouk", "Kizomba")
dance_levels = ("Beginner", "Intermediate", "Advanced", "Competetive")

strlit.title("Dance Choreo Generator")
user_dance_type = strlit.sidebar.selectbox(label="What is your dance type?", options=dance_types )
user_student_level = strlit.sidebar.selectbox(label="What is your class level?", options=dance_levels )

# if user_animal_type == "Bachata":
#     user_animal_color = strlit.sidebar.text_area(label="What color is your Cat?", max_chars=20)
# if user_animal_type == "Dog":
#     user_animal_color = strlit.sidebar.text_area(label="What color is your Dog?", max_chars=20)
# if user_animal_type == "Cow":
#     user_animal_color = strlit.sidebar.text_area(label="What color is your Cow?", max_chars=20)
# if user_animal_type == "Hamster":
#     user_animal_color = strlit.sidebar.text_area(label="What color is your Hamster?", max_chars=20)

    
if user_dance_type and user_student_level:
    response = lch.generate_pet_name(user_dance_type=user_dance_type, user_student_level=user_student_level)
    strlit.text(response['choreo_results'])