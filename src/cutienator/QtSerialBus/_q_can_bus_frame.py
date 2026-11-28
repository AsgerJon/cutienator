"""
QCanBusFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanbusframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCanBusFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanBusFrame: a plain Python object standing in front
  of one C++ QCanBusFrame.

  C++ hands a QCanBusFrame around as a copy, so every C++ QCanBusFrame behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanBusFrame that has a ritual and that Python can
  call so far, 22 names in all: 'isValid', 'frameType', 'setFrameType',
  'hasExtendedFrameFormat', 'setExtendedFrameFormat', 'frameId',
  'setFrameId', 'setPayload', 'setTimeStamp', 'payload', 'timeStamp',
  'error', 'setError', 'toString', 'hasFlexibleDataRateFormat',
  'setFlexibleDataRateFormat', 'hasBitrateSwitch', 'setBitrateSwitch',
  'hasErrorStateIndicator', 'setErrorStateIndicator', 'hasLocalEcho',
  'setLocalEcho'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanBusFrame &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanBusFrame &a1)': an
    operator between other classes, written inside this one.
  - Qt's 'QCanBusFrame::~QCanBusFrame()': the destructor: Python removes its
    C++ QCanBusFrame by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 30 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QCanBusFrame is created at the first use, not by
    'QCanBusFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanBusFrame back gives a copy the ritual made for
    Python, in a new cute QCanBusFrame.
  """

  #  The enums Qt writes inside QCanBusFrame, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FrameError(CuteFlags):
    """
    The flags enum 'QCanBusFrame::FrameError' of Qt, with the 12 names Qt
    gives in it. Qt names the type of its combinations
    'QCanBusFrame::FrameErrors'.
    """

    NoError = 0x0
    TransmissionTimeoutError = 0x1
    LostArbitrationError = 0x2
    ControllerError = 0x4
    ProtocolViolationError = 0x8
    TransceiverError = 0x10
    MissingAcknowledgmentError = 0x20
    BusOffError = 0x40
    BusError = 0x80
    ControllerRestartError = 0x100
    UnknownError = 0x200
    AnyError = 0x1fffffff

  FrameErrors = FrameError

  class FrameType(CuteNum):
    """
    The enum 'QCanBusFrame::FrameType' of Qt, with the 5 names Qt gives in
    it.
    """

    UnknownFrame = Kee[int](0)
    DataFrame = Kee[int](1)
    ErrorFrame = Kee[int](2)
    RemoteRequestFrame = Kee[int](3)
    InvalidFrame = Kee[int](4)

  #  The classes Qt writes inside QCanBusFrame, each a class in here as in
  #  C++.

  class TimeStamp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanBusFrame::TimeStamp: a plain Python object
    standing in front of one C++ QCanBusFrame::TimeStamp.

    C++ hands a QCanBusFrame::TimeStamp around as a copy, so every C++
    QCanBusFrame::TimeStamp behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCanBusFrame::TimeStamp that has a ritual and that
    Python can call so far, 3 names in all: 'fromMicroSeconds', 'seconds',
    'microSeconds'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCanBusFrame::TimeStamp::~TimeStamp()': the destructor: Python
      removes its C++ QCanBusFrame::TimeStamp by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCanBusFrame::TimeStamp is created at the first use, not by
      'QCanBusFrame::TimeStamp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanBusFrame::TimeStamp back gives a copy the
      ritual made for Python, in a new cute QCanBusFrame::TimeStamp.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(int)
    def fromMicroSeconds(usec: int) -> QCanBusFrame.TimeStamp:
      """
      Calls Qt's 'TimeStamp QCanBusFrame::TimeStamp::fromMicroSeconds(qint64
      usec)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusframe-timestamp.html#fromMicroSeconds

      Parameters
      ----------

      usec : int
        Passed on as it is.

      Returns
      -------

      QCanBusFrame.TimeStamp
        A new cute QCanBusFrame::TimeStamp around the copy Qt gave back.
        Python owns it.
      """
      #  TimeStamp QCanBusFrame::TimeStamp::fromMicroSeconds(qint64 usec)
      address = Rituals.call(
          'ritual_ZN12QCanBusFrame9TimeStamp16fromMicroSecondsEx', usec,
      )
      return QCanBusFrame.TimeStamp._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanBusFrame::TimeStamp'

    #  Qt's '~QCanBusFrame::TimeStamp()'. Naming it makes this a value class:
    #  Python owns every C++ QCanBusFrame::TimeStamp behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QCanBusFrame9TimeStampD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def seconds(self) -> int:
      """
      Calls Qt's 'qint64 QCanBusFrame::TimeStamp::seconds() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusframe-timestamp.html#seconds
      """
      #  qint64 QCanBusFrame::TimeStamp::seconds() const
      return self.uglySide.call(
          'ritual_ZNK12QCanBusFrame9TimeStamp7secondsEv',
      )

    def microSeconds(self) -> int:
      """
      Calls Qt's 'qint64 QCanBusFrame::TimeStamp::microSeconds() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusframe-timestamp.html#microSeconds
      """
      #  qint64 QCanBusFrame::TimeStamp::microSeconds() const
      return self.uglySide.call(
          'ritual_ZNK12QCanBusFrame9TimeStamp12microSecondsEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(int)
    @overload(int, int)
    def __init__(self, s: int = 0, usec: int = 0) -> None:
      """
      Notes what was given, for Qt's
      'QCanBusFrame::TimeStamp::TimeStamp(qint64 s, qint64 usec)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusframe-timestamp.html#TimeStamp

      Parameters
      ----------

      s : int
        Passed on as it is. May be left out, as in Qt: it is then 0.

      usec : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QCanBusFrame::TimeStamp::TimeStamp(qint64 s, qint64 usec)
      self._noteCreation(QCanBusFrame.TimeStamp, lambda: Rituals.call(
          'ritual_ZN12QCanBusFrame9TimeStampC1Exx', s, usec,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanBusFrame'

  #  Qt's '~QCanBusFrame()'. Naming it makes this a value class: Python owns
  #  every C++ QCanBusFrame behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCanBusFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#isValid
    """
    #  bool QCanBusFrame::isValid() const
    return self.uglySide.call('ritual_ZNK12QCanBusFrame7isValidEv')

  def frameType(self) -> FrameType:
    """
    Calls Qt's 'FrameType QCanBusFrame::frameType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#frameType

    Returns
    -------

    FrameType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FrameType(number)' gives.
    """
    #  FrameType QCanBusFrame::frameType() const
    return QCanBusFrame.FrameType(self.uglySide.call(
        'ritual_ZNK12QCanBusFrame9frameTypeEv',
    ))

  def hasExtendedFrameFormat(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::hasExtendedFrameFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#hasExtendedFrameFormat
    """
    #  bool QCanBusFrame::hasExtendedFrameFormat() const
    return self.uglySide.call(
        'ritual_ZNK12QCanBusFrame22hasExtendedFrameFormatEv',
    )

  def frameId(self) -> int:
    """
    Calls Qt's 'QCanBusFrame::FrameId QCanBusFrame::frameId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#frameId
    """
    #  QCanBusFrame::FrameId QCanBusFrame::frameId() const
    return self.uglySide.call('ritual_ZNK12QCanBusFrame7frameIdEv')

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCanBusFrame::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCanBusFrame::payload() const
    address = self.uglySide.call('ritual_ZNK12QCanBusFrame7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def timeStamp(self) -> TimeStamp:
    """
    Calls Qt's 'TimeStamp QCanBusFrame::timeStamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#timeStamp

    Returns
    -------

    TimeStamp
      A new cute QCanBusFrame::TimeStamp around the copy Qt gave back. Python
      owns it.
    """
    #  TimeStamp QCanBusFrame::timeStamp() const
    address = self.uglySide.call('ritual_ZNK12QCanBusFrame9timeStampEv')
    return QCanBusFrame.TimeStamp._cuteOwning(address)

  def error(self) -> FrameErrors:
    """
    Calls Qt's 'FrameErrors QCanBusFrame::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#error

    Returns
    -------

    FrameErrors
      The value standing for the combination Qt gave back.
    """
    #  FrameErrors QCanBusFrame::error() const
    return QCanBusFrame.FrameErrors(self.uglySide.call(
        'ritual_ZNK12QCanBusFrame5errorEv',
    ))

  def toString(self) -> str:
    """
    Calls Qt's 'QString QCanBusFrame::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusFrame::toString() const
    return self.uglySide.call('ritual_ZNK12QCanBusFrame8toStringEv')

  def hasFlexibleDataRateFormat(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::hasFlexibleDataRateFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#hasFlexibleDataRateFormat
    """
    #  bool QCanBusFrame::hasFlexibleDataRateFormat() const
    return self.uglySide.call(
        'ritual_ZNK12QCanBusFrame25hasFlexibleDataRateFormatEv',
    )

  def hasBitrateSwitch(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::hasBitrateSwitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#hasBitrateSwitch
    """
    #  bool QCanBusFrame::hasBitrateSwitch() const
    return self.uglySide.call('ritual_ZNK12QCanBusFrame16hasBitrateSwitchEv')

  def hasErrorStateIndicator(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::hasErrorStateIndicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#hasErrorStateIndicator
    """
    #  bool QCanBusFrame::hasErrorStateIndicator() const
    return self.uglySide.call(
        'ritual_ZNK12QCanBusFrame22hasErrorStateIndicatorEv',
    )

  def hasLocalEcho(self) -> bool:
    """
    Calls Qt's 'bool QCanBusFrame::hasLocalEcho() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#hasLocalEcho
    """
    #  bool QCanBusFrame::hasLocalEcho() const
    return self.uglySide.call('ritual_ZNK12QCanBusFrame12hasLocalEchoEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FrameType)
  def setFrameType(self, newFormat: FrameType) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setFrameType(FrameType newFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setFrameType

    Parameters
    ----------

    newFormat : FrameType
      Passed on as its number.
    """
    #  void QCanBusFrame::setFrameType(FrameType newFormat)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame12setFrameTypeENS_9FrameTypeE',
        newFormat.value,
    )

  @overload(bool)
  def setExtendedFrameFormat(self, isExtended: bool) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setExtendedFrameFormat(bool isExtended)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#setExtendedFrameFormat

    Parameters
    ----------

    isExtended : bool
      Passed on as it is.
    """
    #  void QCanBusFrame::setExtendedFrameFormat(bool isExtended)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame22setExtendedFrameFormatEb', isExtended,
    )

  @overload(int)
  def setFrameId(self, newFrameId: int) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setFrameId(QCanBusFrame::FrameId
    newFrameId)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setFrameId

    Parameters
    ----------

    newFrameId : int
      Passed on as it is.
    """
    #  void QCanBusFrame::setFrameId(QCanBusFrame::FrameId newFrameId)
    self.uglySide.call('ritual_ZN12QCanBusFrame10setFrameIdEj', newFrameId)

  @overload(QByteArray)
  def setPayload(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setPayload(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setPayload

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCanBusFrame::setPayload(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame10setPayloadERK10QByteArray',
        self._valueOf(data),
    )

  @overload(TimeStamp)
  def setTimeStamp(self, ts: TimeStamp) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setTimeStamp(TimeStamp ts)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setTimeStamp

    Parameters
    ----------

    ts : TimeStamp
      Passed on as a value: Qt reads the C++ QCanBusFrame::TimeStamp, which
      stays Python's own.
    """
    #  void QCanBusFrame::setTimeStamp(TimeStamp ts)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame12setTimeStampENS_9TimeStampE',
        self._valueOf(ts),
    )

  @overload(FrameErrors)
  def setError(self, e: FrameErrors) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setError(FrameErrors e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setError

    Parameters
    ----------

    e : FrameErrors
      Passed on as its number.
    """
    #  void QCanBusFrame::setError(FrameErrors e)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame8setErrorE6QFlagsINS_10FrameErrorEE',
        e.value,
    )

  @overload(bool)
  def setFlexibleDataRateFormat(self, isFlexibleData: bool) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setFlexibleDataRateFormat(bool
    isFlexibleData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#setFlexibleDataRateFormat

    Parameters
    ----------

    isFlexibleData : bool
      Passed on as it is.
    """
    #  void QCanBusFrame::setFlexibleDataRateFormat(bool isFlexibleData)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame25setFlexibleDataRateFormatEb',
        isFlexibleData,
    )

  @overload(bool)
  def setBitrateSwitch(self, bitrateSwitch: bool) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setBitrateSwitch(bool bitrateSwitch)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setBitrateSwitch

    Parameters
    ----------

    bitrateSwitch : bool
      Passed on as it is.
    """
    #  void QCanBusFrame::setBitrateSwitch(bool bitrateSwitch)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame16setBitrateSwitchEb', bitrateSwitch,
    )

  @overload(bool)
  def setErrorStateIndicator(self, errorStateIndicator: bool) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setErrorStateIndicator(bool
    errorStateIndicator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusframe.html#setErrorStateIndicator

    Parameters
    ----------

    errorStateIndicator : bool
      Passed on as it is.
    """
    #  void QCanBusFrame::setErrorStateIndicator(bool errorStateIndicator)
    self.uglySide.call(
        'ritual_ZN12QCanBusFrame22setErrorStateIndicatorEb',
        errorStateIndicator,
    )

  @overload(bool)
  def setLocalEcho(self, localEcho: bool) -> None:
    """
    Calls Qt's 'void QCanBusFrame::setLocalEcho(bool localEcho)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#setLocalEcho

    Parameters
    ----------

    localEcho : bool
      Passed on as it is.
    """
    #  void QCanBusFrame::setLocalEcho(bool localEcho)
    self.uglySide.call('ritual_ZN12QCanBusFrame12setLocalEchoEb', localEcho)

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
  @overload(FrameType)
  def __init__(self, type: FrameType = FrameType.DataFrame) -> None:
    """
    Notes what was given, for Qt's 'QCanBusFrame::QCanBusFrame(FrameType
    type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#QCanBusFrame

    Parameters
    ----------

    type : FrameType
      Passed on as its number. May be left out, as in Qt: it is then
      FrameType.DataFrame.
    """
    #  QCanBusFrame::QCanBusFrame(FrameType type)
    self._noteCreation(QCanBusFrame, lambda: Rituals.call(
        'ritual_ZN12QCanBusFrameC1ENS_9FrameTypeE', type.value,
    ))

  @overload(int, QByteArray)
  def __init__(self, identifier: int, data: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QCanBusFrame::QCanBusFrame(QCanBusFrame::FrameId identifier, const
    QByteArray &data)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusframe.html#QCanBusFrame

    Parameters
    ----------

    identifier : int
      Passed on as it is.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QCanBusFrame::QCanBusFrame(QCanBusFrame::FrameId identifier, const
    #      QByteArray &data)
    self._noteCreation(QCanBusFrame, lambda: Rituals.call(
        'ritual_ZN12QCanBusFrameC1EjRK10QByteArray',
        identifier, self._valueOf(data),
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


#  Qt's 'QList<QCanBusFrame>': the list of QCanBusFrame, which
#  'QList[QCanBusFrame]' gives. It is made here, so that there is one as soon
#  as there can be a QCanBusFrame.
QList.createKind(
    QCanBusFrame, 'value',
    make='ritual_list_make_QCanBusFrame',
    add='ritual_list_add_QCanBusFrame',
    size='ritual_list_size_QCanBusFrame',
    at='ritual_list_at_QCanBusFrame',
    drop='ritual_list_drop_QCanBusFrame',
)
