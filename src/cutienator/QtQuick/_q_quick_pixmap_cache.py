"""
QQuickPixmapCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpixmapcache_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPixmapCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPixmapCache(QObject):
  """
  The cute side of Qt's QQuickPixmapCache: a plain Python object standing in
  front of one C++ QQuickPixmapCache.

  It is built on the cute 'QObject', as Qt's QQuickPixmapCache is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPixmapCache that has a ritual and that Python
  can call so far, 2 names in all: 'metaObject', 'timerEvent'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPixmapCache::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPixmapCache::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPixmapCache::~QQuickPixmapCache()': the destructor: Python
    never removes a C++ QQuickPixmapCache.

  What has no ritual
  ------------------

  13 of the 18 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QQuickPixmapCache; 2 not a gap; 2 forbidden; 1 leans on 'vtable for
  QQuickPixmapCache', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickPixmapCache is created at the first use, not by
    'QQuickPixmapCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPixmapCache.
  - Qt tells when it has removed the C++ QQuickPixmapCache. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPixmapCache that has no cute function yet,
    '__init__', 'destroyCache', 'instance', 'purgeCache', 'referencePixmap',
    'referencedCost', 'shrinkCache', 'unreferencePixmap', holds a function
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
  __qt_class__ = 'QQuickPixmapCache'

  #  A C++ QQuickPixmapCache Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPixmapCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPixmapCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmapcache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPixmapCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPixmapCache10metaObjectEv',
    )
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
    Qt's 'QQuickPixmapCache::QQuickPixmapCache()': leans on
    'QQuickPixmapCache::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.__init__' has no cute function yet. Qt's "
        "'QQuickPixmapCache::QQuickPixmapCache()': leans on "
        "'QQuickPixmapCache::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickPixmapCache::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpixmapcache.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPixmapCache::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_ZN17QQuickPixmapCache10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @staticmethod
  def destroyCache(*__, **_) -> Never:
    """
    Qt's 'int QQuickPixmapCache::destroyCache()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuickPixmapData'.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.destroyCache' has no cute function yet. Qt's "
        "'int QQuickPixmapCache::destroyCache()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'QQuickPixmapData'.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QQuickPixmapCache *QQuickPixmapCache::instance()': leans on 'vtable
    for QQuickPixmapCache', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.instance' has no cute function yet. Qt's "
        "'QQuickPixmapCache *QQuickPixmapCache::instance()': leans on "
        "'vtable for QQuickPixmapCache', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def purgeCache(*__, **_) -> Never:
    """
    Qt's 'void QQuickPixmapCache::purgeCache()': leans on
    'QQuickPixmapCache::shrinkCache(int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.purgeCache' has no cute function yet. Qt's "
        "'void QQuickPixmapCache::purgeCache()': leans on "
        "'QQuickPixmapCache::shrinkCache(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def referencePixmap(*__, **_) -> Never:
    """
    Qt's 'void QQuickPixmapCache::referencePixmap(QQuickPixmapData *a0)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickPixmapData'.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.referencePixmap' has no cute function yet. Qt's "
        "'void QQuickPixmapCache::referencePixmap(QQuickPixmapData *a0)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickPixmapData'.")

  @staticmethod
  def referencedCost(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickPixmapCache::referencedCost() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickPixmapData'.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.referencedCost' has no cute function yet. Qt's "
        "'qsizetype QQuickPixmapCache::referencedCost() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickPixmapData'.")

  @staticmethod
  def shrinkCache(*__, **_) -> Never:
    """
    Qt's 'void QQuickPixmapCache::shrinkCache(int remove)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'lcImg'.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.shrinkCache' has no cute function yet. Qt's "
        "'void QQuickPixmapCache::shrinkCache(int remove)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'lcImg'.")

  @staticmethod
  def unreferencePixmap(*__, **_) -> Never:
    """
    Qt's 'void QQuickPixmapCache::unreferencePixmap(QQuickPixmapData *a0)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickPixmapData'.
    """
    raise NotImplementedError(
        "'QQuickPixmapCache.unreferencePixmap' has no cute function yet. "
        "Qt's 'void QQuickPixmapCache::unreferencePixmap(QQuickPixmapData "
        "*a0)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuickPixmapData'.")
