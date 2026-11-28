"""
QV4::Property binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4property_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Property to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Property(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Property: a plain Python object standing in
  front of one C++ QV4::Property.

  What exists
  -----------

  Every function of Qt's QV4::Property that has a ritual and that Python can
  call so far, 8 names in all: 'fullyPopulated', 'completed', 'isSubset',
  'getter', 'setter', 'setGetter', 'setSetter', 'copy'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Property::merge(PropertyAttributes &attrs, const Property
    *other, PropertyAttributes otherAttrs)': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool QV4::Property::isCompatible(PropertyAttributes &attrs, const
    Property *other, PropertyAttributes otherAttrs) const': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QV4::Property is created at the first use, not by
    'QV4::Property(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Property.
  - Each name of Qt's QV4::Property that has no cute function yet,
    'isCompatible', 'merge', holds a function that raises
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
  __qt_class__ = 'QV4::Property'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      WAIT['QV4.PropertyAttributes'], THIS, WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      WAIT['QV4.PropertyAttributes'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  def isSubset(
      self,
      attrs: QV4.PropertyAttributes,
      other: Optional[Property],
      otherAttrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Property::isSubset(const PropertyAttributes &attrs,
    const Property *other, PropertyAttributes otherAttrs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#isSubset

    Parameters
    ----------

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.

    other : Optional[Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    otherAttrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::Property::isSubset(const PropertyAttributes &attrs, const
    #      Property *other, PropertyAttributes otherAttrs) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Property8isSubsetERKNS_18PropertyAttributesEPKS0_S1'
        '_',
        self._valueOf(attrs), self._addressOf(other),
        self._valueOf(otherAttrs),
    )

  def getter(self) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject *QV4::Property::getter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#getter

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject *QV4::Property::getter() const
    address = self.uglySide.call('ritual_ZNK3QV48Property6getterEv')
    return QV4.Heap.FunctionObject._cuteAt(address)

  def setter(self) -> Optional[QV4.Heap.FunctionObject]:
    """
    Calls Qt's 'Heap::FunctionObject *QV4::Property::setter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#setter

    Returns
    -------

    Optional[QV4.Heap.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::FunctionObject *QV4::Property::setter() const
    address = self.uglySide.call('ritual_ZNK3QV48Property6setterEv')
    return QV4.Heap.FunctionObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.FunctionObject'])
  @overload(NoneType)
  def setGetter(self, g: Optional[QV4.FunctionObject]) -> None:
    """
    Calls Qt's 'void QV4::Property::setGetter(FunctionObject *g)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#setGetter

    Parameters
    ----------

    g : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Property::setGetter(FunctionObject *g)
    self.uglySide.call(
        'ritual_ZN3QV48Property9setGetterEPNS_14FunctionObjectE',
        self._addressOf(g),
    )

  @overload(WAIT['QV4.FunctionObject'])
  @overload(NoneType)
  def setSetter(self, s: Optional[QV4.FunctionObject]) -> None:
    """
    Calls Qt's 'void QV4::Property::setSetter(FunctionObject *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#setSetter

    Parameters
    ----------

    s : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Property::setSetter(FunctionObject *s)
    self.uglySide.call(
        'ritual_ZN3QV48Property9setSetterEPNS_14FunctionObjectE',
        self._addressOf(s),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::Property::Property()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#Property
    """
    #  QV4::Property::Property()
    self._noteCreation(Property, lambda: Rituals.call(
        'ritual_ZN3QV48PropertyC1Ev',
    ))

  @overload(WAIT['QV4.Heap.FunctionObject'], WAIT['QV4.Heap.FunctionObject'])
  @overload(WAIT['QV4.Heap.FunctionObject'], NoneType)
  @overload(NoneType, WAIT['QV4.Heap.FunctionObject'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      getter: Optional[QV4.Heap.FunctionObject],
      setter: Optional[QV4.Heap.FunctionObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Property::Property(Heap::FunctionObject *getter,
    Heap::FunctionObject *setter)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#Property

    Parameters
    ----------

    getter : Optional[QV4.Heap.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    setter : Optional[QV4.Heap.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Property::Property(Heap::FunctionObject *getter,
    #      Heap::FunctionObject *setter)
    self._noteCreation(Property, lambda: Rituals.call(
        'ritual_ZN3QV48PropertyC1EPNS_4Heap14FunctionObjectES3_',
        self._addressOf(getter), self._addressOf(setter),
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

  @overload(WAIT['QV4.PropertyAttributes'])
  @overload(NoneType)
  def fullyPopulated(self, attrs: Optional[QV4.PropertyAttributes]) -> None:
    """
    Calls Qt's 'void QV4::Property::fullyPopulated(PropertyAttributes
    *attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#fullyPopulated

    Parameters
    ----------

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Property::fullyPopulated(PropertyAttributes *attrs)
    self.uglySide.call(
        'ritual_ZN3QV48Property14fullyPopulatedEPNS_18PropertyAttributesE',
        self._addressOf(attrs),
    )

  @overload(WAIT['QV4.PropertyAttributes'])
  @overload(NoneType)
  def completed(self, attrs: Optional[QV4.PropertyAttributes]) -> None:
    """
    Calls Qt's 'void QV4::Property::completed(PropertyAttributes *attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#completed

    Parameters
    ----------

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Property::completed(PropertyAttributes *attrs)
    self.uglySide.call(
        'ritual_ZN3QV48Property9completedEPNS_18PropertyAttributesE',
        self._addressOf(attrs),
    )

  @overload(THIS, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, WAIT['QV4.PropertyAttributes'])
  def copy(
      self,
      other: Optional[Property],
      attrs: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::Property::copy(const Property *other,
    PropertyAttributes attrs)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-property.html#copy

    Parameters
    ----------

    other : Optional[Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::Property::copy(const Property *other, PropertyAttributes
    #      attrs)
    self.uglySide.call(
        'ritual_ZN3QV48Property4copyEPKS0_NS_18PropertyAttributesE',
        self._addressOf(other), self._valueOf(attrs),
    )

  @staticmethod
  def isCompatible(*__, **_) -> Never:
    """
    Qt's 'bool QV4::Property::isCompatible(PropertyAttributes &attrs, const
    Property *other, PropertyAttributes otherAttrs) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Property.isCompatible' has no cute function yet. Qt's 'bool "
        "QV4::Property::isCompatible(PropertyAttributes &attrs, const "
        "Property *other, PropertyAttributes otherAttrs) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def merge(*__, **_) -> Never:
    """
    Qt's 'void QV4::Property::merge(PropertyAttributes &attrs, const Property
    *other, PropertyAttributes otherAttrs)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Property.merge' has no cute function yet. Qt's 'void "
        "QV4::Property::merge(PropertyAttributes &attrs, const Property "
        "*other, PropertyAttributes otherAttrs)': takes a type Python has "
        "no way to hand over yet.")
