"""
QV4::PropertyKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4propertykey_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::PropertyKey to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertyKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::PropertyKey: a plain Python object standing in
  front of one C++ QV4::PropertyKey.

  C++ hands a QV4::PropertyKey around as a copy, so every C++
  QV4::PropertyKey behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::PropertyKey that has a ritual and that Python
  can call so far, 19 names in all: 'isManaged', 'value', 'invalid',
  'fromArrayIndex', 'isStringOrSymbol', 'asArrayIndex', 'isArrayIndex',
  'isValid', 'isString', 'isSymbol', 'isCanonicalNumericIndexString',
  'toQString', 'toStringOrSymbol', 'id', 'fromId', 'asFunctionName',
  '__eq__', '__ne__', '__lt__'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::PropertyKey::~PropertyKey()': the destructor: Python removes
    its C++ QV4::PropertyKey by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QV4::PropertyKey is created at the first use, not by
    'QV4::PropertyKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::PropertyKey back gives a copy the ritual made
    for Python, in a new cute QV4::PropertyKey.
  - Each name of Qt's QV4::PropertyKey that has no cute function yet,
    'asStringOrSymbol', 'fromStringOrSymbol', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::PropertyKey, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FunctionNamePrefix(CuteNum):
    """
    The enum 'QV4::PropertyKey::FunctionNamePrefix' of Qt, with the 3 names
    Qt gives in it.
    """

    NULL = Kee[int](0)
    Getter = Kee[int](1)
    Setter = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def invalid() -> PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::PropertyKey::invalid()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#invalid

    Returns
    -------

    PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::PropertyKey::invalid()
    address = Rituals.call('ritual_ZN3QV411PropertyKey7invalidEv')
    return PropertyKey._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromArrayIndex(idx: int) -> PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::PropertyKey::fromArrayIndex(uint idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertykey.html#fromArrayIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::PropertyKey::fromArrayIndex(uint idx)
    address = Rituals.call(
        'ritual_ZN3QV411PropertyKey14fromArrayIndexEj', idx,
    )
    return PropertyKey._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromId(id: int) -> PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::PropertyKey::fromId(quint64 id)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#fromId

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::PropertyKey::fromId(quint64 id)
    address = Rituals.call('ritual_ZN3QV411PropertyKey6fromIdEy', id)
    return PropertyKey._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PropertyKey'

  #  Qt's '~QV4::PropertyKey()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::PropertyKey behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV411PropertyKeyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isManaged(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isManaged() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#isManaged
    """
    #  bool QV4::PropertyKey::isManaged() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey9isManagedEv')

  def value(self) -> int:
    """
    Calls Qt's 'quint32 QV4::PropertyKey::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#value
    """
    #  quint32 QV4::PropertyKey::value() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey5valueEv')

  def isStringOrSymbol(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isStringOrSymbol() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertykey.html#isStringOrSymbol
    """
    #  bool QV4::PropertyKey::isStringOrSymbol() const
    return self.uglySide.call(
        'ritual_ZNK3QV411PropertyKey16isStringOrSymbolEv',
    )

  def asArrayIndex(self) -> int:
    """
    Calls Qt's 'uint QV4::PropertyKey::asArrayIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#asArrayIndex
    """
    #  uint QV4::PropertyKey::asArrayIndex() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey12asArrayIndexEv')

  def isArrayIndex(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isArrayIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#isArrayIndex
    """
    #  bool QV4::PropertyKey::isArrayIndex() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey12isArrayIndexEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#isValid
    """
    #  bool QV4::PropertyKey::isValid() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey7isValidEv')

  def isString(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#isString
    """
    #  bool QV4::PropertyKey::isString() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey8isStringEv')

  def isSymbol(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isSymbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#isSymbol
    """
    #  bool QV4::PropertyKey::isSymbol() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey8isSymbolEv')

  def isCanonicalNumericIndexString(self) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::isCanonicalNumericIndexString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertykey.html#isCanonicalNumericIndexString
    """
    #  bool QV4::PropertyKey::isCanonicalNumericIndexString() const
    return self.uglySide.call(
        'ritual_ZNK3QV411PropertyKey29isCanonicalNumericIndexStringEv',
    )

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::PropertyKey::toQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::PropertyKey::toQString() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey9toQStringEv')

  def id(self) -> int:
    """
    Calls Qt's 'quint64 QV4::PropertyKey::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#id
    """
    #  quint64 QV4::PropertyKey::id() const
    return self.uglySide.call('ritual_ZNK3QV411PropertyKey2idEv')

  @overload(WAIT['QV4.ExecutionEngine'], FunctionNamePrefix)
  @overload(NoneType, FunctionNamePrefix)
  def asFunctionName(
      self,
      e: Optional[QV4.ExecutionEngine],
      prefix: FunctionNamePrefix,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String
    *QV4::PropertyKey::asFunctionName(ExecutionEngine *e, FunctionNamePrefix
    prefix) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertykey.html#asFunctionName

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prefix : FunctionNamePrefix
      Passed on as its number.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::PropertyKey::asFunctionName(ExecutionEngine *e,
    #      FunctionNamePrefix prefix) const
    address = self.uglySide.call(
        'ritual_ZNK3QV411PropertyKey14asFunctionNameEPNS_15ExecutionEngineE'
        'NS0_18FunctionNamePrefixE',
        self._addressOf(e), prefix.value,
    )
    return QV4.Heap.String._cuteAt(address)

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
  def __eq__(self, other: PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::operator==(const PropertyKey &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#operator==

    Parameters
    ----------

    other : PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::PropertyKey::operator==(const PropertyKey &other) const
    return self.uglySide.call(
        'ritual_ZNK3QV411PropertyKeyeqERKS0_', self._valueOf(other),
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
  def __ne__(self, other: PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::operator!=(const PropertyKey &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#operator!=

    Parameters
    ----------

    other : PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::PropertyKey::operator!=(const PropertyKey &other) const
    return self.uglySide.call(
        'ritual_ZNK3QV411PropertyKeyneERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __lt__(self, other: PropertyKey) -> bool:
    """
    Calls Qt's 'bool QV4::PropertyKey::operator<(const PropertyKey &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertykey.html#operator<

    Parameters
    ----------

    other : PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::PropertyKey::operator<(const PropertyKey &other) const
    return self.uglySide.call(
        'ritual_ZNK3QV411PropertyKeyltERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def toStringOrSymbol(
      self,
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Heap.StringOrSymbol]:
    """
    Calls Qt's 'Heap::StringOrSymbol
    *QV4::PropertyKey::toStringOrSymbol(ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-propertykey.html#toStringOrSymbol

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.StringOrSymbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::StringOrSymbol
    #      *QV4::PropertyKey::toStringOrSymbol(ExecutionEngine *e)
    address = self.uglySide.call(
        'ritual_ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngine'
        'E',
        self._addressOf(e),
    )
    return QV4.Heap.StringOrSymbol._cuteAt(address)

  @staticmethod
  def asStringOrSymbol(*__, **_) -> Never:
    """
    Qt's 'QV4::PropertyKey::asStringOrSymbol': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.PropertyKey.asStringOrSymbol' has no cute function yet. Qt's "
        "'QV4::PropertyKey::asStringOrSymbol': a template: a pattern and no "
        "single function.")

  @staticmethod
  def fromStringOrSymbol(*__, **_) -> Never:
    """
    Qt's 'QV4::PropertyKey::fromStringOrSymbol': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.PropertyKey.fromStringOrSymbol' has no cute function yet. "
        "Qt's 'QV4::PropertyKey::fromStringOrSymbol': a template: a pattern "
        "and no single function.")
