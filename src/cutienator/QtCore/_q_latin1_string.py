"""
QLatin1String binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlatin1stringview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView, QChar, QLatin1Char
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLatin1String(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLatin1String: a plain Python object standing in
  front of one C++ QLatin1String.

  C++ hands a QLatin1String around as a copy, so every C++ QLatin1String
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLatin1String that has a ritual and that Python can
  call so far, 44 names in all: 'toString', 'toUtf8', 'latin1', 'size',
  'data', 'constData', 'constBegin', 'constEnd', 'first', 'last', 'length',
  'isNull', 'isEmpty', 'empty', 'at', '__getitem__', 'front', 'back',
  'compare', 'startsWith', 'endsWith', 'indexOf', 'contains', 'lastIndexOf',
  'count', 'max_size', 'maxSize', 'mid', 'left', 'right', 'sliced',
  'chopped', 'chop', 'truncate', 'trimmed', '__eq__', '__ne__', '__lt__',
  '__gt__', '__le__', '__ge__', 'verify', 'compare_helper', 'equal_helper'.
  It can be made from Python, in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'short QLatin1String::toShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ushort QLatin1String::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'int QLatin1String::toInt(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'uint QLatin1String::toUInt(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'long QLatin1String::toLong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ulong QLatin1String::toULong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QLatin1String::toLongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'qulonglong QLatin1String::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'float QLatin1String::toFloat(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'double QLatin1String::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'bool operator==(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator==(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator!=(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator!=(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator<(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator>(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator>(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator<(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator<=(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator>=(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator>=(const QChar &lhs, const QLatin1StringView &rhs)':
    takes in Python what 'bool operator<=(const QLatin1StringView &lhs, const
    QChar &rhs)' takes.
  - Qt's 'bool operator==(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator==(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator!=(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator!=(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator<(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator>(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator<=(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>=(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator>=(const QStringView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<=(const QLatin1StringView
    &lhs, const QStringView &rhs)' takes.
  - Qt's 'bool operator==(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator==(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator!=(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator!=(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator<(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator>(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator<=(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>=(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator>=(const QByteArrayView &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<=(const QLatin1StringView
    &lhs, const QByteArrayView &rhs)' takes.
  - Qt's 'bool operator==(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator==(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'bool operator!=(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator!=(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'bool operator<(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'bool operator>(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'bool operator<=(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator>=(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'bool operator>=(const QByteArray &lhs, const QLatin1StringView
    &rhs)': takes in Python what 'bool operator<=(const QLatin1StringView
    &lhs, const QByteArray &rhs)' takes.
  - Qt's 'QLatin1String::~QLatin1String()': the destructor: Python removes
    its C++ QLatin1String by it, and has no other use for it.

  What has no ritual
  ------------------

  26 of the 163 functions Qt declares: 23 takes or gives a type that cannot
  be passed yet; 3 a template.

  What to expect
  --------------

  - The C++ QLatin1String is created at the first use, not by
    'QLatin1String(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLatin1String back gives a copy the ritual made for
    Python, in a new cute QLatin1String.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxSize() -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::maxSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#maxSize
    """
    #  qsizetype QLatin1String::maxSize()
    return Rituals.call('ritual_ZN13QLatin1String7maxSizeEv')

  @staticmethod
  @overload(THIS, str)
  @overload(THIS, NoneType)
  def compare_helper(s1: QLatin1String, s2: Optional[str]) -> int:
    """
    Calls Qt's 'int QLatin1String::compare_helper(const QLatin1StringView
    &s1, const char *s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare_helper

    Parameters
    ----------

    s1 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    s2 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QLatin1String::compare_helper(const QLatin1StringView &s1, const
    #      char *s2)
    return Rituals.call(
        'ritual_ZN13QLatin1String14compare_helperERKS_PKc',
        CuteMixin._valueOf(s1), CuteMixin._bytesOf(s2),
    )

  @staticmethod
  @overload(THIS, str, int)
  @overload(THIS, NoneType, int)
  def compare_helper(s1: QLatin1String, s2: Optional[str], len: int) -> int:
    """
    Calls Qt's 'int QLatin1String::compare_helper(const QLatin1StringView
    &s1, const char *s2, qsizetype len)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare_helper

    Parameters
    ----------

    s1 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    s2 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  int QLatin1String::compare_helper(const QLatin1StringView &s1, const
    #      char *s2, qsizetype len)
    return Rituals.call(
        'ritual_ZN13QLatin1String14compare_helperERKS_PKcx',
        CuteMixin._valueOf(s1), CuteMixin._bytesOf(s2), len,
    )

  @staticmethod
  @overload(QChar, int, THIS)
  @overload(NoneType, int, THIS)
  @overload(QChar, int, THIS, Qt.CaseSensitivity)
  @overload(NoneType, int, THIS, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      s2: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QLatin1String::compare_helper(const QChar *data1,
    qsizetype length1, QLatin1StringView s2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    s2 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QLatin1String::compare_helper(const QChar *data1, qsizetype
    #      length1, QLatin1StringView s2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN13QLatin1String14compare_helperEPK5QCharxS_N2Qt15CaseSens'
        'itivityE',
        CuteMixin._addressOf(data1), length1, CuteMixin._valueOf(s2),
        cs.value,
    )

  @staticmethod
  @overload(THIS, str, int)
  @overload(THIS, NoneType, int)
  def equal_helper(s1: QLatin1String, s2: Optional[str], len: int) -> bool:
    """
    Calls Qt's 'bool QLatin1String::equal_helper(QLatin1StringView s1, const
    char *s2, qsizetype len)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#equal_helper

    Parameters
    ----------

    s1 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    s2 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  bool QLatin1String::equal_helper(QLatin1StringView s1, const char *s2,
    #      qsizetype len)
    return Rituals.call(
        'ritual_ZN13QLatin1String12equal_helperES_PKcx',
        CuteMixin._valueOf(s1), CuteMixin._bytesOf(s2), len,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLatin1String'

  #  Qt's '~QLatin1String()'. Naming it makes this a value class: Python owns
  #  every C++ QLatin1String behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QLatin1StringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QLatin1String::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLatin1String::toString() const
    return self.uglySide.call('ritual_ZNK13QLatin1String8toStringEv')

  def toUtf8(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLatin1String::toUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#toUtf8

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLatin1String::toUtf8() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String6toUtf8Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def latin1(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLatin1String::latin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#latin1

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLatin1String::latin1() const
    chars = self.uglySide.call('ritual_ZNK13QLatin1String6latin1Ev')
    return None if chars is None else chars.decode()

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#size
    """
    #  qsizetype QLatin1String::size() const
    return self.uglySide.call('ritual_ZNK13QLatin1String4sizeEv')

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLatin1String::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLatin1String::data() const
    chars = self.uglySide.call('ritual_ZNK13QLatin1String4dataEv')
    return None if chars is None else chars.decode()

  def constData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLatin1String::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#constData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLatin1String::constData() const
    chars = self.uglySide.call('ritual_ZNK13QLatin1String9constDataEv')
    return None if chars is None else chars.decode()

  def constBegin(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLatin1String::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#constBegin

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLatin1String::constBegin() const
    chars = self.uglySide.call('ritual_ZNK13QLatin1String10constBeginEv')
    return None if chars is None else chars.decode()

  def constEnd(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QLatin1String::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#constEnd

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLatin1String::constEnd() const
    chars = self.uglySide.call('ritual_ZNK13QLatin1String8constEndEv')
    return None if chars is None else chars.decode()

  @overload()
  def first(self) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#first

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::first() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String5firstEv')
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  @overload(int)
  def first(self, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::first(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String5firstEx', n)
    return QLatin1String._cuteOwning(address)

  @overload()
  def last(self) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#last

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::last() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String4lastEv')
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  @overload(int)
  def last(self, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::last(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String4lastEx', n)
    return QLatin1String._cuteOwning(address)

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#length
    """
    #  qsizetype QLatin1String::length() const
    return self.uglySide.call('ritual_ZNK13QLatin1String6lengthEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QLatin1String::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#isNull
    """
    #  bool QLatin1String::isNull() const
    return self.uglySide.call('ritual_ZNK13QLatin1String6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QLatin1String::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#isEmpty
    """
    #  bool QLatin1String::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QLatin1String7isEmptyEv')

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QLatin1String::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#empty
    """
    #  bool QLatin1String::empty() const
    return self.uglySide.call('ritual_ZNK13QLatin1String5emptyEv')

  @overload(int)
  def at(self, i: int) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::at(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String2atEx', i)
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  def front(self) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#front

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::front() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String5frontEv')
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  def back(self) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#back

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::back() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String4backEv')
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def compare(
      self,
      other: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QLatin1String::compare(QStringView other,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QLatin1String::compare(QStringView other, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7compareE11QStringViewN2Qt15CaseSensitivi'
        'tyE',
        other, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def compare(
      self,
      other: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QLatin1String::compare(QLatin1StringView other,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare

    Parameters
    ----------

    other : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QLatin1String::compare(QLatin1StringView other,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7compareES_N2Qt15CaseSensitivityE',
        self._valueOf(other), cs.value,
    )

  @overload(QChar)
  def compare(self, c: QChar) -> int:
    """
    Calls Qt's 'int QLatin1String::compare(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  int QLatin1String::compare(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7compareE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def compare(self, c: QChar, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'int QLatin1String::compare(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#compare

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  int QLatin1String::compare(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7compareE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::startsWith(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#startsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::startsWith(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String10startsWithE11QStringViewN2Qt15CaseSensi'
        'tivityE',
        s, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::startsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#startsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::startsWith(QLatin1StringView s,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String10startsWithES_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  def startsWith(self, c: QChar) -> bool:
    """
    Calls Qt's 'bool QLatin1String::startsWith(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QLatin1String::startsWith(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String10startsWithE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def startsWith(self, c: QChar, cs: Qt.CaseSensitivity) -> bool:
    """
    Calls Qt's 'bool QLatin1String::startsWith(QChar c, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  bool QLatin1String::startsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String10startsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def endsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::endsWith(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#endsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::endsWith(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8endsWithE11QStringViewN2Qt15CaseSensitiv'
        'ityE',
        s, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def endsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::endsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#endsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::endsWith(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8endsWithES_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  def endsWith(self, c: QChar) -> bool:
    """
    Calls Qt's 'bool QLatin1String::endsWith(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QLatin1String::endsWith(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8endsWithE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def endsWith(self, c: QChar, cs: Qt.CaseSensitivity) -> bool:
    """
    Calls Qt's 'bool QLatin1String::endsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  bool QLatin1String::endsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8endsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      s: str,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::indexOf(QStringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#indexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::indexOf(QStringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7indexOfE11QStringViewxN2Qt15CaseSensitiv'
        'ityE',
        s, from_, cs.value,
    )

  @overload(THIS)
  @overload(THIS, int)
  @overload(THIS, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      s: QLatin1String,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::indexOf(QLatin1StringView s,
    qsizetype from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#indexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::indexOf(QLatin1StringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7indexOfES_xN2Qt15CaseSensitivityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(QChar)
  @overload(QChar, int)
  def indexOf(self, c: QChar, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::indexOf(QChar c, qsizetype from)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#indexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QLatin1String::indexOf(QChar c, qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7indexOfE5QCharx', self._valueOf(c), from_,
    )

  @overload(QChar, int, Qt.CaseSensitivity)
  def indexOf(self, c: QChar, from_: int, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::indexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#indexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  qsizetype QLatin1String::indexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String7indexOfE5QCharxN2Qt15CaseSensitivityE',
        self._valueOf(c), from_, cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def contains(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::contains(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#contains

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::contains(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8containsE11QStringViewN2Qt15CaseSensitiv'
        'ityE',
        s, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def contains(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::contains(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#contains

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::contains(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8containsES_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def contains(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QLatin1String::contains(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#contains

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QLatin1String::contains(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String8containsE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::lastIndexOf(QStringView s,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE11QStringViewN2Qt15CaseSens'
        'itivityE',
        s, cs.value,
    )

  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: str,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QStringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::lastIndexOf(QStringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE11QStringViewxN2Qt15CaseSen'
        'sitivityE',
        s, from_, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::lastIndexOf(QLatin1StringView s,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfES_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(THIS, int)
  @overload(THIS, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QLatin1StringView s,
    qsizetype from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::lastIndexOf(QLatin1StringView s, qsizetype
    #      from, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfES_xN2Qt15CaseSensitivityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(QChar)
  def lastIndexOf(self, c: QChar) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  qsizetype QLatin1String::lastIndexOf(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def lastIndexOf(self, c: QChar, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QChar c,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  qsizetype QLatin1String::lastIndexOf(QChar c, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE5QCharN2Qt15CaseSensitivity'
        'E',
        self._valueOf(c), cs.value,
    )

  @overload(QChar, int)
  def lastIndexOf(self, c: QChar, from_: int) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is.
    """
    #  qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE5QCharx',
        self._valueOf(c), from_,
    )

  @overload(QChar, int, Qt.CaseSensitivity)
  def lastIndexOf(self, c: QChar, from_: int, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String11lastIndexOfE5QCharxN2Qt15CaseSensitivit'
        'yE',
        self._valueOf(c), from_, cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def count(
      self,
      str: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::count(QStringView str,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#count

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::count(QStringView str, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String5countE11QStringViewN2Qt15CaseSensitivity'
        'E',
        str, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def count(
      self,
      str: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::count(QLatin1StringView str,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#count

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::count(QLatin1StringView str,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String5countES_N2Qt15CaseSensitivityE',
        self._valueOf(str), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def count(
      self,
      ch: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::count(QChar ch, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#count

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QLatin1String::count(QChar ch, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK13QLatin1String5countE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(ch), cs.value,
    )

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QLatin1String::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#max_size
    """
    #  qsizetype QLatin1String::max_size() const
    return self.uglySide.call('ritual_ZNK13QLatin1String8max_sizeEv')

  @overload(int)
  @overload(int, int)
  def mid(self, pos: int, n: int = -1) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::mid(qsizetype pos, qsizetype
    n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#mid

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::mid(qsizetype pos, qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String3midExx', pos, n)
    return QLatin1String._cuteOwning(address)

  @overload(int)
  def left(self, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::left(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String4leftEx', n)
    return QLatin1String._cuteOwning(address)

  @overload(int)
  def right(self, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::right(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String5rightEx', n)
    return QLatin1String._cuteOwning(address)

  @overload(int)
  def sliced(self, pos: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::sliced(qsizetype pos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::sliced(qsizetype pos) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String6slicedEx', pos)
    return QLatin1String._cuteOwning(address)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::sliced(qsizetype pos,
    qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::sliced(qsizetype pos, qsizetype n)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QLatin1String6slicedExx', pos, n,
    )
    return QLatin1String._cuteOwning(address)

  @overload(int)
  def chopped(self, n: int) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::chopped(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#chopped

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::chopped(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK13QLatin1String7choppedEx', n)
    return QLatin1String._cuteOwning(address)

  def trimmed(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1String::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#trimmed

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1String::trimmed() const
    address = self.uglySide.call('ritual_ZNK13QLatin1String7trimmedEv')
    return QLatin1String._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __getitem__(self, i: int) -> QLatin1Char:
    """
    Calls Qt's 'QLatin1Char QLatin1String::operator[](qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QLatin1Char
      A new cute QLatin1Char around the copy Qt gave back. Python owns it.
    """
    #  QLatin1Char QLatin1String::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK13QLatin1StringixEx', i)
    from . import QLatin1Char
    return QLatin1Char._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator==

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator==(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __eq__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator==

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator==(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __eq__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator==

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator==(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __eq__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator==

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator==(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __eq__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator==(const QLatin1StringView &lhs, const
    QByteArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator==

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator==(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZeqRK13QLatin1StringRK10QByteArray',
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
  def __ne__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator!=

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator!=(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __ne__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator!=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator!=(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZneRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __ne__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator!=

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator!=(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZneRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __ne__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator!=

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator!=(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __ne__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLatin1StringView &lhs, const
    QByteArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator!=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator!=(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZneRK13QLatin1StringRK10QByteArray',
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

  @overload(THIS)
  def __lt__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator<(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __lt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZltRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __lt__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZltRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __lt__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator<(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __lt__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator<(const QLatin1StringView &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator<(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZltRK13QLatin1StringRK10QByteArray',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator>(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __gt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __gt__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator>(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __gt__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator>(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __gt__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator>(const QLatin1StringView &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator>(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZgtRK13QLatin1StringRK10QByteArray',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<=

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator<=(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZleRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __le__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<=(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZleRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __le__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<=

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator<=(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZleRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __le__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<=

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator<=(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZleRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __le__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator<=(const QLatin1StringView &lhs, const
    QByteArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator<=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator<=(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZleRK13QLatin1StringRK10QByteArray',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QLatin1String) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1StringView &lhs, const
    QLatin1StringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>=

    Parameters
    ----------

    rhs : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool operator>=(const QLatin1StringView &lhs, const QLatin1StringView
    #      &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QLatin1StringS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __ge__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1StringView &lhs, const QChar
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>=(const QLatin1StringView &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QLatin1StringRK5QChar',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(str)
  def __ge__(self, rhs: str) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1StringView &lhs, const
    QStringView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>=

    Parameters
    ----------

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool operator>=(const QLatin1StringView &lhs, const QStringView &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QLatin1StringRK11QStringView',
        CuteMixin._valueOf(self), rhs,
    )

  @overload(QByteArrayView)
  def __ge__(self, rhs: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1StringView &lhs, const
    QByteArrayView &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>=

    Parameters
    ----------

    rhs : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool operator>=(const QLatin1StringView &lhs, const QByteArrayView
    #      &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QLatin1StringRK14QByteArrayView',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QByteArray)
  def __ge__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator>=(const QLatin1StringView &lhs, const
    QByteArray &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#operator>=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator>=(const QLatin1StringView &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZgeRK13QLatin1StringRK10QByteArray',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QLatin1String::QLatin1String()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String
    """
    #  QLatin1String::QLatin1String()
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1Ev',
    ))

  @overload(str)
  @overload(NoneType)
  def __init__(self, s: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QLatin1String::QLatin1String(const char
    *s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QLatin1String::QLatin1String(const char *s)
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1EPKc', self._bytesOf(s),
    ))

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def __init__(self, f: Optional[str], l: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QLatin1String::QLatin1String(const char
    *f, const char *l)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String

    Parameters
    ----------

    f : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    l : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QLatin1String::QLatin1String(const char *f, const char *l)
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1EPKcS1_',
        self._bytesOf(f), self._bytesOf(l),
    ))

  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, s: Optional[str], sz: int) -> None:
    """
    Notes what was given, for Qt's 'QLatin1String::QLatin1String(const char
    *s, qsizetype sz)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    sz : int
      Passed on as it is.
    """
    #  QLatin1String::QLatin1String(const char *s, qsizetype sz)
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1EPKcx', self._bytesOf(s), sz,
    ))

  @overload(QByteArray)
  def __init__(self, s: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QLatin1String::QLatin1String(const
    QByteArray &s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String

    Parameters
    ----------

    s : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QLatin1String::QLatin1String(const QByteArray &s)
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1ERK10QByteArray', self._valueOf(s),
    ))

  @overload(QByteArrayView)
  def __init__(self, s: QByteArrayView) -> None:
    """
    Notes what was given, for Qt's
    'QLatin1String::QLatin1String(QByteArrayView s)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#QLatin1String

    Parameters
    ----------

    s : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QLatin1String::QLatin1String(QByteArrayView s)
    self._noteCreation(QLatin1String, lambda: Rituals.call(
        'ritual_ZN13QLatin1StringC1E14QByteArrayView', self._valueOf(s),
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

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QLatin1String::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QLatin1String::chop(qsizetype n)
    self.uglySide.call('ritual_ZN13QLatin1String4chopEx', n)

  @overload(int)
  def truncate(self, n: int) -> None:
    """
    Calls Qt's 'void QLatin1String::truncate(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#truncate

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QLatin1String::truncate(qsizetype n)
    self.uglySide.call('ritual_ZN13QLatin1String8truncateEx', n)

  @overload(int)
  @overload(int, int)
  def verify(self, pos: int, n: int = 1) -> None:
    """
    Calls Qt's 'void QLatin1String::verify(qsizetype pos, qsizetype n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1string.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLatin1String::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK13QLatin1String6verifyExx', pos, n)
