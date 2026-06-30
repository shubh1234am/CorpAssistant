# 🤖 CorpAssistant

### AI-Powered Internal Company Knowledge Assistant using Retrieval-Augmented Generation (RAG)

CorpAssistant is an AI-powered internal knowledge assistant that enables employees to upload company documents and instantly ask questions using natural language. The system retrieves relevant information from uploaded PDFs using ChromaDB and generates accurate responses with Groq LLM, reducing hallucinations by grounding answers in company documents.

---

## 🚀 Features

- 🔐 User Authentication (Login & Signup)
- 📄 Upload Company PDF Documents
- 📚 Automatic Text Extraction
- ✂️ Smart Text Chunking
- 🧠 Semantic Search using ChromaDB
- 🤖 AI Responses using Groq LLM
- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Modern Chat Interface
- 📁 Multiple Document Support
- ⚡ Fast Vector Search
- 🎯 Context-Based Answers
- 📱 Responsive User Interface

---

# 📷 Screenshots

## Login Page

<img width="1920" height="1080" alt="Screenshot (217)" src="https://github.com/user-attachments/assets/12248a26-2784-4ef3-9c5e-03d7fa2f4b3a" />



---

## Dashboard

<img width="1920" height="1080" alt="Screenshot (219)" src="https://github.com/user-attachments/assets/3036507f-41a9-4e30-831d-28b315d126f4" />


---

## Upload Documents

<img width="1920" height="1080" alt="Screenshot (220)" src="https://github.com/user-attachments/assets/3ce8d358-d05d-4ec7-b68f-d80f545554a9" />


---

## Chat Interface

<img width="1920" height="1080" alt="Screenshot (221)" src="https://github.com/user-attachments/assets/cf0d4d17-a162-49ef-8114-bbe5b776624c" />


---

## AI Response

<img width="1920" height="1080" alt="Screenshot (222)" src="https://github.com/user-attachments/assets/3888ba21-4aa8-44b1-8782-f808c82ded57" />


---

# 🏗 Project Architecture

```

User Uploads PDF

↓

Text Extraction

↓

Text Chunking

↓

Embedding Generation

↓

ChromaDB Vector Database

↓

User Question

↓

Similarity Search

↓

Relevant Context

↓

Groq LLM

↓

Final AI Response

```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Django |
| Language | Python |
| Frontend | HTML, CSS, JavaScript |
| Authentication | Django Authentication |
| Database | SQLite |
| Vector Database | ChromaDB |
| LLM | Groq |
| Embedding Model | Sentence Transformers |
| Version Control | Git & GitHub |
| Deployment | Render (Deployment in Progress) |

---

# 📂 Project Structure

```

CorpAssistant/

├── config/

├── documents/

├── media/

├── static/

├── templates/

├── manage.py

├── requirements.txt

├── build.sh

└── README.md

```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/shubh1234am/CorpAssistant.git
```

```
cd CorpAssistant
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
SECRET_KEY=your_secret_key

DEBUG=True

GROQ_API_KEY=your_groq_api_key
```

---

# 💡 How It Works

1. User uploads company PDF documents.
2. PDFs are converted into text.
3. Text is divided into chunks.
4. Embeddings are generated.
5. Embeddings are stored inside ChromaDB.
6. User asks a question.
7. Similar document chunks are retrieved.
8. Retrieved context is sent to Groq LLM.
9. AI generates an accurate context-based response.

---

# 🎯 Future Improvements

- PostgreSQL Support
- Cloud Storage Integration
- OCR Support
- Voice Input
- Conversation History
- Multi-language Support
- Admin Dashboard
- Role-Based Access Control
- Streaming Responses
- Production Deployment

---

# 👨‍💻 Author

**Shubham Nagulkar**

Python Backend Developer

AI & Machine Learning Enthusiast

GitHub:
https://github.com/shubh1234am

LinkedIn:
(Add Your LinkedIn)

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
