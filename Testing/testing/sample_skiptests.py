import unittest
import sys


class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 4, "broken on 3.4")
    def test_skipif(self):
        self.assertEqual(False, True)

    # SKIP nếu hệ điều hành không phải win32 (win32 vẫn chạy)
    @unittest.skipUnless(sys.platform.startswith("Linux"), "broken unless on win32/linux")
    def test_skipunless(self):
        self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()
