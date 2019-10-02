from unittest import TestCase

import KataSimple


class kataSimpleTest(TestCase):
    def test_iteracion1(self):
        self.assertEqual(KataSimple().iteracion1(""), 0, "Cadena vacia")
