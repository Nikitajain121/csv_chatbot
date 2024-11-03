!pip install --upgrade pip
import streamlit as st
import pandas as pd
import os
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
from dotenv import load_dotenv
load_dotenv()

st.title("Analysing this csv")
uploaded_file = st.file_uploader("Upload csv file for analysis",type=['csv'])
openai_api_key = os.environ.get('OPENAI_API_KEY')
llm = OpenAI(api_token=openai_api_key)
#pandas_ai = PandasAI(llm)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt= st.text_area("Enter your query:")
    if st.button("Generate"):
        if prompt:
            st.write("PandasAI is generating an answer, please wait...")
            chat_df = SmartDataframe(df, config={"llm": llm})
            st.write(chat_df.chat(prompt))
        else:
            st.warning("Please eneter a prompt.")
