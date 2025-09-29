import streamlit as st
from transformers import pipeline

# Load summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit UI
st.title("Resume Summarizer")
st.write("Upload your resume text or paste it below to get a concise summary.")

# Upload file
uploaded_file = st.file_uploader("Upload Resume (.txt)", type=["txt"])
resume_text = ""

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")
else:
    resume_text = st.text_area("Or paste your resume text here:")

if st.button("Summarize") and resume_text.strip():
    with st.spinner("Generating summary..."):
        summary = summarizer(resume_text, max_length=150, min_length=60, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
