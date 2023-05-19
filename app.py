import streamlit as st

from textblob import TextBlob
import spacy
from gensim.summarization import summarize
import neattext as nt

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
from wordcloud import WordCloud

