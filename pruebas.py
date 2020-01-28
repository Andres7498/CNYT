
import unittest
import Calculadoracomplejos

class Testing(unittest.TestCase):
    def testsuma(self):
        a = (4,5)
        b = (3.6,-9.5654)
        self.assertEqual(Calculadoracomplejos.sumacom(a,b),(7.6,-4.5654))
    def testresta(self):
        a = (7,-3.5)
        b = (-5,-4)
        self.assertEqual(Calculadoracomplejos.rescom(a,b),(12,0.5))
    def testmulti(self):
        a = (3,-4)
        b = (2,5)
        self.assertEqual(Calculadoracomplejos.multicom(a,b),(26.0,7.0))
    def testmod(self):
        a = (5,-9)
        b = (6.32,5.2)
        self.assertEqual(Calculadoracomplejos.modcom(a,b),(10.295630140987,8.184277610149842))
    def testdiv(self):
        a = (-4,5)
        b = (8,-2)
        self.assertEqual(Calculadoracomplejos.divcom(a,b),(13.92,16.96))
    def testcon(self):
        a = (-4.56,5)
        b = (8,-78.654)
        self.assertEqual(Calculadoracomplejos.concom(a,b),((-4.56,-5.0),(8.0,78.654)))
    def testcart(self):
        a = (8,-2)
        self.assertEqual(Calculadoracomplejos.cartcom(a),(8,-2.0))
    def testfasecom(self):
        a = (3,-5)
        self.assertEqual(Calculadoracomplejos.fasecom(a),(-1.03))
    def testadicivectocom(self):
        a =[(3,-7),(2,-3.6),(5.899,-1.9),(1,2)]
        b=[(-56,86),(4,-9.6),(2.961,-9.1),(1,2)]
        self.assertEqual(Calculadoracomplejos.adicivectocom(a,b),[(-53.0,79.0),(6.0,-13.2),(8.86,-11.0),(2.0,4.0)])
    def testinvervectocom(self):
        a =[(3,-7),(2,-3.6),(5.899,-1.9),(1,2)]
        self.assertEqual(Calculadoracomplejos.invervectocom(a),[(-3,7),(-2,3.6),(-5.899,1.9),(-1,-2)])
    def testmultivectocom(self):
        a =[(3,-7),(2,-3.6),(5.899,-1.9),(1,2)]
        b =(-1,2)
        self.assertEqual(Calculadoracomplejos.multivectocom(a,b),[(11.0,13.0),(5.2,7.6),(-2.099,13.698),(-5.0,0)])
        
        
if __name__ == '__main__':
    unittest.main()
