# 📚 Gutenberg Text Cleaner

A simple and powerful web app that:
- Extracts text from **Project Gutenberg** URLs  
- Cleans, normalizes, and summarizes the text  
- Displays quick statistics (word count, paragraph count, etc.)  
- Shows a 3-sentence summary and preview of the cleaned text  

---

## 🚀 Features
- ✅ Accepts a Project Gutenberg URL  
- ⏳ Shows a loading message while processing  
- 📊 Displays clear, readable text statistics  
- ✂️ Shows the first 500 characters of the cleaned text  
- 🧠 Generates a concise 3-sentence summary  
- ⚙️ Handles errors gracefully (invalid URLs, network issues, etc.)

---

## 🖥️ Demo Screenshots

### 🏠 Landing Page  
*(Insert screenshot here)*  
`![Landing Page](screenshots/landing.png)`

### 📈 Results Page  
*(Insert screenshot here)*  
`![Results Page](screenshots/results.png)`

---

## 🧩 Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Vanilla)  
- **Backend:** Flask (Python)  
- **Libraries:** `requests`, `beautifulsoup4`, `nltk`, `textblob`, `flask-cors`  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/gutenberg-text-cleaner.git
cd gutenberg-text-cleaner
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```

### 4️⃣ Open in Browser
Visit → http://127.0.0.1:5000


### 📂 Project Structure
```cpp
gutenberg_text_cleaner/
│
├── app.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
└── screenshots/
    ├── landing_page_1.png
    ├── landing_page_2.png
    └── test_setup_results.png
```

### 🧠 API Example

#### Endpoint: `/process`

#### Method: `POST`

Request JSON:
```json
{
  "url": "https://www.gutenberg.org/files/1342/1342-h/1342-h.htm"
}
```

Response JSON:
```json
{
  "stats": {
    "word_count": 12345,
    "paragraphs": 320
  },
  "preview": "It is a truth universally acknowledged...",
  "summary": "Pride and Prejudice explores the nature of love..."
}
```

## 🧰 Troubleshooting

If you encounter issues while running the Gutenberg Text Cleaner app, check the table below for quick fixes:

| 🐞 Issue | 💡 Solution |
|----------|-------------|
| **App not loading** | Check Flask server logs for any traceback errors |
| **CORS error** | Ensure `flask-cors` is installed and imported in `app.py` |
| **No text output** | Verify that the Project Gutenberg URL is valid and that you have an active internet connection |
| **Summary gibberish** | Ensure `nltk` data is downloaded using: `import nltk nltk.download('punkt')` |

---

## Student

**Harsh Tikone**  
#### Basics of AI
🎓 EAS 510 Scaffolding Assignment 3: Building a Text Preprocessing Web Service
---