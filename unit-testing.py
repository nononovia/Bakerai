import unittest
import main as m
import json
import pathlib
# Define some constants which we may use for our testing
NEGATIVE_TESTS = ["this is a bad terrible awful low quality product", "you are doing a terrible job", "you are bad at this", "horrible assistant ", "you are not useful at all","you are terrible at your job "]
DEFAULT_TESTS = ["what the" , "tell me more", "what is meaning", "did the chicken come before the egg", "how much does a burger cost"]

class testBotMethods(unittest.TestCase):
    def __init__(self):
        self.loaded_clf = m.load_sentiment_analysis()[0]
        # Take in basic paramaters
        with open(f'{pathlib.Path(__file__).parent.absolute()}\\intents.json') as jsonFile:
            self.data = json.load(jsonFile)
        
    def testIntent(self):
        for test in NEGATIVE_TESTS:
            modelResponse = m.getFinalOutput(self.loaded_clf, test)
            self.assertTrue(modelResponse in m.NEGATIVE_RESPONSES)
        # ensure an extremely negative response is negative

    def testResponses(self):
        possibleOutputs = []
        # ensure we can get desired responses for very typical questions
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]: 
                #sampleInput = one of the input sentences for this tag
                sampleInput = pattern
                modelResponse = m.getFinalOutput(self.loaded_clf, sampleInput)
                for responses in intent["responses"]:
                    possibleOutputs.append(responses)
                #possibleOutputs = list of all outputs for that tag
                self.assertTrue(modelResponse in possibleOutputs)

    def testDefault(self): 
        # ensure we can get a default response when not discussing any subjects
        for test in DEFAULT_TESTS:
            modelResponse = m.getFinalOutput(self.loaded_clf, test)
            self.assertTrue(modelResponse in m.DEFAULT_RESPONSES)

if __name__ == '__main__':
    sampleTest = testBotMethods()
    sampleTest.testDefault()
    sampleTest.testIntent()
    sampleTest.testResponses()