import random

class GameLogic:
    def __init__(self):
        self.target_number = 0
        self.attempts = 0
        self.max_attempts = 3
        self.start_new_game()

    def start_new_game(self):
        self.target_number = random.randint(1, 10)
        self.attempts = 0

    def process_guess(self, user_guess):
        try:
            user_guess = int(user_guess)
        except ValueError:
            return 'Будь ласка, введіть дійсне ціле число.'

        self.attempts += 1

        if user_guess == self.target_number:
            result = f'Вітаємо! Ви вгадали число {self.target_number} за {self.attempts} спроб.'
            self.start_new_game()
        elif self.attempts >= self.max_attempts:
            result = f'Ви не вгадали число {self.target_number}'
            self.start_new_game()
        elif user_guess < self.target_number:
            result = 'Спробуйте більше.'
        else:
            result = 'Спробуйте менше.'

        return result
