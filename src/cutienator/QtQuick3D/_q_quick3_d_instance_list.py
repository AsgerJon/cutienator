"""
QQuick3DInstanceList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DInstanceList to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DInstancing, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DInstanceList(QQuick3DInstancing):
  """
  The cute side of Qt's QQuick3DInstanceList: a plain Python object standing
  in front of one C++ QQuick3DInstanceList.

  It is built on the cute 'QQuick3DInstancing', as Qt's QQuick3DInstanceList
  is built on Qt's QQuick3DInstancing, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DInstanceList that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr',
  'instanceCount', 'instanceCountChanged', 'handleInstanceChange',
  'onInstanceDestroyed', 'generateInstanceData'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DInstanceList::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DInstanceList::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DInstanceList::~QQuick3DInstanceList()': the destructor:
    Python never removes a C++ QQuick3DInstanceList.
  - Qt's 'QByteArray QQuick3DInstanceList::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.
  - Qt's 'QQmlListProperty<QQuick3DInstanceListEntry>
    QQuick3DInstanceList::instances()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DInstanceList::qmlAppendInstanceListEntry(
    QQmlListProperty<QQuick3DInstanceListEntry> *list,
    QQuick3DInstanceListEntry *material)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.
  - Qt's 'QQuick3DInstanceListEntry
    *QQuick3DInstanceList::qmlInstanceListEntryAt(
    QQmlListProperty<QQuick3DInstanceListEntry> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute
    class yet.
  - Qt's 'qsizetype QQuick3DInstanceList::qmlInstanceListEntriesCount(
    QQmlListProperty<QQuick3DInstanceListEntry> *list)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.
  - Qt's 'void QQuick3DInstanceList::qmlClearInstanceListEntries(
    QQmlListProperty<QQuick3DInstanceListEntry> *list)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DInstanceList is created at the first use, not by
    'QQuick3DInstanceList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DInstanceList.
  - Qt tells when it has removed the C++ QQuick3DInstanceList. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DInstanceList that has no cute function yet,
    'instances', 'qmlAppendInstanceListEntry', 'qmlClearInstanceListEntries',
    'qmlInstanceListEntriesCount', 'qmlInstanceListEntryAt', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DInstanceList::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancelist.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DInstanceList::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuick3DInstanceList2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DInstanceList'

  #  A C++ QQuick3DInstanceList Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DInstanceList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DInstanceList::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DInstanceList::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DInstanceList10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DInstanceList::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#instanceCount
    """
    #  int QQuick3DInstanceList::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DInstanceList13instanceCountEv',
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

  @overload()
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DInstanceList::QQuick3DInstanceList(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#QQuick3DInstanceList

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DInstanceList::QQuick3DInstanceList(QQuick3DObject *parent)
    self._noteCreation(QQuick3DInstanceList, lambda: Rituals.call(
        'ritual_ZN20QQuick3DInstanceListC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def instanceCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceList::instanceCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#instanceCountChanged
    """
    #  void QQuick3DInstanceList::instanceCountChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DInstanceList20instanceCountChangedEv',
    )

  def handleInstanceChange(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceList::handleInstanceChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#handleInstanceChange
    """
    #  void QQuick3DInstanceList::handleInstanceChange()
    self.uglySide.call(
        'ritual_ZN20QQuick3DInstanceList20handleInstanceChangeEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def onInstanceDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceList::onInstanceDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#onInstanceDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DInstanceList::onInstanceDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN20QQuick3DInstanceList19onInstanceDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def generateInstanceData(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceList::generateInstanceData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancelist.html#generateInstanceData
    """
    #  void QQuick3DInstanceList::generateInstanceData()
    self.uglySide.call(
        'ritual_ZN20QQuick3DInstanceList20generateInstanceDataEv',
    )

  @staticmethod
  def instances(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DInstanceListEntry>
    QQuick3DInstanceList::instances()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DInstanceList.instances' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DInstanceListEntry> "
        "QQuick3DInstanceList::instances()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def qmlAppendInstanceListEntry(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DInstanceList::qmlAppendInstanceListEntry(
    QQmlListProperty<QQuick3DInstanceListEntry> *list,
    QQuick3DInstanceListEntry *material)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DInstanceList.qmlAppendInstanceListEntry' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DInstanceList::qmlAppendInstanceListEntry(QQmlListProperty<Q"
        "Quick3DInstanceListEntry> *list, QQuick3DInstanceListEntry "
        "*material)': names 'QQmlListProperty<QQuick3DInstanceListEntry>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlClearInstanceListEntries(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DInstanceList::qmlClearInstanceListEntries(
    QQmlListProperty<QQuick3DInstanceListEntry> *list)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DInstanceList.qmlClearInstanceListEntries' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DInstanceList::qmlClearInstanceListEntries(QQmlListProperty<"
        "QQuick3DInstanceListEntry> *list)': names "
        "'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlInstanceListEntriesCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DInstanceList::qmlInstanceListEntriesCount(
    QQmlListProperty<QQuick3DInstanceListEntry> *list)': names
    'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DInstanceList.qmlInstanceListEntriesCount' has no cute "
        "function yet. Qt's 'qsizetype "
        "QQuick3DInstanceList::qmlInstanceListEntriesCount(QQmlListProperty<"
        "QQuick3DInstanceListEntry> *list)': names "
        "'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute "
        "class yet.")

  @staticmethod
  def qmlInstanceListEntryAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DInstanceListEntry
    *QQuick3DInstanceList::qmlInstanceListEntryAt(
    QQmlListProperty<QQuick3DInstanceListEntry> *list, qsizetype index)':
    names 'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DInstanceList.qmlInstanceListEntryAt' has no cute function "
        "yet. Qt's 'QQuick3DInstanceListEntry "
        "*QQuick3DInstanceList::qmlInstanceListEntryAt(QQmlListProperty<QQui"
        "ck3DInstanceListEntry> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DInstanceListEntry>', which has no cute "
        "class yet.")
