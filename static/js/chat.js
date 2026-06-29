// ==========================================================
// CorpAssistant Chat
// ==========================================================

// ==========================
// ELEMENTS
// ==========================

const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatBody = document.getElementById("chatBody");
const welcomeScreen = document.getElementById("welcomeScreen");
const newChatBtn = document.getElementById("newChatBtn");
const conversationInput = document.getElementById("conversationId");

// ==========================
// EVENTS
// ==========================

if (chatForm) {
    chatForm.addEventListener("submit", sendMessage);
}

if (newChatBtn) {
    newChatBtn.addEventListener("click", startNewChat);
}

// ==========================
// SEND MESSAGE
// ==========================

async function sendMessage(event) {

    event.preventDefault();

    const message = messageInput.value.trim();

    if (message === "") return;

    hideWelcome();

    addUserMessage(message);

    messageInput.value = "";

    showThinking();

    try {

        const formData = new URLSearchParams();

        formData.append("question", message);

        if (conversationInput && conversationInput.value !== "") {
            formData.append("conversation_id", conversationInput.value);
        }

        const response = await fetch("/chat/", {

            method: "POST",

            headers: {

                "Content-Type": "application/x-www-form-urlencoded",

                "X-CSRFToken": getCSRFToken(),

            },

            body: formData

        });

        const data = await response.json();

        removeThinking();

        addAIMessage(data.answer);

        // Save conversation id after first message
        if (conversationInput && data.conversation_id) {
            conversationInput.value = data.conversation_id;
        }

    }

    catch (error) {

        removeThinking();

        addAIMessage("Something went wrong while contacting the server.");

        console.error(error);

    }

}

// ==========================
// USER MESSAGE
// ==========================

function addUserMessage(text) {

    const message = document.createElement("div");

    message.className = "message user-message";

    message.innerHTML = `
        <div class="message-box">

            <div class="message-text">
                ${text}
            </div>

            <div class="message-footer">
                <span>${getCurrentTime()}</span>
            </div>

        </div>
    `;

    chatBody.appendChild(message);

    scrollToBottom();

}

// ==========================
// AI MESSAGE
// ==========================

function addAIMessage(text) {

    const message = document.createElement("div");

    message.className = "message ai-message";

    message.innerHTML = `
        <div class="message-avatar">
            🤖
        </div>

        <div class="message-box">

            <div class="message-text">
                ${text}
            </div>

            <div class="message-footer">

                <span>${getCurrentTime()}</span>

                <button class="copy-btn">
                    Copy
                </button>

            </div>

        </div>
    `;

    chatBody.appendChild(message);

    const copyBtn = message.querySelector(".copy-btn");

    copyBtn.addEventListener("click", () => {

        navigator.clipboard.writeText(text);

        copyBtn.innerText = "Copied ✓";

        setTimeout(() => {

            copyBtn.innerText = "Copy";

        }, 1500);

    });

    scrollToBottom();

}

// ==========================
// THINKING
// ==========================

function showThinking() {

    const thinking = document.createElement("div");

    thinking.id = "thinkingMessage";

    thinking.className = "message ai-message";

    thinking.innerHTML = `
        <div class="message-avatar">
            🤖
        </div>

        <div class="message-box">

            <div class="typing">

                <span></span>
                <span></span>
                <span></span>

            </div>

        </div>
    `;

    chatBody.appendChild(thinking);

    scrollToBottom();

}

function removeThinking() {

    const thinking = document.getElementById("thinkingMessage");

    if (thinking) {

        thinking.remove();

    }

}

// ==========================
// WELCOME
// ==========================

function hideWelcome() {

    if (welcomeScreen) {

        welcomeScreen.style.display = "none";

    }

}

// ==========================
// NEW CHAT
// ==========================

function startNewChat() {

    window.location.href = "/chat/";

}

// ==========================
// TIME
// ==========================

function getCurrentTime() {

    return new Date().toLocaleTimeString([], {

        hour: "2-digit",

        minute: "2-digit"

    });

}

// ==========================
// AUTO SCROLL
// ==========================

function scrollToBottom() {

    chatBody.scrollTop = chatBody.scrollHeight;

}

// ==========================
// CSRF TOKEN
// ==========================

function getCSRFToken() {

    let cookieValue = null;

    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {

        cookie = cookie.trim();

        if (cookie.startsWith("csrftoken=")) {

            cookieValue = cookie.substring("csrftoken=".length);

            break;

        }

    }

    return cookieValue;

}