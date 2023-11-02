import streamlit as st
import openai_helper

# Streamlit UI
st.title("Financial Data Extractor")
st.sidebar.header("Input News Article")
article_text = st.sidebar.text_area("Paste your news article here")

if st.sidebar.button("Extract"):
    if article_text:
        # Extract financial data using the function from openai_helper
        financial_data_df = openai_helper.extract_financial_data(article_text)
        if financial_data_df is not None:
            # Display the extracted data in a table on the right side
            st.write("### Extracted Data:")
            st.write(financial_data_df)
        else:
            st.error("No financial data extracted from the article.")

# Example news article for testing
example_article = '''
Q2 Results: Apple Inc, the tech giant, is set to announce its financial results for the quarter ended June 2023 today. The company is expected to report impressive earnings, with a projected revenue of $23.45 billion and an EPS of 12.3 billion $.
'''
st.sidebar.text("Example Article:")
st.sidebar.text(example_article)
