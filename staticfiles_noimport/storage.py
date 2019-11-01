import os
import gzip
import shutil

from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.storage import (
    ManifestStaticFilesStorage as DjangoManifestStaticFilesStorage,
)
from django.contrib.staticfiles.storage import staticfiles_storage


class GZipPostProcessMixin:
    gzip_extensions = (".js", ".css")

    def post_process(self, *args, **kwargs):
        retval = super().post_process(*args, **kwargs)
        # This operation only makes sense for local storage
        # Since we're primarily solving for uWSGI's gzip serving mode
        print(staticfiles_storage.__class__.__name__)
        if isinstance(staticfiles_storage, FileSystemStorage):
            flattened_files = []
            for k, v in self.hashed_files.items():
                flattened_files.append(k)
                flattened_files.append(v)
            for f in flattened_files:
                path = staticfiles_storage.path(f)
                _, ext = os.path.splitext(path)
                if ext in self.gzip_extensions:
                    with open(path, "rb") as f_in:
                        with gzip.open(path + ".gz", "wb") as f_out:
                            shutil.copyfileobj(f_in, f_out)
        return retval


class GZipManifestStaticFilesStorage(
    GZipPostProcessMixin, DjangoManifestStaticFilesStorage
):
    """Extention to ManifestStaticFilesStorage that gzips files for easy uWSGI static serving"""
