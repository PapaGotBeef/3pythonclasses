class score:
    def __init__(self, points, percentcorrect):
        self.points = points
        self.percentcorrect = percentcorrect

def calc_percent(grade):
    import Quiz
    value1 = grade/len(Quiz.questions)
    percent = value1 * 100

    return percent

