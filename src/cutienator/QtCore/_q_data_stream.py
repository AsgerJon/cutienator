"""
QDataStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdatastream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDataStream(QIODeviceBase):
  """
  The cute side of Qt's QDataStream: a plain Python object standing in front
  of one C++ QDataStream.

  It is built on the cute 'QIODeviceBase', as Qt's QDataStream is built on
  Qt's QIODeviceBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDataStream that has a ritual and that Python can
  call so far, 20 names in all: 'device', 'setDevice', 'atEnd', 'status',
  'setStatus', 'resetStatus', 'floatingPointPrecision',
  'setFloatingPointPrecision', 'byteOrder', 'setByteOrder', 'version',
  'setVersion', '__bool__', 'writeRawData', 'skipRawData',
  'startTransaction', 'commitTransaction', 'rollbackTransaction',
  'abortTransaction', 'isDeviceTransactionStarted'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataStream::~QDataStream()': the destructor: Python never removes
    a C++ QDataStream.

  What has no ritual
  ------------------

  48 of the 73 functions Qt declares: 39 takes or gives a type that cannot be
  passed yet; 4 private; 2 a template; 2 forbidden; 1 declared and nowhere to
  be found.

  What to expect
  --------------

  - The C++ QDataStream is created at the first use, not by
    'QDataStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDataStream.
  """

  #  The enums Qt writes inside QDataStream, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ByteOrder(CuteNum):
    """
    The enum 'QDataStream::ByteOrder' of Qt, with the 2 names Qt gives in it.
    """

    BigEndian = Kee[int](0)
    LittleEndian = Kee[int](1)

  class FloatingPointPrecision(CuteNum):
    """
    The enum 'QDataStream::FloatingPointPrecision' of Qt, with the 2 names Qt
    gives in it.
    """

    SinglePrecision = Kee[int](0)
    DoublePrecision = Kee[int](1)

  class Status(CuteNum):
    """
    The enum 'QDataStream::Status' of Qt, with the 5 names Qt gives in it.
    """

    Ok = Kee[int](0)
    ReadPastEnd = Kee[int](1)
    ReadCorruptData = Kee[int](2)
    WriteFailed = Kee[int](3)
    SizeLimitExceeded = Kee[int](4)

  class Version(CuteNum):
    """
    The enum 'QDataStream::Version' of Qt, with the 46 names Qt gives in it.
    """

    Qt_1_0 = Kee[int](1)
    Qt_2_0 = Kee[int](2)
    Qt_2_1 = Kee[int](3)
    Qt_3_0 = Kee[int](4)
    Qt_3_1 = Kee[int](5)
    Qt_3_3 = Kee[int](6)
    Qt_4_0 = Kee[int](7)
    Qt_4_1 = Kee[int](7)
    Qt_4_2 = Kee[int](8)
    Qt_4_3 = Kee[int](9)
    Qt_4_4 = Kee[int](10)
    Qt_4_5 = Kee[int](11)
    Qt_4_6 = Kee[int](12)
    Qt_4_7 = Kee[int](12)
    Qt_4_8 = Kee[int](12)
    Qt_4_9 = Kee[int](12)
    Qt_5_0 = Kee[int](13)
    Qt_5_1 = Kee[int](14)
    Qt_5_2 = Kee[int](15)
    Qt_5_3 = Kee[int](15)
    Qt_5_4 = Kee[int](16)
    Qt_5_5 = Kee[int](16)
    Qt_5_6 = Kee[int](17)
    Qt_5_7 = Kee[int](17)
    Qt_5_8 = Kee[int](17)
    Qt_5_9 = Kee[int](17)
    Qt_5_10 = Kee[int](17)
    Qt_5_11 = Kee[int](17)
    Qt_5_12 = Kee[int](18)
    Qt_5_13 = Kee[int](19)
    Qt_5_14 = Kee[int](19)
    Qt_5_15 = Kee[int](19)
    Qt_6_0 = Kee[int](20)
    Qt_6_1 = Kee[int](20)
    Qt_6_2 = Kee[int](20)
    Qt_6_3 = Kee[int](20)
    Qt_6_4 = Kee[int](20)
    Qt_6_5 = Kee[int](20)
    Qt_6_6 = Kee[int](21)
    Qt_6_7 = Kee[int](22)
    Qt_6_8 = Kee[int](22)
    Qt_6_9 = Kee[int](22)
    Qt_6_10 = Kee[int](23)
    Qt_6_11 = Kee[int](24)
    Qt_6_12 = Kee[int](24)
    Qt_DefaultCompiledVersion = Kee[int](24)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDataStream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QDataStream::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QDataStream::device() const
    address = self.uglySide.call('ritual_ZNK11QDataStream6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QDataStream::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#atEnd
    """
    #  bool QDataStream::atEnd() const
    return self.uglySide.call('ritual_ZNK11QDataStream5atEndEv')

  def status(self) -> Status:
    """
    Calls Qt's 'Status QDataStream::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QDataStream::status() const
    return QDataStream.Status(self.uglySide.call(
        'ritual_ZNK11QDataStream6statusEv',
    ))

  def floatingPointPrecision(self) -> FloatingPointPrecision:
    """
    Calls Qt's 'FloatingPointPrecision QDataStream::floatingPointPrecision()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatastream.html#floatingPointPrecision

    Returns
    -------

    FloatingPointPrecision
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FloatingPointPrecision(number)' gives.
    """
    #  FloatingPointPrecision QDataStream::floatingPointPrecision() const
    return QDataStream.FloatingPointPrecision(self.uglySide.call(
        'ritual_ZNK11QDataStream22floatingPointPrecisionEv',
    ))

  def byteOrder(self) -> ByteOrder:
    """
    Calls Qt's 'ByteOrder QDataStream::byteOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#byteOrder

    Returns
    -------

    ByteOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ByteOrder(number)' gives.
    """
    #  ByteOrder QDataStream::byteOrder() const
    return QDataStream.ByteOrder(self.uglySide.call(
        'ritual_ZNK11QDataStream9byteOrderEv',
    ))

  def version(self) -> int:
    """
    Calls Qt's 'int QDataStream::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#version
    """
    #  int QDataStream::version() const
    return self.uglySide.call('ritual_ZNK11QDataStream7versionEv')

  def isDeviceTransactionStarted(self) -> bool:
    """
    Calls Qt's 'bool QDataStream::isDeviceTransactionStarted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatastream.html#isDeviceTransactionStarted
    """
    #  bool QDataStream::isDeviceTransactionStarted() const
    return self.uglySide.call(
        'ritual_ZNK11QDataStream26isDeviceTransactionStartedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, a0: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QDataStream::setDevice(QIODevice *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#setDevice

    Parameters
    ----------

    a0 : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDataStream::setDevice(QIODevice *a0)
    self.uglySide.call(
        'ritual_ZN11QDataStream9setDeviceEP9QIODevice', self._addressOf(a0),
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QDataStream::setStatus(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QDataStream::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN11QDataStream9setStatusENS_6StatusE', status.value,
    )

  @overload(FloatingPointPrecision)
  def setFloatingPointPrecision(
      self,
      precision: FloatingPointPrecision,
  ) -> None:
    """
    Calls Qt's 'void
    QDataStream::setFloatingPointPrecision(FloatingPointPrecision
    precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatastream.html#setFloatingPointPrecision

    Parameters
    ----------

    precision : FloatingPointPrecision
      Passed on as its number.
    """
    #  void QDataStream::setFloatingPointPrecision(FloatingPointPrecision
    #      precision)
    self.uglySide.call(
        'ritual_ZN11QDataStream25setFloatingPointPrecisionENS_22FloatingPoi'
        'ntPrecisionE',
        precision.value,
    )

  @overload(ByteOrder)
  def setByteOrder(self, a0: ByteOrder) -> None:
    """
    Calls Qt's 'void QDataStream::setByteOrder(ByteOrder a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#setByteOrder

    Parameters
    ----------

    a0 : ByteOrder
      Passed on as its number.
    """
    #  void QDataStream::setByteOrder(ByteOrder a0)
    self.uglySide.call(
        'ritual_ZN11QDataStream12setByteOrderENS_9ByteOrderE', a0.value,
    )

  @overload(int)
  def setVersion(self, a0: int) -> None:
    """
    Calls Qt's 'void QDataStream::setVersion(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#setVersion

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QDataStream::setVersion(int a0)
    self.uglySide.call('ritual_ZN11QDataStream10setVersionEi', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QDataStream::operator bool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#operator bool
    """
    #  bool QDataStream::operator bool() const
    return self.uglySide.call('ritual_ZNK11QDataStreamcvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDataStream::QDataStream()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#QDataStream
    """
    #  QDataStream::QDataStream()
    self._noteCreation(QDataStream, lambda: Rituals.call(
        'ritual_ZN11QDataStreamC1Ev',
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, a0: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QDataStream::QDataStream(QIODevice *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#QDataStream

    Parameters
    ----------

    a0 : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDataStream::QDataStream(QIODevice *a0)
    self._noteCreation(QDataStream, lambda: Rituals.call(
        'ritual_ZN11QDataStreamC1EP9QIODevice', self._addressOf(a0),
    ))

  @overload(QByteArray, QIODeviceBase.OpenMode)
  @overload(NoneType, QIODeviceBase.OpenMode)
  def __init__(
      self,
      a0: Optional[QByteArray],
      flags: QIODeviceBase.OpenMode,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDataStream::QDataStream(QByteArray *a0,
    OpenMode flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#QDataStream

    Parameters
    ----------

    a0 : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  QDataStream::QDataStream(QByteArray *a0, OpenMode flags)
    self._noteCreation(QDataStream, lambda: Rituals.call(
        'ritual_ZN11QDataStreamC1EP10QByteArray6QFlagsIN13QIODeviceBase12Op'
        'enModeFlagEE',
        self._addressOf(a0), flags.value,
    ))

  @overload(QByteArray)
  def __init__(self, a0: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QDataStream::QDataStream(const QByteArray
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#QDataStream

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QDataStream::QDataStream(const QByteArray &a0)
    self._noteCreation(QDataStream, lambda: Rituals.call(
        'ritual_ZN11QDataStreamC1ERK10QByteArray', self._valueOf(a0),
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

  def resetStatus(self) -> None:
    """
    Calls Qt's 'void QDataStream::resetStatus()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#resetStatus
    """
    #  void QDataStream::resetStatus()
    self.uglySide.call('ritual_ZN11QDataStream11resetStatusEv')

  @overload(str, int)
  @overload(NoneType, int)
  def writeRawData(self, a0: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QDataStream::writeRawData(const char *a0, qint64
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#writeRawData

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QDataStream::writeRawData(const char *a0, qint64 len)
    return self.uglySide.call(
        'ritual_ZN11QDataStream12writeRawDataEPKcx', self._bytesOf(a0), len,
    )

  @overload(int)
  def skipRawData(self, len: int) -> int:
    """
    Calls Qt's 'qint64 QDataStream::skipRawData(qint64 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#skipRawData

    Parameters
    ----------

    len : int
      Passed on as it is.
    """
    #  qint64 QDataStream::skipRawData(qint64 len)
    return self.uglySide.call('ritual_ZN11QDataStream11skipRawDataEx', len)

  def startTransaction(self) -> None:
    """
    Calls Qt's 'void QDataStream::startTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#startTransaction
    """
    #  void QDataStream::startTransaction()
    self.uglySide.call('ritual_ZN11QDataStream16startTransactionEv')

  def commitTransaction(self) -> bool:
    """
    Calls Qt's 'bool QDataStream::commitTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#commitTransaction
    """
    #  bool QDataStream::commitTransaction()
    return self.uglySide.call('ritual_ZN11QDataStream17commitTransactionEv')

  def rollbackTransaction(self) -> None:
    """
    Calls Qt's 'void QDataStream::rollbackTransaction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatastream.html#rollbackTransaction
    """
    #  void QDataStream::rollbackTransaction()
    self.uglySide.call('ritual_ZN11QDataStream19rollbackTransactionEv')

  def abortTransaction(self) -> None:
    """
    Calls Qt's 'void QDataStream::abortTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatastream.html#abortTransaction
    """
    #  void QDataStream::abortTransaction()
    self.uglySide.call('ritual_ZN11QDataStream16abortTransactionEv')
