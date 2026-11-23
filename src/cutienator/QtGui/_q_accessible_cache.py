"""
QAccessibleCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleCache to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAccessibleInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleInterface = WAIT['QAccessibleInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleCache(QObject):
  """
  The cute side of Qt's QAccessibleCache: a plain Python object standing in
  front of one C++ QAccessibleCache.

  It is built on the cute 'QObject', as Qt's QAccessibleCache is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleCache that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'instance',
  'interfaceForId', 'idForInterface', 'idForObject', 'containsObject',
  'insert', 'deleteInterface', 'sendObjectDestroyedEvent', 'objectDestroyed',
  'acquireId'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAccessibleCache::~QAccessibleCache()': the destructor: Python
    never removes a C++ QAccessibleCache.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QAccessibleCache is created at the first use, not by
    'QAccessibleCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleCache.
  - Qt tells when it has removed the C++ QAccessibleCache. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QAccessibleCache::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#tr

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
    #  QString QAccessibleCache::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QAccessibleCache2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QAccessibleCache]:
    """
    Calls Qt's 'QAccessibleCache *QAccessibleCache::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#instance

    Returns
    -------

    Optional[QAccessibleCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleCache *QAccessibleCache::instance()
    address = Rituals.call('ritual_ZN16QAccessibleCache8instanceEv')
    return QAccessibleCache._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleCache'

  #  A C++ QAccessibleCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAccessibleCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAccessibleCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def interfaceForId(self, id: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface
    *QAccessibleCache::interfaceForId(QAccessible::Id id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#interfaceForId

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleCache::interfaceForId(QAccessible::Id
    #      id) const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleCache14interfaceForIdEj', id,
    )
    from . import QAccessibleInterface
    return QAccessibleInterface._cuteAt(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def idForInterface(self, iface: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'QAccessible::Id
    QAccessibleCache::idForInterface(QAccessibleInterface *iface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#idForInterface

    Parameters
    ----------

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessible::Id QAccessibleCache::idForInterface(QAccessibleInterface
    #      *iface) const
    return self.uglySide.call(
        'ritual_ZNK16QAccessibleCache14idForInterfaceEP20QAccessibleInterfa'
        'ce',
        self._addressOf(iface),
    )

  @overload(QObject)
  @overload(NoneType)
  def idForObject(self, obj: Optional[QObject]) -> int:
    """
    Calls Qt's 'QAccessible::Id QAccessibleCache::idForObject(QObject *obj)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#idForObject

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessible::Id QAccessibleCache::idForObject(QObject *obj) const
    return self.uglySide.call(
        'ritual_ZNK16QAccessibleCache11idForObjectEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def containsObject(self, obj: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QAccessibleCache::containsObject(QObject *obj) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#containsObject

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleCache::containsObject(QObject *obj) const
    return self.uglySide.call(
        'ritual_ZNK16QAccessibleCache14containsObjectEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QObject, QAccessibleInterface)
  @overload(QObject, NoneType)
  @overload(NoneType, QAccessibleInterface)
  @overload(NoneType, NoneType)
  def insert(
      self,
      object: Optional[QObject],
      iface: Optional[QAccessibleInterface],
  ) -> int:
    """
    Calls Qt's 'QAccessible::Id QAccessibleCache::insert(QObject *object,
    QAccessibleInterface *iface) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#insert

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iface : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessible::Id QAccessibleCache::insert(QObject *object,
    #      QAccessibleInterface *iface) const
    return self.uglySide.call(
        'ritual_ZNK16QAccessibleCache6insertEP7QObjectP20QAccessibleInterfa'
        'ce',
        self._addressOf(object, 'QObject'), self._addressOf(iface),
    )

  def acquireId(self) -> int:
    """
    Calls Qt's 'QAccessible::Id QAccessibleCache::acquireId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessiblecache.html#acquireId
    """
    #  QAccessible::Id QAccessibleCache::acquireId() const
    return self.uglySide.call('ritual_ZNK16QAccessibleCache9acquireIdEv')

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

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def deleteInterface(self, id: int, obj: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QAccessibleCache::deleteInterface(QAccessible::Id id,
    QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#deleteInterface

    Parameters
    ----------

    id : int
      Passed on as it is.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QAccessibleCache::deleteInterface(QAccessible::Id id, QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN16QAccessibleCache15deleteInterfaceEjP7QObject',
        id, self._addressOf(obj, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def sendObjectDestroyedEvent(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAccessibleCache::sendObjectDestroyedEvent(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#sendObjectDestroyedEvent

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleCache::sendObjectDestroyedEvent(QObject *obj)
    self.uglySide.call(
        'ritual_ZN16QAccessibleCache24sendObjectDestroyedEventEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAccessibleCache::objectDestroyed(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblecache.html#objectDestroyed

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleCache::objectDestroyed(QObject *obj)
    self.uglySide.call(
        'ritual_ZN16QAccessibleCache15objectDestroyedEP7QObject',
        self._addressOf(obj, 'QObject'),
    )
