document.addEventListener("DOMContentLoaded", function () {
    let chatbotIcon = document.createElement("div");
    chatbotIcon.id = "chatbot-icon";
    chatbotIcon.innerHTML = "💬";
    chatbotIcon.onclick = openChat;
    document.body.appendChild(chatbotIcon);

    let chatbotBox = document.createElement("div");
    chatbotBox.id = "chatbot-box";
    chatbotBox.innerHTML = `
        <div id="chatbot-header">
            <span>Job Assistant</span>
            <button id="chatbot-close">✖</button>
        </div>
        <div id="chatbot-messages"></div>
        <input type="text" id="chatbot-input" placeholder="Ask about hiring, jobs, HR...">
        <button id="chatbot-send">Send</button>
    `;
    chatbotBox.style.display = "none";
    document.body.appendChild(chatbotBox);

    document.getElementById("chatbot-close").onclick = () => chatbotBox.style.display = "none";
    document.getElementById("chatbot-send").onclick = sendMessage;
});

function openChat() {
    document.getElementById("chatbot-box").style.display = "block";
}

function sendMessage() {
    let input = document.getElementById("chatbot-input");
    let message = input.value.trim();
    if (!message) return;

    let messages = document.getElementById("chatbot-messages");
    messages.innerHTML += `<div class='user-message'>${message}</div>`;

    fetch("/chatbot/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: message }),
    })
    .then(response => response.json())
    .then(data => {
        messages.innerHTML += `<div class='bot-message'>${data.response}</div>`;
    });

    input.value = "";
}
