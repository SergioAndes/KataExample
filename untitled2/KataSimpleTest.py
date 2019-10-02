from unittest import TestCase

from KataSimple import iteracion1


class kataSimpleTest(TestCase):
    def test_iteracion1(self):
        self.assertEqual(iteracion1(""), 0, "Cadena vacia")

    def test_iteracion1_unaCadena(self):
        self.assertEqual(iteracion1("1"), 1, "Un numero")
