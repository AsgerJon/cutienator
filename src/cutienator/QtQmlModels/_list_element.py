"""
ListElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ListElement to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import ModelNodeMetaObject


class ListElement(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ListElement: a plain Python object standing in front
  of one C++ ListElement.

  C++ hands a ListElement around as a copy, so every C++ ListElement behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ListElement that has a ritual and that Python can
  call so far, 2 names in all: 'getUid', 'objectCache'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ListElement::~ListElement()': the destructor: Python removes its
    C++ ListElement by it, and has no other use for it.

  What has no ritual
  ------------------

  36 of the 40 functions Qt declares: 25 leans on 'ListElement; 11 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ ListElement is created at the first use, not by
    'ListElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ListElement back gives a copy the ritual made for
    Python, in a new cute ListElement.
  - Each name of Qt's ListElement that has no cute function yet,
    'clearProperty', 'destroy', 'getDateTimeProperty', 'getFunctionProperty',
    'getGuardProperty', 'getListProperty', 'getProperty',
    'getPropertyMemory', 'getQObjectProperty', 'getStringProperty',
    'getUrlProperty', 'getVariantMapProperty', 'setBoolProperty',
    'setBoolPropertyFast', 'setDateTimeProperty', 'setDateTimePropertyFast',
    'setDoubleProperty', 'setDoublePropertyFast', 'setFunctionProperty',
    'setFunctionPropertyFast', 'setJsProperty', 'setListProperty',
    'setListPropertyFast', 'setQObjectProperty', 'setQObjectPropertyFast',
    'setStringProperty', 'setStringPropertyFast', 'setTranslationProperty',
    'setUrlProperty', 'setUrlPropertyFast', 'setVariantMapFast',
    'setVariantMapProperty', 'setVariantProperty', 'sync', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside ListElement, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ObjectIndestructible(CuteNum):
    """
    The enum 'ListElement::ObjectIndestructible' of Qt, with the 2 names Qt
    gives in it.
    """

    Indestructible = Kee[int](1)
    ExplicitlySet = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ListElement'

  #  Qt's '~ListElement()'. Naming it makes this a value class: Python owns
  #  every C++ ListElement behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11ListElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getUid(self) -> int:
    """
    Calls Qt's 'int ListElement::getUid() const'.

    Qt's own words: https://doc.qt.io/qt-6/listelement.html#getUid
    """
    #  int ListElement::getUid() const
    return self.uglySide.call('ritual_ZNK11ListElement6getUidEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, existingUid: int) -> None:
    """
    Notes what was given, for Qt's 'ListElement::ListElement(int
    existingUid)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/listelement.html#ListElement

    Parameters
    ----------

    existingUid : int
      Passed on as it is.
    """
    #  ListElement::ListElement(int existingUid)
    self._noteCreation(ListElement, lambda: Rituals.call(
        'ritual_ZN11ListElementC1Ei', existingUid,
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

  def objectCache(self) -> Optional[ModelNodeMetaObject]:
    """
    Calls Qt's 'ModelNodeMetaObject *ListElement::objectCache()'.

    Qt's own words: https://doc.qt.io/qt-6/listelement.html#objectCache

    Returns
    -------

    Optional[ModelNodeMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ModelNodeMetaObject *ListElement::objectCache()
    address = self.uglySide.call('ritual_ZN11ListElement11objectCacheEv')
    from . import ModelNodeMetaObject
    return ModelNodeMetaObject._cuteAt(address)

  @staticmethod
  def clearProperty(*__, **_) -> Never:
    """
    Qt's 'void ListElement::clearProperty(const ListLayout::Role &role)':
    leans on 'ListElement::setVariantMapProperty(ListLayout::Role const&,
    QMap<QString, QVariant>*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.clearProperty' has no cute function yet. Qt's 'void "
        "ListElement::clearProperty(const ListLayout::Role &role)': leans "
        "on 'ListElement::setVariantMapProperty(ListLayout::Role const&, "
        "QMap<QString, QVariant>*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    Qt's 'void ListElement::destroy(ListLayout *layout)': leans on
    'ListElement::ListElement()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.destroy' has no cute function yet. Qt's 'void "
        "ListElement::destroy(ListLayout *layout)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def getDateTimeProperty(*__, **_) -> Never:
    """
    Qt's 'QDateTime *ListElement::getDateTimeProperty(const ListLayout::Role
    &role)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.getDateTimeProperty' has no cute function yet. Qt's "
        "'QDateTime *ListElement::getDateTimeProperty(const "
        "ListLayout::Role &role)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def getFunctionProperty(*__, **_) -> Never:
    """
    Qt's 'QJSValue *ListElement::getFunctionProperty(const ListLayout::Role
    &role)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.getFunctionProperty' has no cute function yet. Qt's "
        "'QJSValue *ListElement::getFunctionProperty(const ListLayout::Role "
        "&role)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'isMemoryUsed'.")

  @staticmethod
  def getGuardProperty(*__, **_) -> Never:
    """
    Qt's 'QV4::PersistentValue *ListElement::getGuardProperty(const
    ListLayout::Role &role)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.getGuardProperty' has no cute function yet. Qt's "
        "'QV4::PersistentValue *ListElement::getGuardProperty(const "
        "ListLayout::Role &role)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getListProperty(*__, **_) -> Never:
    """
    Qt's 'ListModel *ListElement::getListProperty(const ListLayout::Role
    &role)': leans on 'ListElement::ListElement()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.getListProperty' has no cute function yet. Qt's "
        "'ListModel *ListElement::getListProperty(const ListLayout::Role "
        "&role)': leans on 'ListElement::ListElement()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getProperty(*__, **_) -> Never:
    """
    Qt's 'QVariant ListElement::getProperty(const ListLayout::Role &role,
    const QQmlListModel *owner, QV4::ExecutionEngine *eng)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.getProperty' has no cute function yet. Qt's 'QVariant "
        "ListElement::getProperty(const ListLayout::Role &role, const "
        "QQmlListModel *owner, QV4::ExecutionEngine *eng)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def getPropertyMemory(*__, **_) -> Never:
    """
    Qt's 'char *ListElement::getPropertyMemory(const ListLayout::Role
    &role)': leans on 'ListElement::ListElement()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.getPropertyMemory' has no cute function yet. Qt's "
        "'char *ListElement::getPropertyMemory(const ListLayout::Role "
        "&role)': leans on 'ListElement::ListElement()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getQObjectProperty(*__, **_) -> Never:
    """
    Qt's 'QV4::QObjectWrapper *ListElement::getQObjectProperty(const
    ListLayout::Role &role)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.getQObjectProperty' has no cute function yet. Qt's "
        "'QV4::QObjectWrapper *ListElement::getQObjectProperty(const "
        "ListLayout::Role &role)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getStringProperty(*__, **_) -> Never:
    """
    Qt's 'StringOrTranslation *ListElement::getStringProperty(const
    ListLayout::Role &role)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.getStringProperty' has no cute function yet. Qt's "
        "'StringOrTranslation *ListElement::getStringProperty(const "
        "ListLayout::Role &role)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def getUrlProperty(*__, **_) -> Never:
    """
    Qt's 'QUrl *ListElement::getUrlProperty(const ListLayout::Role &role)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.getUrlProperty' has no cute function yet. Qt's 'QUrl "
        "*ListElement::getUrlProperty(const ListLayout::Role &role)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isMemoryUsed'.")

  @staticmethod
  def getVariantMapProperty(*__, **_) -> Never:
    """
    Qt's 'QVariantMap *ListElement::getVariantMapProperty(const
    ListLayout::Role &role)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.getVariantMapProperty' has no cute function yet. Qt's "
        "'QVariantMap *ListElement::getVariantMapProperty(const "
        "ListLayout::Role &role)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def setBoolProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setBoolProperty(const ListLayout::Role &role, bool
    b)': leans on 'ListElement::ListElement()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setBoolProperty' has no cute function yet. Qt's 'int "
        "ListElement::setBoolProperty(const ListLayout::Role &role, bool "
        "b)': leans on 'ListElement::ListElement()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setBoolPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setBoolPropertyFast(const ListLayout::Role &role,
    bool b)': leans on 'ListElement::ListElement()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setBoolPropertyFast' has no cute function yet. Qt's "
        "'void ListElement::setBoolPropertyFast(const ListLayout::Role "
        "&role, bool b)': leans on 'ListElement::ListElement()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDateTimeProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setDateTimeProperty(const ListLayout::Role &role,
    const QDateTime &dt)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.setDateTimeProperty' has no cute function yet. Qt's "
        "'int ListElement::setDateTimeProperty(const ListLayout::Role "
        "&role, const QDateTime &dt)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def setDateTimePropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setDateTimePropertyFast(const ListLayout::Role
    &role, const QDateTime &dt)': leans on 'ListElement::ListElement()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setDateTimePropertyFast' has no cute function yet. "
        "Qt's 'void ListElement::setDateTimePropertyFast(const "
        "ListLayout::Role &role, const QDateTime &dt)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setDoubleProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setDoubleProperty(const ListLayout::Role &role,
    double n)': leans on 'ListElement::ListElement()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setDoubleProperty' has no cute function yet. Qt's "
        "'int ListElement::setDoubleProperty(const ListLayout::Role &role, "
        "double n)': leans on 'ListElement::ListElement()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setDoublePropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setDoublePropertyFast(const ListLayout::Role
    &role, double n)': leans on 'ListElement::ListElement()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setDoublePropertyFast' has no cute function yet. Qt's "
        "'void ListElement::setDoublePropertyFast(const ListLayout::Role "
        "&role, double n)': leans on 'ListElement::ListElement()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setFunctionProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setFunctionProperty(const ListLayout::Role &role,
    const QJSValue &f)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.setFunctionProperty' has no cute function yet. Qt's "
        "'int ListElement::setFunctionProperty(const ListLayout::Role "
        "&role, const QJSValue &f)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def setFunctionPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setFunctionPropertyFast(const ListLayout::Role
    &role, const QJSValue &f)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setFunctionPropertyFast' has no cute function yet. "
        "Qt's 'void ListElement::setFunctionPropertyFast(const "
        "ListLayout::Role &role, const QJSValue &f)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setJsProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setJsProperty(const ListLayout::Role &role, const
    QV4::Value &d, QV4::ExecutionEngine *eng)': leans on
    'ListElement::setVariantMapProperty(ListLayout::Role const&,
    QMap<QString, QVariant>*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setJsProperty' has no cute function yet. Qt's 'int "
        "ListElement::setJsProperty(const ListLayout::Role &role, const "
        "QV4::Value &d, QV4::ExecutionEngine *eng)': leans on "
        "'ListElement::setVariantMapProperty(ListLayout::Role const&, "
        "QMap<QString, QVariant>*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setListProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setListProperty(const ListLayout::Role &role,
    ListModel *m)': leans on 'ListElement::ListElement()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'ListElement.setListProperty' has no cute function yet. Qt's 'int "
        "ListElement::setListProperty(const ListLayout::Role &role, "
        "ListModel *m)': leans on 'ListElement::ListElement()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setListPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setListPropertyFast(const ListLayout::Role &role,
    ListModel *m)': leans on 'ListElement::ListElement()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'ListElement.setListPropertyFast' has no cute function yet. Qt's "
        "'void ListElement::setListPropertyFast(const ListLayout::Role "
        "&role, ListModel *m)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setQObjectProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setQObjectProperty(const ListLayout::Role &role,
    QV4::QObjectWrapper *o)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setQObjectProperty' has no cute function yet. Qt's "
        "'int ListElement::setQObjectProperty(const ListLayout::Role &role, "
        "QV4::QObjectWrapper *o)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setQObjectPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setQObjectPropertyFast(const ListLayout::Role
    &role, QV4::QObjectWrapper *o)': leans on 'ListElement::ListElement()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setQObjectPropertyFast' has no cute function yet. "
        "Qt's 'void ListElement::setQObjectPropertyFast(const "
        "ListLayout::Role &role, QV4::QObjectWrapper *o)': leans on "
        "'ListElement::ListElement()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setStringProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setStringProperty(const ListLayout::Role &role,
    const QString &s)': leans on 'ListElement::ListElement()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setStringProperty' has no cute function yet. Qt's "
        "'int ListElement::setStringProperty(const ListLayout::Role &role, "
        "const QString &s)': leans on 'ListElement::ListElement()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setStringPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setStringPropertyFast(const ListLayout::Role
    &role, const QString &s)': leans on 'ListElement::ListElement()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setStringPropertyFast' has no cute function yet. Qt's "
        "'void ListElement::setStringPropertyFast(const ListLayout::Role "
        "&role, const QString &s)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setTranslationProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setTranslationProperty(const ListLayout::Role
    &role, const QV4::CompiledData::Binding *b)': leans on
    'ListElement::ListElement()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setTranslationProperty' has no cute function yet. "
        "Qt's 'int ListElement::setTranslationProperty(const "
        "ListLayout::Role &role, const QV4::CompiledData::Binding *b)': "
        "leans on 'ListElement::ListElement()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setUrlProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setUrlProperty(const ListLayout::Role &role, const
    QUrl &url)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.setUrlProperty' has no cute function yet. Qt's 'int "
        "ListElement::setUrlProperty(const ListLayout::Role &role, const "
        "QUrl &url)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'isMemoryUsed'.")

  @staticmethod
  def setUrlPropertyFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setUrlPropertyFast(const ListLayout::Role &role,
    const QUrl &url)': leans on 'ListElement::ListElement()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setUrlPropertyFast' has no cute function yet. Qt's "
        "'void ListElement::setUrlPropertyFast(const ListLayout::Role "
        "&role, const QUrl &url)': leans on 'ListElement::ListElement()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setVariantMapFast(*__, **_) -> Never:
    """
    Qt's 'void ListElement::setVariantMapFast(const ListLayout::Role &role,
    QV4::Object *o)': leans on 'ListElement::ListElement()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setVariantMapFast' has no cute function yet. Qt's "
        "'void ListElement::setVariantMapFast(const ListLayout::Role &role, "
        "QV4::Object *o)': leans on 'ListElement::ListElement()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setVariantMapProperty(*__, **_) -> Never:
    """
    - Qt's 'int ListElement::setVariantMapProperty(const ListLayout::Role
      &role, QV4::Object *o)': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: use of undeclared
      identifier 'isMemoryUsed'.
    - Qt's 'int ListElement::setVariantMapProperty(const ListLayout::Role
      &role, QVariantMap *m)': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: use of undeclared
      identifier 'isMemoryUsed'.
    """
    raise NotImplementedError(
        "'ListElement.setVariantMapProperty' has no cute function yet. Qt's "
        "'int ListElement::setVariantMapProperty(const ListLayout::Role "
        "&role, QV4::Object *o)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isMemoryUsed'. Qt's 'int "
        "ListElement::setVariantMapProperty(const ListLayout::Role &role, "
        "QVariantMap *m)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'isMemoryUsed'.")

  @staticmethod
  def setVariantProperty(*__, **_) -> Never:
    """
    Qt's 'int ListElement::setVariantProperty(const ListLayout::Role &role,
    const QVariant &d)': leans on
    'ListElement::setVariantMapProperty(ListLayout::Role const&,
    QMap<QString, QVariant>*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.setVariantProperty' has no cute function yet. Qt's "
        "'int ListElement::setVariantProperty(const ListLayout::Role &role, "
        "const QVariant &d)': leans on "
        "'ListElement::setVariantMapProperty(ListLayout::Role const&, "
        "QMap<QString, QVariant>*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'QList<int> ListElement::sync(ListElement *src, ListLayout
    *srcLayout, ListElement *target, ListLayout *targetLayout)': leans on
    'ListElement::setVariantMapProperty(ListLayout::Role const&,
    QMap<QString, QVariant>*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ListElement.sync' has no cute function yet. Qt's 'QList<int> "
        "ListElement::sync(ListElement *src, ListLayout *srcLayout, "
        "ListElement *target, ListLayout *targetLayout)': leans on "
        "'ListElement::setVariantMapProperty(ListLayout::Role const&, "
        "QMap<QString, QVariant>*)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
