import os
import unittest

from pathlib import Path
from path_guard.protector import SafePathGuard



class TestSafePathGuard(unittest.TestCase):
    def setUp(self):
        '''Set up a fake base folder for testing'''
        self.base_dir = Path("/var/www/app/uploads").resolve()
        self.guard = SafePathGuard(str(self.base_dir))


    def test_safe_inputs(self):
        '''
        Dataset of safe paths that must
        return True
        '''
        safe_dataset = [
            "avatar.png",
            "documents/reports/2026/invoice.pdf",
            "nested/folder/./file.txt"
        ]
        for path in safe_dataset:
            with self.subTest(path=path):
                self.assertTrue(self.guard.is_safe_path(path))


    def test_dangerous_inputs(self):
        '''
        Dataset of dangerous input
        return False
        '''
        dangerous_dataset = [
            # Standard traversals
            "../../../etc/passwd",
            "images/../../etc/passwd",
            "..\\..\\..\\windows/win.ini",
            # Obfuscation (URL/Unicode)
            "%2e%2e%2f%2e%2e%2fetc/passwd",
            "nested%252e%252e%252fsecret.txt",
            "folder\u2215..\u2215etc\u2215passwd",
            # Linux sys files
            "/etc/passwd",
            "/proc/self/environ",
            "/etc/nginx/nginx.conf",
            # Secrets and backups
            ".env",
            "secrets.yml",
            "database.sql",
            "main.py.bak",
            ".env.production",
            # Broken or invalid types
            "",
            None,
            1245677362256,
            ["file.txt"],
            ["flags.txt"]
        ]

        # Add OS-specific paths
        if os.name == 'nt':
            dangerous_dataset.append("C:\\Windows\\System32\\drivers\\etc\\hosts")
        else:
            dangerous_dataset.append("/windows/system32/drivers/etc/hosts")

        for path in dangerous_dataset:
            with self.subTest(path=path):
                self.assertFalse(self.guard.is_safe_path(path))

if __name__ == "__main__":
    unittest.main()
