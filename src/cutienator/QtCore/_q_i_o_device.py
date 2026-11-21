"""
QIODevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qiodevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QIODeviceBaseOpenModeFlag, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QIODeviceBase, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIODevice(QObject):
  """
  The cute side of Qt's QIODevice: a plain Python object standing in front of
  one C++ QIODevice.

  It is built on the cute 'QObject', as Qt's QIODevice is built on Qt's
  QObject, and has everything that class has. Qt's QIODevice is built on Qt's
  QIODeviceBase as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QIODevice that has a ritual and that Python can call
  so far, 39 names in all: 'metaObject', 'tr', 'openMode',
  'setTextModeEnabled', 'isTextModeEnabled', 'isOpen', 'isReadable',
  'isWritable', 'isSequential', 'readChannelCount', 'writeChannelCount',
  'currentReadChannel', 'setCurrentReadChannel', 'currentWriteChannel',
  'setCurrentWriteChannel', 'open', 'close', 'pos', 'size', 'seek', 'atEnd',
  'reset', 'bytesAvailable', 'bytesToWrite', 'read', 'readAll', 'readLine',
  'readLineInto', 'canReadLine', 'startTransaction', 'commitTransaction',
  'rollbackTransaction', 'isTransactionStarted', 'write', 'peek', 'skip',
  'waitForReadyRead', 'waitForBytesWritten', 'errorString'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIODevice::~QIODevice()': the destructor: Python never removes a
    C++ QIODevice.
  - Qt's 'void QIODevice::ungetChar(char c)': takes a single letter as C has
    it.
  - Qt's 'bool QIODevice::putChar(char c)': takes a single letter as C has
    it.

  What has no ritual
  ------------------

  30 of the 74 functions Qt declares: 9 takes or gives a type that cannot be
  passed yet; 7 protected; 6 a signal; 3 private; 2 the class is abstract, so
  C++ cannot make one; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QIODevice is created at the first use, not by 'QIODevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIODevice.
  - Qt tells when it has removed the C++ QIODevice. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QIODevice::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIODevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QIODevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIODevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QIODevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QIODevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QIODevice10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def openMode(self) -> QIODeviceBase.OpenMode:
    """
    Calls Qt's 'QIODeviceBase::OpenMode QIODevice::openMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#openMode

    Returns
    -------

    QIODeviceBase.OpenMode
      The value standing for the combination Qt gave back.
    """
    #  QIODeviceBase::OpenMode QIODevice::openMode() const
    return QIODeviceBaseOpenModeFlag(self.uglySide.call(
        'ritual_ZNK9QIODevice8openModeEv',
    ))

  def isTextModeEnabled(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isTextModeEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#isTextModeEnabled
    """
    #  bool QIODevice::isTextModeEnabled() const
    return self.uglySide.call('ritual_ZNK9QIODevice17isTextModeEnabledEv')

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#isOpen
    """
    #  bool QIODevice::isOpen() const
    return self.uglySide.call('ritual_ZNK9QIODevice6isOpenEv')

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#isReadable
    """
    #  bool QIODevice::isReadable() const
    return self.uglySide.call('ritual_ZNK9QIODevice10isReadableEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#isWritable
    """
    #  bool QIODevice::isWritable() const
    return self.uglySide.call('ritual_ZNK9QIODevice10isWritableEv')

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#isSequential
    """
    #  bool QIODevice::isSequential() const
    return self.uglySide.call('ritual_ZNK9QIODevice12isSequentialEv')

  def readChannelCount(self) -> int:
    """
    Calls Qt's 'int QIODevice::readChannelCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#readChannelCount
    """
    #  int QIODevice::readChannelCount() const
    return self.uglySide.call('ritual_ZNK9QIODevice16readChannelCountEv')

  def writeChannelCount(self) -> int:
    """
    Calls Qt's 'int QIODevice::writeChannelCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#writeChannelCount
    """
    #  int QIODevice::writeChannelCount() const
    return self.uglySide.call('ritual_ZNK9QIODevice17writeChannelCountEv')

  def currentReadChannel(self) -> int:
    """
    Calls Qt's 'int QIODevice::currentReadChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#currentReadChannel
    """
    #  int QIODevice::currentReadChannel() const
    return self.uglySide.call('ritual_ZNK9QIODevice18currentReadChannelEv')

  def currentWriteChannel(self) -> int:
    """
    Calls Qt's 'int QIODevice::currentWriteChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#currentWriteChannel
    """
    #  int QIODevice::currentWriteChannel() const
    return self.uglySide.call('ritual_ZNK9QIODevice19currentWriteChannelEv')

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QIODevice::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#pos
    """
    #  qint64 QIODevice::pos() const
    return self.uglySide.call('ritual_ZNK9QIODevice3posEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QIODevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#size
    """
    #  qint64 QIODevice::size() const
    return self.uglySide.call('ritual_ZNK9QIODevice4sizeEv')

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#atEnd
    """
    #  bool QIODevice::atEnd() const
    return self.uglySide.call('ritual_ZNK9QIODevice5atEndEv')

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QIODevice::bytesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#bytesAvailable
    """
    #  qint64 QIODevice::bytesAvailable() const
    return self.uglySide.call('ritual_ZNK9QIODevice14bytesAvailableEv')

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QIODevice::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#bytesToWrite
    """
    #  qint64 QIODevice::bytesToWrite() const
    return self.uglySide.call('ritual_ZNK9QIODevice12bytesToWriteEv')

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#canReadLine
    """
    #  bool QIODevice::canReadLine() const
    return self.uglySide.call('ritual_ZNK9QIODevice11canReadLineEv')

  def isTransactionStarted(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::isTransactionStarted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodevice.html#isTransactionStarted
    """
    #  bool QIODevice::isTransactionStarted() const
    return self.uglySide.call('ritual_ZNK9QIODevice20isTransactionStartedEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QIODevice::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIODevice::errorString() const
    return self.uglySide.call('ritual_ZNK9QIODevice11errorStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTextModeEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QIODevice::setTextModeEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#setTextModeEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QIODevice::setTextModeEnabled(bool enabled)
    self.uglySide.call('ritual_ZN9QIODevice18setTextModeEnabledEb', enabled)

  @overload(int)
  def setCurrentReadChannel(self, channel: int) -> None:
    """
    Calls Qt's 'void QIODevice::setCurrentReadChannel(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodevice.html#setCurrentReadChannel

    Parameters
    ----------

    channel : int
      Passed on as it is.
    """
    #  void QIODevice::setCurrentReadChannel(int channel)
    self.uglySide.call(
        'ritual_ZN9QIODevice21setCurrentReadChannelEi', channel,
    )

  @overload(int)
  def setCurrentWriteChannel(self, channel: int) -> None:
    """
    Calls Qt's 'void QIODevice::setCurrentWriteChannel(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiodevice.html#setCurrentWriteChannel

    Parameters
    ----------

    channel : int
      Passed on as it is.
    """
    #  void QIODevice::setCurrentWriteChannel(int channel)
    self.uglySide.call(
        'ritual_ZN9QIODevice22setCurrentWriteChannelEi', channel,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QIODeviceBaseOpenModeFlag)
  def open(self, mode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QIODevice::open(QIODeviceBase::OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#open

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QIODevice::open(QIODeviceBase::OpenMode mode)
    return self.uglySide.call(
        'ritual_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        mode.value,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QIODevice::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#close
    """
    #  void QIODevice::close()
    self.uglySide.call('ritual_ZN9QIODevice5closeEv')

  @overload(int)
  def seek(self, pos: int) -> bool:
    """
    Calls Qt's 'bool QIODevice::seek(qint64 pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#seek

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  bool QIODevice::seek(qint64 pos)
    return self.uglySide.call('ritual_ZN9QIODevice4seekEx', pos)

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QIODevice::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#reset
    """
    #  bool QIODevice::reset()
    return self.uglySide.call('ritual_ZN9QIODevice5resetEv')

  @overload(int)
  def read(self, maxlen: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIODevice::read(qint64 maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#read

    Parameters
    ----------

    maxlen : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIODevice::read(qint64 maxlen)
    address = self.uglySide.call('ritual_ZN9QIODevice4readEx', maxlen)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def readAll(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIODevice::readAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#readAll

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIODevice::readAll()
    address = self.uglySide.call('ritual_ZN9QIODevice7readAllEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(int)
  def readLine(self, maxlen: int = 0) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIODevice::readLine(qint64 maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#readLine

    Parameters
    ----------

    maxlen : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIODevice::readLine(qint64 maxlen)
    address = self.uglySide.call('ritual_ZN9QIODevice8readLineEx', maxlen)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray)
  @overload(NoneType)
  @overload(QByteArray, int)
  @overload(NoneType, int)
  def readLineInto(
      self,
      result: Optional[QByteArray],
      maxlen: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QIODevice::readLineInto(QByteArray *result, qint64
    maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#readLineInto

    Parameters
    ----------

    result : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maxlen : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QIODevice::readLineInto(QByteArray *result, qint64 maxlen)
    return self.uglySide.call(
        'ritual_ZN9QIODevice12readLineIntoEP10QByteArrayx',
        self._addressOf(result), maxlen,
    )

  def startTransaction(self) -> None:
    """
    Calls Qt's 'void QIODevice::startTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#startTransaction
    """
    #  void QIODevice::startTransaction()
    self.uglySide.call('ritual_ZN9QIODevice16startTransactionEv')

  def commitTransaction(self) -> None:
    """
    Calls Qt's 'void QIODevice::commitTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#commitTransaction
    """
    #  void QIODevice::commitTransaction()
    self.uglySide.call('ritual_ZN9QIODevice17commitTransactionEv')

  def rollbackTransaction(self) -> None:
    """
    Calls Qt's 'void QIODevice::rollbackTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#rollbackTransaction
    """
    #  void QIODevice::rollbackTransaction()
    self.uglySide.call('ritual_ZN9QIODevice19rollbackTransactionEv')

  @overload(str, int)
  @overload(NoneType, int)
  def write(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QIODevice::write(const char *data, qint64 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QIODevice::write(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN9QIODevice5writeEPKcx', self._bytesOf(data), len,
    )

  @overload(str)
  @overload(NoneType)
  def write(self, data: Optional[str]) -> int:
    """
    Calls Qt's 'qint64 QIODevice::write(const char *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#write

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  qint64 QIODevice::write(const char *data)
    return self.uglySide.call(
        'ritual_ZN9QIODevice5writeEPKc', self._bytesOf(data),
    )

  @overload(QByteArray)
  def write(self, data: QByteArray) -> int:
    """
    Calls Qt's 'qint64 QIODevice::write(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#write

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  qint64 QIODevice::write(const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN9QIODevice5writeERK10QByteArray', self._valueOf(data),
    )

  @overload(int)
  def peek(self, maxlen: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIODevice::peek(qint64 maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#peek

    Parameters
    ----------

    maxlen : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIODevice::peek(qint64 maxlen)
    address = self.uglySide.call('ritual_ZN9QIODevice4peekEx', maxlen)
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def skip(self, maxSize: int) -> int:
    """
    Calls Qt's 'qint64 QIODevice::skip(qint64 maxSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#skip

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  qint64 QIODevice::skip(qint64 maxSize)
    return self.uglySide.call('ritual_ZN9QIODevice4skipEx', maxSize)

  @overload(int)
  def waitForReadyRead(self, msecs: int) -> bool:
    """
    Calls Qt's 'bool QIODevice::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  bool QIODevice::waitForReadyRead(int msecs)
    return self.uglySide.call(
        'ritual_ZN9QIODevice16waitForReadyReadEi', msecs,
    )

  @overload(int)
  def waitForBytesWritten(self, msecs: int) -> bool:
    """
    Calls Qt's 'bool QIODevice::waitForBytesWritten(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qiodevice.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  bool QIODevice::waitForBytesWritten(int msecs)
    return self.uglySide.call(
        'ritual_ZN9QIODevice19waitForBytesWrittenEi', msecs,
    )
