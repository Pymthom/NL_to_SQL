from dotenv import load_dotenv
load_dotenv()  # Load environment variables (GOOGLE_API_KEY)

import streamlit as st
import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI


# Function to load Gemini model and provide queries as response
def get_gemini_response(question, prompt):
    # ✅ Use flash model (faster + higher free quota)
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    final_prompt = f"{prompt}\n\nQ: {question}"
    try:
        response = model.invoke(final_prompt)
        return response.content
    except Exception as e:
        return f"Error: {e}"


# Function to retrieve query from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"Database Error: {e}"


# ✅ Shorter Prompt to reduce token usage
SQL_PROMPT = """
You are an expert at converting English questions into SQL queries.

The database table is named MYNTRA_DATA with columns:
- brand_name
- pants_description
- price
- MRP
- discount_percent
- ratings
- number_of_ratings

Rules:
1. Convert the question into a valid SQL query.
2. Return only the SQL query, no explanation or extra text.

Examples:
Q: How many products are there?
A: SELECT COUNT(*) FROM MYNTRA_DATA;

Q: Show all products from brand Adidas.
A: SELECT * FROM MYNTRA_DATA WHERE brand_name = "Adidas";

Q: What is the average discount?
A: SELECT AVG(discount_percent) FROM MYNTRA_DATA;

Q: Top 5 highest-rated products.
A: SELECT * FROM MYNTRA_DATA ORDER BY ratings DESC LIMIT 5;
"""


# Streamlit App
st.set_page_config(page_title="SQL Query Retriever")
st.header("🔎 Gemini App to Retrieve SQL Data from Myntra Dataset")

question = st.text_input("Enter your question in English:", key="input")

submit = st.button("Ask Gemini")

# If submit is clicked
if submit:
    sql_query = get_gemini_response(question, SQL_PROMPT)
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language="sql")

    if sql_query.startswith("SELECT"):
        results = read_sql_query(sql_query, "myntra_dataset.db")
        st.subheader("Query Results:")
        if isinstance(results, str):  # error message
            st.error(results)
        elif results:
            st.table(results)
        else:
            st.info("No results found for this query.")
    else:
        st.error("Invalid SQL generated or API error.")
