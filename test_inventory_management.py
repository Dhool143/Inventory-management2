


# import unittest 
# from inventory import duplicateZeros

# class TestInventoryManagement(unittest.TestCase):
    
    
#     # Normal case
    
    
#  def test_example_case(self):
#      arr = [4,0,1,3,0,2,5,0]
#      duplicateZeros(arr)
#      self.assertEqual(arr, [4,0,0,1,3,0,0,2])
     
#  def test_no_zero(self):
#      arr = [3,2,1]
#      duplicateZeros(arr)
#      self.assertEqual(arr, [3,2,1])
     
#  def test_one_zero_middle(self):
#      arr = [ 1,2,0,3,4]
#      duplicateZeros(arr)
#      self.assertEqual(arr, [1,2,0,0,3])
     
     
#      # Edge case
     
     
#  def test_empty_array(self):
#     arr = []
#     duplicateZeros(arr)
#     self.assertEqual(arr, [])
    
    
#  def test_all_zeros(self):
#     arr = [0,0,0]
#     duplicateZeros(arr)
#     self.assertEqual(arr, [0,0,0])
    
    
#  def test_zero_at_end(self):
#     arr = [1,2,3,0]
#     duplicateZeros(arr)
#     self.assertEqual(arr, [1,2,3,0])
    
    
    
# if __name__ == "__main__":
#     unittest.main()






import unittest

from inventory import duplicateZeros

class TestInventoryManagement(unittest.TestCase):
    
    
    def test_example_case(self):
        arr = [4,0,1,3,0,2,5,0]
        duplicateZeros(arr)
        self.assertEqual(arr, [4,0,0,1,3,0,0,2])
        
        
    def test_no_zeros(self):
        arr = [4,3,2,1]
        duplicateZeros(arr)
        self.assertEqual(arr, [4,3,2,1])
    
    def test_one_zero_at_middle(self):
        arr = [1,2,0,3,4]
        duplicateZeros(arr)
        self.assertEqual(arr, [1,2,0,0,3])
        
        
        
        
        
    def test_empty_array(self):
        arr = []
        duplicateZeros(arr)
        self.assertEqual(arr, [])
        
        
    def test_all_zeros(self):
        arr = [0,0,0]
        duplicateZeros(arr)
        self.assertEqual(arr, [0,0,0])
        
    def test_zero_at_end(self):
        arr = [1,2,3,0,]
        duplicateZeros(arr)
        self.assertEqual(arr, [1,2,3,0])
            
        
if __name__ == "__main__":
    unittest.main()