"""
QOpcUaGenericStructValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuagenericstructvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QVariant
  from . import QOpcUaStructureDefinition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QOpcUaStructureDefinition = WAIT['QOpcUaStructureDefinition']
  QVariant = WAIT['QVariant']


class QOpcUaGenericStructValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaGenericStructValue: a plain Python object
  standing in front of one C++ QOpcUaGenericStructValue.

  C++ hands a QOpcUaGenericStructValue around as a copy, so every C++
  QOpcUaGenericStructValue behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaGenericStructValue that has a ritual and that
  Python can call so far, 12 names in all: 'typeName', 'setTypeName',
  'typeId', 'setTypeId', 'structureDefinition', 'setStructureDefinition',
  'fields', 'setFields', 'toString', '__rlshift__', '__eq__', '__ne__'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaGenericStructValue::~QOpcUaGenericStructValue()': the
    destructor: Python removes its C++ QOpcUaGenericStructValue by it, and
    has no other use for it.
  - Qt's 'QOpcUaGenericStructValue::QOpcUaGenericStructValue(
    QOpcUaGenericStructValue &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QOpcUaGenericStructValue &QOpcUaGenericStructValue::operator=(const
    QOpcUaGenericStructValue &rhs)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'void QOpcUaGenericStructValue::swap(QOpcUaGenericStructValue
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaGenericStructValue
    &QOpcUaGenericStructValue::operator=(QOpcUaGenericStructValue &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaGenericStructValue::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QHash<QString, QVariant> &QOpcUaGenericStructValue::fieldsRef()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaGenericStructValue is created at the first use, not by
    'QOpcUaGenericStructValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaGenericStructValue back gives a copy the ritual
    made for Python, in a new cute QOpcUaGenericStructValue.
  - Each name of Qt's QOpcUaGenericStructValue that has no cute function yet,
    'fieldsRef', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaGenericStructValue'

  #  Qt's '~QOpcUaGenericStructValue()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaGenericStructValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QOpcUaGenericStructValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QOpcUaGenericStructValue::typeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructValue::typeName() const
    return self.uglySide.call(
        'ritual_ZNK24QOpcUaGenericStructValue8typeNameEv',
    )

  def typeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaGenericStructValue::typeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#typeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructValue::typeId() const
    return self.uglySide.call(
        'ritual_ZNK24QOpcUaGenericStructValue6typeIdEv',
    )

  def structureDefinition(self) -> QOpcUaStructureDefinition:
    """
    Calls Qt's 'QOpcUaStructureDefinition
    QOpcUaGenericStructValue::structureDefinition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#structureDefinition

    Returns
    -------

    QOpcUaStructureDefinition
      A new cute QOpcUaStructureDefinition around the copy Qt gave back.
      Python owns it.
    """
    #  QOpcUaStructureDefinition
    #      QOpcUaGenericStructValue::structureDefinition() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpcUaGenericStructValue19structureDefinitionEv',
    )
    from . import QOpcUaStructureDefinition
    return QOpcUaStructureDefinition._cuteOwning(address)

  def fields(self) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QHash<QString, QVariant> QOpcUaGenericStructValue::fields()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#fields

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QVariant> QOpcUaGenericStructValue::fields() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpcUaGenericStructValue6fieldsEv',
    )
    from ..QtCore import QVariant
    return QHash[str, QVariant]._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QOpcUaGenericStructValue::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaGenericStructValue::toString() const
    return self.uglySide.call(
        'ritual_ZNK24QOpcUaGenericStructValue8toStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTypeName(self, typeName: str) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructValue::setTypeName(const QString
    &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#setTypeName

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaGenericStructValue::setTypeName(const QString &typeName)
    self.uglySide.call(
        'ritual_ZN24QOpcUaGenericStructValue11setTypeNameERK7QString',
        typeName,
    )

  @overload(str)
  def setTypeId(self, typeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructValue::setTypeId(const QString
    &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#setTypeId

    Parameters
    ----------

    typeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaGenericStructValue::setTypeId(const QString &typeId)
    self.uglySide.call(
        'ritual_ZN24QOpcUaGenericStructValue9setTypeIdERK7QString', typeId,
    )

  @overload(QOpcUaStructureDefinition)
  def setStructureDefinition(
      self,
      structureDefinition: QOpcUaStructureDefinition,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructValue::setStructureDefinition(const
    QOpcUaStructureDefinition &structureDefinition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html

    Parameters
    ----------

    structureDefinition : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.
    """
    #  void QOpcUaGenericStructValue::setStructureDefinition(const
    #      QOpcUaStructureDefinition &structureDefinition)
    self.uglySide.call(
        'ritual_ZN24QOpcUaGenericStructValue22setStructureDefinitionERK25QO'
        'pcUaStructureDefinition',
        self._valueOf(structureDefinition),
    )

  @overload(QHash[str, QVariant])
  def setFields(self, fields: QHash[str, QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaGenericStructValue::setFields(const QHash<QString,
    QVariant> &fields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#setFields

    Parameters
    ----------

    fields : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QOpcUaGenericStructValue::setFields(const QHash<QString,
    #      QVariant> &fields)
    self.uglySide.call(
        'ritual_ZN24QOpcUaGenericStructValue9setFieldsERK5QHashI7QString8QV'
        'ariantE',
        self._valueOf(fields),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const
    QOpcUaGenericStructValue &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QOpcUaGenericStructValue &s)
    address = Rituals.call(
        'ritual_Zls6QDebugRK24QOpcUaGenericStructValue',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
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

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaGenericStructValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaGenericStructValue &lhs, const
    QOpcUaGenericStructValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#operator==

    Parameters
    ----------

    rhs : QOpcUaGenericStructValue
      Passed on as a value: Qt reads the C++ QOpcUaGenericStructValue, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaGenericStructValue &lhs, const
    #      QOpcUaGenericStructValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK24QOpcUaGenericStructValueS1_',
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
  def __ne__(self, rhs: QOpcUaGenericStructValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaGenericStructValue &lhs, const
    QOpcUaGenericStructValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaGenericStructValue
      Passed on as a value: Qt reads the C++ QOpcUaGenericStructValue, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaGenericStructValue &lhs, const
    #      QOpcUaGenericStructValue &rhs)
    return Rituals.call(
        'ritual_ZneRK24QOpcUaGenericStructValueS1_',
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
    'QOpcUaGenericStructValue::QOpcUaGenericStructValue()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html
    """
    #  QOpcUaGenericStructValue::QOpcUaGenericStructValue()
    self._noteCreation(QOpcUaGenericStructValue, lambda: Rituals.call(
        'ritual_ZN24QOpcUaGenericStructValueC1Ev',
    ))

  @overload(str, str, QOpcUaStructureDefinition)
  def __init__(
      self,
      typeName: str,
      typeId: str,
      definition: QOpcUaStructureDefinition,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
    &typeName, const QString &typeId, const QOpcUaStructureDefinition
    &definition)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    definition : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.
    """
    #  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
    #      &typeName, const QString &typeId, const QOpcUaStructureDefinition
    #      &definition)
    self._noteCreation(QOpcUaGenericStructValue, lambda: Rituals.call(
        'ritual_ZN24QOpcUaGenericStructValueC1ERK7QStringS2_RK25QOpcUaStruc'
        'tureDefinition',
        typeName, typeId, self._valueOf(definition),
    ))

  @overload(str, str, QOpcUaStructureDefinition, QHash[str, QVariant])
  def __init__(
      self,
      typeName: str,
      typeId: str,
      definition: QOpcUaStructureDefinition,
      fields: QHash[str, QVariant],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
    &typeName, const QString &typeId, const QOpcUaStructureDefinition
    &definition, const QHash<QString, QVariant> &fields)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    definition : QOpcUaStructureDefinition
      Passed on as a value: Qt reads the C++ QOpcUaStructureDefinition, which
      stays Python's own.

    fields : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const QString
    #      &typeName, const QString &typeId, const QOpcUaStructureDefinition
    #      &definition, const QHash<QString, QVariant> &fields)
    self._noteCreation(QOpcUaGenericStructValue, lambda: Rituals.call(
        'ritual_ZN24QOpcUaGenericStructValueC1ERK7QStringS2_RK25QOpcUaStruc'
        'tureDefinitionRK5QHashIS0_8QVariantE',
        typeName, typeId, self._valueOf(definition), self._valueOf(fields),
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaGenericStructValue) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaGenericStructValue::QOpcUaGenericStructValue(const
    QOpcUaGenericStructValue &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuagenericstructvalue.html

    Parameters
    ----------

    other : QOpcUaGenericStructValue
      Passed on as a value: Qt reads the C++ QOpcUaGenericStructValue, which
      stays Python's own.
    """
    #  QOpcUaGenericStructValue::QOpcUaGenericStructValue(const
    #      QOpcUaGenericStructValue &other)
    self._noteCreation(QOpcUaGenericStructValue, lambda: Rituals.call(
        'ritual_ZN24QOpcUaGenericStructValueC1ERKS_', self._valueOf(other),
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
  def fieldsRef(*__, **_) -> Never:
    """
    Qt's 'QHash<QString, QVariant> &QOpcUaGenericStructValue::fieldsRef()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructValue.fieldsRef' has no cute function yet. "
        "Qt's 'QHash<QString, QVariant> "
        "&QOpcUaGenericStructValue::fieldsRef()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaGenericStructValue::swap(QOpcUaGenericStructValue
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaGenericStructValue.swap' has no cute function yet. Qt's "
        "'void QOpcUaGenericStructValue::swap(QOpcUaGenericStructValue "
        "&other)': takes a type Python has no way to hand over yet.")
