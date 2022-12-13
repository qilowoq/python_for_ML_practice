import unittest
from complex import Complex
import math

class TestComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.complex = Complex


    def test_add(self) -> None:
        self.assertEqual(self.complex(1, 2) + self.complex(3, 1), self.complex(4, 3))
        self.assertEqual(self.complex(1, -1) + self.complex(-3, 1), self.complex(-2, 0))
    

    def test_sub(self) -> None:
        self.assertEqual(self.complex(1, 2) - self.complex(3, 1), self.complex(-2, 1))
        self.assertEqual(self.complex(1, -1) - self.complex(-3, 1), self.complex(4, -2))


    def test_mul(self) -> None:
        self.assertEqual(self.complex(1, 2) * self.complex(3, 1), self.complex(1, 7))
        self.assertEqual(self.complex(1, -1) * self.complex(-3, 1), self.complex(-2, 4))


    def test_div(self) -> None:
        self.assertEqual(self.complex(1, 2) / self.complex(2, -1), self.complex(0, 1))
        self.assertEqual(self.complex(1, -1) / self.complex(3, 4), self.complex(-0.04, -0.28))


    def test_abs(self) -> None:
        self.assertEqual(self.complex(1,1).abs(), math.sqrt(2))
        self.assertEqual(self.complex(0,1).abs(), 1)
        self.assertEqual(self.complex(1,-5).abs(), math.sqrt(26))
        self.assertEqual(self.complex(-3, 4).abs(), 5)


if __name__ == "__main__":
    unittest.main()