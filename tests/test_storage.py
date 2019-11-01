import os
import gzip
import tempfile
import subprocess
import unittest


class TestGZipManifestStaticFilesStorage(unittest.TestCase):
    def setUp(self):
        tmp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(tmp_dir.cleanup)
        self.static_root = tmp_dir.name
        os.environ["STATIC_ROOT"] = self.static_root
        os.environ["SECRET_KEY"] = "staticfiles"
        os.environ["DJANGO_SETTINGS_MODULE"] = "settings.static"
        os.environ[
            "STATICFILES_STORAGE"
        ] = "staticfiles_noimport.storage.GZipManifestStaticFilesStorage"

        # Set current working directory to the root of exampleproj
        tests_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(os.path.join(tests_root, "exampleproj"))
        super().setUp()

    def test_no_gzip_other_filetypes(self):
        subprocess.check_call(["collectstatic"])
        import pdb

        pdb.set_trace()
        self.assertTrue(os.path.isfile(os.path.join(self.static_root, "foo.txt")))
        self.assertFalse(os.path.isfile(os.path.join(self.static_root, "foo.txt.gz")))

    def test_gzip_file_base_name(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(os.path.isfile(os.path.join(self.static_root, "jquery.js.gz")))

    def test_gzip_file_hashed_name(self):
        subprocess.check_call(["collectstatic"])
        self.assertTrue(
            os.path.isfile(os.path.join(self.static_root, "jquery.11c05eb286ed.js.gz"))
        )

    def test_gzip_validate_file_contents(self):
        subprocess.check_call(["collectstatic"])
        src_jquery_path = os.path.join(self.static_root, "jquery.js")
        gzip_jquery_path = os.path.join(self.static_root, "jquery.js.gz")
        src_jquery, gzip_jquery = (True, False)
        with open(src_jquery_path, "rb") as inf:
            src_jquery = inf.read()
        with gzip.open(gzip_jquery_path, "rb") as inf:
            gzip_jquery = inf.read()
        self.assertEqual(src_jquery, gzip_jquery)
