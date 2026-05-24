import random
from collections import Counter
from colorama import init, Fore, Style
init(autoreset=True)
MOVES = ["rock", "paper", "scissors"]
WIN_RULES ={"rock": "scissors","scissors": "paper","paper": "rock"}
def get_player_move():
    while True:
        move = input(
            Fore.CYAN + "\nEnter Rock, Paper, or Scissors: ").lower().strip()
        if move in MOVES:
            return move
        else:
            print(Fore.RED + "Invalid input! Try again.")
def get_ai_move(player_history):
    if len(player_history) < 3:
        return random.choice(MOVES)
    move_counts = Counter(player_history)
    predicted_move = move_counts.most_common(1)[0][0]
    counter ={"rock": "paper",
        "paper": "scissors",
        "scissors": "rock"}
    return counter[predicted_move]
def determine_winner(player, ai):
    if player == ai:
        return "tie"
    elif WIN_RULES[player] == ai:
        return "player"
    else:
        return "ai"
def display_result(player, ai, winner):
    print(Fore.YELLOW + f"\nYou chose: {player.capitalize()}")
    print(Fore.MAGENTA + f"AI chose: {ai.capitalize()}")
    if winner == "tie":
        print(Fore.BLUE + "It's a Tie!")
    elif winner == "player":
        print(Fore.GREEN + "You Win This Round!")
    else:
        print(Fore.RED + "AI Wins This Round!")
def play_game():
    print(Fore.GREEN + Style.BRIGHT +"ROCK PAPER SCISSORS")
    player_score = 0
    ai_score = 0
    ties = 0
    player_history = []
    while True:
        player_move = get_player_move()
        ai_move = get_ai_move(player_history)
        player_history.append(player_move)
        winner = determine_winner(player_move, ai_move)
        display_result(player_move, ai_move, winner)
        if winner == "player":
            player_score += 1
        elif winner == "ai":
            ai_score += 1
        else:
            ties += 1
        again = input(
            Fore.YELLOW + "\nPlay again? (yes/no): "
        ).lower().strip()
        if again not in ["yes", "y"]:
            print(Fore.MAGENTA + "\nThanks for playing!")
            break
if __name__ == "__main__":
    play_game()