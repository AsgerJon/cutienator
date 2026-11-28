"""
QByteDeviceWrappingIoDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QByteDeviceWrappingIoDevice to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QIODevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QByteDeviceWrappingIoDevice(QIODevice):
  """
  The cute side of Qt's QByteDeviceWrappingIoDevice: a plain Python object
  standing in front of one C++ QByteDeviceWrappingIoDevice.

  It is built on the cute 'QIODevice', as Qt's QByteDeviceWrappingIoDevice is
  built on Qt's QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QByteDeviceWrappingIoDevice that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'isSequential',
  'atEnd', 'reset', 'size', 'writeData'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QByteDeviceWrappingIoDevice::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QByteDeviceWrappingIoDevice::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QByteDeviceWrappingIoDevice::~QByteDeviceWrappingIoDevice()': the
    destructor: Python never removes a C++ QByteDeviceWrappingIoDevice.
  - Qt's 'qint64 QByteDeviceWrappingIoDevice::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QByteDeviceWrappingIoDevice.

  What to expect
  --------------

  - The C++ QByteDeviceWrappingIoDevice is created at the first use, not by
    'QByteDeviceWrappingIoDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QByteDeviceWrappingIoDevice.
  - Qt tells when it has removed the C++ QByteDeviceWrappingIoDevice. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QByteDeviceWrappingIoDevice that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QByteDeviceWrappingIoDevice'

  #  A C++ QByteDeviceWrappingIoDevice Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QByteDeviceWrappingIoDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QByteDeviceWrappingIoDevice::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QByteDeviceWrappingIoDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QByteDeviceWrappingIoDevice10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QByteDeviceWrappingIoDevice::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#isSequential
    """
    #  bool QByteDeviceWrappingIoDevice::isSequential() const
    ritual = 'ritual_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QByteDeviceWrappingIoDevice12isSequentialEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QByteDeviceWrappingIoDevice::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#atEnd
    """
    #  bool QByteDeviceWrappingIoDevice::atEnd() const
    ritual = 'ritual_ZNK27QByteDeviceWrappingIoDevice5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QByteDeviceWrappingIoDevice5atEndEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QByteDeviceWrappingIoDevice::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#size
    """
    #  qint64 QByteDeviceWrappingIoDevice::size() const
    ritual = 'ritual_ZNK27QByteDeviceWrappingIoDevice4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QByteDeviceWrappingIoDevice4sizeEv'
    return self.uglySide.call(ritual)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice(
    QNonContiguousByteDevice *bd)': leans on
    'QByteDeviceWrappingIoDevice::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QByteDeviceWrappingIoDevice.__init__' has no cute function yet. "
        "Qt's "
        "'QByteDeviceWrappingIoDevice::QByteDeviceWrappingIoDevice(QNonConti"
        "guousByteDevice *bd)': leans on "
        "'QByteDeviceWrappingIoDevice::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QByteDeviceWrappingIoDevice::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#reset
    """
    #  bool QByteDeviceWrappingIoDevice::reset()
    ritual = 'ritual_ZN27QByteDeviceWrappingIoDevice5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QByteDeviceWrappingIoDevice5resetEv'
    return self.uglySide.call(ritual)

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QByteDeviceWrappingIoDevice::writeData(const char
    *data, qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbytedevicewrappingiodevice.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QByteDeviceWrappingIoDevice::writeData(const char *data, qint64
    #      maxSize)
    return self.uglySide.call(
        'ritual_ZN27QByteDeviceWrappingIoDevice9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )
