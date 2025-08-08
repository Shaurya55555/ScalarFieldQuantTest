import streamlit as st
from src.utils import setup_dbqa
import timeit

def main():
    st.title("SEC Filings QA Agent: A Retrieval-Augmented Generation (RAG) System for Financial Research Across Public Companies")

    # Sidebar content with explanations for first-time users
    st.sidebar.header('About the App')
    st.sidebar.write("""
    **Overview:**
This application leverages a Retrieval Augmented Generation (RAG) approach, powered by OpenAI’s `gpt-3.5-turbo-instruct`, to analyze SEC filings (10-K, 10-Q, 8-K, DEF 14A, Forms 3/4/5) from 10–15 public companies across sectors. It is designed to assist financial analysts and quantitative researchers in answering complex research questions using up-to-date regulatory data.

**Why Use RAG?**
- **Real-Time Financial Intelligence:** Unlike static GPT models, RAG retrieves the most recent filings (e.g., Apple’s 2023 10-K) directly from the SEC, ensuring up-to-date and relevant insights.
- **Complex Query Handling:** Supports nuanced questions involving specific tickers, time periods, form types, and financial sections (e.g., “Compare 2022 R&D trends for Microsoft and Google”).
- **Secure & Customizable:** Enables organizations to conduct proprietary analysis securely within their infrastructure.
- **Source Attribution:** Every answer is traceable to its source in the original SEC filings, ensuring transparency and auditability.

**Getting Started:**
1. **Input Your Query:** Use the input box to type questions like _"How has Amazon's AI strategy evolved?"_ or _"What are the most common risk factors in 2023 tech sector filings?"_
2. **Submit Your Query:** Click **'Analyze Query'** to fetch and analyze relevant documents.
3. **View Results:** Review the answer and linked source excerpts directly from official SEC filings.
    """)

    # User input for custom query
    user_query = st.text_input("Enter your query:", 
                               placeholder="E.g. Which FAANG company generated the highest revenue?")

    # Button to trigger the computation
    if st.button('Analyze Query'):
        if user_query:  # Ensure there is a query to process
            with st.spinner('Fetching data...'):
                start = timeit.default_timer()
                dbqa = setup_dbqa()
                response = dbqa({'query': user_query})
                end = timeit.default_timer()

                time_elapsed = end - start

                if response["result"]:
                    st.success(f'Answer: {response["result"]}')
                else:
                    st.error("No answer found.")

                # Process source documents
                if 'source_documents' in response:
                    st.write('### Source Documents')
                    for i, doc in enumerate(response['source_documents']):
                        st.write(f'#### Source Document {i+1}')
                        st.text(f'Source Text: {doc.page_content}')
                        st.text(f'Document Name: {doc.metadata["source"]}')
                        st.text(f'Page Number: {doc.metadata["page"]}')
                        st.write('='*60)
                st.info(f"Time to retrieve response: {time_elapsed:.2f} seconds")
        else:
            st.warning("Please enter a query to analyze.")

if __name__ == '__main__':
    main()


