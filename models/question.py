class Question:

    def __init__(self, question, answer, week):
        self.question = question
        self.answer = answer
        self.week = week

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getWeek(self):
        return self.week