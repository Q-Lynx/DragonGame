import unittest
import os
from os.path import join, getsize
from DragonGame import Dragon


class DragonUnitTest(unittest.TestCase):

    def test_name(self):
        drag = Dragon("Stefan", 5)
        self.assertEqual(drag.name, "Stefan")
        self.assertTrue(drag.name == "Stefan")
        self.assertFalse(drag.name == "Grzegorz")

    def test_level(self):
        drag = Dragon("Stefan", 5)
        self.assertEqual(drag.level, 5)
        drag2 = Dragon("Stefan")
        self.assertEqual(drag2.level, 0)
        self.assertTrue(drag2.level == 0)
        self.assertFalse(drag2.level == 1)

    def test_str(self):
        drag = Dragon("Stefan", 5)
        self.assertEqual(str(drag), "name: Stefan, level: 5")

    def test_levelUp(self):
        drag = Dragon("Stefan")
        drag.levelUp()
        self.assertEqual(drag.level, 1)
    
    def test_save(self):
        filename = "Stefan.sv"
        drag = Dragon("Stefan", 5)
        drag.save(filename)
        for root, dirs, files in os.walk('/Users/macbook/Smoki'): #TODOFIX
           if filename in files:
               self.assertTrue(True) 
           else:
               self.assertFalse(True)  

#    def test_load(self):
#        name = None
#        level = None
#        filename = "Stefan.sv"
#        drag2 = Dragon.load("Stefan.sv")
#        self.assertThat(drag2, instanceof(Dragon))
#        self.assertEqual(drag2.name == "Stefan")
#        self.assertEqual(drag2.level == 5)
       
 
if __name__ == '__main__':
    unittest.main()
    



