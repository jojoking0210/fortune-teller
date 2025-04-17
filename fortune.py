import random

print("🔮 Welcome to Pranav Tanaji Sarate's Fortune Teller (21JE0673) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "Great things await you, Aryan! Keep smiling. ✨",
        "Your joy is contagious—spread it around! 🌞",
        "Happiness will bring new opportunities soon. 🍀"
    ],
    "sad": [
        "Tough times don't last, but tough people do. 💪",
        "Even rainy days end in rainbows. 🌈",
        "A smile is coming your way, Aryan. 😊"
    ],
    "neutral": [
        "Today may seem ordinary, but surprises await. 🎁",
        "Balance is good—stay centered. 🧘",
        "Your calm energy brings peace to others. 🌿"
    ],
    "stressed": [
        "Take a deep breath—peace is coming. 🕊️",
        "Aryan, you're stronger than the stress. 💥",
        "This pressure will lead to diamonds. 💎"
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("Sorry, I can't read that mood yet... 🤔")
