async function sendMessage() {
    const input = document.getElementById("userInput");
    const messages = document.getElementById("messages");

    const question = input.value.trim();

    if (question === "") {
        return;
    }

    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = question;
    messages.appendChild(userMessage);

    input.value = "";

    const thinking = document.createElement("div");
    thinking.className = "ai-message";
    thinking.textContent = "Srybo is thinking... 🤔";
    messages.appendChild(thinking);

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        if (data.answer) {
            thinking.textContent = data.answer;
        } else {
            thinking.textContent = "Srybo could not find an answer.";
        }

    } catch (error) {
        thinking.textContent =
            "Sorry, I couldn't connect to Srybo's Python backend. ❌";

        console.error(error);
    }
}


function openChat() {
    document.getElementById("chat").scrollIntoView({
        behavior: "smooth"
    });
}


function quickAsk(message) {
    const input = document.getElementById("userInput");

    if (input) {
        input.value = message;
        input.focus();
    }
}
