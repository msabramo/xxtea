import unittest
import random
import xxtea


class TestXXTEA(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(xxtea.encrypt('How do you do?', 'Fine. And you?'), b'dd2c3bffc7b08b20c2700eb51539c18f')

    def test_decrypt(self):
        self.assertEqual(xxtea.decrypt('dd2c3bffc7b08b20c2700eb51539c18f', 'Fine. And you?'), b'How do you do?')

    def test_raw(self):
        enc = xxtea.encrypt('How do you do?', 'Fine. And you?', xxtea.RESULT_TYPE_RAW)
        dec = xxtea.decrypt(enc, 'Fine. And you?', xxtea.RESULT_TYPE_RAW)
        self.assertEqual(b'How do you do?', dec)


if __name__ == '__main__':
    unittest.main()
