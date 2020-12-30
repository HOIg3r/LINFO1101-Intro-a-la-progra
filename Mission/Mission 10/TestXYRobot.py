#Programme Réalisé par Jacques HOGGE et Cindie Scheuren
#25 novembre 2020
import unittest
import XYRobot as x

#definition de la classe Test
class TestXYRobot(unittest.TestCase):
    
    def setUp(self): #set up et toujours appelé pour chaque test et recrée un robot
        self.r = x.XYRobot("R2-D2")
    
    def test_robot_is_instance_of_robot(self):
        self.assertIsInstance(self.r, x.XYRobot)
        
    def test_angle_robot(self):
        self.assertEqual(self.r.getangle(), 0)
        self.r.turnleft()
        self.assertEqual(self.r.getangle(), 270)
        self.r.turnleft()
        self.assertEqual(self.r.getangle(), 180)
    
    def test_angle_rad_robot(self):
        self.assertEqual(self.r.getanglerad(), 0)
        self.r.turnleft()
        self.assertEqual(self.r.getanglerad(), -1.5707963267948966)
        self.r.turnleft()
        self.assertEqual(self.r.getanglerad(), -3.141592653589793)
    
    def test_position_robot(self):
        self.assertAlmostEqual(self.r.position(), (0,0))
        self.r.moveforward(50)
        self.assertAlmostEqual(self.r.position(), (50,0))
        
    def test_getx(self):
        self.assertEqual(self.r.getx(), 0)
        self.r.moveforward(20)
        self.assertEqual(self.r.getx(), 20)
        self.r.movebackward(10)
        self.assertEqual(self.r.getx(), 10)
        self.r.turnright()
        self.r.moveforward(10)
        self.assertEqual(self.r.getx(), 10)
    
    def test_gety(self):
        self.assertEqual(self.r.gety(), 0)
        self.r.moveforward(20)
        self.assertEqual(self.r.gety(), 0)
        self.r.movebackward(10)
        self.assertEqual(self.r.gety(), 0)
        self.r.turnright()
        self.r.moveforward(10)
        self.assertEqual(self.r.getx(), 10)
        self.r.movebackward(2)
        self.assertEqual(self.r.gety(), 8)

if __name__ == '__main__':
    unittest.main()