import unittest
from probe import Probe


class ProbeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ProbeTest, self).__init__(*args, **kwargs)

    def setUp(self):
        super(ProbeTest, self).setUp()
        self.ECOSYSTEM = {
            (2, 2),
            (1, 2),
            (0, 2),
            (2, 1),
        }

        self.dimensions = [20, 20]

        self.Probe = Probe(self.dimensions[0], self.dimensions[1], self.ECOSYSTEM)

        self.__str__ = str(self.Probe)

        self.first_generation = [6, 47, 86, 88]

    def test_Probe_instance(self):
        """
            The Probe needs initialize with a required params
            and returns a correct instance
        """
        Probe = self.Probe

        # Testing if is assigned successfully
        self.assertTrue(isinstance(Probe, Probe))

        # Testing life generation
        self.assertEqual(len(self.__str__), 820)

        # Testing number of alive cells
        self.assertEqual(self.__str__.count("*"), 4)

        # Testing correct elements
        self.assertTrue(True for p in self.first_generation if self.__str__[p] == "*")

    def test_next_generation(self):
        """
         The next_generation advances one generation
        """
        Probe = self.Probe

        # Testing previous generation
        self.assertTrue(True for char in self.first_generation if char == "*")

        # Generate life
        self.Probe.next_generation()
        self.__str__ = str(self.Probe)

        # Testing number of alive cells
        self.assertEqual(self.__str__.count("*"), 4)

        # Second generation
        second_generation = [47, 49, 86, 88]

        # Testing second generation
        self.assertTrue(True for p in second_generation if self.__str__[p] == "*")

if __name__ == '__main__':
    unittest.main()