# 🧴 IngreDecode – Skincare Ingredient Chatbot

IngreDecode is an AI-powered skincare chatbot that helps users understand ingredients and build personalized routines. Ask anything like:  
> “I have oily skin. Can you give me a routine?”  
> “What actives are safe for sensitive acne-prone skin?”  

Built with Flask + Cohere API on the backend, and a clean vanilla JS frontend.

---

## ✨ Features

- 💬 Real-time AI chat about skincare ingredients and routines
- 🧠 Powered by Cohere’s `command` model for natural responses
- 🌙 Dark mode toggle
- 🗂 Chat history stored locally and downloadable
- 🔁 Future-ready for multi-chat session sidebar like ChatGPT

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript  
- **Backend:** Python, Flask, Cohere API  
- **AI:** Cohere Command  
- **Extras:** LocalStorage, `.env` config, downloadable logs

---

## 📁 Project Structure

```
ingredecode/
├── backend/
│   ├── app.py             # Flask backend logic
│   ├── .env               # Contains COHERE_API_KEY (ignored from Git)
│   ├── chat_log.txt       # Saved conversations
│   └── requirements.txt
├── frontend/
│   └── index.html         # Chatbot interface
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/chemtrailsx/skincare-bot.git
cd skincare-bot
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate    # On Mac/Linux use: source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Your API Key

Create a `.env` file inside `/backend`:

```env
COHERE_API_KEY=your_real_api_key_here
```

### 4. Run Backend

```bash
python app.py
```

Backend will run on:  
`http://localhost:5000`

---

## 💻 Use the Frontend

Simply open this file in your browser:  
`frontend/index.html`

Then ask skincare-related questions and get helpful responses. You can:

- Toggle dark mode 🌓
- Download the chat 💬
- Add new prompts anytime 🧴

---

## 🧪 Sample Questions

```txt
I have oily skin. Can you build an AM and PM routine for me?

What actives should I use for sensitive acne-prone skin?

Is it okay to use glycolic acid and retinol together?

What does niacinamide do?

How to layer actives for dry skin?
```

---

## 🔐 Environment Variables

Make sure your `.env` is NOT committed:

```bash
# .gitignore
backend/.env
```

---

## 📦 requirements.txt (for backend)

```txt
Flask
flask-cors
cohere
python-dotenv
```

Save this in `backend/requirements.txt`.

---

## 🧭 Roadmap

- [ ] Sidebar for switching between saved chats
- [ ] Persistent session history
- [ ] Product recommendation integration
- [ ] Deploy on Render / Railway
- [ ] Add INCI decoding support

---

## 🤝 Contributing

Want to improve IngreDecode? Feel free to open issues or PRs. Let’s make skincare smarter together ✨

---

## 🪪 License

MIT License

---

## 👤 Author

Built with ❤️ by [@chemtrailsx](https://github.com/chemtrailsx)
