import os
import random


class Game():
    def __init__(self):
        self.min_word_length = 4
        self.max_word_length = 14
        self.wrong_letters = []

    def clear(self):
        os.system('clear') if os.name == 'posix' else os.system('cls')

    def load_word_list(self):
        f = open('words.txt', 'r')
        words = f.read().split('\n')
        f.close()

        return words

    def set_difficulty(self):
        while True:
            self.clear()

            print("Please choose a difficulty:\n")

            difficulty = input(('(e)asy: 4- or 5-letter words\n'
                                '(m)edium: 6- or 7-letter words\n'
                                '(h)ard: 8- to 14-letter words\n'
                                '(r)andom: Any length word from 4 to 14 letters\n\n')
                               ).lower()

            if difficulty and difficulty[0] in 'emhr':
                break

        return difficulty

    def set_random_word(self, difficulty, word_list):
        if difficulty != 'r':
            if difficulty == 'e':
                self.max_word_length = 5
            elif difficulty == 'm':
                self.min_word_length = 6
                self.max_word_length = 7
            else:
                self.min_word_length = 8

        random_word = random.choice(
            [w for w in word_list if self.min_word_length <= len(w) <= self.max_word_length])

        return random_word

    def guess_letter(self, display, word):
        while True:
            self.clear()

            print(" ".join(display))
            if self.wrong_letters:
                self.draw_hangman(self.wrong_letters)
                print(
                    f"\nGuessed letters not in the word: {', '.join(self.wrong_letters)}")

            guess = input("\nGuess a letter: ").lower()

            if guess.isalpha() and len(guess) == 1:
                if guess not in self.wrong_letters and guess not in display:
                    break

        if guess in word:
            for index, letter in enumerate(word):
                if word[index] == guess:
                    display[index] = guess
        else:
            self.wrong_letters.append(guess)

            if len(self.wrong_letters) >= 7:
                if display.count('_') == 1 and len(self.wrong_letters) == 7:
                    self.clear()

                    print(" ".join(display))
                    self.draw_hangman(self.wrong_letters)
                    print(
                        f"\nGuessed letters not in the word: {', '.join(self.wrong_letters)}")
                    print(
                        "\nYou are so close to solving the word and saving your stick man!")
                    input("Press enter for one more guess.\n")
                    self.guess_letter(display, word)
                else:
                    self.clear()

                    self.draw_hangman(self.wrong_letters)
                    print(
                        f"You've lost!\nThe word was: {word}.\n\nBetter luck next time!\n")
                    exit()

        self.check_win(display, word)

    def draw_hangman(self, wrong_letters):
        HANGINGMAN = ['''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
           \O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
           \O/  |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
           \O/  |
            |   |
           /    |
                |
            =========''', '''
            +---+
            |   |
           \O/  |
            |   |
           / \  |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========''']

        print(HANGINGMAN[len(wrong_letters) - 1])

    def check_win(self, display, word):
        if "".join(display) == word:
            self.clear()

            print(f"You won! Congratulations!\nThe word was: {word}\n")
            exit()
        else:
            self.guess_letter(display, word)

    def run(self):
        while True:
            self.clear()

            print("Welcome to Hangman. Please choose an option:\n")
            response = input("(p)lay\n(q)uit\n\n").lower()[0]

            if response and response in 'pq':
                break

        if response == 'p':
            word_list = self.load_word_list()
            difficulty = self.set_difficulty()
            word = self.set_random_word(difficulty, word_list)

            self.clear()

            display = ["_"] * len(word)

            self.guess_letter(display, word)
        else:
            self.clear()

            print("Goodbye\n")
            exit()


if __name__ == '__main__':
    game = Game()
    game.run()
