import re
import types

class TextPreprocessor:
    def __init__(self):
        self.remove_words = set()
        
    def load_remove_words(self, remove_file_path):
        with open(remove_file_path, 'r', encoding='utf-8') as file:
            self.remove_words = set(word.strip() for word in file.readlines())
    
    def clean_words(self, text: str):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        words = text.split()
        cleaned_words = [word for word in words if word not in self.remove_words]
        return cleaned_words
    
    def get_text(self, words):
        cleaned_text = ' '.join(words)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text
    
    def clean_text(self, text):
        words = self.clean_words(text)
        return self.get_text(words)

    def clean_name(self, name):
        cleaned_name = self.clean_words(name)
        return cleaned_name

    def preprocess_sentences(self, sentences):
        processed_sentences = []
        for sentence in sentences:
            cleaned_text = self.clean_text(sentence)
            words = cleaned_text.split()
            if words:
                processed_sentences.append(words)
        return processed_sentences

    def preprocess_people(self, people):
        processed_people = []
        unique_names = set()
        for person in people:
            cleaned_name = self.clean_name(person.name)
            cleaned_other_names = [self.clean_name(name) for name in person.other_names]
            if cleaned_name and cleaned_name not in unique_names:
                unique_names.add(cleaned_name)
                person.cleaned_name = cleaned_name
                person.cleaned_other_names = cleaned_other_names
                processed_people.append([cleaned_name, cleaned_other_names])
        return processed_people