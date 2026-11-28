"""
QQmlInterceptorMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlInterceptorMetaObject to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QDynamicMetaObjectData, QMetaObject
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlPropertyIndex, QQmlPropertyValueInterceptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']
  QQmlPropertyValueInterceptor = WAIT['QQmlPropertyValueInterceptor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlInterceptorMetaObject(QDynamicMetaObjectData):
  """
  The cute side of Qt's QQmlInterceptorMetaObject: a plain Python object
  standing in front of one C++ QQmlInterceptorMetaObject.

  It is built on the cute 'QDynamicMetaObjectData', as Qt's
  QQmlInterceptorMetaObject is built on Qt's QDynamicMetaObjectData, and has
  everything that class has.

  C++ hands a QQmlInterceptorMetaObject around as a copy, so every C++
  QQmlInterceptorMetaObject behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlInterceptorMetaObject that has a ritual and that
  Python can call so far, 8 names in all: 'registerInterceptor', 'get',
  'toDynamicMetaObject', 'propertyCache', 'setPropertyCache', 'intercepts',
  'invalidate', 'setInterceptionMode'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlInterceptorMetaObject::~QQmlInterceptorMetaObject()': the
    destructor: Python removes its C++ QQmlInterceptorMetaObject by it, and
    has no other use for it.
  - Qt's 'int QQmlInterceptorMetaObject::metaCall(QObject *o,
    QMetaObject::Call c, int id, void **a)': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool QQmlInterceptorMetaObject::intercept(QMetaObject::Call c, int
    id, void **a)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlInterceptorMetaObject::doIntercept(QMetaObject::Call c,
    int id, void **a)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlInterceptorMetaObject is created at the first use, not by
    'QQmlInterceptorMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlInterceptorMetaObject back gives a copy the
    ritual made for Python, in a new cute QQmlInterceptorMetaObject.
  - Each name of Qt's QQmlInterceptorMetaObject that has no cute function
    yet, 'doIntercept', 'intercept', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlInterceptorMetaObject, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InterceptionBehavior(CuteNum):
    """
    The enum 'QQmlInterceptorMetaObject::InterceptionBehavior' of Qt, with
    the 2 names Qt gives in it.
    """

    Intercept = Kee[int](0)
    SkipInterception = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def get(obj: Optional[QObject]) -> Optional[QQmlInterceptorMetaObject]:
    """
    Calls Qt's 'QQmlInterceptorMetaObject
    *QQmlInterceptorMetaObject::get(QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#get

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlInterceptorMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInterceptorMetaObject *QQmlInterceptorMetaObject::get(QObject
    #      *obj)
    address = Rituals.call(
        'ritual_ZN25QQmlInterceptorMetaObject3getEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return QQmlInterceptorMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject, InterceptionBehavior)
  @overload(NoneType, InterceptionBehavior)
  def setInterceptionMode(
      object: Optional[QObject],
      behavior: InterceptionBehavior,
  ) -> None:
    """
    Calls Qt's 'void QQmlInterceptorMetaObject::setInterceptionMode(QObject
    *object, InterceptionBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#setInterceptionMode

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    behavior : InterceptionBehavior
      Passed on as its number.
    """
    #  void QQmlInterceptorMetaObject::setInterceptionMode(QObject *object,
    #      InterceptionBehavior behavior)
    Rituals.call(
        'ritual_ZN25QQmlInterceptorMetaObject19setInterceptionModeEP7QObjec'
        'tNS_20InterceptionBehaviorE',
        CuteMixin._addressOf(object, 'QObject'), behavior.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInterceptorMetaObject'

  #  A C++ QQmlInterceptorMetaObject Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlInterceptorMetaObject'

  #  Qt's '~QQmlInterceptorMetaObject()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlInterceptorMetaObject behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQmlInterceptorMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def propertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlInterceptorMetaObject::propertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#propertyCache

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlInterceptorMetaObject::propertyCache()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlInterceptorMetaObject13propertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(QQmlPropertyIndex)
  def intercepts(self, propertyIndex: QQmlPropertyIndex) -> bool:
    """
    Calls Qt's 'bool QQmlInterceptorMetaObject::intercepts(QQmlPropertyIndex
    propertyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#intercepts

    Parameters
    ----------

    propertyIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.
    """
    #  bool QQmlInterceptorMetaObject::intercepts(QQmlPropertyIndex
    #      propertyIndex) const
    return self.uglySide.call(
        'ritual_ZNK25QQmlInterceptorMetaObject10interceptsE17QQmlPropertyIn'
        'dex',
        self._valueOf(propertyIndex),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlPropertyCache.ConstPtr)
  def setPropertyCache(self, newCache: QQmlPropertyCache.ConstPtr) -> None:
    """
    Calls Qt's 'void QQmlInterceptorMetaObject::setPropertyCache(const
    QQmlPropertyCache::ConstPtr &newCache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#setPropertyCache

    Parameters
    ----------

    newCache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlInterceptorMetaObject::setPropertyCache(const
    #      QQmlPropertyCache::ConstPtr &newCache)
    self.uglySide.call(
        'ritual_ZN25QQmlInterceptorMetaObject16setPropertyCacheERKN17QQmlPr'
        'opertyCache8ConstPtrE',
        self._valueOf(newCache),
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

  @overload(QObject, QQmlPropertyCache.ConstPtr)
  @overload(NoneType, QQmlPropertyCache.ConstPtr)
  def __init__(
      self,
      obj: Optional[QObject],
      cache: QQmlPropertyCache.ConstPtr,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlInterceptorMetaObject::QQmlInterceptorMetaObject(QObject *obj, const
    QQmlPropertyCache::ConstPtr &cache)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  QQmlInterceptorMetaObject::QQmlInterceptorMetaObject(QObject *obj,
    #      const QQmlPropertyCache::ConstPtr &cache)
    self._noteCreation(QQmlInterceptorMetaObject, lambda: Rituals.call(
        'ritual_ZN25QQmlInterceptorMetaObjectC1EP7QObjectRKN17QQmlPropertyC'
        'ache8ConstPtrE',
        self._addressOf(obj, 'QObject'), self._valueOf(cache),
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

  @overload(QQmlPropertyIndex, QQmlPropertyValueInterceptor)
  @overload(QQmlPropertyIndex, NoneType)
  def registerInterceptor(
      self,
      index: QQmlPropertyIndex,
      interceptor: Optional[QQmlPropertyValueInterceptor],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlInterceptorMetaObject::registerInterceptor(QQmlPropertyIndex index,
    QQmlPropertyValueInterceptor *interceptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#registerInterceptor

    Parameters
    ----------

    index : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    interceptor : Optional[QQmlPropertyValueInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInterceptorMetaObject::registerInterceptor(QQmlPropertyIndex
    #      index, QQmlPropertyValueInterceptor *interceptor)
    self.uglySide.call(
        'ritual_ZN25QQmlInterceptorMetaObject19registerInterceptorE17QQmlPr'
        'opertyIndexP28QQmlPropertyValueInterceptor',
        self._valueOf(index), self._addressOf(interceptor,
        'QQmlPropertyValueInterceptor'),
    )

  @overload(QObject)
  @overload(NoneType)
  def toDynamicMetaObject(
      self,
      o: Optional[QObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject
    *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#toDynamicMetaObject

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject
    #      *o)
    ritual = (
        'ritual_ZN25QQmlInterceptorMetaObject19toDynamicMetaObjectEP7QObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQmlInterceptorMetaObject19toDynamicMetaObjectEP7'
          'QObject')
    address = self.uglySide.call(ritual, self._addressOf(o, 'QObject'))
    return QMetaObject._cuteAt(address)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQmlInterceptorMetaObject::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinterceptormetaobject.html#invalidate
    """
    #  void QQmlInterceptorMetaObject::invalidate()
    self.uglySide.call('ritual_ZN25QQmlInterceptorMetaObject10invalidateEv')

  @staticmethod
  def doIntercept(*__, **_) -> Never:
    """
    Qt's 'bool QQmlInterceptorMetaObject::doIntercept(QMetaObject::Call c,
    int id, void **a)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlInterceptorMetaObject.doIntercept' has no cute function yet. "
        "Qt's 'bool "
        "QQmlInterceptorMetaObject::doIntercept(QMetaObject::Call c, int "
        "id, void **a)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def intercept(*__, **_) -> Never:
    """
    Qt's 'bool QQmlInterceptorMetaObject::intercept(QMetaObject::Call c, int
    id, void **a)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlInterceptorMetaObject.intercept' has no cute function yet. "
        "Qt's 'bool QQmlInterceptorMetaObject::intercept(QMetaObject::Call "
        "c, int id, void **a)': takes a type Python has no way to hand over "
        "yet.")
