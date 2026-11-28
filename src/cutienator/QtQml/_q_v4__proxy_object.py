"""
QV4::ProxyObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::ProxyObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ProxyObject(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::ProxyObject: a plain Python object standing in
  front of one C++ QV4::ProxyObject.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::ProxyObject is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ProxyObject that has a ritual and that Python
  can call so far, 13 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'virtualPut', 'virtualDeleteProperty',
  'virtualHasProperty', 'virtualGetOwnProperty', 'virtualDefineOwnProperty',
  'virtualIsExtensible', 'virtualPreventExtensions', 'virtualGetPrototypeOf',
  'virtualSetPrototypeOf'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ReturnedValue QV4::ProxyObject::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  6 of the 20 functions Qt declares: 3 forbidden; 1 not a gap; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::ProxyObject is created at the first use, not by
    'QV4::ProxyObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ProxyObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::ProxyObject::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::ProxyObject::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV411ProxyObject20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualPut(Managed *m, PropertyKey id,
    const Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualPut

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ProxyObject::virtualPut(Managed *m, PropertyKey id, const
    #      Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject10virtualPutEPNS_7ManagedENS_11PropertyK'
        'eyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualDeleteProperty(Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualDeleteProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ProxyObject::virtualDeleteProperty(Managed *m, PropertyKey
    #      id)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject21virtualDeletePropertyEPNS_7ManagedENS_'
        '11PropertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualHasProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualHasProperty(const Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualHasProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ProxyObject::virtualHasProperty(const Managed *m,
    #      PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject18virtualHasPropertyEPKNS_7ManagedENS_11'
        'PropertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(NoneType, WAIT['QV4.PropertyKey'], NoneType)
  def virtualGetOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes
    QV4::ProxyObject::virtualGetOwnProperty(const Managed *m, PropertyKey id,
    Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualGetOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::ProxyObject::virtualGetOwnProperty(const
    #      Managed *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV411ProxyObject21virtualGetOwnPropertyEPKNS_7ManagedENS'
        '_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  def virtualDefineOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualDefineOwnProperty(Managed *m,
    PropertyKey id, const Property *p, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualDefineOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::ProxyObject::virtualDefineOwnProperty(Managed *m,
    #      PropertyKey id, const Property *p, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject24virtualDefineOwnPropertyEPNS_7ManagedE'
        'NS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p), CuteMixin._valueOf(attrs),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualIsExtensible(m: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualIsExtensible(const Managed
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualIsExtensible

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ProxyObject::virtualIsExtensible(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject19virtualIsExtensibleEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualPreventExtensions(a0: Optional[QV4.Managed]) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualPreventExtensions(Managed
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualPreventExtensions

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ProxyObject::virtualPreventExtensions(Managed *a0)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject24virtualPreventExtensionsEPNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetPrototypeOf(
      a0: Optional[QV4.Managed],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ProxyObject::virtualGetPrototypeOf(const
    Managed *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualGetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ProxyObject::virtualGetPrototypeOf(const Managed
    #      *a0)
    address = Rituals.call(
        'ritual_ZN3QV411ProxyObject21virtualGetPrototypeOfEPKNS_7ManagedE',
        CuteMixin._addressOf(a0),
    )
    return QV4.Heap.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, QV4.Object)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Object)
  @overload(NoneType, NoneType)
  def virtualSetPrototypeOf(
      a0: Optional[QV4.Managed],
      a1: Optional[QV4.Object],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ProxyObject::virtualSetPrototypeOf(Managed *a0,
    const Object *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-proxyobject.html#virtualSetPrototypeOf

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ProxyObject::virtualSetPrototypeOf(Managed *a0, const Object
    #      *a1)
    return Rituals.call(
        'ritual_ZN3QV411ProxyObject21virtualSetPrototypeOfEPNS_7ManagedEPKN'
        'S_6ObjectE',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ProxyObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ProxyObject]:
    """
    Calls Qt's 'QV4::Heap::ProxyObject *QV4::ProxyObject::d_unchecked()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxyobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ProxyObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ProxyObject *QV4::ProxyObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV411ProxyObject11d_uncheckedEv',
    )
    return QV4.Heap.ProxyObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ProxyObject]:
    """
    Calls Qt's 'QV4::Heap::ProxyObject *QV4::ProxyObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxyobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ProxyObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ProxyObject *QV4::ProxyObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV411ProxyObject1dEv')
    return QV4.Heap.ProxyObject._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::ProxyObject::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-proxyobject.html#__dataTest
    """
    #  void QV4::ProxyObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV411ProxyObject10__dataTestEv')
