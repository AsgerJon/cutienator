"""
QQmlDelegateModelAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlDelegateModel


class QQmlDelegateModelAttached(QObject):
  """
  The cute side of Qt's QQmlDelegateModelAttached: a plain Python object
  standing in front of one C++ QQmlDelegateModelAttached.

  It is built on the cute 'QObject', as Qt's QQmlDelegateModelAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelAttached that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'inPersistedItems',
  'persistedItemsIndex', 'inItems', 'itemsIndex', 'model', 'groups',
  'isUnresolved', 'groupsChanged', 'unresolvedChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDelegateModelAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlDelegateModelAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDelegateModelAttached::~QQmlDelegateModelAttached()': the
    destructor: Python never removes a C++ QQmlDelegateModelAttached.

  What has no ritual
  ------------------

  13 of the 26 functions Qt declares: 5 leans on 'QQmlDelegateModelAttached;
  5 leans on 'QQmlListCompositor; 2 not a gap; 1 cannot be called and cannot
  be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlDelegateModelAttached is created at the first use, not by
    'QQmlDelegateModelAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDelegateModelAttached.
  - Qt tells when it has removed the C++ QQmlDelegateModelAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlDelegateModelAttached that has no cute function
    yet, '__init__', 'emitChanges', 'emitUnresolvedChanged',
    'resetCurrentIndex', 'setCacheItem', 'setGroups', 'setInGroup',
    'setInItems', 'setInPersistedItems', holds a function that raises
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
  __qt_class__ = 'QQmlDelegateModelAttached'

  #  A C++ QQmlDelegateModelAttached Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDelegateModelAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDelegateModelAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inPersistedItems(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelAttached::inPersistedItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#inPersistedItems
    """
    #  bool QQmlDelegateModelAttached::inPersistedItems() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached16inPersistedItemsEv',
    )

  def persistedItemsIndex(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelAttached::persistedItemsIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#persistedItemsIndex
    """
    #  int QQmlDelegateModelAttached::persistedItemsIndex() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached19persistedItemsIndexEv',
    )

  def inItems(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelAttached::inItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#inItems
    """
    #  bool QQmlDelegateModelAttached::inItems() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached7inItemsEv',
    )

  def itemsIndex(self) -> int:
    """
    Calls Qt's 'int QQmlDelegateModelAttached::itemsIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#itemsIndex
    """
    #  int QQmlDelegateModelAttached::itemsIndex() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached10itemsIndexEv',
    )

  def model(self) -> Optional[QQmlDelegateModel]:
    """
    Calls Qt's 'QQmlDelegateModel *QQmlDelegateModelAttached::model() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#model

    Returns
    -------

    Optional[QQmlDelegateModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModel *QQmlDelegateModelAttached::model() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached5modelEv',
    )
    from . import QQmlDelegateModel
    return QQmlDelegateModel._cuteAt(address)

  def groups(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDelegateModelAttached::groups() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#groups

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDelegateModelAttached::groups() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached6groupsEv',
    )
    return QStringList._cuteOwning(address)

  def isUnresolved(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelegateModelAttached::isUnresolved() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#isUnresolved
    """
    #  bool QQmlDelegateModelAttached::isUnresolved() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDelegateModelAttached12isUnresolvedEv',
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQmlDelegateModelAttached::QQmlDelegateModelAttached(QObject
      *parent)': leans on
      'QQmlDelegateModelAttached::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'QQmlDelegateModelAttached::QQmlDelegateModelAttached(
      QQmlDelegateModelItem *cacheItem, QObject *parent)': leans on
      'QQmlDelegateModelAttached::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.__init__' has no cute function yet. "
        "Qt's 'QQmlDelegateModelAttached::QQmlDelegateModelAttached(QObject "
        "*parent)': leans on "
        "'QQmlDelegateModelAttached::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QQmlDelegateModelAttached::QQmlDelegateModelAttached(QQmlDelegateM"
        "odelItem *cacheItem, QObject *parent)': leans on "
        "'QQmlDelegateModelAttached::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def groupsChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelAttached::groupsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#groupsChanged
    """
    #  void QQmlDelegateModelAttached::groupsChanged()
    self.uglySide.call(
        'ritual_ZN25QQmlDelegateModelAttached13groupsChangedEv',
    )

  def unresolvedChanged(self) -> None:
    """
    Calls Qt's 'void QQmlDelegateModelAttached::unresolvedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelattached.html#unresolvedChanged
    """
    #  void QQmlDelegateModelAttached::unresolvedChanged()
    self.uglySide.call(
        'ritual_ZN25QQmlDelegateModelAttached17unresolvedChangedEv',
    )

  @staticmethod
  def emitChanges(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::emitChanges()': leans on
    'QQmlDelegateModelAttached::groupsChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.emitChanges' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelAttached::emitChanges()': leans on "
        "'QQmlDelegateModelAttached::groupsChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emitUnresolvedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::emitUnresolvedChanged()': leans on
    'QQmlDelegateModelAttached::unresolvedChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.emitUnresolvedChanged' has no cute "
        "function yet. Qt's 'void "
        "QQmlDelegateModelAttached::emitUnresolvedChanged()': leans on "
        "'QQmlDelegateModelAttached::unresolvedChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def resetCurrentIndex(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::resetCurrentIndex()': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.resetCurrentIndex' has no cute function "
        "yet. Qt's 'void QQmlDelegateModelAttached::resetCurrentIndex()': "
        "leans on 'QQmlListCompositor::find(QQmlListCompositor::Group, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def setCacheItem(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::setCacheItem(QQmlDelegateModelItem
    *item)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.setCacheItem' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelAttached::setCacheItem(QQmlDelegateModelItem "
        "*item)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setGroups(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::setGroups(const QStringList
    &groups)': leans on 'QQmlListCompositor::find(QQmlListCompositor::Group,
    int)', which Qt's source does not mark for use from outside Qt and has no
    code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.setGroups' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelAttached::setGroups(const QStringList "
        "&groups)': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setInGroup(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDelegateModelAttached::setInGroup(QQmlListCompositor::Group group,
    bool inGroup)': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.setInGroup' has no cute function yet. "
        "Qt's 'void "
        "QQmlDelegateModelAttached::setInGroup(QQmlListCompositor::Group "
        "group, bool inGroup)': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setInItems(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::setInItems(bool inItems)': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.setInItems' has no cute function yet. "
        "Qt's 'void QQmlDelegateModelAttached::setInItems(bool inItems)': "
        "leans on 'QQmlListCompositor::find(QQmlListCompositor::Group, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def setInPersistedItems(*__, **_) -> Never:
    """
    Qt's 'void QQmlDelegateModelAttached::setInPersistedItems(bool
    inPersisted)': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelAttached.setInPersistedItems' has no cute "
        "function yet. Qt's 'void "
        "QQmlDelegateModelAttached::setInPersistedItems(bool inPersisted)': "
        "leans on 'QQmlListCompositor::find(QQmlListCompositor::Group, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")
