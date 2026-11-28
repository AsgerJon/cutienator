"""
QQmlJS::ContextualTypes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJS::ContextualTypes to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ContextualTypes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::ContextualTypes: a plain Python object
  standing in front of one C++ QQmlJS::ContextualTypes.

  C++ hands a QQmlJS::ContextualTypes around as a copy, so every C++
  QQmlJS::ContextualTypes behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::ContextualTypes that has a ritual and that
  Python can call so far, 12 names in all: 'context', 'hasType', 'type',
  'setType', 'setFileSelectedType', 'clearType', 'isNullType', 'addTypes',
  'hasFileSelectors', 'currentFileSelector', 'setCurrentFileSelector',
  'clearTypes'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::ContextualTypes::ContextualTypes(CompileContext context,
    const QHash<QString, ContextualType> &types, const
    QMultiHash<QQmlJSScope::ConstPtr, QString> &names, const
    QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJS::ContextualTypes::arrayType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QString QQmlJS::ContextualTypes::name(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QHash<QString, ContextualType>
    &QQmlJS::ContextualTypes::types() const': gives a type Python has no way
    to take yet.
  - Qt's 'FileSelectorInfo QQmlJS::ContextualTypes::fileSelectorInfoFor(const
    QQmlJSScope::ConstPtr &scope) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
    &QQmlJS::ContextualTypes::names() const': gives a type Python has no way
    to take yet.
  - Qt's 'std::optional<ContextualType>
    QQmlJS::ContextualTypes::fileSelectedTypeFor(const QString &name, const
    QString &selector) const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJS::ContextualTypes::~ContextualTypes()': the destructor:
    Python removes its C++ QQmlJS::ContextualTypes by it, and has no other
    use for it.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlJS::ContextualTypes is created at the first use, not by
    'QQmlJS::ContextualTypes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::ContextualTypes back gives a copy the ritual
    made for Python, in a new cute QQmlJS::ContextualTypes.
  - Each name of Qt's QQmlJS::ContextualTypes that has no cute function yet,
    '__init__', 'arrayType', 'fileSelectedTypeFor',
    'fileSelectionsEqualRange', 'fileSelectorInfoFor', 'name', 'names',
    'types', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlJS::ContextualTypes, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CompileContext(CuteNum):
    """
    The enum 'QQmlJS::ContextualTypes::CompileContext' of Qt, with the 2
    names Qt gives in it.
    """

    INTERNAL = Kee[int](0)
    QML = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::ContextualTypes'

  #  Qt's '~QQmlJS::ContextualTypes()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJS::ContextualTypes behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS15ContextualTypesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def context(self) -> CompileContext:
    """
    Calls Qt's 'CompileContext QQmlJS::ContextualTypes::context() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#context

    Returns
    -------

    CompileContext
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CompileContext(number)'
      gives.
    """
    #  CompileContext QQmlJS::ContextualTypes::context() const
    return ContextualTypes.CompileContext(self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes7contextEv',
    ))

  @overload(str)
  def hasType(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJS::ContextualTypes::hasType(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#hasType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJS::ContextualTypes::hasType(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes7hasTypeERK7QString', name,
    )

  @overload(str)
  def type(self, name: str) -> QQmlJS.ContextualType:
    """
    Calls Qt's 'ContextualType QQmlJS::ContextualTypes::type(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#type

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJS.ContextualType
      A new cute QQmlJS::ContextualType around the copy Qt gave back. Python
      owns it.
    """
    #  ContextualType QQmlJS::ContextualTypes::type(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes4typeERK7QString', name,
    )
    return QQmlJS.ContextualType._cuteOwning(address)

  @overload(str)
  def isNullType(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJS::ContextualTypes::isNullType(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#isNullType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJS::ContextualTypes::isNullType(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes10isNullTypeERK7QString', name,
    )

  def hasFileSelectors(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::ContextualTypes::hasFileSelectors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#hasFileSelectors
    """
    #  bool QQmlJS::ContextualTypes::hasFileSelectors() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes16hasFileSelectorsEv',
    )

  def currentFileSelector(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::ContextualTypes::currentFileSelector()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#currentFileSelector

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::ContextualTypes::currentFileSelector() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS15ContextualTypes19currentFileSelectorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, WAIT['QQmlJS.ContextualType'])
  def setType(self, name: str, type: QQmlJS.ContextualType) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::setType(const QString &name,
    const ContextualType &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#setType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    type : QQmlJS.ContextualType
      Passed on as a value: Qt reads the C++ QQmlJS::ContextualType, which
      stays Python's own.
    """
    #  void QQmlJS::ContextualTypes::setType(const QString &name, const
    #      ContextualType &type)
    self.uglySide.call(
        'ritual_ZN6QQmlJS15ContextualTypes7setTypeERK7QStringRKNS_14Context'
        'ualTypeE',
        name, self._valueOf(type),
    )

  @overload(str, str, WAIT['QQmlJS.ContextualType'])
  def setFileSelectedType(
      self,
      fileSelector: str,
      name: str,
      type: QQmlJS.ContextualType,
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::setFileSelectedType(const
    QString &fileSelector, const QString &name, const ContextualType &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#setFileSelectedType

    Parameters
    ----------

    fileSelector : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    type : QQmlJS.ContextualType
      Passed on as a value: Qt reads the C++ QQmlJS::ContextualType, which
      stays Python's own.
    """
    #  void QQmlJS::ContextualTypes::setFileSelectedType(const QString
    #      &fileSelector, const QString &name, const ContextualType &type)
    self.uglySide.call(
        'ritual_ZN6QQmlJS15ContextualTypes19setFileSelectedTypeERK7QStringS'
        '3_RKNS_14ContextualTypeE',
        fileSelector, name, self._valueOf(type),
    )

  @overload(str)
  def setCurrentFileSelector(self, selector: str) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::setCurrentFileSelector(const
    QString &selector)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#setCurrentFileSelector

    Parameters
    ----------

    selector : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::ContextualTypes::setCurrentFileSelector(const QString
    #      &selector)
    self.uglySide.call(
        'ritual_ZN6QQmlJS15ContextualTypes22setCurrentFileSelectorERK7QStri'
        'ng',
        selector,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::ContextualTypes::ContextualTypes(CompileContext context,
    const QHash<QString, ContextualType> &types, const
    QMultiHash<QQmlJSScope::ConstPtr, QString> &names, const
    QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.__init__' has no cute function yet. Qt's "
        "'QQmlJS::ContextualTypes::ContextualTypes(CompileContext context, "
        "const QHash<QString, ContextualType> &types, const "
        "QMultiHash<QQmlJSScope::ConstPtr, QString> &names, const "
        "QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way "
        "to hand over yet.")

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
  def clearType(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::clearType(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#clearType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJS::ContextualTypes::clearType(const QString &name)
    self.uglySide.call(
        'ritual_ZN6QQmlJS15ContextualTypes9clearTypeERK7QString', name,
    )

  @overload(THIS)
  def addTypes(self, types: ContextualTypes) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::addTypes(const ContextualTypes
    &types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#addTypes

    Parameters
    ----------

    types : ContextualTypes
      Passed on as a value: Qt reads the C++ QQmlJS::ContextualTypes, which
      stays Python's own.
    """
    #  void QQmlJS::ContextualTypes::addTypes(const ContextualTypes &types)
    self.uglySide.call(
        'ritual_ZN6QQmlJS15ContextualTypes8addTypesERKS0_',
        self._valueOf(types),
    )

  def clearTypes(self) -> None:
    """
    Calls Qt's 'void QQmlJS::ContextualTypes::clearTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-contextualtypes.html#clearTypes
    """
    #  void QQmlJS::ContextualTypes::clearTypes()
    self.uglySide.call('ritual_ZN6QQmlJS15ContextualTypes10clearTypesEv')

  @staticmethod
  def arrayType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJS::ContextualTypes::arrayType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.arrayType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJS::ContextualTypes::arrayType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def fileSelectedTypeFor(*__, **_) -> Never:
    """
    Qt's 'std::optional<ContextualType>
    QQmlJS::ContextualTypes::fileSelectedTypeFor(const QString &name, const
    QString &selector) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.fileSelectedTypeFor' has no cute function "
        "yet. Qt's 'std::optional<ContextualType> "
        "QQmlJS::ContextualTypes::fileSelectedTypeFor(const QString &name, "
        "const QString &selector) const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def fileSelectionsEqualRange(*__, **_) -> Never:
    """
    Qt's 'std::pair<const_iterator, const_iterator>
    QQmlJS::ContextualTypes::fileSelectionsEqualRange(const QString &name)
    const': the compiler refuses its ritual as it would be written here: use
    of undeclared identifier 'const_iterator'.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.fileSelectionsEqualRange' has no cute "
        "function yet. Qt's 'std::pair<const_iterator, const_iterator> "
        "QQmlJS::ContextualTypes::fileSelectionsEqualRange(const QString "
        "&name) const': the compiler refuses its ritual as it would be "
        "written here: use of undeclared identifier 'const_iterator'.")

  @staticmethod
  def fileSelectorInfoFor(*__, **_) -> Never:
    """
    Qt's 'FileSelectorInfo QQmlJS::ContextualTypes::fileSelectorInfoFor(const
    QQmlJSScope::ConstPtr &scope) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.fileSelectorInfoFor' has no cute function "
        "yet. Qt's 'FileSelectorInfo "
        "QQmlJS::ContextualTypes::fileSelectorInfoFor(const "
        "QQmlJSScope::ConstPtr &scope) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def name(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJS::ContextualTypes::name(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.name' has no cute function yet. Qt's "
        "'QString QQmlJS::ContextualTypes::name(const QQmlJSScope::ConstPtr "
        "&type) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def names(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
    &QQmlJS::ContextualTypes::names() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.names' has no cute function yet. Qt's "
        "'const QMultiHash<QQmlJSScope::ConstPtr, QString> "
        "&QQmlJS::ContextualTypes::names() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def types(*__, **_) -> Never:
    """
    Qt's 'const QHash<QString, ContextualType>
    &QQmlJS::ContextualTypes::types() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.ContextualTypes.types' has no cute function yet. Qt's "
        "'const QHash<QString, ContextualType> "
        "&QQmlJS::ContextualTypes::types() const': gives a type Python has "
        "no way to take yet.")
