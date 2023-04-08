import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#Dont run from here
#streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)


my_cur.execute("Insert into Fruit_Load_List values('from Streamlit')")
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My parents new healthy diner")

streamlit.header('🥣 Breakfast Menu')

streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#Section to display fruityvise API Responce

streamlit.header('🥣 Fruityvise fruit advice !!!')
try:
   fruit_choice = streamlit.text_input('what fruit information would you like to have ?','Kiwi')
   if not fruit_chouce:
      streamlit.error("Please select a fruit to get information")
   else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
      fruit_choice1 = streamlit.text_input('What fruit would you like to add ?','Kiwi')
      streamlit.write('The user entered',fruit_choice1)
except URLError as e:
   streamlit.error()







   
