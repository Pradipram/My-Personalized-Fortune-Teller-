def get_fortune(mood):
    # Dictionary of fortunes based on mood
    fortunes = {
        "happy": ["✨ Your fortune: Great things await you, Pradip! Keep smiling.✨", 
                 "✨ Your positivity will bring you success today!✨"],
        "sad": ["✨ Don't worry, better days are ahead. The sun will shine again.✨",
               "✨ This feeling is temporary. Joy is on its way to you.✨"],
        "neutral": ["✨ Interesting opportunities are coming your way soon.✨",
                  "✨ A surprise awaits you before the week ends.✨"]
    }
    
    # Return a fortune based on the mood
    if mood in fortunes:
        import random
        return random.choice(fortunes[mood])
    else:
        return "✨ I cannot read your fortune with that mood. Try happy, sad, or neutral.✨"

def main():
    # Display welcome message with your name and admission number
    print("🔮 Welcome to Pradip's Fortune Teller (21JE0664)🔮")
    
    # Get user's mood
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    # Display fortune
    print(get_fortune(mood))

if __name__ == "__main__":
    main()