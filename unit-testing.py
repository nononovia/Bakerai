import unittest
import main as m
# Define some constants which we may use for our testing
NEGATIVE_TESTS = ["this is a bad terrible awful low quality product"]
DEFAULT_TESTS = ["what the"]

class testBotMethods(unittest.TestCase):
    def __init__(self):
        self.loaded_clf = load_sentiment_analysis()[0]
        # Take in basic paramaters
        
    def testIntent(self):
        for test in NEGATIVE_TESTS:
            modelResponse = m.getFinalOutput(self.loaded_clf, test)
            self.assertTrue(modelResponse in m.NEGATIVE_RESPONSES)
        # ensure an extremely negative response is negative

    def testResponses(self):
        # ensure we can get desired responses for very typical questions
        for tag in intents.json:
            sampleInput = one of the input sentences for this tag
            modelResponse = m.getFinalOutput(self.loaded_clf, sampleInput)
            possibleOutputs = list of all outputs for that tag
            self.assertTrue(modelResponse in possibleOutputs)

    def testDefault(self): 
        # ensure we can get a default response when not discussing any subjects
        for test in DEFAULT_TESTS:
            modelResponse = m.getFinalOutput(self.loaded_clf, test)
            self.assertTrue(modelResponse in m.DEFAULT_RESPONSES)

if __name__ == '__main__':
    unittest.main()