from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I love working with Python')
        self.assertEqual( result_1, 'joy' ) 
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual( result_1, 'anger' ) 
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual( result_1, 'disgust' ) 
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual( result_1, 'sadness' ) 
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual( result_1, 'fear' ) 

unittest.main()