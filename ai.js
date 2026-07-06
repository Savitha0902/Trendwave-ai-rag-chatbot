console.log("JS Loaded");

async function sendMessage() {

    try {

        const chatbox = document.getElementById("chatbox");
        const input = document.getElementById("message");
        const message = input.value.trim();

        if (!message) return;

        console.log("Message:", message);

        // User message
        chatbox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>`;

        // Clear input
        input.value = "";

        // Typing indicator
        chatbox.innerHTML += `
        <div class="bot-message typing" id="typing">
            Curio is typing...
        </div>`;

        const response = await fetch(
            "http://127.0.0.1:5000/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            }
        );

        console.log("Status:", response.status);

        const data = await response.json();

        // Remove typing message
        document.getElementById("typing").remove();

        console.log("Response Data:", data);

        // Bot response
        chatbox.innerHTML += `
        <div class="bot-message">
            ${data.reply}
        </div>`;

        chatbox.scrollTop = chatbox.scrollHeight;

    }
    catch(error) {

        console.error("ERROR:", error);

    }
}