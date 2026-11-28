"""
QSpiDBusCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qspidbuscache_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSpiDBusCache to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QSpiAccessibleCacheItem, QSpiObjectReference
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSpiAccessibleCacheItem = WAIT['QSpiAccessibleCacheItem']
  QSpiObjectReference = WAIT['QSpiObjectReference']


class QSpiDBusCache(QObject):
  """
  The cute side of Qt's QSpiDBusCache: a plain Python object standing in
  front of one C++ QSpiDBusCache.

  It is built on the cute 'QObject', as Qt's QSpiDBusCache is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpiDBusCache that has a ritual and that Python can
  call so far, 4 names in all: 'metaObject', 'AddAccessible',
  'RemoveAccessible', 'GetItems'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSpiDBusCache::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSpiDBusCache::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 3 leans on 'QSpiDBusCache; 2 not a gap;
  1 Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QSpiDBusCache is created at the first use, not by
    'QSpiDBusCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpiDBusCache.
  - Qt tells when it has removed the C++ QSpiDBusCache. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSpiDBusCache that has no cute function yet,
    '__init__', 'emitAddAccessible', 'emitRemoveAccessible', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpiDBusCache'

  #  A C++ QSpiDBusCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpiDBusCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSpiDBusCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspidbuscache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSpiDBusCache::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSpiDBusCache10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QSpiDBusCache::QSpiDBusCache(QDBusConnection c, QObject *parent)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'CacheAdaptor'.
    """
    raise NotImplementedError(
        "'QSpiDBusCache.__init__' has no cute function yet. Qt's "
        "'QSpiDBusCache::QSpiDBusCache(QDBusConnection c, QObject "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'CacheAdaptor'.")

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

  @overload(QSpiAccessibleCacheItem)
  def AddAccessible(self, nodeAdded: QSpiAccessibleCacheItem) -> None:
    """
    Calls Qt's 'void QSpiDBusCache::AddAccessible(const
    QSpiAccessibleCacheItem &nodeAdded)'.

    Qt's own words: https://doc.qt.io/qt-6/qspidbuscache.html#AddAccessible

    Parameters
    ----------

    nodeAdded : QSpiAccessibleCacheItem
      Passed on as a value: Qt reads the C++ QSpiAccessibleCacheItem, which
      stays Python's own.
    """
    #  void QSpiDBusCache::AddAccessible(const QSpiAccessibleCacheItem
    #      &nodeAdded)
    self.uglySide.call(
        'ritual_ZN13QSpiDBusCache13AddAccessibleERK23QSpiAccessibleCacheIte'
        'm',
        self._valueOf(nodeAdded),
    )

  @overload(QSpiObjectReference)
  def RemoveAccessible(self, nodeRemoved: QSpiObjectReference) -> None:
    """
    Calls Qt's 'void QSpiDBusCache::RemoveAccessible(const
    QSpiObjectReference &nodeRemoved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspidbuscache.html#RemoveAccessible

    Parameters
    ----------

    nodeRemoved : QSpiObjectReference
      Passed on as a value: Qt reads the C++ QSpiObjectReference, which stays
      Python's own.
    """
    #  void QSpiDBusCache::RemoveAccessible(const QSpiObjectReference
    #      &nodeRemoved)
    self.uglySide.call(
        'ritual_ZN13QSpiDBusCache16RemoveAccessibleERK19QSpiObjectReference',
        self._valueOf(nodeRemoved),
    )

  def GetItems(self) -> QList[QSpiAccessibleCacheItem]:
    """
    Calls Qt's 'QSpiAccessibleCacheArray QSpiDBusCache::GetItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qspidbuscache.html#GetItems

    Returns
    -------

    QList[QSpiAccessibleCacheItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QSpiAccessibleCacheArray QSpiDBusCache::GetItems()
    address = self.uglySide.call('ritual_ZN13QSpiDBusCache8GetItemsEv')
    from . import QSpiAccessibleCacheItem
    return QList[QSpiAccessibleCacheItem]._cuteOwning(address)

  @staticmethod
  def emitAddAccessible(*__, **_) -> Never:
    """
    Qt's 'void QSpiDBusCache::emitAddAccessible(const QSpiAccessibleCacheItem
    &item)': leans on 'QSpiDBusCache::AddAccessible(QSpiAccessibleCacheItem
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSpiDBusCache.emitAddAccessible' has no cute function yet. Qt's "
        "'void QSpiDBusCache::emitAddAccessible(const "
        "QSpiAccessibleCacheItem &item)': leans on "
        "'QSpiDBusCache::AddAccessible(QSpiAccessibleCacheItem const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def emitRemoveAccessible(*__, **_) -> Never:
    """
    Qt's 'void QSpiDBusCache::emitRemoveAccessible(const QSpiObjectReference
    &item)': leans on 'QSpiDBusCache::RemoveAccessible(QSpiObjectReference
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSpiDBusCache.emitRemoveAccessible' has no cute function yet. "
        "Qt's 'void QSpiDBusCache::emitRemoveAccessible(const "
        "QSpiObjectReference &item)': leans on "
        "'QSpiDBusCache::RemoveAccessible(QSpiObjectReference const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
