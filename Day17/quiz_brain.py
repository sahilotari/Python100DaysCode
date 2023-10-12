class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def next_question(self):
        cur_que = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {cur_que.text} (True, False): ")
        self.check_answer(choice,cur_que.answer)

    def still_has_question(self):
        if self.question_number <= len(self.question_list) - 1:
            return True
        else:
            return False
    
    def check_answer(self,choice, correct):
        if choice.lower() == correct.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct}")
        print(f"Your current Score is: {self.score}/{self.question_number}\n")