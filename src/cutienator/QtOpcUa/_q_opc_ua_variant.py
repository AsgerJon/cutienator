"""
QOpcUaVariant binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuavariant.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QOpcUaVariant(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaVariant: a plain Python object standing in
  front of one C++ QOpcUaVariant.

  C++ hands a QOpcUaVariant around as a copy, so every C++ QOpcUaVariant
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaVariant that has a ritual and that Python can
  call so far, 6 names in all: 'value', 'setValue', 'type', 'isArray',
  '__eq__', '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaVariant::QOpcUaVariant(ValueType type, const QVariant &value,
    const QList<qint32> arrayDimensions)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QOpcUaVariant::~QOpcUaVariant()': the destructor: Python removes
    its C++ QOpcUaVariant by it, and has no other use for it.
  - Qt's 'void QOpcUaVariant::swap(QOpcUaVariant &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOpcUaVariant &QOpcUaVariant::operator=(QOpcUaVariant &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaVariant::QOpcUaVariant(QOpcUaVariant &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOpcUaVariant &QOpcUaVariant::operator=(const QOpcUaVariant &rhs)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QOpcUaVariant::setValue(ValueType type, const QVariant &value,
    const QList<qint32> &arrayDimensions)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<qint32> QOpcUaVariant::arrayDimensions() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QOpcUaVariant::setArrayDimensions(const QList<qint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant QOpcUaVariant::operator QVariant() const': an operator
    Python has no name for.

  What to expect
  --------------

  - The C++ QOpcUaVariant is created at the first use, not by
    'QOpcUaVariant(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaVariant back gives a copy the ritual made for
    Python, in a new cute QOpcUaVariant.
  - Each name of Qt's QOpcUaVariant that has no cute function yet,
    'arrayDimensions', 'setArrayDimensions', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaVariant, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ValueType(CuteNum, scoped=True):
    """
    The enum 'QOpcUaVariant::ValueType' of Qt, with the 26 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unknown = Kee[int](0)
    Boolean = Kee[int](1)
    SByte = Kee[int](2)
    Byte = Kee[int](3)
    Int16 = Kee[int](4)
    UInt16 = Kee[int](5)
    Int32 = Kee[int](6)
    UInt32 = Kee[int](7)
    Int64 = Kee[int](8)
    UInt64 = Kee[int](9)
    Float = Kee[int](10)
    Double = Kee[int](11)
    String = Kee[int](12)
    DateTime = Kee[int](13)
    Guid = Kee[int](14)
    ByteString = Kee[int](15)
    XmlElement = Kee[int](16)
    NodeId = Kee[int](17)
    ExpandedNodeId = Kee[int](18)
    StatusCode = Kee[int](19)
    QualifiedName = Kee[int](20)
    LocalizedText = Kee[int](21)
    ExtensionObject = Kee[int](22)
    DataValue = Kee[int](23)
    Variant = Kee[int](24)
    DiagnosticInfo = Kee[int](25)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaVariant'

  #  Qt's '~QOpcUaVariant()'. Naming it makes this a value class: Python owns
  #  every C++ QOpcUaVariant behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QOpcUaVariantD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaVariant::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaVariant::value() const
    address = self.uglySide.call('ritual_ZNK13QOpcUaVariant5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def type(self) -> ValueType:
    """
    Calls Qt's 'ValueType QOpcUaVariant::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#type

    Returns
    -------

    ValueType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ValueType(number)' gives.
    """
    #  ValueType QOpcUaVariant::type() const
    return QOpcUaVariant.ValueType(self.uglySide.call(
        'ritual_ZNK13QOpcUaVariant4typeEv',
    ))

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaVariant::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#isArray
    """
    #  bool QOpcUaVariant::isArray() const
    return self.uglySide.call('ritual_ZNK13QOpcUaVariant7isArrayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ValueType, QVariant)
  def setValue(self, type: ValueType, value: QVariant) -> None:
    """
    Calls Qt's 'void QOpcUaVariant::setValue(ValueType type, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#setValue

    Parameters
    ----------

    type : ValueType
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QOpcUaVariant::setValue(ValueType type, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN13QOpcUaVariant8setValueENS_9ValueTypeERK8QVariant',
        type.value, self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaVariant) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaVariant &lhs, const QOpcUaVariant
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#operator==

    Parameters
    ----------

    rhs : QOpcUaVariant
      Passed on as a value: Qt reads the C++ QOpcUaVariant, which stays
      Python's own.
    """
    #  bool operator==(const QOpcUaVariant &lhs, const QOpcUaVariant &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QOpcUaVariantS1_',
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
  def __ne__(self, rhs: QOpcUaVariant) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaVariant &lhs, const QOpcUaVariant
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaVariant
      Passed on as a value: Qt reads the C++ QOpcUaVariant, which stays
      Python's own.
    """
    #  bool operator!=(const QOpcUaVariant &lhs, const QOpcUaVariant &rhs)
    return Rituals.call(
        'ritual_ZneRK13QOpcUaVariantS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaVariant::QOpcUaVariant()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#QOpcUaVariant
    """
    #  QOpcUaVariant::QOpcUaVariant()
    self._noteCreation(QOpcUaVariant, lambda: Rituals.call(
        'ritual_ZN13QOpcUaVariantC1Ev',
    ))

  @overload(ValueType, QVariant)
  def __init__(self, type: ValueType, value: QVariant) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaVariant::QOpcUaVariant(ValueType
    type, const QVariant &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#QOpcUaVariant

    Parameters
    ----------

    type : ValueType
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QOpcUaVariant::QOpcUaVariant(ValueType type, const QVariant &value)
    self._noteCreation(QOpcUaVariant, lambda: Rituals.call(
        'ritual_ZN13QOpcUaVariantC1ENS_9ValueTypeERK8QVariant',
        type.value, self._valueOf(value),
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaVariant) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaVariant::QOpcUaVariant(const
    QOpcUaVariant &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuavariant.html#QOpcUaVariant

    Parameters
    ----------

    other : QOpcUaVariant
      Passed on as a value: Qt reads the C++ QOpcUaVariant, which stays
      Python's own.
    """
    #  QOpcUaVariant::QOpcUaVariant(const QOpcUaVariant &other)
    self._noteCreation(QOpcUaVariant, lambda: Rituals.call(
        'ritual_ZN13QOpcUaVariantC1ERKS_', self._valueOf(other),
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
  def arrayDimensions(*__, **_) -> Never:
    """
    Qt's 'QList<qint32> QOpcUaVariant::arrayDimensions() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaVariant.arrayDimensions' has no cute function yet. Qt's "
        "'QList<qint32> QOpcUaVariant::arrayDimensions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setArrayDimensions(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaVariant::setArrayDimensions(const QList<qint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaVariant.setArrayDimensions' has no cute function yet. Qt's "
        "'void QOpcUaVariant::setArrayDimensions(const QList<qint32> "
        "&arrayDimensions)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaVariant::swap(QOpcUaVariant &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaVariant.swap' has no cute function yet. Qt's 'void "
        "QOpcUaVariant::swap(QOpcUaVariant &other)': takes a type Python "
        "has no way to hand over yet.")
