# fortune.py

def main():
    name = "Pranav Tanaji Sarate"
    admission_number = "21JE0673"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

    if mood == "happy":
        print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("💧 Your fortune: Better days are coming. Hang in there. 💧")
    elif mood == "neutral":
        print("🌤 Your fortune: Stay curious—something unexpected is on its way. 🌤")
    else:
        print("🤔 I don't understand that mood, but stay positive!")

if __name__ == "__main__":
    main()
