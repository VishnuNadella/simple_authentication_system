import streamlit as st
from pymongo import *

usn = st.secrets["DB_USN"]
pwd = st.secrets["DB_PWD"]
connection = f"mongodb+srv://{usn}:{pwd}@cluster0.vzd4elr.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(connection)

db = cluster["hackathon"]
collection = db["participants"]

st.title("Welcome to TLE hack")
st.subheader('Mark your self as attended')

# df = pd.read_csv("./registered.csv")
cursor = collection.find({})
names = []
for i in cursor:
    # print(i["Name"])
    names.append(i["Name"])
    
names = tuple(names)
# df.drop()
# name = tuple(df["Name"])

person = st.selectbox(
    "Please select your name",
    names
)

if st.button("Mark as Attended"):
    dets = collection.find_one({"Name" : person})
    if dets["Attended?"] == False:
        collection.update_one({"Name" : person}, {"$set" : {"Attended?" : True}})
        st.success("Welcome to TLE hack, We wish you all the best")
    elif dets["Attended?"] == True:
        st.error("Please, you have already participated in hackathon")
    
    # if df.at[index, "Attended?"] == False:
    #     stat = df.loc[index]["Attended?"]
    #     df.at[index, "Attended?"] = True
    #     # df.to_csv("./registered.csv", index = False)
    #     st.success("Welcome to TLE hack, We wish you all the best")
    # elif df.at[index, "Attended?"] == True:
    #     st.error("Please, you have already participated in hackathon")

