"""
QOpcUaStructureDefinition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuastructuredefinition.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaStructureField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaStructureField = WAIT['QOpcUaStructureField']


class QOpcUaStructureDefinition(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaStructureDefinition: a plain Python object
  standing in front of one C++ QOpcUaStructureDefinition.

  C++ hands a QOpcUaStructureDefinition around as a copy, so every C++
  QOpcUaStructureDefinition behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaStructureDefinition that has a ritual and that
  Python can call so far, 9 names in all: 'defaultEncodingId',
  'setDefaultEncodingId', 'baseDataType', 'setBaseDataType', 'structureType',
  'fields', 'setFields', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpcUaStructureDefinition::swap(QOpcUaStructureDefinition
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaStructureDefinition
    &QOpcUaStructureDefinition::operator=(QOpcUaStructureDefinition
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaStructureDefinition::QOpcUaStructureDefinition(
    QOpcUaStructureDefinition &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QOpcUaStructureDefinition
    &QOpcUaStructureDefinition::operator=(const QOpcUaStructureDefinition
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaStructureDefinition::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaStructureDefinition::~QOpcUaStructureDefinition()': the
    destructor: Python removes its C++ QOpcUaStructureDefinition by it, and
    has no other use for it.
  - Qt's 'void QOpcUaStructureDefinition::setStructureType(const
    QOpcUaStructureDefinition::StructureType &structureType)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaStructureDefinition is created at the first use, not by
    'QOpcUaStructureDefinition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaStructureDefinition back gives a copy the
    ritual made for Python, in a new cute QOpcUaStructureDefinition.
  - Each name of Qt's QOpcUaStructureDefinition that has no cute function
    yet, 'setStructureType', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaStructureDefinition, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StructureType(CuteNum, scoped=True):
    """
    The enum 'QOpcUaStructureDefinition::StructureType' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Structure = Kee[int](0)
    StructureWithOptionalFields = Kee[int](1)
    Union = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaStructureDefinition'

  #  Qt's '~QOpcUaStructureDefinition()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaStructureDefinition behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaStructureDefinitionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultEncodingId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaStructureDefinition::defaultEncodingId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#defaultEncodingId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaStructureDefinition::defaultEncodingId() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaStructureDefinition17defaultEncodingIdEv',
    )

  def baseDataType(self) -> str:
    """
    Calls Qt's 'QString QOpcUaStructureDefinition::baseDataType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#baseDataType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaStructureDefinition::baseDataType() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaStructureDefinition12baseDataTypeEv',
    )

  def structureType(self) -> StructureType:
    """
    Calls Qt's 'QOpcUaStructureDefinition::StructureType
    QOpcUaStructureDefinition::structureType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#structureType

    Returns
    -------

    StructureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StructureType(number)'
      gives.
    """
    #  QOpcUaStructureDefinition::StructureType
    #      QOpcUaStructureDefinition::structureType() const
    return QOpcUaStructureDefinition.StructureType(self.uglySide.call(
        'ritual_ZNK25QOpcUaStructureDefinition13structureTypeEv',
    ))

  def fields(self) -> QList[QOpcUaStructureField]:
    """
    Calls Qt's 'QList<QOpcUaStructureField>
    QOpcUaStructureDefinition::fields() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#fields

    Returns
    -------

    QList[QOpcUaStructureField]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaStructureField> QOpcUaStructureDefinition::fields() const
    address = self.uglySide.call(
        'ritual_ZNK25QOpcUaStructureDefinition6fieldsEv',
    )
    from . import QOpcUaStructureField
    return QList[QOpcUaStructureField]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDefaultEncodingId(self, defaultEncodingId: str) -> None:
    """
    Calls Qt's 'void QOpcUaStructureDefinition::setDefaultEncodingId(const
    QString &defaultEncodingId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html

    Parameters
    ----------

    defaultEncodingId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaStructureDefinition::setDefaultEncodingId(const QString
    #      &defaultEncodingId)
    self.uglySide.call(
        'ritual_ZN25QOpcUaStructureDefinition20setDefaultEncodingIdERK7QStr'
        'ing',
        defaultEncodingId,
    )

  @overload(str)
  def setBaseDataType(self, baseDataType: str) -> None:
    """
    Calls Qt's 'void QOpcUaStructureDefinition::setBaseDataType(const QString
    &baseDataType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#setBaseDataType

    Parameters
    ----------

    baseDataType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaStructureDefinition::setBaseDataType(const QString
    #      &baseDataType)
    self.uglySide.call(
        'ritual_ZN25QOpcUaStructureDefinition15setBaseDataTypeERK7QString',
        baseDataType,
    )

  @overload(QList[QOpcUaStructureField])
  def setFields(self, fields: QList[QOpcUaStructureField]) -> None:
    """
    Calls Qt's 'void QOpcUaStructureDefinition::setFields(const
    QList<QOpcUaStructureField> &fields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#setFields

    Parameters
    ----------

    fields : QList[QOpcUaStructureField]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaStructureDefinition::setFields(const
    #      QList<QOpcUaStructureField> &fields)
    self.uglySide.call(
        'ritual_ZN25QOpcUaStructureDefinition9setFieldsERK5QListI20QOpcUaSt'
        'ructureFieldE',
        self._valueOf(fields),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaStructureDefinition) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaStructureDefinition &lhs, const
    QOpcUaStructureDefinition &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#operator==

    Parameters
    ----------

    rhs : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaStructureDefinition &lhs, const
    #      QOpcUaStructureDefinition &rhs)
    return Rituals.call(
        'ritual_ZeqRK25QOpcUaStructureDefinitionS1_',
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
  def __ne__(self, rhs: QOpcUaStructureDefinition) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaStructureDefinition &lhs, const
    QOpcUaStructureDefinition &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaStructureDefinition &lhs, const
    #      QOpcUaStructureDefinition &rhs)
    return Rituals.call(
        'ritual_ZneRK25QOpcUaStructureDefinitionS1_',
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
    Notes what was given, for Qt's
    'QOpcUaStructureDefinition::QOpcUaStructureDefinition()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html
    """
    #  QOpcUaStructureDefinition::QOpcUaStructureDefinition()
    self._noteCreation(QOpcUaStructureDefinition, lambda: Rituals.call(
        'ritual_ZN25QOpcUaStructureDefinitionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaStructureDefinition) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaStructureDefinition::QOpcUaStructureDefinition(const
    QOpcUaStructureDefinition &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructuredefinition.html

    Parameters
    ----------

    a0 : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.
    """
    #  QOpcUaStructureDefinition::QOpcUaStructureDefinition(const
    #      QOpcUaStructureDefinition &a0)
    self._noteCreation(QOpcUaStructureDefinition, lambda: Rituals.call(
        'ritual_ZN25QOpcUaStructureDefinitionC1ERKS_', self._valueOf(a0),
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
  def setStructureType(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaStructureDefinition::setStructureType(const
    QOpcUaStructureDefinition::StructureType &structureType)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaStructureDefinition.setStructureType' has no cute function "
        "yet. Qt's 'void QOpcUaStructureDefinition::setStructureType(const "
        "QOpcUaStructureDefinition::StructureType &structureType)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaStructureDefinition::swap(QOpcUaStructureDefinition
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaStructureDefinition.swap' has no cute function yet. Qt's "
        "'void QOpcUaStructureDefinition::swap(QOpcUaStructureDefinition "
        "&other)': takes a type Python has no way to hand over yet.")
