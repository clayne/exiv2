# -*- coding: utf-8 -*-

from system_tests import CaseMeta, CopyTmpFiles, path, check_no_ASAN_UBSAN_errors


@CopyTmpFiles("$data_path/issue_1881_poc.jpg", "$data_path/issue_1881_coverage.jpg")
class SonyPreviewImageLargeAllocation(metaclass=CaseMeta):
    """
    Regression test for the bug described in:
    https://github.com/Exiv2/exiv2/issues/1881
    """

    url = "https://github.com/Exiv2/exiv2/issues/1881"

    filename1 = path("$tmp_path/issue_1881_poc.jpg")
    filename2 = path("$tmp_path/issue_1881_coverage.jpg")
    commands = ["$exiv2 -q -d I rm $filename1", "$exiv2 -q -d I rm $filename2"]
    stderr = [
        f"""$exception_in_erase {filename1}:
$kerFailedToReadImageData
""",
        "",
    ]
    retval = [1, 0]

    compare_stdout = check_no_ASAN_UBSAN_errors
