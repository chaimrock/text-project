class Person:
    def __init__(self, name, other_names=None):
        self.name = name
        self.other_names = other_names if other_names else []
        self.cleaned_name = None
        self.cleaned_other_names = []

    def __repr__(self):
        return self.name
    
        