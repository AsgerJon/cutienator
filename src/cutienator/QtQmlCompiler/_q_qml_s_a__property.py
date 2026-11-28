"""
QQmlSA::Property binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class Property(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::Property: a plain Python object standing in
  front of one C++ QQmlSA::Property.

  C++ hands a QQmlSA::Property around as a copy, so every C++
  QQmlSA::Property behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::Property that has a ritual and that Python
  can call so far, 7 names in all: 'd_func', 'typeName', 'isValid',
  'isReadonly', 'type', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const PropertyPrivate *QQmlSA::Property::d_func() const': takes in
    Python what 'PropertyPrivate *QQmlSA::Property::d_func()' takes.
  - Qt's 'QQmlSA::Property::Property(Property &&a0)': takes a type Python has
    no way to hand over yet.
  - Qt's 'Property &QQmlSA::Property::operator=(const Property &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'Property &QQmlSA::Property::operator=(Property &&a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::Property::~Property()': the destructor: Python removes its
    C++ QQmlSA::Property by it, and has no other use for it.
  - Qt's 'bool QQmlSA::Property::operatorEqualsImpl(const Property &a0, const
    Property &a1)': an operator Python has no name for.

  What to expect
  --------------

  - The C++ QQmlSA::Property is created at the first use, not by
    'QQmlSA::Property(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::Property back gives a copy the ritual made
    for Python, in a new cute QQmlSA::Property.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::Property'

  #  Qt's '~QQmlSA::Property()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSA::Property behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA8PropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Property::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Property::typeName() const
    return self.uglySide.call('ritual_ZNK6QQmlSA8Property8typeNameEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Property::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#isValid
    """
    #  bool QQmlSA::Property::isValid() const
    return self.uglySide.call('ritual_ZNK6QQmlSA8Property7isValidEv')

  def isReadonly(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Property::isReadonly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#isReadonly
    """
    #  bool QQmlSA::Property::isReadonly() const
    return self.uglySide.call('ritual_ZNK6QQmlSA8Property10isReadonlyEv')

  def type(self) -> QQmlSA.Element:
    """
    Calls Qt's 'QQmlSA::Element QQmlSA::Property::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#type

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSA::Element QQmlSA::Property::type() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA8Property4typeEv')
    return QQmlSA.Element._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: Property) -> bool:
    """
    Calls Qt's 'bool operator==(const Property &lhs, const Property &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#operator==

    Parameters
    ----------

    rhs : Property
      Passed on as a value: Qt reads the C++ QQmlSA::Property, which stays
      Python's own.
    """
    #  bool operator==(const Property &lhs, const Property &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_8PropertyES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: Property) -> bool:
    """
    Calls Qt's 'bool operator!=(const Property &lhs, const Property &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#operator!=

    Parameters
    ----------

    rhs : Property
      Passed on as a value: Qt reads the C++ QQmlSA::Property, which stays
      Python's own.
    """
    #  bool operator!=(const Property &lhs, const Property &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_8PropertyES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Property::Property()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#Property
    """
    #  QQmlSA::Property::Property()
    self._noteCreation(Property, lambda: Rituals.call(
        'ritual_ZN6QQmlSA8PropertyC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: Property) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Property::Property(const Property
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#Property

    Parameters
    ----------

    a0 : Property
      Passed on as a value: Qt reads the C++ QQmlSA::Property, which stays
      Python's own.
    """
    #  QQmlSA::Property::Property(const Property &a0)
    self._noteCreation(Property, lambda: Rituals.call(
        'ritual_ZN6QQmlSA8PropertyC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlSA.PropertyPrivate]:
    """
    Calls Qt's 'PropertyPrivate *QQmlSA::Property::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-property.html#d_func

    Returns
    -------

    Optional[QQmlSA.PropertyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PropertyPrivate *QQmlSA::Property::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA8Property6d_funcEv')
    return QQmlSA.PropertyPrivate._cuteAt(address)
