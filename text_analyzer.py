import csv
import json
from sentence import Sentence
from person import Person
from text_preprocessor import TextPreprocessor
from collections import defaultdict

class TextAnalyzer:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.sentences = []
        self.cleaned_sentences = []
        self.people = []
        self.graph = None
        
    def load_data(self, sentences_path=None, names_path=None, remove_path=None, preprocessed_path=None):
        if sentences_path:
            with open(sentences_path, 'r') as file:
                reader = csv.DictReader(file)
                self.sentences = [Sentence(row['sentence']) for row in reader]
        if names_path:
            with open(names_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    other_names = [nickname for nickname in row['Other Names'].split(',')] if row['Other Names'] else []
                    self.people.append(Person(name, other_names))
        if remove_path:
            self.preprocessor.load_remove_words(remove_path)
        if preprocessed_path:
            with open(preprocessed_path, 'r') as file:
                data = json.load(file)
                self.cleaned_sentences = [Sentence(clean_sentence) for clean_sentence in data['Question 1'] ['Processed Sentences']]
                self.people = [Person(person[0], person[1]) for person in data['Question 1']['Processed Names']]
                print(self.cleaned_sentences)
                print(self.people)
                
    def analyze_task1(self):
        """Initial Text Preprocessing"""
        processed_sentences = []
        for sentence in self.sentences:
            cleaned_text = self.preprocessor.clean_words(sentence.text)
            self.cleaned_sentences.append(cleaned_text)
            words = cleaned_text
            if words:
                sentence.cleaned_text = cleaned_text
                sentence.words = words
                processed_sentences.append(words)
        
        processed_people = self.preprocessor.preprocess_people(self.people)
        
        result = {
            "Question 1": {
                "Processed Sentences": processed_sentences,
                "Processed Names": processed_people
            }
        }
        return result
        
        
    def analyze_task2(self, max_k):
        """Counting Sequences of Words"""
        pass
        
    def analyze_task3(self):
        """Counting Person Mentions"""
        pass
        
    def analyze_task4(self, qseq_path):
        """Basic Search Engine Functionality"""
        pass
        
    def analyze_task5(self, max_k):
        """Contexts of People and Associated K-seqs"""
        pass
        
    def analyze_task6(self, window_size, threshold):
        """Finding Direct Connections Between People"""
        pass
        
    def analyze_task7(self, window_size, threshold, pairs_path, maximal_distance):
        """Determining Indirect Connections Through a Graph"""
        pass
        
    def analyze_task8(self, window_size, threshold, pairs_path, fixed_length):
        """Checking Fixed-Length Paths Between People"""
        pass
        
    def analyze_task9(self, threshold):
        """Grouping Sentences by Shared Words"""
        pass
