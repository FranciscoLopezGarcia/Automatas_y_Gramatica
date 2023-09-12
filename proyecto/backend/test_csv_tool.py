import unittest
from parameterized import parameterized
import re
from csv_tool import MAC_AP_RE, MAC_CLIENT_RE, IP_NAS_RE, ID_RE, ID_SESION_RE, ID_CONEXION_UNICA_RE, USER_RE, DATE_RE, HOUR_RE

class TestRegex(unittest.TestCase):

    @parameterized.expand([
        ("Valid MAC_AP", MAC_AP_RE, "00:1A:2B:3C:4D:5E:HCDD", True),
        ("Invalid MAC_AP", MAC_AP_RE, "Invalid", False),
        ("Valid MAC_CLIENT", MAC_CLIENT_RE, "00:1A:2B:3C:4D:5E", True),
        ("Invalid MAC_CLIENT", MAC_CLIENT_RE, "Invalid", False),
        ("Valid IP_NAS", IP_NAS_RE, "192.168.247.12", True),
        ("Invalid IP_NAS", IP_NAS_RE, "Invalid", False),
        ("Valid ID", ID_RE, "1234567", True),
        ("Invalid ID", ID_RE, "Invalid", False),
        ("Valid ID_SESION", ID_SESION_RE, "/ABCDEF12-ABCDEF12", True),
        ("Invalid ID_SESION", ID_SESION_RE, "/Invalid", False),
        ("Valid ID_CONEXION_UNICA", ID_CONEXION_UNICA_RE, "/abcdef0123456789", True),
        ("Invalid ID_CONEXION_UNICA", ID_CONEXION_UNICA_RE, "/Invalid", False),
        ("Valid USER", USER_RE, "user123", True),
        ("Invalid USER", USER_RE, "Invalid-User", False),
        ("Invalid USER", USER_RE, "Invalid/User", False),
        ("Invalid USER", USER_RE, "Invalid_User", False),
        ("Valid DATE", DATE_RE, "2023-09-12", True),
        ("Invalid DATE", DATE_RE, "2023-13-01", False),
        ("Valid HOUR", HOUR_RE, "15:30:45", True),
        ("Invalid HOUR", HOUR_RE, "25:30:45", False),
    ])
    def test_regex(self, name, regex, input_str, expected_result):
        self.assertEqual(bool(re.fullmatch(regex, input_str)), expected_result)

if __name__ == "__main__":
    unittest.main()
