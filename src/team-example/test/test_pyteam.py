import unittest


class PyTeamTest(unittest.TestCase):
    def test_base_success(self):
        print('Great success')

        self.failIf(False, 'should not fail')

    def test_base_fail(self):
        self.fail('Force failing this test')


if __name__ == '__main__':
    unittest.main(verbosity=2)
