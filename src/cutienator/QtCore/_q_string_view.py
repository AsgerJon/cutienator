"""
QStringView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QChar, QLatin1String, QRegularExpression
  from . import QRegularExpressionMatch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QLatin1String = WAIT['QLatin1String']
  QRegularExpression = WAIT['QRegularExpression']
  QRegularExpressionMatch = WAIT['QRegularExpressionMatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringView(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringView: a plain Python object standing in front
  of one C++ QStringView.

  C++ hands a QStringView around as a copy, so every C++ QStringView behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringView that has a ritual and that Python can
  call so far, 43 names in all: 'lengthHelperPointer', 'toString', 'maxSize',
  'size', '__getitem__', 'toLatin1', 'toUtf8', 'toLocal8Bit', 'at', 'mid',
  'left', 'right', 'first', 'last', 'sliced', 'chopped', 'truncate', 'chop',
  'trimmed', 'compare', 'localeAwareCompare', 'startsWith', 'endsWith',
  'indexOf', 'contains', 'count', 'lastIndexOf', 'isRightToLeft',
  'isValidUtf16', 'isUpper', 'isLower', 'split', 'empty', 'front', 'back',
  'max_size', 'isNull', 'isEmpty', 'length', 'verify',
  'compare_single_char_helper', 'equal_helper', 'compare_helper'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const storage_type *QStringView::castHelper(const storage_type
    *str)': names 'QStringView::storage_type', which has no cute class yet.
  - Qt's 'QStringView::QStringView(std::nullptr_t a0)': takes in Python what
    'QStringView::QStringView()' takes.
  - Qt's 'const_pointer QStringView::data() const': gives 'value_type', which
    has no cute class yet.
  - Qt's 'const_pointer QStringView::constData() const': gives 'value_type',
    which has no cute class yet.
  - Qt's 'const storage_type *QStringView::utf16() const': gives 'unsigned
    short', which has no cute class yet.
  - Qt's 'QList<uint> QStringView::toUcs4() const': gives a type Python has
    no way to take yet.
  - Qt's 'QStringView &QStringView::slice(qsizetype pos)': gives a type
    Python has no way to take yet.
  - Qt's 'QStringView &QStringView::slice(qsizetype pos, qsizetype n)': gives
    a type Python has no way to take yet.
  - Qt's 'int QStringView::compare(QUtf8StringView other, Qt::CaseSensitivity
    cs) const': takes a type Python has no way to hand over yet.
  - Qt's 'short QStringView::toShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ushort QStringView::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'int QStringView::toInt(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'uint QStringView::toUInt(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'long QStringView::toLong(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'ulong QStringView::toULong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QStringView::toLongLong(bool *ok, int base) const': takes
    a number to change where it is.
  - Qt's 'qulonglong QStringView::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'float QStringView::toFloat(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'double QStringView::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'qsizetype QStringView::toWCharArray(wchar_t *array) const': names
    'wchar_t', which has no cute class yet.
  - Qt's 'bool operator==(const QStringView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QStringView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QStringView &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QStringView &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QStringView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QStringView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QStringView &lhs, const QChar &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QChar &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'const_iterator QStringView::begin() const': gives 'value_type',
    which has no cute class yet.
  - Qt's 'const_iterator QStringView::end() const': gives 'value_type', which
    has no cute class yet.
  - Qt's 'const_iterator QStringView::cbegin() const': gives 'value_type',
    which has no cute class yet.
  - Qt's 'const_iterator QStringView::cend() const': gives 'value_type',
    which has no cute class yet.
  - Qt's 'const_reverse_iterator QStringView::rbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringView::rend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringView::crbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringView::crend() const': gives a type
    Python has no way to take yet.
  - Qt's 'std::u16string_view QStringView::operator basic_string_view()
    const': an operator Python has no name for.
  - Qt's 'const_iterator QStringView::constBegin() const': gives
    'value_type', which has no cute class yet.
  - Qt's 'const_iterator QStringView::constEnd() const': gives 'value_type',
    which has no cute class yet.
  - Qt's 'bool operator==(const QStringView &lhs, const QByteArrayView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QStringView &lhs, const QByteArrayView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QStringView &lhs, const QByteArrayView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QStringView &lhs, const QByteArrayView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QStringView &lhs, const QByteArrayView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QStringView &lhs, const QByteArrayView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QByteArrayView &lhs, const QStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QByteArrayView &lhs, const QStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QByteArrayView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QByteArrayView &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QByteArrayView &lhs, const QStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QByteArrayView &lhs, const QStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QStringView &lhs, const QByteArray &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QByteArray &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator==(const QStringView &lhs, const char *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QStringView &lhs, const char *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QStringView &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QStringView &lhs, const char *const &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QStringView &lhs, const char *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QStringView &lhs, const char *const &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator==(const char *const &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const char *const &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const char *const &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator>(const char *const &lhs, const QStringView &rhs)': an
    operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const char *const &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const char *const &lhs, const QStringView &rhs)':
    an operator between other classes, written inside this one.
  - Qt's 'QStringView::~QStringView()': the destructor: Python removes its
    C++ QStringView by it, and has no other use for it.

  What has no ritual
  ------------------

  12 of the 171 functions Qt declares: 12 a template.

  What to expect
  --------------

  - The C++ QStringView is created at the first use, not by
    'QStringView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringView back gives a copy the ritual made for
    Python, in a new cute QStringView.
  - Each name of Qt's QStringView that has no cute function yet, 'arg',
    'begin', 'castHelper', 'cbegin', 'cend', 'constBegin', 'constData',
    'constEnd', 'crbegin', 'crend', 'data', 'end', 'fromArray', 'rbegin',
    'rend', 'slice', 'toDouble', 'toFloat', 'toInt', 'toLong', 'toLongLong',
    'toShort', 'toUInt', 'toULong', 'toULongLong', 'toUShort', 'toUcs4',
    'toWCharArray', 'tokenize', 'utf16', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QChar)
  @overload(NoneType)
  def lengthHelperPointer(str: Optional[QChar]) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lengthHelperPointer(const QChar
    *str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringview.html#lengthHelperPointer

    Parameters
    ----------

    str : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QStringView::lengthHelperPointer(const QChar *str)
    return Rituals.call(
        'ritual_ZN11QStringView19lengthHelperPointerEPK5QChar',
        CuteMixin._addressOf(str),
    )

  @staticmethod
  def maxSize() -> int:
    """
    Calls Qt's 'qsizetype QStringView::maxSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#maxSize
    """
    #  qsizetype QStringView::maxSize()
    return Rituals.call('ritual_ZN11QStringView7maxSizeEv')

  @staticmethod
  @overload(str, str, int)
  @overload(str, NoneType, int)
  def equal_helper(sv: str, data: Optional[str], len: int) -> bool:
    """
    Calls Qt's 'bool QStringView::equal_helper(QStringView sv, const char
    *data, qsizetype len)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#equal_helper

    Parameters
    ----------

    sv : str
      Passed on as it is: a QString is made of it for the call.

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  bool QStringView::equal_helper(QStringView sv, const char *data,
    #      qsizetype len)
    return Rituals.call(
        'ritual_ZN11QStringView12equal_helperES_PKcx',
        sv, CuteMixin._bytesOf(data), len,
    )

  @staticmethod
  @overload(str, str, int)
  @overload(str, NoneType, int)
  def compare_helper(sv: str, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'int QStringView::compare_helper(QStringView sv, const char
    *data, qsizetype len)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#compare_helper

    Parameters
    ----------

    sv : str
      Passed on as it is: a QString is made of it for the call.

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  int QStringView::compare_helper(QStringView sv, const char *data,
    #      qsizetype len)
    return Rituals.call(
        'ritual_ZN11QStringView14compare_helperES_PKcx',
        sv, CuteMixin._bytesOf(data), len,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringView'

  #  Qt's '~QStringView()'. Naming it makes this a value class: Python owns
  #  every C++ QStringView behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QStringViewD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QStringView::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringView::toString() const
    return self.uglySide.call('ritual_ZNK11QStringView8toStringEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QStringView::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#size
    """
    #  qsizetype QStringView::size() const
    return self.uglySide.call('ritual_ZNK11QStringView4sizeEv')

  def toLatin1(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringView::toLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#toLatin1

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringView::toLatin1() const
    address = self.uglySide.call('ritual_ZNK11QStringView8toLatin1Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toUtf8(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringView::toUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#toUtf8

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringView::toUtf8() const
    address = self.uglySide.call('ritual_ZNK11QStringView6toUtf8Ev')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toLocal8Bit(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringView::toLocal8Bit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#toLocal8Bit

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringView::toLocal8Bit() const
    address = self.uglySide.call('ritual_ZNK11QStringView11toLocal8BitEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def at(self, n: int) -> QChar:
    """
    Calls Qt's 'QChar QStringView::at(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#at

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::at(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK11QStringView2atEx', n)
    from . import QChar
    return QChar._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def mid(self, pos: int, n: int = -1) -> str:
    """
    Calls Qt's 'QStringView QStringView::mid(qsizetype pos, qsizetype n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#mid

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::mid(qsizetype pos, qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView3midExx', pos, n)

  @overload(int)
  def left(self, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::left(qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView4leftEx', n)

  @overload(int)
  def right(self, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::right(qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView5rightEx', n)

  @overload(int)
  def first(self, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::first(qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView5firstEx', n)

  @overload()
  def first(self) -> QChar:
    """
    Calls Qt's 'QChar QStringView::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#first

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::first() const
    address = self.uglySide.call('ritual_ZNK11QStringView5firstEv')
    from . import QChar
    return QChar._cuteOwning(address)

  @overload(int)
  def last(self, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::last(qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView4lastEx', n)

  @overload()
  def last(self) -> QChar:
    """
    Calls Qt's 'QChar QStringView::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#last

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::last() const
    address = self.uglySide.call('ritual_ZNK11QStringView4lastEv')
    from . import QChar
    return QChar._cuteOwning(address)

  @overload(int)
  def sliced(self, pos: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::sliced(qsizetype pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::sliced(qsizetype pos) const
    return self.uglySide.call('ritual_ZNK11QStringView6slicedEx', pos)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::sliced(qsizetype pos, qsizetype n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::sliced(qsizetype pos, qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView6slicedExx', pos, n)

  @overload(int)
  def chopped(self, n: int) -> str:
    """
    Calls Qt's 'QStringView QStringView::chopped(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#chopped

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::chopped(qsizetype n) const
    return self.uglySide.call('ritual_ZNK11QStringView7choppedEx', n)

  def trimmed(self) -> str:
    """
    Calls Qt's 'QStringView QStringView::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#trimmed

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QStringView::trimmed() const
    return self.uglySide.call('ritual_ZNK11QStringView7trimmedEv')

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def compare(
      self,
      other: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringView::compare(QStringView other,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#compare

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringView::compare(QStringView other, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7compareES_N2Qt15CaseSensitivityE',
        other, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def compare(
      self,
      other: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringView::compare(QLatin1StringView other,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#compare

    Parameters
    ----------

    other : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringView::compare(QLatin1StringView other, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7compareE13QLatin1StringN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(other), cs.value,
    )

  @overload(QChar)
  def compare(self, c: QChar) -> int:
    """
    Calls Qt's 'int QStringView::compare(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#compare

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  int QStringView::compare(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7compareE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def compare(self, c: QChar, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'int QStringView::compare(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#compare

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  int QStringView::compare(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7compareE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  def localeAwareCompare(self, other: str) -> int:
    """
    Calls Qt's 'int QStringView::localeAwareCompare(QStringView other)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringview.html#localeAwareCompare

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QStringView::localeAwareCompare(QStringView other) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView18localeAwareCompareES_', other,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::startsWith(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#startsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::startsWith(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView10startsWithES_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::startsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#startsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::startsWith(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView10startsWithE13QLatin1StringN2Qt15CaseSensi'
        'tivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  def startsWith(self, c: QChar) -> bool:
    """
    Calls Qt's 'bool QStringView::startsWith(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QStringView::startsWith(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView10startsWithE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def startsWith(self, c: QChar, cs: Qt.CaseSensitivity) -> bool:
    """
    Calls Qt's 'bool QStringView::startsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  bool QStringView::startsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView10startsWithE5QCharN2Qt15CaseSensitivityE',
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
    Calls Qt's 'bool QStringView::endsWith(QStringView s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#endsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::endsWith(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8endsWithES_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def endsWith(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::endsWith(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#endsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::endsWith(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8endsWithE13QLatin1StringN2Qt15CaseSensitiv'
        'ityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  def endsWith(self, c: QChar) -> bool:
    """
    Calls Qt's 'bool QStringView::endsWith(QChar c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QStringView::endsWith(QChar c) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8endsWithE5QChar', self._valueOf(c),
    )

  @overload(QChar, Qt.CaseSensitivity)
  def endsWith(self, c: QChar, cs: Qt.CaseSensitivity) -> bool:
    """
    Calls Qt's 'bool QStringView::endsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  bool QStringView::endsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8endsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(QChar)
  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      c: QChar,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::indexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#indexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::indexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7indexOfE5QCharxN2Qt15CaseSensitivityE',
        self._valueOf(c), from_, cs.value,
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
    Calls Qt's 'qsizetype QStringView::indexOf(QStringView s, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#indexOf

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
    #  qsizetype QStringView::indexOf(QStringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7indexOfES_xN2Qt15CaseSensitivityE',
        s, from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      s: QLatin1String,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::indexOf(QLatin1StringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#indexOf

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
    #  qsizetype QStringView::indexOf(QLatin1StringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7indexOfE13QLatin1StringxN2Qt15CaseSensitiv'
        'ityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, QRegularExpressionMatch)
  @overload(QRegularExpression, int, NoneType)
  def indexOf(
      self,
      re: QRegularExpression,
      from_: int = 0,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::indexOf(const QRegularExpression &re,
    qsizetype from, QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#indexOf

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qsizetype QStringView::indexOf(const QRegularExpression &re, qsizetype
    #      from, QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView7indexOfERK18QRegularExpressionxP23QRegular'
        'ExpressionMatch',
        self._valueOf(re), from_, self._addressOf(rmatch),
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def contains(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::contains(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#contains

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::contains(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8containsE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def contains(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::contains(QStringView s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#contains

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::contains(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8containsES_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def contains(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::contains(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#contains

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringView::contains(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8containsE13QLatin1StringN2Qt15CaseSensitiv'
        'ityE',
        self._valueOf(s), cs.value,
    )

  @overload(QRegularExpression)
  @overload(QRegularExpression, QRegularExpressionMatch)
  @overload(QRegularExpression, NoneType)
  def contains(
      self,
      re: QRegularExpression,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStringView::contains(const QRegularExpression &re,
    QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#contains

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QStringView::contains(const QRegularExpression &re,
    #      QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView8containsERK18QRegularExpressionP23QRegular'
        'ExpressionMatch',
        self._valueOf(re), self._addressOf(rmatch),
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def count(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::count(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#count

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::count(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView5countE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def count(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::count(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#count

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::count(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView5countES_N2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def count(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::count(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#count

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::count(QLatin1StringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView5countE13QLatin1StringN2Qt15CaseSensitivity'
        'E',
        self._valueOf(s), cs.value,
    )

  @overload(QRegularExpression)
  def count(self, re: QRegularExpression) -> int:
    """
    Calls Qt's 'qsizetype QStringView::count(const QRegularExpression &re)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#count

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.
    """
    #  qsizetype QStringView::count(const QRegularExpression &re) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView5countERK18QRegularExpression',
        self._valueOf(re),
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QChar c,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::lastIndexOf(QChar c, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      c: QChar,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QChar c, qsizetype from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::lastIndexOf(QChar c, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfE5QCharxN2Qt15CaseSensitivityE',
        self._valueOf(c), from_, cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::lastIndexOf(QStringView s, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfES_N2Qt15CaseSensitivityE',
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
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QStringView s, qsizetype
    from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

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
    #  qsizetype QStringView::lastIndexOf(QStringView s, qsizetype from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfES_xN2Qt15CaseSensitivityE',
        s, from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QLatin1StringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  qsizetype QStringView::lastIndexOf(QLatin1StringView s,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfE13QLatin1StringN2Qt15CaseSens'
        'itivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      s: QLatin1String,
      from_: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(QLatin1StringView s,
    qsizetype from, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

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
    #  qsizetype QStringView::lastIndexOf(QLatin1StringView s, qsizetype
    #      from, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfE13QLatin1StringxN2Qt15CaseSen'
        'sitivityE',
        self._valueOf(s), from_, cs.value,
    )

  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, QRegularExpressionMatch)
  @overload(QRegularExpression, int, NoneType)
  def lastIndexOf(
      self,
      re: QRegularExpression,
      from_: int,
      rmatch: Optional[QRegularExpressionMatch] = None,
  ) -> int:
    """
    Calls Qt's 'qsizetype QStringView::lastIndexOf(const QRegularExpression
    &re, qsizetype from, QRegularExpressionMatch *rmatch) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#lastIndexOf

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    from_ : int
      Passed on as it is.

    rmatch : Optional[QRegularExpressionMatch]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qsizetype QStringView::lastIndexOf(const QRegularExpression &re,
    #      qsizetype from, QRegularExpressionMatch *rmatch) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView11lastIndexOfERK18QRegularExpressionxP23QRe'
        'gularExpressionMatch',
        self._valueOf(re), from_, self._addressOf(rmatch),
    )

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isRightToLeft
    """
    #  bool QStringView::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK11QStringView13isRightToLeftEv')

  def isValidUtf16(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isValidUtf16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isValidUtf16
    """
    #  bool QStringView::isValidUtf16() const
    return self.uglySide.call('ritual_ZNK11QStringView12isValidUtf16Ev')

  def isUpper(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isUpper
    """
    #  bool QStringView::isUpper() const
    return self.uglySide.call('ritual_ZNK11QStringView7isUpperEv')

  def isLower(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isLower
    """
    #  bool QStringView::isLower() const
    return self.uglySide.call('ritual_ZNK11QStringView7isLowerEv')

  @overload(str)
  @overload(str, Qt.SplitBehavior)
  @overload(str, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: str,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QList[QStringView]:
    """
    Calls Qt's 'QList<QStringView> QStringView::split(QStringView sep,
    Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#split

    Parameters
    ----------

    sep : str
      Passed on as it is: a QString is made of it for the call.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.

    Returns
    -------

    QList[QStringView]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStringView> QStringView::split(QStringView sep,
    #      Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK11QStringView5splitES_6QFlagsIN2Qt18SplitBehaviorFlagsEE'
        'NS1_15CaseSensitivityE',
        sep, behavior.value, cs.value,
    )
    return QList[QStringView]._cuteOwning(address)

  @overload(QChar)
  @overload(QChar, Qt.SplitBehavior)
  @overload(QChar, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: QChar,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QList[QStringView]:
    """
    Calls Qt's 'QList<QStringView> QStringView::split(QChar sep,
    Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#split

    Parameters
    ----------

    sep : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.

    Returns
    -------

    QList[QStringView]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStringView> QStringView::split(QChar sep, Qt::SplitBehavior
    #      behavior, Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK11QStringView5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFla'
        'gsEENS2_15CaseSensitivityE',
        self._valueOf(sep), behavior.value, cs.value,
    )
    return QList[QStringView]._cuteOwning(address)

  @overload(QRegularExpression)
  @overload(QRegularExpression, Qt.SplitBehavior)
  def split(
      self,
      sep: QRegularExpression,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
  ) -> QList[QStringView]:
    """
    Calls Qt's 'QList<QStringView> QStringView::split(const
    QRegularExpression &sep, Qt::SplitBehavior behavior) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#split

    Parameters
    ----------

    sep : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    behavior : Qt.SplitBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SplitBehavior.KeepEmptyParts.

    Returns
    -------

    QList[QStringView]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStringView> QStringView::split(const QRegularExpression &sep,
    #      Qt::SplitBehavior behavior) const
    address = self.uglySide.call(
        'ritual_ZNK11QStringView5splitERK18QRegularExpression6QFlagsIN2Qt18'
        'SplitBehaviorFlagsEE',
        self._valueOf(sep), behavior.value,
    )
    return QList[QStringView]._cuteOwning(address)

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QStringView::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#empty
    """
    #  bool QStringView::empty() const
    return self.uglySide.call('ritual_ZNK11QStringView5emptyEv')

  def front(self) -> QChar:
    """
    Calls Qt's 'QChar QStringView::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#front

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::front() const
    address = self.uglySide.call('ritual_ZNK11QStringView5frontEv')
    from . import QChar
    return QChar._cuteOwning(address)

  def back(self) -> QChar:
    """
    Calls Qt's 'QChar QStringView::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#back

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::back() const
    address = self.uglySide.call('ritual_ZNK11QStringView4backEv')
    from . import QChar
    return QChar._cuteOwning(address)

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QStringView::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#max_size
    """
    #  qsizetype QStringView::max_size() const
    return self.uglySide.call('ritual_ZNK11QStringView8max_sizeEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isNull
    """
    #  bool QStringView::isNull() const
    return self.uglySide.call('ritual_ZNK11QStringView6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QStringView::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#isEmpty
    """
    #  bool QStringView::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QStringView7isEmptyEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QStringView::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#length
    """
    #  qsizetype QStringView::length() const
    return self.uglySide.call('ritual_ZNK11QStringView6lengthEv')

  @overload(int)
  def compare_single_char_helper(self, diff: int) -> int:
    """
    Calls Qt's 'int QStringView::compare_single_char_helper(int diff) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringview.html#compare_single_char_helper

    Parameters
    ----------

    diff : int
      Passed on as it is.
    """
    #  int QStringView::compare_single_char_helper(int diff) const
    return self.uglySide.call(
        'ritual_ZNK11QStringView26compare_single_char_helperEi', diff,
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

  @overload(int)
  def __getitem__(self, n: int) -> QChar:
    """
    Calls Qt's 'QChar QStringView::operator[](qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#operator[]

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringView::operator[](qsizetype n) const
    address = self.uglySide.call('ritual_ZNK11QStringViewixEx', n)
    from . import QChar
    return QChar._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStringView::QStringView()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#QStringView
    """
    #  QStringView::QStringView()
    self._noteCreation(QStringView, lambda: Rituals.call(
        'ritual_ZN11QStringViewC1Ev',
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
  def truncate(self, n: int) -> None:
    """
    Calls Qt's 'void QStringView::truncate(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#truncate

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QStringView::truncate(qsizetype n)
    self.uglySide.call('ritual_ZN11QStringView8truncateEx', n)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QStringView::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QStringView::chop(qsizetype n)
    self.uglySide.call('ritual_ZN11QStringView4chopEx', n)

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QStringView::verify(qsizetype pos, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringview.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QStringView::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK11QStringView6verifyExx', pos, n)

  @staticmethod
  def arg(*__, **_) -> Never:
    """
    Qt's 'QStringView::arg': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QStringView.arg' has no cute function yet. Qt's "
        "'QStringView::arg': a template: a pattern and no single function.")

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::begin() const': gives 'value_type',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.begin' has no cute function yet. Qt's 'const_iterator "
        "QStringView::begin() const': gives 'value_type', which has no cute "
        "class yet.")

  @staticmethod
  def castHelper(*__, **_) -> Never:
    """
    - Qt's 'const storage_type *QStringView::castHelper(const storage_type
      *str)': names 'QStringView::storage_type', which has no cute class yet.
    - Qt's 'QStringView::castHelper': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QStringView.castHelper' has no cute function yet. Qt's 'const "
        "storage_type *QStringView::castHelper(const storage_type *str)': "
        "names 'QStringView::storage_type', which has no cute class yet. "
        "Qt's 'QStringView::castHelper': a template: a pattern and no "
        "single function.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::cbegin() const': gives 'value_type',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.cbegin' has no cute function yet. Qt's "
        "'const_iterator QStringView::cbegin() const': gives 'value_type', "
        "which has no cute class yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::cend() const': gives 'value_type',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.cend' has no cute function yet. Qt's 'const_iterator "
        "QStringView::cend() const': gives 'value_type', which has no cute "
        "class yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::constBegin() const': gives
    'value_type', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.constBegin' has no cute function yet. Qt's "
        "'const_iterator QStringView::constBegin() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    Qt's 'const_pointer QStringView::constData() const': gives 'value_type',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.constData' has no cute function yet. Qt's "
        "'const_pointer QStringView::constData() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::constEnd() const': gives 'value_type',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.constEnd' has no cute function yet. Qt's "
        "'const_iterator QStringView::constEnd() const': gives "
        "'value_type', which has no cute class yet.")

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringView::crbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringView::crbegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringView::crend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringView::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'const_pointer QStringView::data() const': gives 'value_type', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.data' has no cute function yet. Qt's 'const_pointer "
        "QStringView::data() const': gives 'value_type', which has no cute "
        "class yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const_iterator QStringView::end() const': gives 'value_type', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.end' has no cute function yet. Qt's 'const_iterator "
        "QStringView::end() const': gives 'value_type', which has no cute "
        "class yet.")

  @staticmethod
  def fromArray(*__, **_) -> Never:
    """
    Qt's 'QStringView::fromArray': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QStringView.fromArray' has no cute function yet. Qt's "
        "'QStringView::fromArray': a template: a pattern and no single "
        "function.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringView::rbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringView::rbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringView::rend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringView::rend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def slice(*__, **_) -> Never:
    """
    - Qt's 'QStringView &QStringView::slice(qsizetype pos)': gives a type
      Python has no way to take yet.
    - Qt's 'QStringView &QStringView::slice(qsizetype pos, qsizetype n)':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.slice' has no cute function yet. Qt's 'QStringView "
        "&QStringView::slice(qsizetype pos)': gives a type Python has no "
        "way to take yet. Qt's 'QStringView &QStringView::slice(qsizetype "
        "pos, qsizetype n)': gives a type Python has no way to take yet.")

  @staticmethod
  def toDouble(*__, **_) -> Never:
    """
    Qt's 'double QStringView::toDouble(bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toDouble' has no cute function yet. Qt's 'double "
        "QStringView::toDouble(bool *ok) const': takes a number to change "
        "where it is.")

  @staticmethod
  def toFloat(*__, **_) -> Never:
    """
    Qt's 'float QStringView::toFloat(bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toFloat' has no cute function yet. Qt's 'float "
        "QStringView::toFloat(bool *ok) const': takes a number to change "
        "where it is.")

  @staticmethod
  def toInt(*__, **_) -> Never:
    """
    Qt's 'int QStringView::toInt(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toInt' has no cute function yet. Qt's 'int "
        "QStringView::toInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toLong(*__, **_) -> Never:
    """
    Qt's 'long QStringView::toLong(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toLong' has no cute function yet. Qt's 'long "
        "QStringView::toLong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toLongLong(*__, **_) -> Never:
    """
    Qt's 'qlonglong QStringView::toLongLong(bool *ok, int base) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toLongLong' has no cute function yet. Qt's 'qlonglong "
        "QStringView::toLongLong(bool *ok, int base) const': takes a number "
        "to change where it is.")

  @staticmethod
  def toShort(*__, **_) -> Never:
    """
    Qt's 'short QStringView::toShort(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toShort' has no cute function yet. Qt's 'short "
        "QStringView::toShort(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUInt(*__, **_) -> Never:
    """
    Qt's 'uint QStringView::toUInt(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toUInt' has no cute function yet. Qt's 'uint "
        "QStringView::toUInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULong(*__, **_) -> Never:
    """
    Qt's 'ulong QStringView::toULong(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toULong' has no cute function yet. Qt's 'ulong "
        "QStringView::toULong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULongLong(*__, **_) -> Never:
    """
    Qt's 'qulonglong QStringView::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toULongLong' has no cute function yet. Qt's "
        "'qulonglong QStringView::toULongLong(bool *ok, int base) const': "
        "takes a number to change where it is.")

  @staticmethod
  def toUShort(*__, **_) -> Never:
    """
    Qt's 'ushort QStringView::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringView.toUShort' has no cute function yet. Qt's 'ushort "
        "QStringView::toUShort(bool *ok, int base) const': takes a number "
        "to change where it is.")

  @staticmethod
  def toUcs4(*__, **_) -> Never:
    """
    Qt's 'QList<uint> QStringView::toUcs4() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QStringView.toUcs4' has no cute function yet. Qt's 'QList<uint> "
        "QStringView::toUcs4() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def toWCharArray(*__, **_) -> Never:
    """
    Qt's 'qsizetype QStringView::toWCharArray(wchar_t *array) const': names
    'wchar_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.toWCharArray' has no cute function yet. Qt's "
        "'qsizetype QStringView::toWCharArray(wchar_t *array) const': names "
        "'wchar_t', which has no cute class yet.")

  @staticmethod
  def tokenize(*__, **_) -> Never:
    """
    Qt's 'QStringView::tokenize': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QStringView.tokenize' has no cute function yet. Qt's "
        "'QStringView::tokenize': a template: a pattern and no single "
        "function.")

  @staticmethod
  def utf16(*__, **_) -> Never:
    """
    Qt's 'const storage_type *QStringView::utf16() const': gives 'unsigned
    short', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QStringView.utf16' has no cute function yet. Qt's 'const "
        "storage_type *QStringView::utf16() const': gives 'unsigned short', "
        "which has no cute class yet.")


#  Qt's 'QList<QStringView>': the list of QStringView, which
#  'QList[QStringView]' gives. It is made here, so that there is one as soon
#  as there can be a QStringView.
QList.createKind(
    QStringView, 'value',
    make='ritual_list_make_QStringView',
    add='ritual_list_add_QStringView',
    size='ritual_list_size_QStringView',
    at='ritual_list_at_QStringView',
    drop='ritual_list_drop_QStringView',
)
