# -*- coding: utf-8 -*-

"""
requests.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

# Note: We've patched out simplejson support in pip because it prevents
#       upgrading simplejson on Windows.
# try:
#     import simplejson as json
# except (ImportError, SyntaxError):
#     # simplejson does not support Python 3.2, it throws a SyntaxError
#     # because of u'...' Unicode literals.
import json

# ---------
# Specifics
# ---------

if is_py2:
    from urllib2 import parse_http_list
    from StringIO import StringIO
    # Keep OrderedDict for backwards compatibility.

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)
    integer_types = (int, long)

elif is_py3:
    from http.cookies import Morsel
    from io import StringIO
    # Keep OrderedDict for backwards compatibility.
    from collections import OrderedDict

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)
    integer_types = (int,)
