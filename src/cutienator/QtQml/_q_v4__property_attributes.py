"""
QV4::PropertyAttributes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4global_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::PropertyAttributes to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QV4


class PropertyAttributes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::PropertyAttributes: a plain Python object
  standing in front of one C++ QV4::PropertyAttributes.

  C++ hands a QV4::PropertyAttributes around as a copy, so every C++
  QV4::PropertyAttributes behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::PropertyAttributes that has a ritual and that
  Python can call so far, 25 names in all: 'setType', 'type', 'isData',
  'isAccessor', 'isGeneric', 'hasType', 'hasWritable', 'hasConfigurable',
  'hasEnumerable', 'setWritable', 'setConfigurable', 'setEnumerable',
  'resolve', 'isWritable', 'isEnumerable', 'isConfigurable', 'clearType',
  'clearWritable', 'clearEnumerable', 'clearConfigurable', 'clear',
  'isEmpty', 'all', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::PropertyAttributes::PropertyAttributes(PropertyFlags f)':
    takes in Python what
    'QV4::PropertyAttributes::PropertyAttributes(PropertyFlag f)' takes.
  - Qt's 'QV4::PropertyAttributes::~PropertyAttributes()': the destructor:
    Python removes its C++ QV4::PropertyAttributes by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QV4::PropertyAttributes is created at the first use, not by
    'QV4::PropertyAttributes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::PropertyAttributes back gives a copy the ritual
    made for Python, in a new cute QV4::PropertyAttributes.
  """

  #  The enums Qt writes inside QV4::PropertyAttributes, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QV4::PropertyAttributes::Type' of Qt, with the 3 names Qt gives
    in it.
    """

    Data = Kee[int](0)
    Accessor = Kee[int](1)
    Generic = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PropertyAttributes'

  #  Qt's '~QV4::PropertyAttributes()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::PropertyAttributes behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV418PropertyAttributesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QV4::PropertyAttributes::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyattributes.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QV4::PropertyAttributes::type() const
    return PropertyAttributes.Type(self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes4typeEv',
    ))

  def isData(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyattributes.html#isData
    """
    #  bool QV4::PropertyAttributes::isData() const
    return self.uglySide.call('ritual_ZNK3QV418PropertyAttributes6isDataEv')

  def isAccessor(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isAccessor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isAccessor
    """
    #  bool QV4::PropertyAttributes::isAccessor() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes10isAccessorEv',
    )

  def isGeneric(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isGeneric() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isGeneric
    """
    #  bool QV4::PropertyAttributes::isGeneric() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes9isGenericEv',
    )

  def hasType(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::hasType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#hasType
    """
    #  bool QV4::PropertyAttributes::hasType() const
    return self.uglySide.call('ritual_ZNK3QV418PropertyAttributes7hasTypeEv')

  def hasWritable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::hasWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#hasWritable
    """
    #  bool QV4::PropertyAttributes::hasWritable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes11hasWritableEv',
    )

  def hasConfigurable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::hasConfigurable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#hasConfigurable
    """
    #  bool QV4::PropertyAttributes::hasConfigurable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes15hasConfigurableEv',
    )

  def hasEnumerable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::hasEnumerable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#hasEnumerable
    """
    #  bool QV4::PropertyAttributes::hasEnumerable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes13hasEnumerableEv',
    )

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isWritable
    """
    #  bool QV4::PropertyAttributes::isWritable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes10isWritableEv',
    )

  def isEnumerable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isEnumerable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isEnumerable
    """
    #  bool QV4::PropertyAttributes::isEnumerable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes12isEnumerableEv',
    )

  def isConfigurable(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isConfigurable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isConfigurable
    """
    #  bool QV4::PropertyAttributes::isConfigurable() const
    return self.uglySide.call(
        'ritual_ZNK3QV418PropertyAttributes14isConfigurableEv',
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#isEmpty
    """
    #  bool QV4::PropertyAttributes::isEmpty() const
    return self.uglySide.call('ritual_ZNK3QV418PropertyAttributes7isEmptyEv')

  def all(self) -> int:
    """
    Calls Qt's 'uint QV4::PropertyAttributes::all() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyattributes.html#all
    """
    #  uint QV4::PropertyAttributes::all() const
    return self.uglySide.call('ritual_ZNK3QV418PropertyAttributes3allEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def setType(self, t: Type) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::setType(Type t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#setType

    Parameters
    ----------

    t : Type
      Passed on as its number.
    """
    #  void QV4::PropertyAttributes::setType(Type t)
    self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributes7setTypeENS0_4TypeE', t.value,
    )

  @overload(bool)
  def setWritable(self, b: bool) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::setWritable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#setWritable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QV4::PropertyAttributes::setWritable(bool b)
    self.uglySide.call('ritual_ZN3QV418PropertyAttributes11setWritableEb', b)

  @overload(bool)
  def setConfigurable(self, b: bool) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::setConfigurable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#setConfigurable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QV4::PropertyAttributes::setConfigurable(bool b)
    self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributes15setConfigurableEb', b,
    )

  @overload(bool)
  def setEnumerable(self, b: bool) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::setEnumerable(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#setEnumerable

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QV4::PropertyAttributes::setEnumerable(bool b)
    self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributes13setEnumerableEb', b,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: PropertyAttributes) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::operator==(PropertyAttributes
    other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#operator==

    Parameters
    ----------

    other : PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::PropertyAttributes::operator==(PropertyAttributes other)
    return self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributeseqES0_', self._valueOf(other),
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
  def __ne__(self, other: PropertyAttributes) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyAttributes::operator!=(PropertyAttributes
    other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#operator!=

    Parameters
    ----------

    other : PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::PropertyAttributes::operator!=(PropertyAttributes other)
    return self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributesneES0_', self._valueOf(other),
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
    Notes what was given, for Qt's
    'QV4::PropertyAttributes::PropertyAttributes()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#PropertyAttributes
    """
    #  QV4::PropertyAttributes::PropertyAttributes()
    self._noteCreation(PropertyAttributes, lambda: Rituals.call(
        'ritual_ZN3QV418PropertyAttributesC1Ev',
    ))

  @overload(QV4.PropertyFlag)
  def __init__(self, f: QV4.PropertyFlag) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PropertyAttributes::PropertyAttributes(PropertyFlag f)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#PropertyAttributes

    Parameters
    ----------

    f : QV4.PropertyFlag
      Passed on as its number.
    """
    #  QV4::PropertyAttributes::PropertyAttributes(PropertyFlag f)
    self._noteCreation(PropertyAttributes, lambda: Rituals.call(
        'ritual_ZN3QV418PropertyAttributesC1ENS_12PropertyFlagE', f.value,
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

  def resolve(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::resolve()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#resolve
    """
    #  void QV4::PropertyAttributes::resolve()
    self.uglySide.call('ritual_ZN3QV418PropertyAttributes7resolveEv')

  def clearType(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::clearType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#clearType
    """
    #  void QV4::PropertyAttributes::clearType()
    self.uglySide.call('ritual_ZN3QV418PropertyAttributes9clearTypeEv')

  def clearWritable(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::clearWritable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#clearWritable
    """
    #  void QV4::PropertyAttributes::clearWritable()
    self.uglySide.call('ritual_ZN3QV418PropertyAttributes13clearWritableEv')

  def clearEnumerable(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::clearEnumerable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#clearEnumerable
    """
    #  void QV4::PropertyAttributes::clearEnumerable()
    self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributes15clearEnumerableEv',
    )

  def clearConfigurable(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::clearConfigurable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertyattributes.html#clearConfigurable
    """
    #  void QV4::PropertyAttributes::clearConfigurable()
    self.uglySide.call(
        'ritual_ZN3QV418PropertyAttributes17clearConfigurableEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::PropertyAttributes::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyattributes.html#clear
    """
    #  void QV4::PropertyAttributes::clear()
    self.uglySide.call('ritual_ZN3QV418PropertyAttributes5clearEv')
