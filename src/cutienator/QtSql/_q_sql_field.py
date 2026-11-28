"""
QSqlField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlfield.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QVariant

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']


class QSqlField(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlField: a plain Python object standing in front of
  one C++ QSqlField.

  C++ hands a QSqlField around as a copy, so every C++ QSqlField behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlField that has a ritual and that Python can call
  so far, 33 names in all: '__eq__', '__ne__', 'setValue', 'value',
  'setName', 'name', 'setTableName', 'tableName', 'isNull', 'setReadOnly',
  'isReadOnly', 'clear', 'isAutoValue', 'metaType', 'setMetaType', 'type',
  'setType', 'setRequiredStatus', 'setRequired', 'setLength', 'setPrecision',
  'setDefaultValue', 'setSqlType', 'setGenerated', 'setAutoValue',
  'requiredStatus', 'length', 'precision', 'defaultValue', 'typeID',
  'isGenerated', 'isValid', 'detach'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlField &QSqlField::operator=(const QSqlField &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSqlField::QSqlField(QSqlField &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSqlField &QSqlField::operator=(QSqlField &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSqlField::~QSqlField()': the destructor: Python removes its C++
    QSqlField by it, and has no other use for it.
  - Qt's 'void QSqlField::swap(QSqlField &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 44 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSqlField is created at the first use, not by 'QSqlField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlField back gives a copy the ritual made for
    Python, in a new cute QSqlField.
  - Each name of Qt's QSqlField that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSqlField, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class RequiredStatus(CuteNum):
    """
    The enum 'QSqlField::RequiredStatus' of Qt, with the 3 names Qt gives in
    it.
    """

    Unknown = Kee[int](-1)
    Optional = Kee[int](0)
    Required = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlField'

  #  Qt's '~QSqlField()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlField behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSqlFieldD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlField::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlField::value() const
    address = self.uglySide.call('ritual_ZNK9QSqlField5valueEv')
    return QVariant._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QSqlField::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlField::name() const
    return self.uglySide.call('ritual_ZNK9QSqlField4nameEv')

  def tableName(self) -> str:
    """
    Calls Qt's 'QString QSqlField::tableName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#tableName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlField::tableName() const
    return self.uglySide.call('ritual_ZNK9QSqlField9tableNameEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSqlField::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#isNull
    """
    #  bool QSqlField::isNull() const
    return self.uglySide.call('ritual_ZNK9QSqlField6isNullEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QSqlField::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#isReadOnly
    """
    #  bool QSqlField::isReadOnly() const
    return self.uglySide.call('ritual_ZNK9QSqlField10isReadOnlyEv')

  def isAutoValue(self) -> bool:
    """
    Calls Qt's 'bool QSqlField::isAutoValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#isAutoValue
    """
    #  bool QSqlField::isAutoValue() const
    return self.uglySide.call('ritual_ZNK9QSqlField11isAutoValueEv')

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QSqlField::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QSqlField::metaType() const
    address = self.uglySide.call('ritual_ZNK9QSqlField8metaTypeEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def type(self) -> QVariant.Type:
    """
    Calls Qt's 'QVariant::Type QSqlField::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#type

    Returns
    -------

    QVariant.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QVariant.Type(number)'
      gives.
    """
    #  QVariant::Type QSqlField::type() const
    return QVariant.Type(self.uglySide.call('ritual_ZNK9QSqlField4typeEv'))

  def requiredStatus(self) -> RequiredStatus:
    """
    Calls Qt's 'RequiredStatus QSqlField::requiredStatus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#requiredStatus

    Returns
    -------

    RequiredStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RequiredStatus(number)'
      gives.
    """
    #  RequiredStatus QSqlField::requiredStatus() const
    return QSqlField.RequiredStatus(self.uglySide.call(
        'ritual_ZNK9QSqlField14requiredStatusEv',
    ))

  def length(self) -> int:
    """
    Calls Qt's 'int QSqlField::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#length
    """
    #  int QSqlField::length() const
    return self.uglySide.call('ritual_ZNK9QSqlField6lengthEv')

  def precision(self) -> int:
    """
    Calls Qt's 'int QSqlField::precision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#precision
    """
    #  int QSqlField::precision() const
    return self.uglySide.call('ritual_ZNK9QSqlField9precisionEv')

  def defaultValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlField::defaultValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#defaultValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlField::defaultValue() const
    address = self.uglySide.call('ritual_ZNK9QSqlField12defaultValueEv')
    return QVariant._cuteOwning(address)

  def typeID(self) -> int:
    """
    Calls Qt's 'int QSqlField::typeID() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#typeID
    """
    #  int QSqlField::typeID() const
    return self.uglySide.call('ritual_ZNK9QSqlField6typeIDEv')

  def isGenerated(self) -> bool:
    """
    Calls Qt's 'bool QSqlField::isGenerated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#isGenerated
    """
    #  bool QSqlField::isGenerated() const
    return self.uglySide.call('ritual_ZNK9QSqlField11isGeneratedEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlField::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#isValid
    """
    #  bool QSqlField::isValid() const
    return self.uglySide.call('ritual_ZNK9QSqlField7isValidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QSqlField::setValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSqlField::setValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN9QSqlField8setValueERK8QVariant', self._valueOf(value),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QSqlField::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlField::setName(const QString &name)
    self.uglySide.call('ritual_ZN9QSqlField7setNameERK7QString', name)

  @overload(str)
  def setTableName(self, tableName: str) -> None:
    """
    Calls Qt's 'void QSqlField::setTableName(const QString &tableName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setTableName

    Parameters
    ----------

    tableName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlField::setTableName(const QString &tableName)
    self.uglySide.call(
        'ritual_ZN9QSqlField12setTableNameERK7QString', tableName,
    )

  @overload(bool)
  def setReadOnly(self, readOnly: bool) -> None:
    """
    Calls Qt's 'void QSqlField::setReadOnly(bool readOnly)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setReadOnly

    Parameters
    ----------

    readOnly : bool
      Passed on as it is.
    """
    #  void QSqlField::setReadOnly(bool readOnly)
    self.uglySide.call('ritual_ZN9QSqlField11setReadOnlyEb', readOnly)

  @overload(QMetaType)
  def setMetaType(self, type: QMetaType) -> None:
    """
    Calls Qt's 'void QSqlField::setMetaType(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setMetaType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QSqlField::setMetaType(QMetaType type)
    self.uglySide.call(
        'ritual_ZN9QSqlField11setMetaTypeE9QMetaType', self._valueOf(type),
    )

  @overload(QVariant.Type)
  def setType(self, type: QVariant.Type) -> None:
    """
    Calls Qt's 'void QSqlField::setType(QVariant::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setType

    Parameters
    ----------

    type : QVariant.Type
      Passed on as its number.
    """
    #  void QSqlField::setType(QVariant::Type type)
    self.uglySide.call(
        'ritual_ZN9QSqlField7setTypeEN8QVariant4TypeE', type.value,
    )

  @overload(RequiredStatus)
  def setRequiredStatus(self, status: RequiredStatus) -> None:
    """
    Calls Qt's 'void QSqlField::setRequiredStatus(RequiredStatus status)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setRequiredStatus

    Parameters
    ----------

    status : RequiredStatus
      Passed on as its number.
    """
    #  void QSqlField::setRequiredStatus(RequiredStatus status)
    self.uglySide.call(
        'ritual_ZN9QSqlField17setRequiredStatusENS_14RequiredStatusE',
        status.value,
    )

  @overload(bool)
  def setRequired(self, required: bool) -> None:
    """
    Calls Qt's 'void QSqlField::setRequired(bool required)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setRequired

    Parameters
    ----------

    required : bool
      Passed on as it is.
    """
    #  void QSqlField::setRequired(bool required)
    self.uglySide.call('ritual_ZN9QSqlField11setRequiredEb', required)

  @overload(int)
  def setLength(self, fieldLength: int) -> None:
    """
    Calls Qt's 'void QSqlField::setLength(int fieldLength)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setLength

    Parameters
    ----------

    fieldLength : int
      Passed on as it is.
    """
    #  void QSqlField::setLength(int fieldLength)
    self.uglySide.call('ritual_ZN9QSqlField9setLengthEi', fieldLength)

  @overload(int)
  def setPrecision(self, precision: int) -> None:
    """
    Calls Qt's 'void QSqlField::setPrecision(int precision)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setPrecision

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QSqlField::setPrecision(int precision)
    self.uglySide.call('ritual_ZN9QSqlField12setPrecisionEi', precision)

  @overload(QVariant)
  def setDefaultValue(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QSqlField::setDefaultValue(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setDefaultValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSqlField::setDefaultValue(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN9QSqlField15setDefaultValueERK8QVariant',
        self._valueOf(value),
    )

  @overload(int)
  def setSqlType(self, type: int) -> None:
    """
    Calls Qt's 'void QSqlField::setSqlType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setSqlType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QSqlField::setSqlType(int type)
    self.uglySide.call('ritual_ZN9QSqlField10setSqlTypeEi', type)

  @overload(bool)
  def setGenerated(self, gen: bool) -> None:
    """
    Calls Qt's 'void QSqlField::setGenerated(bool gen)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setGenerated

    Parameters
    ----------

    gen : bool
      Passed on as it is.
    """
    #  void QSqlField::setGenerated(bool gen)
    self.uglySide.call('ritual_ZN9QSqlField12setGeneratedEb', gen)

  @overload(bool)
  def setAutoValue(self, autoVal: bool) -> None:
    """
    Calls Qt's 'void QSqlField::setAutoValue(bool autoVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#setAutoValue

    Parameters
    ----------

    autoVal : bool
      Passed on as it is.
    """
    #  void QSqlField::setAutoValue(bool autoVal)
    self.uglySide.call('ritual_ZN9QSqlField12setAutoValueEb', autoVal)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QSqlField) -> bool:
    """
    Calls Qt's 'bool QSqlField::operator==(const QSqlField &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#operator==

    Parameters
    ----------

    other : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  bool QSqlField::operator==(const QSqlField &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSqlFieldeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSqlField) -> bool:
    """
    Calls Qt's 'bool QSqlField::operator!=(const QSqlField &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#operator!=

    Parameters
    ----------

    other : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  bool QSqlField::operator!=(const QSqlField &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSqlFieldneERKS_', self._valueOf(other),
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
  @overload(str)
  @overload(str, QMetaType)
  @overload(str, QMetaType, str)
  def __init__(
      self,
      fieldName: str = '',
      type: Optional[QMetaType] = None,
      tableName: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlField::QSqlField(const QString
    &fieldName, QMetaType type, const QString &tableName)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#QSqlField

    Parameters
    ----------

    fieldName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    type : Optional[QMetaType]
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own. May be left out, as in Qt: a new 'QMetaType()' is then passed on.

    tableName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSqlField::QSqlField(const QString &fieldName, QMetaType type, const
    #      QString &tableName)
    if type is None:
      from ..QtCore import QMetaType
      type = QMetaType()
    self._noteCreation(QSqlField, lambda: Rituals.call(
        'ritual_ZN9QSqlFieldC1ERK7QString9QMetaTypeS2_',
        fieldName, self._valueOf(type), tableName,
    ))

  @overload(THIS)
  def __init__(self, other: QSqlField) -> None:
    """
    Notes what was given, for Qt's 'QSqlField::QSqlField(const QSqlField
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#QSqlField

    Parameters
    ----------

    other : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.
    """
    #  QSqlField::QSqlField(const QSqlField &other)
    self._noteCreation(QSqlField, lambda: Rituals.call(
        'ritual_ZN9QSqlFieldC1ERKS_', self._valueOf(other),
    ))

  @overload(str, QVariant.Type)
  @overload(str, QVariant.Type, str)
  def __init__(
      self,
      fieldName: str,
      type: QVariant.Type,
      tableName: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlField::QSqlField(const QString
    &fieldName, QVariant::Type type, const QString &tableName)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#QSqlField

    Parameters
    ----------

    fieldName : str
      Passed on as it is: a QString is made of it for the call.

    type : QVariant.Type
      Passed on as its number.

    tableName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSqlField::QSqlField(const QString &fieldName, QVariant::Type type,
    #      const QString &tableName)
    self._noteCreation(QSqlField, lambda: Rituals.call(
        'ritual_ZN9QSqlFieldC1ERK7QStringN8QVariant4TypeES2_',
        fieldName, type.value, tableName,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlField::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#clear
    """
    #  void QSqlField::clear()
    self.uglySide.call('ritual_ZN9QSqlField5clearEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QSqlField::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlfield.html#detach
    """
    #  void QSqlField::detach()
    self.uglySide.call('ritual_ZN9QSqlField6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSqlField::swap(QSqlField &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlField.swap' has no cute function yet. Qt's 'void "
        "QSqlField::swap(QSqlField &other)': takes a type Python has no way "
        "to hand over yet.")
