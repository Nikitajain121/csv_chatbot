# from dotenv import load_dotenv
# import os
# import pandas as pd
# from pandasai import SmartDataframe
# from pandasai.llm import OpenAI
# load_dotenv()
# openai_api_key  = os.environ.get('OPANAI_API_KEY')
# llm = OpenAI(api_token=openai_api_key)
# df = pd.read_csv("data/titanic.csv")
# chat_df = SmartDataframe(df, config={"llm": llm})
# chat_df.chat("Which person is oldest?")
import streamlit as st
import pandas as pd
import os
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
#from pandasai import PandasAI

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