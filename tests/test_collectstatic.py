import os
import unittest
import tempfile
import subprocess


class TestCollectStatic(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory for STATIC_ROOT
        tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(tmp_dir.cleanup)
        self.static_root = tmp_dir.name
        os.environ["STATIC_ROOT"] = self.static_root
        os.environ["SECRET_KEY"] = "staticfiles"
        os.environ["DJANGO_SETTINGS_MODULE"] = "settings.static"

        # Set current working directory to the root of exampleproj
        tests_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(os.path.join(tests_root, "exampleproj"))
        super().setUp()

    def test_django_contrib_admin_collected(self):
        subprocess.check_call(["collectstatic"])
        # Assert we collected admin/css/base.css
        self.assertTrue(
            os.path.isfile(os.path.join(self.static_root, "admin", "css", "base.css"))
        )

    def test_file_system_finder_static_collected(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(os.path.isfile(os.path.join(self.static_root, "bar.txt")))

    def test_projectapp_static_collected(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(os.path.isfile(os.path.join(self.static_root, "foo.txt")))

    def test_file_system_finder_static_fingerprint(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(
            os.path.isfile(os.path.join(self.static_root, "bar.09730bc4e0b6.txt"))
        )

    def test_projectapp_static_fingerprint(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(
            os.path.isfile(os.path.join(self.static_root, "foo.45509a73b8fe.txt"))
        )
