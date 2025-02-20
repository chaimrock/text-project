class Sentence:
    def __init__(self, text):
        self.text = text
        self.cleaned_text = None
        self.words = []
        self.mentioned_people = set()

    def __repr__(self):
        return self.text
