import unittest
def sum(a,b):
    return a + b

class sumTest(unittest.TestCase):
    #we use the setUp method to replace the arrange part since it is repeted
    def setUp(self):
        print('setUp is called')
        self.a = 10
        self.b = 20

    def tearDown(self):
        self.a = 0
        self.b = 0
        print("tearDown function is called")    
    def test_sum_func1(self):
        print("function1 is called")
        # Act
        result = sum(self.a,self.b)
        # Assert   
        self.assertEqual(result,self.a + self.b) 
        
    def test_sum_func2(self):
        print("function2 is called")
        #Act
        result = sum(self.b,self.a)
        #Assert
        self.assertEqual(result,self.a + self.b)
if __name__ == "__main__":
    unittest.main()        