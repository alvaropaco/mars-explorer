import unittest
from probe import Probe


class ProbeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ProbeTest, self).__init__(*args, **kwargs)

    def setUp(self):
        super(ProbeTest, self).setUp()

        self.Probe = Probe('5', '5', '1', '2', 'N')

        self.Probe.explore("LMLMLMLMM")

        self.__str__ = str(self.Probe)

    def test_Probe_instance(self):
        new_probe = Probe('5', '5', '3', '3', 'E')

        self.assertTrue(isinstance(new_probe, Probe))

    def test_Probe_explore(self):
        self.assertEqual(self.__str__, "1 3 N")

    def test_Probe_explore(self):
        with self.assertRaises(Exception) as context:
            Probe('5', '5', '$', '3', 'E')

        self.assertTrue('invalid literal for int() with base 10: \'$\''
                         in context.exception)

if __name__ == '__main__':
    unittest.main()
