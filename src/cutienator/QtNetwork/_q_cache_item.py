"""
QCacheItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCacheItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QFileDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileDevice = WAIT['QFileDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCacheItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCacheItem: a plain Python object standing in front
  of one C++ QCacheItem.

  What exists
  -----------

  Every function of Qt's QCacheItem that has a ritual and that Python can
  call so far, 5 names in all: 'size', 'reset', 'writeHeader',
  'writeCompressedData', 'canCompress'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCacheItem::~QCacheItem()': the destructor: Python never removes a
    C++ QCacheItem.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCacheItem is created at the first use, not by 'QCacheItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCacheItem.
  - Each name of Qt's QCacheItem that has no cute function yet, 'read', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCacheItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QCacheItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcacheitem.html#size
    """
    #  qint64 QCacheItem::size() const
    return self.uglySide.call('ritual_ZNK10QCacheItem4sizeEv')

  def canCompress(self) -> bool:
    """
    Calls Qt's 'bool QCacheItem::canCompress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcacheitem.html#canCompress
    """
    #  bool QCacheItem::canCompress() const
    return self.uglySide.call('ritual_ZNK10QCacheItem11canCompressEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCacheItem::QCacheItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcacheitem.html#QCacheItem
    """
    #  QCacheItem::QCacheItem()
    self._noteCreation(QCacheItem, lambda: Rituals.call(
        'ritual_ZN10QCacheItemC1Ev',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def reset(self) -> None:
    """
    Calls Qt's 'void QCacheItem::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qcacheitem.html#reset
    """
    #  void QCacheItem::reset()
    self.uglySide.call('ritual_ZN10QCacheItem5resetEv')

  @overload(QFileDevice)
  @overload(NoneType)
  def writeHeader(self, device: Optional[QFileDevice]) -> None:
    """
    Calls Qt's 'void QCacheItem::writeHeader(QFileDevice *device) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcacheitem.html#writeHeader

    Parameters
    ----------

    device : Optional[QFileDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCacheItem::writeHeader(QFileDevice *device) const
    self.uglySide.call(
        'ritual_ZNK10QCacheItem11writeHeaderEP11QFileDevice',
        self._addressOf(device),
    )

  @overload(QFileDevice)
  @overload(NoneType)
  def writeCompressedData(self, device: Optional[QFileDevice]) -> None:
    """
    Calls Qt's 'void QCacheItem::writeCompressedData(QFileDevice *device)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcacheitem.html#writeCompressedData

    Parameters
    ----------

    device : Optional[QFileDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCacheItem::writeCompressedData(QFileDevice *device) const
    self.uglySide.call(
        'ritual_ZNK10QCacheItem19writeCompressedDataEP11QFileDevice',
        self._addressOf(device),
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'bool QCacheItem::read(QFileDevice *device, bool readData)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'CacheMagic'.
    """
    raise NotImplementedError(
        "'QCacheItem.read' has no cute function yet. Qt's 'bool "
        "QCacheItem::read(QFileDevice *device, bool readData)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'CacheMagic'.")
