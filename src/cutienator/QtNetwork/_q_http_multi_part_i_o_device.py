"""
QHttpMultiPartIODevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QHttpMultiPartIODevice to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QIODevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QHttpMultiPartPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpMultiPartPrivate = WAIT['QHttpMultiPartPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpMultiPartIODevice(QIODevice):
  """
  The cute side of Qt's QHttpMultiPartIODevice: a plain Python object
  standing in front of one C++ QHttpMultiPartIODevice.

  It is built on the cute 'QIODevice', as Qt's QHttpMultiPartIODevice is
  built on Qt's QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpMultiPartIODevice that has a ritual and that
  Python can call so far, 8 names in all: 'atEnd', 'bytesAvailable', 'close',
  'bytesToWrite', 'size', 'isSequential', 'reset', 'writeData'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpMultiPartIODevice::~QHttpMultiPartIODevice()': the destructor:
    Python never removes a C++ QHttpMultiPartIODevice.
  - Qt's 'qint64 QHttpMultiPartIODevice::readData(char *data, qint64
    maxSize)': names 'char', which has no cute class yet.

  What to expect
  --------------

  - The C++ QHttpMultiPartIODevice is created at the first use, not by
    'QHttpMultiPartIODevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpMultiPartIODevice.
  - Qt tells when it has removed the C++ QHttpMultiPartIODevice. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpMultiPartIODevice'

  #  A C++ QHttpMultiPartIODevice Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpMultiPartIODevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QHttpMultiPartIODevice::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#atEnd
    """
    #  bool QHttpMultiPartIODevice::atEnd() const
    ritual = 'ritual_ZNK22QHttpMultiPartIODevice5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QHttpMultiPartIODevice5atEndEv'
    return self.uglySide.call(ritual)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QHttpMultiPartIODevice::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#bytesAvailable
    """
    #  qint64 QHttpMultiPartIODevice::bytesAvailable() const
    ritual = 'ritual_ZNK22QHttpMultiPartIODevice14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QHttpMultiPartIODevice14bytesAvailableEv'
    return self.uglySide.call(ritual)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QHttpMultiPartIODevice::bytesToWrite() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#bytesToWrite
    """
    #  qint64 QHttpMultiPartIODevice::bytesToWrite() const
    ritual = 'ritual_ZNK22QHttpMultiPartIODevice12bytesToWriteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QHttpMultiPartIODevice12bytesToWriteEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QHttpMultiPartIODevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#size
    """
    #  qint64 QHttpMultiPartIODevice::size() const
    ritual = 'ritual_ZNK22QHttpMultiPartIODevice4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QHttpMultiPartIODevice4sizeEv'
    return self.uglySide.call(ritual)

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QHttpMultiPartIODevice::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#isSequential
    """
    #  bool QHttpMultiPartIODevice::isSequential() const
    ritual = 'ritual_ZNK22QHttpMultiPartIODevice12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QHttpMultiPartIODevice12isSequentialEv'
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

  @overload(QHttpMultiPartPrivate)
  @overload(NoneType)
  def __init__(
      self,
      parentMultiPart: Optional[QHttpMultiPartPrivate],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpMultiPartIODevice::QHttpMultiPartIODevice(QHttpMultiPartPrivate
    *parentMultiPart)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#QHttpMultiPartIODevice

    Parameters
    ----------

    parentMultiPart : Optional[QHttpMultiPartPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpMultiPartIODevice::QHttpMultiPartIODevice(QHttpMultiPartPrivate
    #      *parentMultiPart)
    self._noteCreation(QHttpMultiPartIODevice, lambda: Rituals.call(
        'ritual_ZN22QHttpMultiPartIODeviceC1EP21QHttpMultiPartPrivate',
        self._addressOf(parentMultiPart),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QHttpMultiPartIODevice::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#close
    """
    #  void QHttpMultiPartIODevice::close()
    ritual = 'ritual_ZN22QHttpMultiPartIODevice5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QHttpMultiPartIODevice5closeEv'
    self.uglySide.call(ritual)

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QHttpMultiPartIODevice::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#reset
    """
    #  bool QHttpMultiPartIODevice::reset()
    ritual = 'ritual_ZN22QHttpMultiPartIODevice5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QHttpMultiPartIODevice5resetEv'
    return self.uglySide.call(ritual)

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QHttpMultiPartIODevice::writeData(const char *data,
    qint64 maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpmultipartiodevice.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QHttpMultiPartIODevice::writeData(const char *data, qint64
    #      maxSize)
    return self.uglySide.call(
        'ritual_ZN22QHttpMultiPartIODevice9writeDataEPKcx',
        self._bytesOf(data), maxSize,
    )
