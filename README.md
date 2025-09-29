# Deployed Resume Summarizer (GenAI)

This project is a **Resume Summarizer Tool** built using **Hugging Face Transformers** and deployed with **Streamlit**. It automatically summarizes resumes to highlight key information like skills, work experience, education, and projects.

---

## Features

- Upload a resume in `.txt` format.
- Summarizes the resume using a pretrained NLP model.
- Interactive web app using Streamlit.
- Can handle multiple resumes.

---

## Project Structure

```
smart-resume/
│
├─ app.py               # Streamlit app
├─ requirements.txt     # Python dependencies
├─ sample_resume.txt    # Sample resume for testing
└─ README.md
```

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/krishang-1/smart-resume.git
cd smart-resume
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**
```bash
streamlit run app.py
```

5. **Open in browser**  
Streamlit will open a local URL (e.g., `http://localhost:8501`) where you can upload a resume and get a summary.

---

## Sample Usage

- Upload `sample_resume.txt`.
- Click **Summarize**.
- View summarized output in the app.

---

## Notes

- Make sure your `sample_resume.txt` or other resumes are in plain text format.
- You can replace the pretrained model with any Hugging Face model for fine-tuning or customization.

---

## Screenshots / Demo
- You can upload videos to YouTube or Google Drive and link them in README:

```markdown
Watch Demo Video --> (https://youtu.be/kI3IQc-4xLg)
```

---

## Dependencies

- Python >= 3.8  
- streamlit  
- pandas  
- transformers  

Install via `pip install -r requirements.txt`.

---

## License

MIT License
