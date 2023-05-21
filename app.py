import streamlit as st

st.set_page_config(
    page_title="Simple NLP App",
    page_icon=":smile:",
    layout="centered",
    initial_sidebar_state="auto",
)

from textblob import TextBlob
import spacy
from gensim.summarization import summarize
import neattext as nt
from deep_translator import GoogleTranslator

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("agg")
from wordcloud import WordCloud
import subprocess


def generate_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    fig = plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)


@st.cache_data
def analyse_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    text_data = [
        ('"Token": {}, \n"Lemma": {}'.format(token.text, token.lemma_)) for token in doc
    ]
    return text_data


def main():
    # st.title("NLP Simple Example")
    download_en_core_web_sm()

    title_template = """
	<div style="background-color:black;padding:8px;border-style:solid;border-color:white;border-width:thin;">
    <h1 style="color:white">Simple NLP App</h1>
    </div>
	"""

    st.markdown(title_template, unsafe_allow_html=True)

    subheader_templ = """
    <div style="background-color:grey;padding:8px;border-style:solid;border-color:white;border-width:thin;">
    <h3 style="color:white">Natural Language Processing On the Go...</h3>
    </div>
    """

    st.markdown(subheader_templ, unsafe_allow_html=True)

    st.sidebar.image("nlp.jpg", use_column_width=True)

    activity = ["Text Analysis", "Translation", "Sentiment Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", activity)

    if choice == "Text Analysis":
        st.subheader("Text Analysis")

        raw_text = st.text_area(
            "Write something", "Enter something in English...", height=250
        )

        if st.button("Analyse"):
            if len(raw_text) == 0:
                st.warning("Enter a text...")
            else:
                blob = TextBlob(raw_text)

                st.info("Basic Features")
                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("Basic Info"):
                        st.info("Text Stats")
                        text_stats = nt.TextFrame(raw_text).word_stats()
                        # st.markdown(text_stats, unsafe_allow_html=False)
                        text_display = {
                            "Length of Text": text_stats["Length of Text"],
                            "Num of Vowels": text_stats["Num of Vowels"],
                            "Num of Consonants": text_stats["Num of Consonants"],
                            "Num of Stopwords": text_stats["Num of Stopwords"],
                        }
                        st.write(text_display)

                    with st.expander("Word Cloud"):
                        st.info("Word Cloud")
                        generate_wordcloud(raw_text)

                with col2:
                    with st.expander("Processed Text"):
                        st.success("Stopword excluded Texts")
                        processed_text = str(nt.TextFrame(raw_text).remove_stopwords())
                        st.write(processed_text)
                    with st.expander("Stopwords"):
                        st.success("Stopword List")
                        stop_words = nt.TextExtractor(raw_text).extract_stopwords()
                        st.error(stop_words)

                st.info("Advanced Features")

                col3, col4 = st.columns(2)

                with col3:
                    with st.expander("Tokens & Lemmas"):
                        st.info("Tokens & Lemmas")
                        text_data = str(nt.TextFrame(raw_text).remove_stopwords())
                        text_data = str(nt.TextFrame(text_data).remove_puncts())
                        text_data = str(
                            nt.TextFrame(text_data).remove_special_characters()
                        )
                        text_data = analyse_text(raw_text)
                        st.json(text_data)

                with col4:
                    with st.expander("Summarize"):
                        st.info("Summarize")
                        try:
                            summary_text = summarize(raw_text, ratio=0.4)
                        except:
                            summary_text = ""
                        if summary_text != "":
                            st.success(summary_text)
                        else:
                            st.warning("Please insert a longer text...")

                # if blob.detect_language() != "en": -- not working anymore
                #     st.warning("Enter a text in English...")

    if choice == "Translation":
        st.subheader("Translation")

        raw_text = st.text_area(
            "Write something to be translated...",
            "Text to be translated...",
        )

        if len(raw_text) < 3:
            st.warning("Please provide a string with at least 3 characters...")

        translate_option = st.selectbox(
            "Select translation language",
            ["Chinese", "English", "German", "Italian", "Russian", "Spanish"],
        )

        if st.button("Translate"):
            translate_lkp = {
                "Chinese": "zh-CN",
                "English": "en",
                "German": "de",
                "Italian": "it",
                "Russian": "ru",
                "Spanish": "es",
            }
            translate_language = translate_lkp[translate_option]
            translator = GoogleTranslator(source="auto", target=translate_language)
            translated_text = translator.translate(raw_text)
            st.text(f"Translating to {translate_option}...")
            st.success(translated_text)

    if choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")

        raw_text = st.text_area("Enter some text to analyse...", "Text to analyse...")

        if st.button("Evaluate"):
            if len(raw_text) == 0:
                st.warning("Please enter some text...")
            else:
                translator = GoogleTranslator(source="auto", target="en")
                translated_text = translator.translate(raw_text)
                blob = TextBlob(str(translated_text))
                sentiment_result = blob.sentiment

                st.info(
                    "Sentiment Polarity: {}".format(sentiment_result.polarity)
                )  # from 1 (positive) to -1 (negative)
                st.info(
                    "Sentiment Subjectivity: {}".format(sentiment_result.subjectivity)
                )  # from 0 (objective) to 1 (subjective)

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
