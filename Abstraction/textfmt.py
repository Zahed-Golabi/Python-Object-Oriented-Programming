from abc import ABC, abstractmethod


class TextFormatter(ABC):

    @abstractmethod
    def format(self, text):
        pass


class UpperCaseFormatter(TextFormatter):

    def format(self, text):
        return text.upper()
    

class LowerCaseFormatter(TextFormatter):

    def format(self, text):
        return text.lower()
    

class TitleCaseFormatter(TextFormatter):

    def format(self, text):
        return text.title()
    

class TextEditor():
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter

    def publish(self, text):
        return self.formatter.format(text)



# Testing
editor1 = TextEditor(UpperCaseFormatter())
print(editor1.publish("hello world"))                   # HELLO WORLD

editor2 = TextEditor(LowerCaseFormatter())
print(editor2.publish("HELLO WORLD"))                   # hello world

editor3 = TextEditor(TitleCaseFormatter())
print(editor3.publish("hello world"))                   # Hello World