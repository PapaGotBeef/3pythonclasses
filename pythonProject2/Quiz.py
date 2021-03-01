class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What color are apples?\n(a) red\green\n(b) purple\pink\n(c) orange\n",
    "Where do kids come from?\n(a) Santa\n(b) Stork\n(c) The Domino's delivery guy\n",
    "What time is midnight?\n(a) 1am\n(b) 12pm\n(c) 12am\n"
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")

    ]

def run_test(questions):
        points = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                points += 1

        return points