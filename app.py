import streamlit as st

st.set_page_config(
    page_title="NLP Simple Example",
    page_icon=":smile:",
    layout="centered",
    initial_sidebar_state="auto",
)

from textblob import TextBlob
import spacy
from gensim.summarization import summarize
import neattext as nt

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")
from wordcloud import WordCloud


def main():
    # st.title("NLP Simple Example")

    title_template = """
	<div style="background-color:black;padding:8px;border-style:solid;border-color:white;border-width:thin;">
    <h1 style="color:white">NLP Simple Examples</h1>
    </div>
	"""

    st.markdown(title_template, unsafe_allow_html=True)

    subheader_templ = """
    <div style="background-color:grey;padding:8px;border-style:solid;border-color:white;border-width:thin;">
    <h3 style="color:white">Natural Language Processing On the Go...</h3>
    </div>
    """

    st.markdown(subheader_templ, unsafe_allow_html=True)

    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", activity)

    if choice == "Text Analysis":
        st.subheader("Text Analysis")

    if choice == "Translation":
        st.subheader("Translation")

    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")

    if choice == "About":
        st.subheader("About")

        st.markdown(
            """
        ### NLP Simple Examples (App with Streamlit and TextBlob)
        
        ##### By
        + **[Rosario Moscato LAB](https://www.youtube.com/channel/UCDn-FahQNJQOekLrOcR7-7Q)**
        + [rosariomoscatolab@gmail.com](mailto:rosariomoscatolab@gmail.com)
        """
        )


if __name__ == "__main__":
    main()
