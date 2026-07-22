
class WordleGame:
    
    def __init__(self, answer):
        self.answer = answer
        self.rounds = self.get_rounds(answer)
        self.won = False

    def check_guess(self, guess):
        result = [0] * len(self.answer)
        answer_chars = list(self.answer)

        for i in range(len(self.answer)):
            if guess[i] == self.answer[i]:
                result[i] = 1
                answer_chars[i] = None

        for i in range(len(self.answer)):
            if result[i] == 0 and guess[i] in answer_chars:
                result[i] = 2
                answer_chars[answer_chars.index(guess[i])] = None

        return result

    def is_won(self, guess):
        if guess == self.answer:
            self.won = True
        return self.won
    
    def decrease_round(self):
        self.rounds -= 1
    
    def get_rounds(self, answer):
        return len(answer) + 1