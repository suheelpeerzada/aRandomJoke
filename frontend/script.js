const BASE_URL = "http://127.0.0.1:8000";

// Load random joke from backend
function getRandomJoke() {
    fetch(`${BASE_URL}/joke/random`)
        .then(r => r.json())
        .then(data => {
            document.getElementById("joke-area").innerText =
                `${data.setup} ${data.punchline}`;
        });
}

// Save joke to favourites
function saveJoke() {
    const jokeText = document.getElementById("joke-area").innerText;
    console.log("Sending to backend:", JSON.stringify(jokeText));
    fetch("http://127.0.0.1:8000/favourites", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(jokeText)   // <-- raw JSON string body
    })
    .then(response => response.json())
    .then(data => {
        console.log("Saved:", data);
        alert("Saved to favourites!");
    })
    .catch(err => console.error("Error:", err));
}

// Load favourites
function loadFavourites() {
    fetch(`${BASE_URL}/favourites`)
        .then(r => r.json())
        .then(data => {
            const container = document.getElementById("fav-list");
            container.innerHTML = "";

            data.forEach(item => {
                const div = document.createElement("div");
                div.className = "joke-item";
                div.innerHTML = `
                    <p>${item.content}</p>
                    <button onclick="deleteFav('${item.id}')">Delete</button>
                `;
                container.appendChild(div);
            });
        });
}

// Delete favourite by ID
function deleteFav(id) {
    fetch(`${BASE_URL}/favourites/${id}`, {
        method: "DELETE"
    })
    .then(r => r.json())
    .then(() => {
        loadFavourites();
    });
}