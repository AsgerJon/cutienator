"""
QV4::ArgumentsObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4argumentsobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ArgumentsObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ArgumentsObject(QV4.Object):
  """
  The cute side of Qt's QV4::ArgumentsObject: a plain Python object standing
  in front of one C++ QV4::ArgumentsObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::ArgumentsObject is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ArgumentsObject that has a ritual and that
  Python can call so far, 13 names in all: '__dataTest', 'd_unchecked', 'd',
  'context', 'fullyCreated', 'virtualDefineOwnProperty', 'virtualPut',
  'virtualDeleteProperty', 'virtualGetOwnProperty', 'virtualGetLength',
  'fullyCreate', 'isMapped', 'removeMapping'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ReturnedValue QV4::ArgumentsObject::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::ArgumentsObject::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.

  What has no ritual
  ------------------

  6 of the 21 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::ArgumentsObject is created at the first use, not by
    'QV4::ArgumentsObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ArgumentsObject.
  - Each name of Qt's QV4::ArgumentsObject that has no cute function yet,
    'isNonStrictArgumentsObject', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
      desc: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ArgumentsObject::virtualDefineOwnProperty(Managed
    *m, PropertyKey id, const Property *desc, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#virtualDefineOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    desc : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::ArgumentsObject::virtualDefineOwnProperty(Managed *m,
    #      PropertyKey id, const Property *desc, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV415ArgumentsObject24virtualDefineOwnPropertyEPNS_7Mana'
        'gedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(desc), CuteMixin._valueOf(attrs),
    )

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
    Calls Qt's 'bool QV4::ArgumentsObject::virtualPut(Managed *m, PropertyKey
    id, const Value &value, Value *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#virtualPut

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
    #  bool QV4::ArgumentsObject::virtualPut(Managed *m, PropertyKey id,
    #      const Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV415ArgumentsObject10virtualPutEPNS_7ManagedENS_11Prope'
        'rtyKeyERKNS_5ValueEPS4_',
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
    Calls Qt's 'bool QV4::ArgumentsObject::virtualDeleteProperty(Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#virtualDeleteProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ArgumentsObject::virtualDeleteProperty(Managed *m,
    #      PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV415ArgumentsObject21virtualDeletePropertyEPNS_7Managed'
        'ENS_11PropertyKeyE',
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
    QV4::ArgumentsObject::virtualGetOwnProperty(const Managed *m, PropertyKey
    id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#virtualGetOwnProperty

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
    #  PropertyAttributes QV4::ArgumentsObject::virtualGetOwnProperty(const
    #      Managed *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV415ArgumentsObject21virtualGetOwnPropertyEPKNS_7Manage'
        'dENS_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetLength(m: Optional[QV4.Managed]) -> int:
    """
    Calls Qt's 'qint64 QV4::ArgumentsObject::virtualGetLength(const Managed
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#virtualGetLength

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QV4::ArgumentsObject::virtualGetLength(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV415ArgumentsObject16virtualGetLengthEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ArgumentsObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ArgumentsObject]:
    """
    Calls Qt's 'QV4::Heap::ArgumentsObject
    *QV4::ArgumentsObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ArgumentsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArgumentsObject *QV4::ArgumentsObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ArgumentsObject11d_uncheckedEv',
    )
    return QV4.Heap.ArgumentsObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ArgumentsObject]:
    """
    Calls Qt's 'QV4::Heap::ArgumentsObject *QV4::ArgumentsObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-argumentsobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ArgumentsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArgumentsObject *QV4::ArgumentsObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV415ArgumentsObject1dEv')
    return QV4.Heap.ArgumentsObject._cuteAt(address)

  def context(self) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext *QV4::ArgumentsObject::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-argumentsobject.html#context

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext *QV4::ArgumentsObject::context() const
    address = self.uglySide.call('ritual_ZNK3QV415ArgumentsObject7contextEv')
    return QV4.Heap.CallContext._cuteAt(address)

  def fullyCreated(self) -> bool:
    """
    Calls Qt's 'bool QV4::ArgumentsObject::fullyCreated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#fullyCreated
    """
    #  bool QV4::ArgumentsObject::fullyCreated() const
    return self.uglySide.call(
        'ritual_ZNK3QV415ArgumentsObject12fullyCreatedEv',
    )

  @overload(int)
  def isMapped(self, arg: int) -> bool:
    """
    Calls Qt's 'bool QV4::ArgumentsObject::isMapped(uint arg) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-argumentsobject.html#isMapped

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  bool QV4::ArgumentsObject::isMapped(uint arg) const
    return self.uglySide.call(
        'ritual_ZNK3QV415ArgumentsObject8isMappedEj', arg,
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
    Calls Qt's 'void QV4::ArgumentsObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#__dataTest
    """
    #  void QV4::ArgumentsObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV415ArgumentsObject10__dataTestEv')

  def fullyCreate(self) -> None:
    """
    Calls Qt's 'void QV4::ArgumentsObject::fullyCreate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#fullyCreate
    """
    #  void QV4::ArgumentsObject::fullyCreate()
    self.uglySide.call('ritual_ZN3QV415ArgumentsObject11fullyCreateEv')

  @overload(int)
  def removeMapping(self, arg: int) -> None:
    """
    Calls Qt's 'void QV4::ArgumentsObject::removeMapping(uint arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-argumentsobject.html#removeMapping

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QV4::ArgumentsObject::removeMapping(uint arg)
    self.uglySide.call(
        'ritual_ZN3QV415ArgumentsObject13removeMappingEj', arg,
    )

  @staticmethod
  def isNonStrictArgumentsObject(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ArgumentsObject::isNonStrictArgumentsObject(Managed *m)':
    leans on 'QV4::ArgumentsObject::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ArgumentsObject.isNonStrictArgumentsObject' has no cute "
        "function yet. Qt's 'bool "
        "QV4::ArgumentsObject::isNonStrictArgumentsObject(Managed *m)': "
        "leans on 'QV4::ArgumentsObject::static_vtbl', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
