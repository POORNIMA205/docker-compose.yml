import os
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Travel Explorer")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


# =========================
# TRAVEL DESTINATION DATA
# =========================

destinations = [
    {
        "id": 1,
        "name": "Paris",
        "country": "France",
        "category": "City",
        "price": "$1200",
        "rating": 4.9,
        "description": "Experience romance, art, history, and iconic architecture.",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34"
    },
    {
        "id": 2,
        "name": "Maldives",
        "country": "Maldives",
        "category": "Beach",
        "price": "$1800",
        "rating": 4.8,
        "description": "Relax on beautiful islands surrounded by crystal-clear water.",
        "image": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8"
    },
    {
        "id": 3,
        "name": "Bali",
        "country": "Indonesia",
        "category": "Beach",
        "price": "$900",
        "rating": 4.8,
        "description": "Discover tropical beaches, temples, culture, and nature.",
        "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4"
    },
    {
        "id": 4,
        "name": "Dubai",
        "country": "UAE",
        "category": "City",
        "price": "$1400",
        "rating": 4.7,
        "description": "Experience luxury, futuristic architecture, and desert adventures.",
        "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c"
    },
    {
        "id": 5,
        "name": "Swiss Alps",
        "country": "Switzerland",
        "category": "Mountain",
        "price": "$2200",
        "rating": 4.9,
        "description": "Explore breathtaking mountains, snow, and adventure.",
        "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4"
    },
    {
        "id": 6,
        "name": "Tokyo",
        "country": "Japan",
        "category": "City",
        "price": "$1500",
        "rating": 4.7,
        "description": "Explore technology, culture, food, and modern city life.",
        "image": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf"
    }
]


# =========================
# HTML + CSS + JAVASCRIPT
# =========================

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{{ app_name }}</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #f5f7fb;
    color: #222;
}


/* ================= NAVBAR ================= */

nav {
    background: white;
    padding: 18px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 15px rgba(0,0,0,0.08);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo {
    font-size: 25px;
    font-weight: bold;
}

.logo span {
    color: #0077ff;
}

nav ul {
    display: flex;
    list-style: none;
    gap: 30px;
}

nav a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
}

nav a:hover {
    color: #0077ff;
}


/* ================= HERO ================= */

.hero {
    min-height: 550px;

    background:
    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.55)
    ),
    url('https://images.unsplash.com/photo-1488646953014-85cb44e25828');

    background-size: cover;
    background-position: center;

    display: flex;
    justify-content: center;
    align-items: center;

    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 60px;
    margin-bottom: 20px;
}

.hero p {
    font-size: 20px;
    margin-bottom: 30px;
}


/* ================= SEARCH ================= */

.search-box {
    display: flex;
    justify-content: center;
    gap: 10px;
}

.search-box input {
    width: 350px;
    padding: 16px;

    border: none;
    border-radius: 8px;

    font-size: 15px;
}

.search-box button {
    padding: 16px 28px;

    border: none;
    border-radius: 8px;

    background: #0077ff;
    color: white;

    cursor: pointer;
    font-size: 15px;
}

.search-box button:hover {
    background: #005fcc;
}


/* ================= SECTION ================= */

.section {
    padding: 80px 8%;
}

.section h2 {
    text-align: center;
    font-size: 36px;
    margin-bottom: 15px;
}

.section-subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 45px;
}


/* ================= DESTINATION CARDS ================= */

.destination-grid {

    display: grid;

    grid-template-columns:
    repeat(auto-fit, minmax(280px, 1fr));

    gap: 30px;
}

.card {

    background: white;

    border-radius: 15px;

    overflow: hidden;

    box-shadow:
    0 5px 25px rgba(0,0,0,0.08);

    transition: 0.3s;
}

.card:hover {

    transform:
    translateY(-10px);

    box-shadow:
    0 15px 35px rgba(0,0,0,0.15);
}

.card img {

    width: 100%;

    height: 220px;

    object-fit: cover;
}

.card-content {

    padding: 22px;
}

.card h3 {

    font-size: 24px;

    margin-bottom: 8px;
}

.country {

    color: #777;

    margin-bottom: 12px;
}

.description {

    font-size: 14px;

    color: #555;

    line-height: 1.6;
}

.details {

    display: flex;

    justify-content: space-between;

    margin-top: 20px;

    font-weight: bold;
}

.book-btn {

    width: 100%;

    margin-top: 20px;

    padding: 13px;

    border: none;

    border-radius: 8px;

    background: #0077ff;

    color: white;

    cursor: pointer;

    font-size: 15px;
}

