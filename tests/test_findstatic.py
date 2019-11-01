import os
import subprocess
import unittest


class TestFindStatic(unittest.TestCase):
    def setUp(self):
        os.environ["STATIC_ROOT"] = ""
        os.environ["SECRET_KEY"] = "staticfiles"
        os.environ["DJANGO_SETTINGS_MODULE"] = "settings.static"

        # Set current working directory to the root of exampleproj
        tests_root = os.path.dirname(os.path.abspath(__file__))
        self.exampleproj_root = os.path.join(tests_root, "exampleproj")
        os.chdir(self.exampleproj_root)
        super().setUp()

    def test_findstatic_quiet(self):
        out = subprocess.check_output(["findstatic", "foo.txt", "--verbosity", "0"])
        full_path = out.decode("utf-8").strip()
        self.assertEqual(
            full_path, os.path.join(self.exampleproj_root, "projectapp/static/foo.txt")
        )
