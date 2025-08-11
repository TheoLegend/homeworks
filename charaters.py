characters = [
    {
        "name": "Lena Hart",
        "age": 23,
        "hobby": "painting",
        "favorite_color": "Sky Blue",
        "desc": "A cheerful artist who loves sunsets, coffee, and rainy days."
    },
    {
        "name": "Ethan Cole",
        "age": 28,
        "hobby": "cycling",
        "favorite_color": "Forest Green",
        "desc": "An adventurous traveler with a passion for photography and nature."
    }
]

for c in characters:
    print(f"Meet {c['name']}!")
    print(f" Age: {c['age']}")
    print(f" Hobby: {c['hobby']}")
    print(f" Favorite Color: {c['favorite_color']}")
    print(f" About: {c['desc']}")
    print("-" * 40)
