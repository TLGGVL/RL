from blackjack import BlackjackGame
from qlearning import BlackjackQLearning

def main():
    agent = BlackjackQLearning()
    episodes = 5000000
    agent.train(episodes)

    test_games = 1000000
    wins = 0
    losses = 0
    draws = 0

    for _ in range(test_games):
        print("-----")
        result = agent.play()
        print(result)
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            draws += 1

    print(f"Kazanma: {wins}, Kaybetme: {losses}, Beraberlik: {draws}")
    print(f"Kazanma oranı: {wins/(wins + losses)*100:.2f}%")

if __name__ == "__main__":
    main()
