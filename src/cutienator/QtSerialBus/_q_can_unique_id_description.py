"""
QCanUniqueIdDescription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanuniqueiddescription.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QSysInfo
from . import QtCanBus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCanUniqueIdDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanUniqueIdDescription: a plain Python object
  standing in front of one C++ QCanUniqueIdDescription.

  C++ hands a QCanUniqueIdDescription around as a copy, so every C++
  QCanUniqueIdDescription behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanUniqueIdDescription that has a ritual and that
  Python can call so far, 9 names in all: 'isValid', 'source', 'setSource',
  'startBit', 'setStartBit', 'bitLength', 'setBitLength', 'endian',
  'setEndian'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QCanUniqueIdDescription::QCanUniqueIdDescription(QCanUniqueIdDescription
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanUniqueIdDescription::~QCanUniqueIdDescription()': the
    destructor: Python removes its C++ QCanUniqueIdDescription by it, and has
    no other use for it.
  - Qt's 'QCanUniqueIdDescription &QCanUniqueIdDescription::operator=(const
    QCanUniqueIdDescription &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QCanUniqueIdDescription
    &QCanUniqueIdDescription::operator=(QCanUniqueIdDescription &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanUniqueIdDescription::swap(QCanUniqueIdDescription
    &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QCanUniqueIdDescription is created at the first use, not by
    'QCanUniqueIdDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanUniqueIdDescription back gives a copy the ritual
    made for Python, in a new cute QCanUniqueIdDescription.
  - Each name of Qt's QCanUniqueIdDescription that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanUniqueIdDescription'

  #  Qt's '~QCanUniqueIdDescription()'. Naming it makes this a value class:
  #  Python owns every C++ QCanUniqueIdDescription behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QCanUniqueIdDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCanUniqueIdDescription::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#isValid
    """
    #  bool QCanUniqueIdDescription::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QCanUniqueIdDescription7isValidEv',
    )

  def source(self) -> QtCanBus.DataSource:
    """
    Calls Qt's 'QtCanBus::DataSource QCanUniqueIdDescription::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#source

    Returns
    -------

    QtCanBus.DataSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCanBus.DataSource(number)' gives.
    """
    #  QtCanBus::DataSource QCanUniqueIdDescription::source() const
    return QtCanBus.DataSource(self.uglySide.call(
        'ritual_ZNK23QCanUniqueIdDescription6sourceEv',
    ))

  def startBit(self) -> int:
    """
    Calls Qt's 'quint16 QCanUniqueIdDescription::startBit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#startBit
    """
    #  quint16 QCanUniqueIdDescription::startBit() const
    return self.uglySide.call(
        'ritual_ZNK23QCanUniqueIdDescription8startBitEv',
    )

  def bitLength(self) -> int:
    """
    Calls Qt's 'quint8 QCanUniqueIdDescription::bitLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#bitLength
    """
    #  quint8 QCanUniqueIdDescription::bitLength() const
    return self.uglySide.call(
        'ritual_ZNK23QCanUniqueIdDescription9bitLengthEv',
    )

  def endian(self) -> QSysInfo.Endian:
    """
    Calls Qt's 'QSysInfo::Endian QCanUniqueIdDescription::endian() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#endian

    Returns
    -------

    QSysInfo.Endian
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSysInfo.Endian(number)'
      gives.
    """
    #  QSysInfo::Endian QCanUniqueIdDescription::endian() const
    return QSysInfo.Endian(self.uglySide.call(
        'ritual_ZNK23QCanUniqueIdDescription6endianEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtCanBus.DataSource)
  def setSource(self, source: QtCanBus.DataSource) -> None:
    """
    Calls Qt's 'void QCanUniqueIdDescription::setSource(QtCanBus::DataSource
    source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#setSource

    Parameters
    ----------

    source : QtCanBus.DataSource
      Passed on as its number.
    """
    #  void QCanUniqueIdDescription::setSource(QtCanBus::DataSource source)
    self.uglySide.call(
        'ritual_ZN23QCanUniqueIdDescription9setSourceEN8QtCanBus10DataSourc'
        'eE',
        source.value,
    )

  @overload(int)
  def setStartBit(self, bit: int) -> None:
    """
    Calls Qt's 'void QCanUniqueIdDescription::setStartBit(quint16 bit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#setStartBit

    Parameters
    ----------

    bit : int
      Passed on as it is.
    """
    #  void QCanUniqueIdDescription::setStartBit(quint16 bit)
    self.uglySide.call(
        'ritual_ZN23QCanUniqueIdDescription11setStartBitEt', bit,
    )

  @overload(int)
  def setBitLength(self, length: int) -> None:
    """
    Calls Qt's 'void QCanUniqueIdDescription::setBitLength(quint8 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#setBitLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QCanUniqueIdDescription::setBitLength(quint8 length)
    self.uglySide.call(
        'ritual_ZN23QCanUniqueIdDescription12setBitLengthEh', length,
    )

  @overload(QSysInfo.Endian)
  def setEndian(self, endian: QSysInfo.Endian) -> None:
    """
    Calls Qt's 'void QCanUniqueIdDescription::setEndian(QSysInfo::Endian
    endian)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html#setEndian

    Parameters
    ----------

    endian : QSysInfo.Endian
      Passed on as its number.
    """
    #  void QCanUniqueIdDescription::setEndian(QSysInfo::Endian endian)
    self.uglySide.call(
        'ritual_ZN23QCanUniqueIdDescription9setEndianEN8QSysInfo6EndianE',
        endian.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanUniqueIdDescription::QCanUniqueIdDescription()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html
    """
    #  QCanUniqueIdDescription::QCanUniqueIdDescription()
    self._noteCreation(QCanUniqueIdDescription, lambda: Rituals.call(
        'ritual_ZN23QCanUniqueIdDescriptionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCanUniqueIdDescription) -> None:
    """
    Notes what was given, for Qt's
    'QCanUniqueIdDescription::QCanUniqueIdDescription(const
    QCanUniqueIdDescription &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanuniqueiddescription.html

    Parameters
    ----------

    other : QCanUniqueIdDescription
      Passed on as a value: Qt reads the C++ QCanUniqueIdDescription, which
      stays Python's own.
    """
    #  QCanUniqueIdDescription::QCanUniqueIdDescription(const
    #      QCanUniqueIdDescription &other)
    self._noteCreation(QCanUniqueIdDescription, lambda: Rituals.call(
        'ritual_ZN23QCanUniqueIdDescriptionC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanUniqueIdDescription::swap(QCanUniqueIdDescription
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanUniqueIdDescription.swap' has no cute function yet. Qt's "
        "'void QCanUniqueIdDescription::swap(QCanUniqueIdDescription "
        "&other)': takes a type Python has no way to hand over yet.")