.book-btn:hover {

    background: #005fcc;
}


/* ================= ABOUT ================= */

.about {

    background: white;

    text-align: center;

    padding: 80px 15%;
}

.about h2 {

    font-size: 35px;

    margin-bottom: 20px;
}

.about p {

    color: #666;

    line-height: 1.8;

    font-size: 17px;
}


/* ================= FOOTER ================= */

footer {

    background: #111827;

    color: white;

    text-align: center;

    padding: 30px;
}


/* ================= RESPONSIVE ================= */

@media(max-width: 700px) {

    nav ul {
        display: none;
    }

    .hero h1 {
        font-size: 40px;
    }

    .search-box {
        flex-direction: column;
        align-items: center;
    }

    .search-box input {
        width: 280px;
    }

}

</style>

</head>


<body>


<!-- NAVBAR -->

<nav>

<div class="logo">

Travel<span>Explorer</span>

</div>

<ul>

<li><a href="#home">Home</a></li>

<li><a href="#destinations">Destinations</a></li>

<li><a href="#about">About</a></li>

</ul>

</nav>


<!-- HERO -->

<section class="hero" id="home">

<div>

<h1>Discover Your Next Adventure</h1>

<p>
Explore breathtaking destinations around the world.
Your journey starts here.
</p>


<div class="search-box">

<input
type="text"
id="searchInput"
placeholder="Search destinations..."
>

<button onclick="searchDestinations()">

Search

</button>

</div>

</div>

</section>


<!-- DESTINATIONS -->

<section class="section" id="destinations">

<h2>Popular Destinations</h2>

<p class="section-subtitle">

Discover places that inspire unforgettable journeys.

</p>


<div
class="destination-grid"
id="destinationGrid"
>


{% for destination in destinations %}

<div class="card">

<img
src="{{ destination.image }}"
alt="{{ destination.name }}"
>


<div class="card-content">


<h3>

{{ destination.name }}

</h3>


<p class="country">

📍 {{ destination.country }}

</p>


<p class="description">

{{ destination.description }}

</p>


<div class="details">

<span>

{{ destination.price }}

</span>


<span>

⭐ {{ destination.rating }}

</span>

</div>


<button
class="book-btn"
onclick="bookTrip('{{ destination.name }}')"
>

Explore Trip

</button>


</div>

</div>

{% endfor %}


</div>

</section>


<!-- ABOUT -->

<section class="about" id="about">

<h2>Explore Beyond Borders</h2>

<p>

TravelExplorer helps you discover amazing destinations
around the world. From tropical beaches and historic
cities to breathtaking mountains, your next adventure
is waiting for you.

</p>

</section>


<!-- FOOTER -->

<footer>

<p>

© 2026 TravelExplorer

|

Explore. Discover. Experience. 🌍

</p>

</footer>


<!-- JAVASCRIPT -->

<script>


function searchDestinations() {

    const query =
        document
        .getElementById("searchInput")
        .value
        .toLowerCase();


    const cards =
        document
        .querySelectorAll(".card");


    cards.forEach(card => {


        const name =
            card
            .querySelector("h3")
            .innerText
            .toLowerCase();


        const country =
            card
            .querySelector(".country")
            .innerText
            .toLowerCase();


        if (
            name.includes(query) ||
            country.includes(query)
        ) {

            card.style.display = "block";

        }

        else {

            card.style.display = "none";

        }

    });

}


function bookTrip(destination) {

    alert(

        "🌍 Great Choice!\\n\\n" +

        "You selected: " +

        destination +

        "\\n\\nYour adventure starts soon!"

    );

}


document
.getElementById("searchInput")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {

        searchDestinations();

    }

});


</script>


</body>

</html>
"""


# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return render_template_string(
        HTML_PAGE,
        destinations=destinations,
        app_name=APP_NAME
    )


@app.route("/api/destinations")
def get_destinations():
    return jsonify(destinations)


@app.route("/api/search")
def search_destination():

    query = request.args.get("q", "").lower()

    results = [
        destination
        for destination in destinations
        if query in destination["name"].lower()
        or query in destination["country"].lower()
        or query in destination["category"].lower()
    ]

    return jsonify(results)


@app.route("/api/destinations/<int:destination_id>")
def get_destination(destination_id):

    destination = next(
        (
            item
            for item in destinations
            if item["id"] == destination_id
        ),
        None
    )

    if destination:
        return jsonify(destination)

    return jsonify({
        "error": "Destination not found"
    }), 404


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "application": APP_NAME
    })


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=DEBUG
    )