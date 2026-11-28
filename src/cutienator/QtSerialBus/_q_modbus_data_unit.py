"""
QModbusDataUnit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusdataunit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QModbusDataUnit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModbusDataUnit: a plain Python object standing in
  front of one C++ QModbusDataUnit.

  C++ hands a QModbusDataUnit around as a copy, so every C++ QModbusDataUnit
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModbusDataUnit that has a ritual and that Python
  can call so far, 9 names in all: 'registerType', 'setRegisterType',
  'startAddress', 'setStartAddress', 'valueCount', 'setValueCount',
  'setValue', 'value', 'isValid'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModbusDataUnit::QModbusDataUnit(RegisterType type, int
    newStartAddress, const QList<quint16> &newValues)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<quint16> QModbusDataUnit::values() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QModbusDataUnit::setValues(const QList<quint16> &newValues)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QModbusDataUnit::~QModbusDataUnit()': the destructor: Python
    removes its C++ QModbusDataUnit by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QModbusDataUnit is created at the first use, not by
    'QModbusDataUnit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusDataUnit back gives a copy the ritual made for
    Python, in a new cute QModbusDataUnit.
  - Each name of Qt's QModbusDataUnit that has no cute function yet,
    'setValues', 'values', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QModbusDataUnit, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RegisterType(CuteNum):
    """
    The enum 'QModbusDataUnit::RegisterType' of Qt, with the 5 names Qt gives
    in it.
    """

    Invalid = Kee[int](0)
    DiscreteInputs = Kee[int](1)
    Coils = Kee[int](2)
    InputRegisters = Kee[int](3)
    HoldingRegisters = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusDataUnit'

  #  Qt's '~QModbusDataUnit()'. Naming it makes this a value class: Python
  #  owns every C++ QModbusDataUnit behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QModbusDataUnitD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def registerType(self) -> RegisterType:
    """
    Calls Qt's 'RegisterType QModbusDataUnit::registerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#registerType

    Returns
    -------

    RegisterType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RegisterType(number)'
      gives.
    """
    #  RegisterType QModbusDataUnit::registerType() const
    return QModbusDataUnit.RegisterType(self.uglySide.call(
        'ritual_ZNK15QModbusDataUnit12registerTypeEv',
    ))

  def startAddress(self) -> int:
    """
    Calls Qt's 'int QModbusDataUnit::startAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#startAddress
    """
    #  int QModbusDataUnit::startAddress() const
    return self.uglySide.call('ritual_ZNK15QModbusDataUnit12startAddressEv')

  def valueCount(self) -> int:
    """
    Calls Qt's 'qsizetype QModbusDataUnit::valueCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#valueCount
    """
    #  qsizetype QModbusDataUnit::valueCount() const
    return self.uglySide.call('ritual_ZNK15QModbusDataUnit10valueCountEv')

  @overload(int)
  def value(self, index: int) -> int:
    """
    Calls Qt's 'quint16 QModbusDataUnit::value(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#value

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  quint16 QModbusDataUnit::value(qsizetype index) const
    return self.uglySide.call('ritual_ZNK15QModbusDataUnit5valueEx', index)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QModbusDataUnit::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#isValid
    """
    #  bool QModbusDataUnit::isValid() const
    return self.uglySide.call('ritual_ZNK15QModbusDataUnit7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RegisterType)
  def setRegisterType(self, type: RegisterType) -> None:
    """
    Calls Qt's 'void QModbusDataUnit::setRegisterType(RegisterType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdataunit.html#setRegisterType

    Parameters
    ----------

    type : RegisterType
      Passed on as its number.
    """
    #  void QModbusDataUnit::setRegisterType(RegisterType type)
    self.uglySide.call(
        'ritual_ZN15QModbusDataUnit15setRegisterTypeENS_12RegisterTypeE',
        type.value,
    )

  @overload(int)
  def setStartAddress(self, newAddress: int) -> None:
    """
    Calls Qt's 'void QModbusDataUnit::setStartAddress(int newAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdataunit.html#setStartAddress

    Parameters
    ----------

    newAddress : int
      Passed on as it is.
    """
    #  void QModbusDataUnit::setStartAddress(int newAddress)
    self.uglySide.call(
        'ritual_ZN15QModbusDataUnit15setStartAddressEi', newAddress,
    )

  @overload(int)
  def setValueCount(self, newCount: int) -> None:
    """
    Calls Qt's 'void QModbusDataUnit::setValueCount(qsizetype newCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#setValueCount

    Parameters
    ----------

    newCount : int
      Passed on as it is.
    """
    #  void QModbusDataUnit::setValueCount(qsizetype newCount)
    self.uglySide.call(
        'ritual_ZN15QModbusDataUnit13setValueCountEx', newCount,
    )

  @overload(int, int)
  def setValue(self, index: int, newValue: int) -> None:
    """
    Calls Qt's 'void QModbusDataUnit::setValue(qsizetype index, quint16
    newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusdataunit.html#setValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    newValue : int
      Passed on as it is.
    """
    #  void QModbusDataUnit::setValue(qsizetype index, quint16 newValue)
    self.uglySide.call(
        'ritual_ZN15QModbusDataUnit8setValueExt', index, newValue,
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
    Notes what was given, for Qt's 'QModbusDataUnit::QModbusDataUnit()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdataunit.html#QModbusDataUnit
    """
    #  QModbusDataUnit::QModbusDataUnit()
    self._noteCreation(QModbusDataUnit, lambda: Rituals.call(
        'ritual_ZN15QModbusDataUnitC1Ev',
    ))

  @overload(RegisterType)
  def __init__(self, type: RegisterType) -> None:
    """
    Notes what was given, for Qt's
    'QModbusDataUnit::QModbusDataUnit(RegisterType type)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdataunit.html#QModbusDataUnit

    Parameters
    ----------

    type : RegisterType
      Passed on as its number.
    """
    #  QModbusDataUnit::QModbusDataUnit(RegisterType type)
    self._noteCreation(QModbusDataUnit, lambda: Rituals.call(
        'ritual_ZN15QModbusDataUnitC1ENS_12RegisterTypeE', type.value,
    ))

  @overload(RegisterType, int, int)
  def __init__(
      self,
      type: RegisterType,
      newStartAddress: int,
      newValueCount: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QModbusDataUnit::QModbusDataUnit(RegisterType type, int newStartAddress,
    quint16 newValueCount)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusdataunit.html#QModbusDataUnit

    Parameters
    ----------

    type : RegisterType
      Passed on as its number.

    newStartAddress : int
      Passed on as it is.

    newValueCount : int
      Passed on as it is.
    """
    #  QModbusDataUnit::QModbusDataUnit(RegisterType type, int
    #      newStartAddress, quint16 newValueCount)
    self._noteCreation(QModbusDataUnit, lambda: Rituals.call(
        'ritual_ZN15QModbusDataUnitC1ENS_12RegisterTypeEit',
        type.value, newStartAddress, newValueCount,
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
  def setValues(*__, **_) -> Never:
    """
    Qt's 'void QModbusDataUnit::setValues(const QList<quint16> &newValues)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusDataUnit.setValues' has no cute function yet. Qt's 'void "
        "QModbusDataUnit::setValues(const QList<quint16> &newValues)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def values(*__, **_) -> Never:
    """
    Qt's 'QList<quint16> QModbusDataUnit::values() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QModbusDataUnit.values' has no cute function yet. Qt's "
        "'QList<quint16> QModbusDataUnit::values() const': gives a type "
        "Python has no way to take yet.")
