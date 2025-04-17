import random

# Personal details
my_name = "Pranav Tanaji Sarate"
admission_number = "21JE0673"

print(f"🔮 Welcome to {my_name}'s Fortune Teller ({admission_number}) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        f"Great things await you, {my_name}! Keep smiling. ✨",
        "Your joy is contagious—spread it around! 🌞",
        "Happiness will bring new opportunities soon. 🍀"
    ],
    "sad": [
        "Tough times don't last, but tough people do. 💪",
        "Even rainy days end in rainbows. 🌈",
        f"A smile is coming your way, {my_name}. 😊"
    ],
    "neutral": [
        "Today may seem ordinary, but surprises await. 🎁",
        "Balance is good—stay centered. 🧘",
        "Your calm energy brings peace to others. 🌿"
    ],
    "stressed": [
        "Take a deep breath—peace is coming. 🕊️",
        f"{my_name}, you're stronger than the stress. 💥",
        "This pressure will lead to diamonds. 💎"
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("Sorry, I can't read that mood yet... 🤔")
