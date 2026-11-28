"""
QCanSignalDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcansignaldescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QSysInfo
from . import QtCanBus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QVariant = WAIT['QVariant']


class QCanSignalDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanSignalDescription: a plain Python object standing
  in front of one C++ QCanSignalDescription.

  C++ hands a QCanSignalDescription around as a copy, so every C++
  QCanSignalDescription behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanSignalDescription that has a ritual and that
  Python can call so far, 34 names in all: 'isValid', 'name', 'setName',
  'physicalUnit', 'setPhysicalUnit', 'receiver', 'setReceiver', 'comment',
  'setComment', 'dataSource', 'setDataSource', 'dataEndian', 'setDataEndian',
  'dataFormat', 'setDataFormat', 'startBit', 'setStartBit', 'bitLength',
  'setBitLength', 'factor', 'setFactor', 'offset', 'setOffset', 'scaling',
  'setScaling', 'minimum', 'maximum', 'setRange', 'multiplexState',
  'setMultiplexState', 'clearMultiplexSignals', 'addMultiplexSignal',
  '__rlshift__', 'debugStreaming'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanSignalDescription::QCanSignalDescription(QCanSignalDescription
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanSignalDescription::~QCanSignalDescription()': the destructor:
    Python removes its C++ QCanSignalDescription by it, and has no other use
    for it.
  - Qt's 'QCanSignalDescription &QCanSignalDescription::operator=(const
    QCanSignalDescription &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QCanSignalDescription
    &QCanSignalDescription::operator=(QCanSignalDescription &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanSignalDescription::swap(QCanSignalDescription &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'MultiplexSignalValues QCanSignalDescription::multiplexSignals()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QCanSignalDescription::setMultiplexSignals(const
    MultiplexSignalValues &multiplexorSignals)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QCanSignalDescription::addMultiplexSignal(const QString &name,
    const MultiplexValues &ranges)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QCanSignalDescription is created at the first use, not by
    'QCanSignalDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanSignalDescription back gives a copy the ritual
    made for Python, in a new cute QCanSignalDescription.
  - Each name of Qt's QCanSignalDescription that has no cute function yet,
    'multiplexSignals', 'setMultiplexSignals', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QCanSignalDescription, each a class in here
  #  as in C++.

  class MultiplexValueRange(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanSignalDescription::MultiplexValueRange: a plain
    Python object standing in front of one C++
    QCanSignalDescription::MultiplexValueRange.

    C++ hands a QCanSignalDescription::MultiplexValueRange around as a copy,
    so every C++ QCanSignalDescription::MultiplexValueRange behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCanSignalDescription::MultiplexValueRange that
    has a ritual and that Python can call so far, 4 names in all: '__eq__',
    '__ne__', '__rlshift__', 'debugStreaming'. None can be made from Python:
    one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QCanSignalDescription::MultiplexValueRange::~MultiplexValueRange()':
      the destructor: Python removes its C++
      QCanSignalDescription::MultiplexValueRange by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCanSignalDescription::MultiplexValueRange is created at the
      first use, not by 'QCanSignalDescription::MultiplexValueRange(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanSignalDescription::MultiplexValueRange back
      gives a copy the ritual made for Python, in a new cute
      QCanSignalDescription::MultiplexValueRange.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDebug = WAIT['QDebug']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(QDebug, THIS)
    def debugStreaming(
        dbg: QDebug,
        range: QCanSignalDescription.MultiplexValueRange,
    ) -> QDebug:
      """
      Calls Qt's 'QDebug
      QCanSignalDescription::MultiplexValueRange::debugStreaming(QDebug dbg,
      const MultiplexValueRange &range)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcansignaldescription-multiplexvaluerange.html

      Parameters
      ----------

      dbg : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      range : QCanSignalDescription.MultiplexValueRange
        Passed on as a value: Qt reads the C++
        QCanSignalDescription::MultiplexValueRange, which stays Python's own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug QCanSignalDescription::MultiplexValueRange::debugStreaming(
      #      QDebug dbg, const MultiplexValueRange &range)
      address = Rituals.call(
          'ritual_ZN21QCanSignalDescription19MultiplexValueRange14debugStre'
          'amingE6QDebugRKS0_',
          CuteMixin._valueOf(dbg), CuteMixin._valueOf(range),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanSignalDescription::MultiplexValueRange'

    #  Qt's '~QCanSignalDescription::MultiplexValueRange()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCanSignalDescription::MultiplexValueRange behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN21QCanSignalDescription19MultiplexValueRangeD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, rhs: QCanSignalDescription.MultiplexValueRange) -> bool:
      """
      Calls Qt's 'bool operator==(const MultiplexValueRange &lhs, const
      MultiplexValueRange &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcansignaldescription-multiplexvaluerange.html

      Parameters
      ----------

      rhs : QCanSignalDescription.MultiplexValueRange
        Passed on as a value: Qt reads the C++
        QCanSignalDescription::MultiplexValueRange, which stays Python's own.
      """
      #  bool operator==(const MultiplexValueRange &lhs, const
      #      MultiplexValueRange &rhs)
      return Rituals.call(
          'ritual_ZeqRKN21QCanSignalDescription19MultiplexValueRangeES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __ne__(self, rhs: QCanSignalDescription.MultiplexValueRange) -> bool:
      """
      Calls Qt's 'bool operator!=(const MultiplexValueRange &lhs, const
      MultiplexValueRange &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcansignaldescription-multiplexvaluerange.html

      Parameters
      ----------

      rhs : QCanSignalDescription.MultiplexValueRange
        Passed on as a value: Qt reads the C++
        QCanSignalDescription::MultiplexValueRange, which stays Python's own.
      """
      #  bool operator!=(const MultiplexValueRange &lhs, const
      #      MultiplexValueRange &rhs)
      return Rituals.call(
          'ritual_ZneRKN21QCanSignalDescription19MultiplexValueRangeES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(QDebug)
    def __rlshift__(self, dbg: QDebug) -> QDebug:
      """
      Calls Qt's 'QDebug operator<<(QDebug dbg, const MultiplexValueRange
      &range)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcansignaldescription-multiplexvaluerange.html

      Parameters
      ----------

      dbg : QDebug
        Passed on as a value: Qt reads the C++ QDebug, which stays Python's
        own.

      Returns
      -------

      QDebug
        A new cute QDebug around the copy Qt gave back. Python owns it.
      """
      #  QDebug operator<<(QDebug dbg, const MultiplexValueRange &range)
      address = Rituals.call(
          'ritual_Zls6QDebugRKN21QCanSignalDescription19MultiplexValueRange'
          'E',
          CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
      )
      from ..QtCore import QDebug
      return QDebug._cuteOwning(address)

    @overload.fallback
    def __rlshift__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, sig: QCanSignalDescription) -> QDebug:
    """
    Calls Qt's 'QDebug QCanSignalDescription::debugStreaming(QDebug dbg,
    const QCanSignalDescription &sig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    sig : QCanSignalDescription
      Passed on as a value: Qt reads the C++ QCanSignalDescription, which
      stays Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QCanSignalDescription::debugStreaming(QDebug dbg, const
    #      QCanSignalDescription &sig)
    address = Rituals.call(
        'ritual_ZN21QCanSignalDescription14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(sig),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanSignalDescription'

  #  Qt's '~QCanSignalDescription()'. Naming it makes this a value class:
  #  Python owns every C++ QCanSignalDescription behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QCanSignalDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCanSignalDescription::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#isValid
    """
    #  bool QCanSignalDescription::isValid() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription7isValidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QCanSignalDescription::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanSignalDescription::name() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription4nameEv')

  def physicalUnit(self) -> str:
    """
    Calls Qt's 'QString QCanSignalDescription::physicalUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#physicalUnit

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanSignalDescription::physicalUnit() const
    return self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription12physicalUnitEv',
    )

  def receiver(self) -> str:
    """
    Calls Qt's 'QString QCanSignalDescription::receiver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#receiver

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanSignalDescription::receiver() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription8receiverEv')

  def comment(self) -> str:
    """
    Calls Qt's 'QString QCanSignalDescription::comment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#comment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanSignalDescription::comment() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription7commentEv')

  def dataSource(self) -> QtCanBus.DataSource:
    """
    Calls Qt's 'QtCanBus::DataSource QCanSignalDescription::dataSource()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#dataSource

    Returns
    -------

    QtCanBus.DataSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCanBus.DataSource(number)' gives.
    """
    #  QtCanBus::DataSource QCanSignalDescription::dataSource() const
    return QtCanBus.DataSource(self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription10dataSourceEv',
    ))

  def dataEndian(self) -> QSysInfo.Endian:
    """
    Calls Qt's 'QSysInfo::Endian QCanSignalDescription::dataEndian() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#dataEndian

    Returns
    -------

    QSysInfo.Endian
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSysInfo.Endian(number)'
      gives.
    """
    #  QSysInfo::Endian QCanSignalDescription::dataEndian() const
    return QSysInfo.Endian(self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription10dataEndianEv',
    ))

  def dataFormat(self) -> QtCanBus.DataFormat:
    """
    Calls Qt's 'QtCanBus::DataFormat QCanSignalDescription::dataFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#dataFormat

    Returns
    -------

    QtCanBus.DataFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCanBus.DataFormat(number)' gives.
    """
    #  QtCanBus::DataFormat QCanSignalDescription::dataFormat() const
    return QtCanBus.DataFormat(self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription10dataFormatEv',
    ))

  def startBit(self) -> int:
    """
    Calls Qt's 'quint16 QCanSignalDescription::startBit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#startBit
    """
    #  quint16 QCanSignalDescription::startBit() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription8startBitEv')

  def bitLength(self) -> int:
    """
    Calls Qt's 'quint16 QCanSignalDescription::bitLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#bitLength
    """
    #  quint16 QCanSignalDescription::bitLength() const
    return self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription9bitLengthEv',
    )

  def factor(self) -> float:
    """
    Calls Qt's 'double QCanSignalDescription::factor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#factor
    """
    #  double QCanSignalDescription::factor() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription6factorEv')

  def offset(self) -> float:
    """
    Calls Qt's 'double QCanSignalDescription::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#offset
    """
    #  double QCanSignalDescription::offset() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription6offsetEv')

  def scaling(self) -> float:
    """
    Calls Qt's 'double QCanSignalDescription::scaling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#scaling
    """
    #  double QCanSignalDescription::scaling() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription7scalingEv')

  def minimum(self) -> float:
    """
    Calls Qt's 'double QCanSignalDescription::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#minimum
    """
    #  double QCanSignalDescription::minimum() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription7minimumEv')

  def maximum(self) -> float:
    """
    Calls Qt's 'double QCanSignalDescription::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#maximum
    """
    #  double QCanSignalDescription::maximum() const
    return self.uglySide.call('ritual_ZNK21QCanSignalDescription7maximumEv')

  def multiplexState(self) -> QtCanBus.MultiplexState:
    """
    Calls Qt's 'QtCanBus::MultiplexState
    QCanSignalDescription::multiplexState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#multiplexState

    Returns
    -------

    QtCanBus.MultiplexState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCanBus.MultiplexState(number)' gives.
    """
    #  QtCanBus::MultiplexState QCanSignalDescription::multiplexState() const
    return QtCanBus.MultiplexState(self.uglySide.call(
        'ritual_ZNK21QCanSignalDescription14multiplexStateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcansignaldescription.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanSignalDescription::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription7setNameERK7QString', name,
    )

  @overload(str)
  def setPhysicalUnit(self, unit: str) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setPhysicalUnit(const QString
    &unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setPhysicalUnit

    Parameters
    ----------

    unit : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanSignalDescription::setPhysicalUnit(const QString &unit)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription15setPhysicalUnitERK7QString', unit,
    )

  @overload(str)
  def setReceiver(self, receiver: str) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setReceiver(const QString
    &receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setReceiver

    Parameters
    ----------

    receiver : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanSignalDescription::setReceiver(const QString &receiver)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription11setReceiverERK7QString', receiver,
    )

  @overload(str)
  def setComment(self, text: str) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setComment(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setComment

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanSignalDescription::setComment(const QString &text)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription10setCommentERK7QString', text,
    )

  @overload(QtCanBus.DataSource)
  def setDataSource(self, source: QtCanBus.DataSource) -> None:
    """
    Calls Qt's 'void
    QCanSignalDescription::setDataSource(QtCanBus::DataSource source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setDataSource

    Parameters
    ----------

    source : QtCanBus.DataSource
      Passed on as its number.
    """
    #  void QCanSignalDescription::setDataSource(QtCanBus::DataSource source)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription13setDataSourceEN8QtCanBus10DataSo'
        'urceE',
        source.value,
    )

  @overload(QSysInfo.Endian)
  def setDataEndian(self, endian: QSysInfo.Endian) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setDataEndian(QSysInfo::Endian
    endian)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setDataEndian

    Parameters
    ----------

    endian : QSysInfo.Endian
      Passed on as its number.
    """
    #  void QCanSignalDescription::setDataEndian(QSysInfo::Endian endian)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription13setDataEndianEN8QSysInfo6EndianE',
        endian.value,
    )

  @overload(QtCanBus.DataFormat)
  def setDataFormat(self, format: QtCanBus.DataFormat) -> None:
    """
    Calls Qt's 'void
    QCanSignalDescription::setDataFormat(QtCanBus::DataFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setDataFormat

    Parameters
    ----------

    format : QtCanBus.DataFormat
      Passed on as its number.
    """
    #  void QCanSignalDescription::setDataFormat(QtCanBus::DataFormat format)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription13setDataFormatEN8QtCanBus10DataFo'
        'rmatE',
        format.value,
    )

  @overload(int)
  def setStartBit(self, bit: int) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setStartBit(quint16 bit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setStartBit

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  void QCanSignalDescription::setStartBit(quint16 bit)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription11setStartBitEt', bit,
    )

  @overload(int)
  def setBitLength(self, length: int) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setBitLength(quint16 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setBitLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QCanSignalDescription::setBitLength(quint16 length)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription12setBitLengthEt', length,
    )

  @overload(float)
  def setFactor(self, factor: float) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setFactor(double factor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setFactor

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QCanSignalDescription::setFactor(double factor)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription9setFactorEd', factor,
    )

  @overload(float)
  def setOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setOffset(double offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QCanSignalDescription::setOffset(double offset)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription9setOffsetEd', offset,
    )

  @overload(float)
  def setScaling(self, scaling: float) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setScaling(double scaling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setScaling

    Parameters
    ----------

    scaling : float
      Passed on as it is.
    """
    #  void QCanSignalDescription::setScaling(double scaling)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription10setScalingEd', scaling,
    )

  @overload(float, float)
  def setRange(self, minimum: float, maximum: float) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::setRange(double minimum, double
    maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setRange

    Parameters
    ----------

    minimum : float
      Passed on as it is.

    maximum : float
      Passed on as it is.
    """
    #  void QCanSignalDescription::setRange(double minimum, double maximum)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription8setRangeEdd', minimum, maximum,
    )

  @overload(QtCanBus.MultiplexState)
  def setMultiplexState(self, state: QtCanBus.MultiplexState) -> None:
    """
    Calls Qt's 'void
    QCanSignalDescription::setMultiplexState(QtCanBus::MultiplexState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#setMultiplexState

    Parameters
    ----------

    state : QtCanBus.MultiplexState
      Passed on as its number.
    """
    #  void QCanSignalDescription::setMultiplexState(QtCanBus::MultiplexState
    #      state)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription17setMultiplexStateEN8QtCanBus14Mu'
        'ltiplexStateE',
        state.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QCanSignalDescription
    &sig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QCanSignalDescription &sig)
    address = Rituals.call(
        'ritual_Zls6QDebugRK21QCanSignalDescription',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanSignalDescription::QCanSignalDescription()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#QCanSignalDescription
    """
    #  QCanSignalDescription::QCanSignalDescription()
    self._noteCreation(QCanSignalDescription, lambda: Rituals.call(
        'ritual_ZN21QCanSignalDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCanSignalDescription) -> None:
    """
    Notes what was given, for Qt's
    'QCanSignalDescription::QCanSignalDescription(const QCanSignalDescription
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#QCanSignalDescription

    Parameters
    ----------

    other : QCanSignalDescription
      Passed on as a value: Qt reads the C++ QCanSignalDescription, which
      stays Python's own.
    """
    #  QCanSignalDescription::QCanSignalDescription(const
    #      QCanSignalDescription &other)
    self._noteCreation(QCanSignalDescription, lambda: Rituals.call(
        'ritual_ZN21QCanSignalDescriptionC1ERKS_', self._valueOf(other),
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

  def clearMultiplexSignals(self) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::clearMultiplexSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#clearMultiplexSignals
    """
    #  void QCanSignalDescription::clearMultiplexSignals()
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription21clearMultiplexSignalsEv',
    )

  @overload(str, QVariant)
  def addMultiplexSignal(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QCanSignalDescription::addMultiplexSignal(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcansignaldescription.html#addMultiplexSignal

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QCanSignalDescription::addMultiplexSignal(const QString &name,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QCanSignalDescription18addMultiplexSignalERK7QStringRK8'
        'QVariant',
        name, self._valueOf(value),
    )

  @staticmethod
  def multiplexSignals(*__, **_) -> Never:
    """
    Qt's 'MultiplexSignalValues QCanSignalDescription::multiplexSignals()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCanSignalDescription.multiplexSignals' has no cute function yet. "
        "Qt's 'MultiplexSignalValues "
        "QCanSignalDescription::multiplexSignals() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setMultiplexSignals(*__, **_) -> Never:
    """
    Qt's 'void QCanSignalDescription::setMultiplexSignals(const
    MultiplexSignalValues &multiplexorSignals)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanSignalDescription.setMultiplexSignals' has no cute function "
        "yet. Qt's 'void QCanSignalDescription::setMultiplexSignals(const "
        "MultiplexSignalValues &multiplexorSignals)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanSignalDescription::swap(QCanSignalDescription &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanSignalDescription.swap' has no cute function yet. Qt's 'void "
        "QCanSignalDescription::swap(QCanSignalDescription &other)': takes "
        "a type Python has no way to hand over yet.")


#  Qt's 'QList<QCanSignalDescription>': the list of QCanSignalDescription,
#  which 'QList[QCanSignalDescription]' gives. It is made here, so that there
#  is one as soon as there can be a QCanSignalDescription.
QList.createKind(
    QCanSignalDescription, 'value',
    make='ritual_list_make_QCanSignalDescription',
    add='ritual_list_add_QCanSignalDescription',
    size='ritual_list_size_QCanSignalDescription',
    at='ritual_list_at_QCanSignalDescription',
    drop='ritual_list_drop_QCanSignalDescription',
)
