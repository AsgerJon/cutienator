"""Opens the shared object of the example and readies its functions."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ctypes
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Tuple

#  The four kinds of value that cross between Python and C++ here.
ADDRESS = ctypes.c_void_p  # where a C++ object is
FLAG = ctypes.c_bool  # True or False
TEXT = ctypes.c_char_p  # UTF-8 bytes handed to C++
COUNT = ctypes.c_longlong  # a whole number

#  For each function of the shared object: what comes back, then what
#  goes in. This must say the same as the ritual files do, and nothing
#  checks that it does.
SIGNATURES = {
    'QObject_new': (ADDRESS, ADDRESS),
    'QObject_delete': (None, ADDRESS),
    'QObject_parent': (ADDRESS, ADDRESS),
    'QObject_setParent': (None, ADDRESS, ADDRESS),
    'QObject_isWidgetType': (FLAG, ADDRESS),
    'QObject_signalsBlocked': (FLAG, ADDRESS),
    'QObject_blockSignals': (FLAG, ADDRESS, FLAG),
    'QObject_inherits': (FLAG, ADDRESS, TEXT),
    'QObject_deleteLater': (None, ADDRESS),
    'QObject_setObjectName': (None, ADDRESS, TEXT),
    'QObject_objectName': (ADDRESS, ADDRESS),
    'QByteArray_constData': (ADDRESS, ADDRESS),
    'QByteArray_size': (COUNT, ADDRESS),
    'QByteArray_delete': (None, ADDRESS),
}  # type: Dict[str, Tuple[Any, ...]]


def openExample(path: str) -> ctypes.CDLL:
  """
  Opens the shared object and tells 'ctypes' what goes in and out of
  each function listed in 'SIGNATURES'.

  Parameters
  ----------

  path : str
    The path of the shared object, as 'Build.run' returns it.

  Returns
  -------

  ctypes.CDLL
    The opened shared object; each function is an attribute of it.

  Raises
  ------

  FileNotFoundError
    There is no shared object at the path; 'Build.run' makes it.

  LookupError
    The shared object offers no function of a listed name.
  """
  try:
    ours = ctypes.CDLL(path)
  except OSError as osError:
    infoSpec = """There is no shared object at '%s' to open. 'Build.run'
    makes it."""
    info = ' '.join((infoSpec % path).split())
    raise FileNotFoundError(info) from osError
  for name, (gives, *takes) in SIGNATURES.items():
    try:
      function = getattr(ours, name)
    except AttributeError as attributeError:
      infoSpec = """'%s' offers no function named '%s'."""
      raise LookupError(infoSpec % (path, name)) from attributeError
    function.restype = gives
    function.argtypes = takes
  return ours


def readText(ours: ctypes.CDLL, held: int) -> str:
  """
  Reads the text of a QByteArray and deletes the QByteArray.

  Parameters
  ----------

  ours : ctypes.CDLL
    The opened shared object.

  held : int
    The address of the QByteArray, as a function returning text gives.

  Returns
  -------

  str
    The text.
  """
  start = ours.QByteArray_constData(held)
  size = ours.QByteArray_size(held)
  try:
    return ctypes.string_at(start, size).decode('utf-8')
  finally:
    ours.QByteArray_delete(held)
