import random

# Define emojis and choices
emojis = {"r": "🪨 Rock", "p": "📃 Paper", "s": "✂️ Scissors"}
choices = ("r", "p", "s")

# Initialize scores
user_score = 0
computer_score = 0
rounds_played = 0

# Game loop
while True:
    print("\n" + "="*10 + " Let's Play Rock, Paper, Scissors! " + "="*10)
    
    user_choice = input("Choose Rock, Paper, or Scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("❌ Invalid Choice! Please choose 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(choices)

    # Display choices
    print("\n" + "-"*40)
    print(f"🧍‍♂️ You chose: {emojis[user_choice]}")
    print(f"💻 Computer chose: {emojis[computer_choice]}")
    print("-"*40)

    # Determine the outcome
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        print("🎉 You Win! 🎉")
        user_score += 1
    else:
        print("😢 You Lose!")
        computer_score += 1

    # Show current scores
    rounds_played += 1
    print("\n" + "="*10 + " Current Scores " + "="*10)
    print(f"🧍‍♂️ You: {user_score}  |  💻 Computer: {computer_score}")
    print(f"Rounds Played: {rounds_played}")
    print("="*40)

    # Continue or exit the game
    should_continue = input("\nDo you want to play another round? (y/n): ").lower()
    if should_continue == "n":
        print("👋 Thanks for playing! See you next time!")
        break





# import random

# emojis = { "r": "🪨", "s": "✂️", "p": "📃"}
# choices = ("r", "p", "s")

# while True:
#     user_choice = input("Rock, Paper, Or Scissors? (r/p/s): ").lower()
#     if user_choice not in choices:
#         print("Invalid Choice !")
#         continue

#     computer_choice = random.choice(choices)

#     print(f"You Chose {emojis[user_choice]}")
#     print(f"Computer Chose {emojis[computer_choice]}")

#     if user_choice == computer_choice:
#         print("Tie !")
#     elif (
#         (user_choice == "r" and computer_choice == "s") or
#         (user_choice == "s" and computer_choice == "p") or
#         (user_choice == "p" and computer_choice == "r")):
#         print("You WIn")
#     else:
#         print("You Lose")

#     should_continue = input("Continue? (y/n): ").lower()
#     if should_continue == "n":
#         break

