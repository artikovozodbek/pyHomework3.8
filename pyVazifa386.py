filmlar = {
    "Titanic": "Jack Dawson",
    "Harry Potter": "Harry Potter",
    "The Dark Knight": "Bruce Wayne (Batman)",
    "The Matrix": "Neo (Thomas Anderson)",
    "Forrest Gump": "Forrest Gump",
    "Gladiator": "Maximus Decimus Meridius",
    "Inception": "Dom Cobb",
    "Spider-Man": "Peter Parker",
    "Iron Man": "Tony Stark",
    "The Lord of the Rings": "Frodo Baggins"
}

film_kirit = input("Film nomi: ")

try:
    hero = filmlar[film_kirit]
    print(hero)
except:
    print("Bunday film yo'q")
