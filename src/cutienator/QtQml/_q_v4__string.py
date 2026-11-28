"""
QV4::String binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::String to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class String(QV4.StringOrSymbol):
  """
  The cute side of Qt's QV4::String: a plain Python object standing in front
  of one C++ QV4::String.

  It is built on the cute 'QV4::StringOrSymbol', as Qt's QV4::String is built
  on Qt's QV4::StringOrSymbol, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::String that has a ritual and that Python can
  call so far, 15 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'subtype', 'setSubtype', 'equals', 'isEqualTo',
  'lessThan', 'toQString', 'hashValue', 'createPropertyKeyImpl',
  'startsWithUpper', 'virtualIsEqualTo', 'virtualGetLength'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::String::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'uint QV4::String::toUInt(bool *ok) const': takes a number to change
    where it is.
  - Qt's 'uint QV4::String::createHashValue(const QChar *ch, int length, uint
    *subtype)': takes a number to change where it is.
  - Qt's 'uint QV4::String::createHashValueDisallowingArrayIndex(const QChar
    *ch, int length, uint *subtype)': takes a number to change where it is.
  - Qt's 'uint QV4::String::createHashValue(const char *ch, int length, uint
    *subtype)': takes a number to change where it is.

  What has no ritual
  ------------------

  5 of the 25 functions Qt declares: 3 forbidden; 1 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QV4::String is created at the first use, not by
    'QV4::String(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::String.
  - Each name of Qt's QV4::String that has no cute function yet,
    'calculateHashValue', 'createHashValue',
    'createHashValueDisallowingArrayIndex', 'toUInt', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::String, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class IndicesBehavior(CuteNum):
    """
    The enum 'QV4::String::IndicesBehavior' of Qt, with the 2 names Qt gives
    in it.
    """

    Default = Kee[int](0)
    DisallowArrayIndex = Kee[int](1)

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
    *QV4::String::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-string.html#defaultInternalClass

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
    #  Heap::InternalClass *QV4::String::defaultInternalClass(QV4::EngineBase
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV46String20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, QV4.Managed)
  @overload(QV4.Managed, NoneType)
  @overload(NoneType, QV4.Managed)
  @overload(NoneType, NoneType)
  def virtualIsEqualTo(
      that: Optional[QV4.Managed],
      o: Optional[QV4.Managed],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::String::virtualIsEqualTo(Managed *that, Managed
    *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#virtualIsEqualTo

    Parameters
    ----------

    that : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    o : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::String::virtualIsEqualTo(Managed *that, Managed *o)
    return Rituals.call(
        'ritual_ZN3QV46String16virtualIsEqualToEPNS_7ManagedES2_',
        CuteMixin._addressOf(that), CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(QV4.Managed)
  @overload(NoneType)
  def virtualGetLength(m: Optional[QV4.Managed]) -> int:
    """
    Calls Qt's 'qint64 QV4::String::virtualGetLength(const Managed *m)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#virtualGetLength

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QV4::String::virtualGetLength(const Managed *m)
    return Rituals.call(
        'ritual_ZN3QV46String16virtualGetLengthEPKNS_7ManagedE',
        CuteMixin._addressOf(m),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::String'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'QV4::Heap::String *QV4::String::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::String *QV4::String::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV46String11d_uncheckedEv')
    return QV4.Heap.String._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'QV4::Heap::String *QV4::String::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#d

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::String *QV4::String::d() const
    address = self.uglySide.call('ritual_ZNK3QV46String1dEv')
    return QV4.Heap.String._cuteAt(address)

  def subtype(self) -> int:
    """
    Calls Qt's 'uchar QV4::String::subtype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#subtype
    """
    #  uchar QV4::String::subtype() const
    return self.uglySide.call('ritual_ZNK3QV46String7subtypeEv')

  @overload(THIS)
  @overload(NoneType)
  def equals(self, other: Optional[String]) -> bool:
    """
    Calls Qt's 'bool QV4::String::equals(String *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#equals

    Parameters
    ----------

    other : Optional[String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::String::equals(String *other) const
    return self.uglySide.call(
        'ritual_ZNK3QV46String6equalsEPS0_', self._addressOf(other),
    )

  @overload(THIS)
  @overload(NoneType)
  def isEqualTo(self, other: Optional[String]) -> bool:
    """
    Calls Qt's 'bool QV4::String::isEqualTo(const String *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#isEqualTo

    Parameters
    ----------

    other : Optional[String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::String::isEqualTo(const String *other) const
    return self.uglySide.call(
        'ritual_ZNK3QV46String9isEqualToEPKS0_', self._addressOf(other),
    )

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::String::toQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::String::toQString() const
    return self.uglySide.call('ritual_ZNK3QV46String9toQStringEv')

  def hashValue(self) -> int:
    """
    Calls Qt's 'unsigned int QV4::String::hashValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#hashValue
    """
    #  unsigned int QV4::String::hashValue() const
    return self.uglySide.call('ritual_ZNK3QV46String9hashValueEv')

  def startsWithUpper(self) -> bool:
    """
    Calls Qt's 'bool QV4::String::startsWithUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#startsWithUpper
    """
    #  bool QV4::String::startsWithUpper() const
    return self.uglySide.call('ritual_ZNK3QV46String15startsWithUpperEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSubtype(self, subtype: int) -> None:
    """
    Calls Qt's 'void QV4::String::setSubtype(uchar subtype) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#setSubtype

    Parameters
    ----------

    subtype : int
      Passed on as it is.
    """
    #  void QV4::String::setSubtype(uchar subtype) const
    self.uglySide.call('ritual_ZNK3QV46String10setSubtypeEh', subtype)

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
    Calls Qt's 'void QV4::String::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#__dataTest
    """
    #  void QV4::String::__dataTest()
    self.uglySide.call('ritual_ZN3QV46String10__dataTestEv')

  @overload(THIS)
  @overload(NoneType)
  def lessThan(self, other: Optional[String]) -> bool:
    """
    Calls Qt's 'bool QV4::String::lessThan(const String *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-string.html#lessThan

    Parameters
    ----------

    other : Optional[String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::String::lessThan(const String *other)
    return self.uglySide.call(
        'ritual_ZN3QV46String8lessThanEPKS0_', self._addressOf(other),
    )

  def createPropertyKeyImpl(self) -> None:
    """
    Calls Qt's 'void QV4::String::createPropertyKeyImpl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-string.html#createPropertyKeyImpl
    """
    #  void QV4::String::createPropertyKeyImpl() const
    self.uglySide.call('ritual_ZNK3QV46String21createPropertyKeyImplEv')

  @staticmethod
  def calculateHashValue(*__, **_) -> Never:
    """
    Qt's 'QV4::String::calculateHashValue': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.String.calculateHashValue' has no cute function yet. Qt's "
        "'QV4::String::calculateHashValue': a template: a pattern and no "
        "single function.")

  @staticmethod
  def createHashValue(*__, **_) -> Never:
    """
    - Qt's 'uint QV4::String::createHashValue(const QChar *ch, int length,
      uint *subtype)': takes a number to change where it is.
    - Qt's 'uint QV4::String::createHashValue(const char *ch, int length,
      uint *subtype)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.String.createHashValue' has no cute function yet. Qt's 'uint "
        "QV4::String::createHashValue(const QChar *ch, int length, uint "
        "*subtype)': takes a number to change where it is. Qt's 'uint "
        "QV4::String::createHashValue(const char *ch, int length, uint "
        "*subtype)': takes a number to change where it is.")

  @staticmethod
  def createHashValueDisallowingArrayIndex(*__, **_) -> Never:
    """
    Qt's 'uint QV4::String::createHashValueDisallowingArrayIndex(const QChar
    *ch, int length, uint *subtype)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.String.createHashValueDisallowingArrayIndex' has no cute "
        "function yet. Qt's 'uint "
        "QV4::String::createHashValueDisallowingArrayIndex(const QChar *ch, "
        "int length, uint *subtype)': takes a number to change where it is.")

  @staticmethod
  def toUInt(*__, **_) -> Never:
    """
    Qt's 'uint QV4::String::toUInt(bool *ok) const': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QV4.String.toUInt' has no cute function yet. Qt's 'uint "
        "QV4::String::toUInt(bool *ok) const': takes a number to change "
        "where it is.")
