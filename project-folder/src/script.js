document.addEventListener('DOMContentLoaded', () => {
    const socket = io();  // Подключение к серверу через Socket.IO

    const messageForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const messagesContainer = document.getElementById('messages');

    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (message) {
            socket.emit('chatMessage', message);  // Отправка сообщения на сервер
            messageInput.value = '';
        }
    });

    socket.on('message', (message) => {
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    });
});
