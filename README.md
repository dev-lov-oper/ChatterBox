# 💬 Chatter Box - Realtime Chat Application

A simple realtime chat room application built with Django, HTML, CSS, JavaScript, jQuery, and SQLite. Users can create or join chat rooms and exchange messages with other participants in near real-time.

## 🚀 Features

* Create and join chat rooms
* Send and receive messages instantly
* Dynamic chat updates using AJAX polling
* Responsive and modern chat interface
* Room-based communication
* Automatic message refresh without page reload
* Clean WhatsApp-inspired UI

## 🛠️ Tech Stack

### Backend

* Django
* Python
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript
* jQuery AJAX

## ⚙️ How It Works

1. Users enter a username and room name.
2. Django creates or retrieves the requested chat room.
3. Messages are stored in the database.
4. The frontend sends AJAX requests every second to fetch the latest messages.
5. New messages are displayed dynamically without refreshing the page.

## 📂 Project Structure

```text
chat-app/
│
├── chat/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── chatterbox/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```


## 🎯 Learning Outcomes

Through this project, I learned:

* Django Models and Views
* URL Routing
* Template Rendering
* AJAX and Asynchronous JavaScript
* Database Operations with Django ORM
* Frontend and Backend Integration
* Building Realtime-like Applications

## 🔮 Future Improvements

* WebSocket implementation using Django Channels
* User authentication
* Online user status
* Message notifications
* Typing indicators
* File and image sharing
* Message reactions
* Chat history search


