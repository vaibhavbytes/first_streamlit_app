import streamlit
import pandas
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

con = snowflake.connector.connect(
    user='vaibhavbytes',
    password='Sandhy@99',
    #account='WL02737.us-east-2.aws'
    account = 'NIUQEZH-MM41596'
)
my_cur = con.cursor() 
my_cur.execute("use warehouse pc_rivery_wh; use role pc_rivery_role")
my_cur.execute("Select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains")
streamlit.text(my_data_row)

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


import requests
streamlit.header('🥣 Breakfast Menu recommendations !!!')
fruit_choice = streamlit.text_input('what fruit information would you like to have ?','Kiwi')
streamlit.write('The user entered',fruit_choice)
# Display the table on the page.
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)






   
