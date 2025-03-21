# -*- coding: utf-8 -*-

from system_tests import CaseMeta, path


class OutOfMemoryInJp2ImageReadMetadata(metaclass=CaseMeta):
    """
    Regression test for the bug described in:
    https://github.com/Exiv2/exiv2/issues/1812

    Due to a missing bounds check, this test triggers a 4GB memory
    allocation. So the test will fail with a std::bad_alloc exception
    if less than 4GB is available.  On Linux, you can use `ulimit -v
    4000000` to reduce the available memory to slightly less than 4GB.
    """

    url = "https://github.com/Exiv2/exiv2/issues/1812"

    filename = path("$data_path/issue_1812_poc.jp2")
    commands = ["$exiv2 $filename"]
    stdout = [""]
    stderr = [
        """$exiv2_exception_message $filename:
$kerCorruptedMetadata
"""
    ]
    retval = [1]
