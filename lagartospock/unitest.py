import unittest
import lagartospock
#Nota:hay que el optimizar test
class Test_Game(unittest.TestCase):
    def test_increment(self):

        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("piedra","tijera"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("piedra","lagarto"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("papel","spock"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("papel","piedra"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("tijera","lagarto"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("tijera","papel"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("lagarto","spock"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("lagarto","papel"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("spock","tijera"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("spock","piedra"),"Player 1 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("tijera","piedra"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("lagarto","piedra"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("spock","papel"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("piedra","papel"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("lagarto","tijera"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("papel","tijera"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("spock","lagarto"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("papel","lagarto"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("tijera","spock"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("piedra","spock"),"Player 2 gana")
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("piedra","piedra"),'Empate')
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("papel","papel"),'Empate')
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("tijera","tijera"),'Empate')
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("lagarto","lagarto"),'Empate')
        self.assertEqual(lagartospock.Game(lagartospock.Player(), lagartospock.Player()).play("spock","spock"),'Empate') 

if __name__ == '__main__':
    unittest.main()