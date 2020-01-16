
import unittest
import cnyt

class Testing(unittest.TestCase):
    def testsuma(self):
        a = (4,5)
        b = (3.6,-9.5654)
        self.assertEqual(cnyt.sumacom(a,b),(7.6,-4.5654))
    def testresta(self):
        a = (7,-3.5)
        b = (-5,-4)
        self.assertEqual(cnyt.rescom(a,b),(12,0.5))
    def testmulti(self):
        a = (4,-6)
        b = (2,3)
        self.assertEqual(cnyt.multicom(a,b),(26,0))
    def testmod(self):
        a = (5,-9)
        b = (6.32,5.2)
        self.assertEqual(cnyt.modcom(a,b),(10.295630140987,8.184277610149842))
    def testdiv(self):
        a = (-4,5)
        b = (8,-2)
        self.assertEqual(cnyt.divcom(a,b),(13.92,16.96))
    def testcon(self):
        a = (-4.56,5)
        b = (8,-78.654)
        self.assertEqual(cnyt.concom(a,b),((-4.56,-5.0),(8.0,78.654)))
    def testcart(self):
        a = (-4.56,5)
        self.assertEqual(cnyt.cartcom(a),((4.56,-5.0))) 
if __name__ == '__main__':
    unittest.main()
