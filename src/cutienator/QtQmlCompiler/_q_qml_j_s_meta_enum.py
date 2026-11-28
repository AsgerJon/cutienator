"""
QQmlJSMetaEnum binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSMetaEnum to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QHash, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlJSMetaEnum(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSMetaEnum: a plain Python object standing in
  front of one C++ QQmlJSMetaEnum.

  C++ hands a QQmlJSMetaEnum around as a copy, so every C++ QQmlJSMetaEnum
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSMetaEnum that has a ritual and that Python can
  call so far, 23 names in all: 'isValid', 'name', 'setName', 'alias',
  'setAlias', 'isFlag', 'setIsFlag', 'isScoped', 'setIsScoped', 'isQml',
  'setIsQml', 'addKey', 'keys', 'addValue', 'hasValues', 'value', 'hasKey',
  'typeName', 'setTypeName', 'lineNumber', 'setLineNumber', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> QQmlJSMetaEnum::values() const': gives a type Python has
    no way to take yet.
  - Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaEnum::type() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQmlJSMetaEnum::setType(const QSharedPointer<const
    QQmlJSScope> &type)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSMetaEnum::~QQmlJSMetaEnum()': the destructor: Python removes
    its C++ QQmlJSMetaEnum by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSMetaEnum is created at the first use, not by
    'QQmlJSMetaEnum(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSMetaEnum back gives a copy the ritual made for
    Python, in a new cute QQmlJSMetaEnum.
  - Each name of Qt's QQmlJSMetaEnum that has no cute function yet,
    'setType', 'type', 'values', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSMetaEnum'

  #  Qt's '~QQmlJSMetaEnum()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSMetaEnum behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QQmlJSMetaEnumD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#isValid
    """
    #  bool QQmlJSMetaEnum::isValid() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum7isValidEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaEnum::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaEnum::name() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum4nameEv')

  def alias(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaEnum::alias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#alias

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaEnum::alias() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum5aliasEv')

  def isFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::isFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#isFlag
    """
    #  bool QQmlJSMetaEnum::isFlag() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum6isFlagEv')

  def isScoped(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::isScoped() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#isScoped
    """
    #  bool QQmlJSMetaEnum::isScoped() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum8isScopedEv')

  def isQml(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::isQml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#isQml
    """
    #  bool QQmlJSMetaEnum::isQml() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum5isQmlEv')

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSMetaEnum::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSMetaEnum::keys() const
    address = self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum4keysEv')
    return QStringList._cuteOwning(address)

  def hasValues(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::hasValues() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#hasValues
    """
    #  bool QQmlJSMetaEnum::hasValues() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum9hasValuesEv')

  @overload(str)
  def value(self, key: str) -> int:
    """
    Calls Qt's 'int QQmlJSMetaEnum::value(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QQmlJSMetaEnum::value(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlJSMetaEnum5valueERK7QString', key,
    )

  @overload(str)
  def hasKey(self, key: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaEnum::hasKey(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#hasKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSMetaEnum::hasKey(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlJSMetaEnum6hasKeyERK7QString', key,
    )

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaEnum::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaEnum::typeName() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum8typeNameEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QQmlJSMetaEnum::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#lineNumber
    """
    #  int QQmlJSMetaEnum::lineNumber() const
    return self.uglySide.call('ritual_ZNK14QQmlJSMetaEnum10lineNumberEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaEnum::setName(const QString &name)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum7setNameERK7QString', name)

  @overload(str)
  def setAlias(self, alias: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setAlias(const QString &alias)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setAlias

    Parameters
    ----------

    alias : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaEnum::setAlias(const QString &alias)
    self.uglySide.call(
        'ritual_ZN14QQmlJSMetaEnum8setAliasERK7QString', alias,
    )

  @overload(bool)
  def setIsFlag(self, isFlag: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setIsFlag(bool isFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setIsFlag

    Parameters
    ----------

    isFlag : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaEnum::setIsFlag(bool isFlag)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum9setIsFlagEb', isFlag)

  @overload(bool)
  def setIsScoped(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setIsScoped(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setIsScoped

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaEnum::setIsScoped(bool v)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum11setIsScopedEb', v)

  @overload(bool)
  def setIsQml(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setIsQml(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setIsQml

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaEnum::setIsQml(bool v)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum8setIsQmlEb', v)

  @overload(str)
  def setTypeName(self, typeName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setTypeName(const QString &typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setTypeName

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaEnum::setTypeName(const QString &typeName)
    self.uglySide.call(
        'ritual_ZN14QQmlJSMetaEnum11setTypeNameERK7QString', typeName,
    )

  @overload(int)
  def setLineNumber(self, lineNumber: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::setLineNumber(int lineNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#setLineNumber

    Parameters
    ----------

    lineNumber : int
      Passed on as it is.
    """
    #  void QQmlJSMetaEnum::setLineNumber(int lineNumber)
    self.uglySide.call(
        'ritual_ZN14QQmlJSMetaEnum13setLineNumberEi', lineNumber,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlJSMetaEnum) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#operator==

    Parameters
    ----------

    b : QQmlJSMetaEnum
      Passed on as a value: Qt reads the C++ QQmlJSMetaEnum, which stays
      Python's own.
    """
    #  bool operator==(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum &b)
    return Rituals.call(
        'ritual_ZeqRK14QQmlJSMetaEnumS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QQmlJSMetaEnum) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#operator!=

    Parameters
    ----------

    b : QQmlJSMetaEnum
      Passed on as a value: Qt reads the C++ QQmlJSMetaEnum, which stays
      Python's own.
    """
    #  bool operator!=(const QQmlJSMetaEnum &a, const QQmlJSMetaEnum &b)
    return Rituals.call(
        'ritual_ZneRK14QQmlJSMetaEnumS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    Notes what was given, for Qt's 'QQmlJSMetaEnum::QQmlJSMetaEnum()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#QQmlJSMetaEnum
    """
    #  QQmlJSMetaEnum::QQmlJSMetaEnum()
    self._noteCreation(QQmlJSMetaEnum, lambda: Rituals.call(
        'ritual_ZN14QQmlJSMetaEnumC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QQmlJSMetaEnum::QQmlJSMetaEnum(QString
    name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#QQmlJSMetaEnum

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJSMetaEnum::QQmlJSMetaEnum(QString name)
    self._noteCreation(QQmlJSMetaEnum, lambda: Rituals.call(
        'ritual_ZN14QQmlJSMetaEnumC1E7QString', name,
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

  @overload(str)
  def addKey(self, key: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::addKey(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#addKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaEnum::addKey(const QString &key)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum6addKeyERK7QString', key)

  @overload(int)
  def addValue(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaEnum::addValue(int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetaenum.html#addValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSMetaEnum::addValue(int value)
    self.uglySide.call('ritual_ZN14QQmlJSMetaEnum8addValueEi', value)

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaEnum::setType(const QSharedPointer<const
    QQmlJSScope> &type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaEnum.setType' has no cute function yet. Qt's 'void "
        "QQmlJSMetaEnum::setType(const QSharedPointer<const QQmlJSScope> "
        "&type)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def type(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaEnum::type() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaEnum.type' has no cute function yet. Qt's "
        "'QSharedPointer<const QQmlJSScope> QQmlJSMetaEnum::type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def values(*__, **_) -> Never:
    """
    Qt's 'QList<int> QQmlJSMetaEnum::values() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaEnum.values' has no cute function yet. Qt's 'QList<int> "
        "QQmlJSMetaEnum::values() const': gives a type Python has no way to "
        "take yet.")


#  Qt's 'QHash<QString, QQmlJSMetaEnum>': the QHash from text to
#  QQmlJSMetaEnum, which 'QHash[str, QQmlJSMetaEnum]' gives. It is completed
#  here, in the file of the class of its values.
QHash.createKind(
    str, QQmlJSMetaEnum, 'value',
    make='ritual_map_make_QHash_QString_QQmlJSMetaEnum',
    put='ritual_map_put_QHash_QString_QQmlJSMetaEnum',
    size='ritual_map_size_QHash_QString_QQmlJSMetaEnum',
    key='ritual_map_key_QHash_QString_QQmlJSMetaEnum',
    value='ritual_map_value_QHash_QString_QQmlJSMetaEnum',
    has='ritual_map_has_QHash_QString_QQmlJSMetaEnum',
    get='ritual_map_get_QHash_QString_QQmlJSMetaEnum',
    drop='ritual_map_drop_QHash_QString_QQmlJSMetaEnum',
)
