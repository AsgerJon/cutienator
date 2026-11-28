"""
QV4::VariantAssociationObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::VariantAssociationObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VariantAssociationObject(QV4.ReferenceObject):
  """
  The cute side of Qt's QV4::VariantAssociationObject: a plain Python object
  standing in front of one C++ QV4::VariantAssociationObject.

  It is built on the cute 'QV4::ReferenceObject', as Qt's
  QV4::VariantAssociationObject is built on Qt's QV4::ReferenceObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::VariantAssociationObject that has a ritual and
  that Python can call so far, 7 names in all: '__dataTest', 'd_unchecked',
  'd', 'defaultPrototype', 'virtualPut', 'virtualDeleteProperty',
  'virtualGetOwnProperty'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::VariantAssociationObject::staticVTable()':
    gives 'QV4::VTable', which has no cute class yet.
  - Qt's 'QV4::ReturnedValue QV4::VariantAssociationObject::virtualGet(const
    QV4::Managed *that, PropertyKey id, const Value *receiver, bool
    *hasProperty)': takes a number to change where it is.
  - Qt's 'QV4::OwnPropertyKeyIterator
    *QV4::VariantAssociationObject::virtualOwnPropertyKeys(const Object *m,
    Value *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute
    class yet.
  - Qt's 'int QV4::VariantAssociationObject::virtualMetacall(Object *object,
    QMetaObject::Call call, int index, void **a)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 3 forbidden; 1 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::VariantAssociationObject is created at the first use, not by
    'QV4::VariantAssociationObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::VariantAssociationObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::VariantAssociationObject::defaultPrototype(QV4::ExecutionEngine
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object *QV4::VariantAssociationObject::defaultPrototype(QV4::
    #      ExecutionEngine *e)
    address = Rituals.call(
        'ritual_ZN3QV424VariantAssociationObject16defaultPrototypeEPNS_15Ex'
        'ecutionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      that: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::VariantAssociationObject::virtualPut(Managed *that,
    PropertyKey id, const QV4::Value &value, Value *receiver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html#virtualPut

    Parameters
    ----------

    that : Optional[QV4.Managed]
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
    #  bool QV4::VariantAssociationObject::virtualPut(Managed *that,
    #      PropertyKey id, const QV4::Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV424VariantAssociationObject10virtualPutEPNS_7ManagedEN'
        'S_11PropertyKeyERKNS_5ValueEPS4_',
        CuteMixin._addressOf(that), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      that: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool
    QV4::VariantAssociationObject::virtualDeleteProperty(QV4::Managed *that,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::VariantAssociationObject::virtualDeleteProperty(QV4::Managed
    #      *that, PropertyKey id)
    return Rituals.call(
        'ritual_ZN3QV424VariantAssociationObject21virtualDeletePropertyEPNS'
        '_7ManagedENS_11PropertyKeyE',
        CuteMixin._addressOf(that), CuteMixin._valueOf(id),
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
    QV4::VariantAssociationObject::virtualGetOwnProperty(const Managed *m,
    PropertyKey id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html

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
    #  PropertyAttributes
    #      QV4::VariantAssociationObject::virtualGetOwnProperty(const Managed
    #      *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV424VariantAssociationObject21virtualGetOwnPropertyEPKN'
        'S_7ManagedENS_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::VariantAssociationObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.VariantAssociationObject]:
    """
    Calls Qt's 'QV4::Heap::VariantAssociationObject
    *QV4::VariantAssociationObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.VariantAssociationObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::VariantAssociationObject
    #      *QV4::VariantAssociationObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424VariantAssociationObject11d_uncheckedEv',
    )
    return QV4.Heap.VariantAssociationObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.VariantAssociationObject]:
    """
    Calls Qt's 'QV4::Heap::VariantAssociationObject
    *QV4::VariantAssociationObject::d() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html#d

    Returns
    -------

    Optional[QV4.Heap.VariantAssociationObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::VariantAssociationObject
    #      *QV4::VariantAssociationObject::d() const
    address = self.uglySide.call(
        'ritual_ZNK3QV424VariantAssociationObject1dEv',
    )
    return QV4.Heap.VariantAssociationObject._cuteAt(address)

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
    Calls Qt's 'void QV4::VariantAssociationObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-variantassociationobject.html#__dataTest
    """
    #  void QV4::VariantAssociationObject::__dataTest()
    self.uglySide.call(
        'ritual_ZN3QV424VariantAssociationObject10__dataTestEv',
    )
