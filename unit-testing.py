import unittest
import main as m
# Define some constants which we may use for our testing
NEGATIVE_MESSAGE = ""

class testBotMethods(unittest.TestCase):
    def __init__(self):
        self.loaded_clf = load_sentiment_analysis()[0]
        # Take in basic paramaters
        
    def testIntent():
        # ensure an extremely negative response is negative

    def testResponses():
        # ensure we can get desired responses for very typical questions
        for tag in intents.json:
            sampleInput = one of the input tags
            modelResponse = m.getFinalOutput(self.loaded_clf, sampleInput)
            possibleOutputs = list of all outputs for that tag
            self.assertTrue(modelResponse in possibleOutputs)

    def testDefault(): 
        # ensure we can get a default response when not discussing any subjects

if __name__ == '__main__':
    unittest.main()