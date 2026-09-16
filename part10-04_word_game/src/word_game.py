# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
                    return 2
        else:
            return None

class MostVowels(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aiueo"
        count1 = sum(1 for char in player1_word if char in vowels)
        count2 = sum(1 for char in player2_word if char in vowels)
        if count1 > count2:
            return 1
        elif count1 < count2:
            return 2
        else:
            return None

class RockPaperScissors(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        choices = ["rock", "paper", "scissors"]
        p1_valid = player1_word in choices
        p2_valid = player2_word in choices

        if not p1_valid and not p2_valid:
            return None
        if player1_word == player2_word:
            return None
        if not p1_valid:
            return 2
        if not p2_valid:
            return 1

        winning_rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if winning_rules[player1_word] == player2_word:
            return 1
        return 2
        