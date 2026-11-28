"""
QImageReaderWriterHelpers stands for the namespace
'QImageReaderWriterHelpers' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QImageReaderWriterHelpers:
  """
  The namespace 'QImageReaderWriterHelpers' of Qt, which holds no objects. It
  holds the 2 enums Qt writes in it, each under its name, and the 0 names Qt
  has for the combinations of a flags enum, each holding the class of that
  enum. It is never made into an object.
  """

  class Capability(CuteNum):
    """
    The enum 'QImageReaderWriterHelpers::Capability' of Qt, with the 2 names
    Qt gives in it.
    """

    CanRead = Kee[int](0)
    CanWrite = Kee[int](1)

  class _qt_BuiltInFormatType(CuteNum):
    """
    The enum 'QImageReaderWriterHelpers::_qt_BuiltInFormatType' of Qt, with
    the 9 names Qt gives in it.
    """

    _qt_PngFormat = Kee[int](0)
    _qt_BmpFormat = Kee[int](1)
    _qt_PpmFormat = Kee[int](2)
    _qt_PgmFormat = Kee[int](3)
    _qt_PbmFormat = Kee[int](4)
    _qt_XbmFormat = Kee[int](5)
    _qt_XpmFormat = Kee[int](6)
    _qt_NumFormats = Kee[int](7)
    _qt_NoFormat = Kee[int](-1)
