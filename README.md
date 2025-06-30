# 🚀 SmartSDLC – AI-Powered Software Development Lifecycle Assistant

SmartSDLC is an AI-enhanced platform that streamlines the entire Software Development Lifecycle (SDLC) using IBM Watsonx foundation models and modern web technologies.

It helps developers by:
- Classifying requirements from PDFs
- Generating code from natural language prompts
- Fixing buggy code automatically
- Creating test cases using AI
- Summarizing source code
- Providing an AI chatbot assistant

---

## 🧠 Features

- 📄 **Requirement Classifier**: Upload a PDF and classify each line as Functional or Non-Functional.
- 💻 **Code Generator**: Convert natural language prompts into Python code.
- 🐞 **Bug Fixer**: Automatically correct buggy code.
- ✅ **Test Case Generator**: Generate unit tests from source code.
- 📜 **Code Summarizer**: Understand code via AI-generated summaries.
- 🤖 **AI Chat Assistant**: Interactive LangChain chatbot for SDLC help.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI/ML**: IBM Watsonx.ai (Granite 20B Code Instruct)
- **NLP**: LangChain
- **Containerization**: Docker
- **Language**: Python 3.11+

---

## 📂 Folder Structure

```

SmartSDLC/
├── app/
│   ├── main.py
│   ├── routes/
│   └── services/
├── smart\_sdlc\_frontend/
│   └── \[Streamlit UI files]
├── .env
├── Dockerfile
├── requirements.txt

````

---

## ⚙️ Prerequisites

- Python 3.11+
- IBM Cloud Watsonx.ai credentials
- Docker (for containerization)
- Git

---

## 🔑 Environment Variables (`.env`)

```env
WATSONX_API_KEY=your_ibm_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_MODEL_ID=ibm/granite-20b-code-instruct
WATSONX_API_URL=https://eu-de.ml.cloud.ibm.com
````

---

## ▶️ How to Run the Project

### 💡 1. Clone the Repo

```bash
git clone https://github.com/manu-vasamsetti/SmartSDLC.git
cd SmartSDLC
```

---

### 🔌 2. Set Up Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate    # For Windows
pip install -r requirements.txt
```

---

### 🚀 3. Run the FastAPI Backend

```bash
cd app
uvicorn main:app --reload --port 8000
```

> Swagger Docs will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🌐 4. Run the Streamlit Frontend

In a **new terminal window**:

```bash
cd smart_sdlc_frontend
streamlit run Home.py
```

> Streamlit UI will open at: [http://localhost:8501/](http://localhost:8501/)

---

## 🐳 Run with Docker (Optional)

```bash
docker build -t smart-sdlc .
docker run -p 8000:8000 smart-sdlc
```

---

## 📸 Screenshots


> ![image](https://github.com/user-attachments/assets/8cced36d-6216-426c-ab92-5985a65fc77a)
> ![image](https://github.com/user-attachments/assets/a8b162a2-e3fd-46f2-b8e6-8535a1a09578)


---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

* **Hima Manikanta Vasamsetti**
  [GitHub](https://github.com/manu-vasamsetti) | [LinkedIn](https://linkedin.com/in/hima-manikanta-vasamsetti-a5485427a)

---

## 📬 Contact

For questions or feedback, reach out to:
📧 **[himamanikantavasamsetty@gmail.com](mailto:himamanikantavasamsetty@gmail.com)**
📱 **+91 7893606650**

````
