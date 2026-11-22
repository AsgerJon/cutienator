"""
QByteArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt, QHash, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArrayView, QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QByteArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QByteArray: a plain Python object standing in front
  of one C++ QByteArray.

  C++ hands a QByteArray around as a copy, so every C++ QByteArray behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QByteArray that has a ritual and that Python can
  call so far, 64 names in all: 'isEmpty', 'resize', 'resizeForOverwrite',
  'capacity', 'reserve', 'squeeze', 'data', 'constData', 'detach',
  'isDetached', 'isSharedWith', 'clear', 'indexOf', 'lastIndexOf',
  'contains', 'count', 'compare', 'left', 'right', 'mid', 'first', 'last',
  'sliced', 'chopped', 'startsWith', 'endsWith', 'isUpper', 'isLower',
  'isValidUtf8', 'truncate', 'chop', 'toLower', 'toUpper', 'trimmed',
  'simplified', '__iadd__', 'repeated', 'toBase64', 'number', 'fromRawData',
  'fromBase64Encoding', 'fromBase64', 'fromHex', 'begin', 'cbegin',
  'constBegin', 'end', 'cend', 'constEnd', 'push_back', 'push_front',
  'shrink_to_fit', 'max_size', 'maxSize', 'size', 'length', 'isNull',
  'nullTerminated', '__eq__', '__ne__', '__lt__', '__gt__', '__le__',
  '__ge__'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QByteArray::QByteArray(qsizetype size, char c)': takes a single
    letter as C has it.
  - Qt's 'QByteArray::~QByteArray()': the destructor: Python removes its C++
    QByteArray by it, and has no other use for it.
  - Qt's 'void QByteArray::resize(qsizetype size, char c)': takes a single
    letter as C has it.
  - Qt's 'const char *QByteArray::operator const char *() const': an operator
    Python has no name for.
  - Qt's 'char QByteArray::at(qsizetype i) const': gives a single letter as C
    has it.
  - Qt's 'char QByteArray::operator[](qsizetype i) const': gives a single
    letter as C has it.
  - Qt's 'char QByteArray::front() const': gives a single letter as C has it.
  - Qt's 'char QByteArray::back() const': gives a single letter as C has it.
  - Qt's 'qsizetype QByteArray::indexOf(char c, qsizetype from) const': takes
    a single letter as C has it.
  - Qt's 'qsizetype QByteArray::lastIndexOf(char c, qsizetype from) const':
    takes a single letter as C has it.
  - Qt's 'bool QByteArray::contains(char c) const': takes a single letter as
    C has it.
  - Qt's 'qsizetype QByteArray::count(char c) const': takes a single letter
    as C has it.
  - Qt's 'bool QByteArray::startsWith(char c) const': takes a single letter
    as C has it.
  - Qt's 'bool QByteArray::endsWith(char c) const': takes a single letter as
    C has it.
  - Qt's 'QByteArray QByteArray::leftJustified(qsizetype width, char fill,
    bool truncate) const': takes a single letter as C has it.
  - Qt's 'QByteArray QByteArray::rightJustified(qsizetype width, char fill,
    bool truncate) const': takes a single letter as C has it.
  - Qt's 'QByteArray &QByteArray::operator+=(char c)': takes a single letter
    as C has it.
  - Qt's 'QList<QByteArray> QByteArray::split(char sep) const': takes a
    single letter as C has it.
  - Qt's 'short QByteArray::toShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ushort QByteArray::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'int QByteArray::toInt(bool *ok, int base) const': takes a number to
    change where it is.
  - Qt's 'uint QByteArray::toUInt(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'long QByteArray::toLong(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'ulong QByteArray::toULong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QByteArray::toLongLong(bool *ok, int base) const': takes
    a number to change where it is.
  - Qt's 'qulonglong QByteArray::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'float QByteArray::toFloat(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'double QByteArray::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'QByteArray QByteArray::toHex(char separator) const': takes a single
    letter as C has it.
  - Qt's 'QByteArray QByteArray::toPercentEncoding(const QByteArray &exclude,
    const QByteArray &include, char percent) const': takes a single letter as
    C has it.
  - Qt's 'QByteArray QByteArray::percentDecoded(char percent) const': takes a
    single letter as C has it.
  - Qt's 'QByteArray QByteArray::number(uint a0, int base)': takes in Python
    what 'QByteArray QByteArray::number(int a0, int base)' takes.
  - Qt's 'QByteArray QByteArray::number(long a0, int base)': takes in Python
    what 'QByteArray QByteArray::number(int a0, int base)' takes.
  - Qt's 'QByteArray QByteArray::number(ulong a0, int base)': takes in Python
    what 'QByteArray QByteArray::number(int a0, int base)' takes.
  - Qt's 'QByteArray QByteArray::number(qlonglong a0, int base)': takes in
    Python what 'QByteArray QByteArray::number(int a0, int base)' takes.
  - Qt's 'QByteArray QByteArray::number(qulonglong a0, int base)': takes in
    Python what 'QByteArray QByteArray::number(int a0, int base)' takes.
  - Qt's 'QByteArray QByteArray::number(double a0, char format, int
    precision)': takes a single letter as C has it.
  - Qt's 'QByteArray QByteArray::fromPercentEncoding(const QByteArray
    &pctEncoded, char percent)': takes a single letter as C has it.
  - Qt's 'void QByteArray::push_back(char c)': takes a single letter as C has
    it.
  - Qt's 'void QByteArray::push_front(char c)': takes a single letter as C
    has it.
  - Qt's 'bool operator==(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator!=(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<=(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>=(const QByteArray &lhs, const char &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator==(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator!=(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator<=(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator>=(const char &lhs, const QByteArray &rhs)': takes a
    single letter as C has it.
  - Qt's 'bool operator==(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator==(const QByteArray &lhs, const QChar &rhs)'
    takes.
  - Qt's 'bool operator!=(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator!=(const QByteArray &lhs, const QChar &rhs)'
    takes.
  - Qt's 'bool operator<(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator>(const QByteArray &lhs, const QChar &rhs)'
    takes.
  - Qt's 'bool operator>(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator<(const QByteArray &lhs, const QChar &rhs)'
    takes.
  - Qt's 'bool operator<=(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator>=(const QByteArray &lhs, const QChar &rhs)'
    takes.
  - Qt's 'bool operator>=(const QChar &lhs, const QByteArray &rhs)': takes in
    Python what 'bool operator<=(const QByteArray &lhs, const QChar &rhs)'
    takes.

  What has no ritual
  ------------------

  140 of the 283 functions Qt declares: 110 takes or gives a type that cannot
  be passed yet; 14 can only be called on a value about to be thrown away; 13
  private; 3 a template.

  What to expect
  --------------

  - The C++ QByteArray is created at the first use, not by 'QByteArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QByteArray back gives a copy the ritual made for
    Python, in a new cute QByteArray.
  """

  #  The enums Qt writes inside QByteArray, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Base64DecodingStatus(CuteNum, scoped=True):
    """
    The enum 'QByteArray::Base64DecodingStatus' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Ok = Kee[int](0)
    IllegalInputLength = Kee[int](1)
    IllegalCharacter = Kee[int](2)
    IllegalPadding = Kee[int](3)

  class Base64Option(CuteFlags):
    """
    The flags enum 'QByteArray::Base64Option' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QByteArray::Base64Options'.
    """

    Base64Encoding = 0x0
    Base64UrlEncoding = 0x1
    KeepTrailingEquals = 0x0
    OmitTrailingEquals = 0x2
    IgnoreBase64DecodingErrors = 0x0
    AbortOnBase64DecodingErrors = 0x4

  Base64Options = Base64Option

  #  The classes Qt writes inside QByteArray, each a class in here as in C++.

  class FromBase64Result(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QByteArray::FromBase64Result: a plain Python object
    standing in front of one C++ QByteArray::FromBase64Result.

    C++ hands a QByteArray::FromBase64Result around as a copy, so every C++
    QByteArray::FromBase64Result behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QByteArray::FromBase64Result that has a ritual and
    that Python can call so far, 3 names in all: '__bool__', '__eq__',
    '__ne__'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const QByteArray &QByteArray::FromBase64Result::operator*()
      const': an operator Python has no name for.
    - Qt's 'QByteArray::FromBase64Result::~FromBase64Result()': the
      destructor: Python removes its C++ QByteArray::FromBase64Result by it,
      and has no other use for it.

    What has no ritual
    ------------------

    4 of the 9 functions Qt declares: 2 takes or gives a type that cannot be
    passed yet; 2 can only be called on a value about to be thrown away.

    What to expect
    --------------

    - The C++ QByteArray::FromBase64Result is created at the first use, not
      by 'QByteArray::FromBase64Result(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QByteArray::FromBase64Result back gives a copy the
      ritual made for Python, in a new cute QByteArray::FromBase64Result.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QByteArray::FromBase64Result'

    #  Qt's '~QByteArray::FromBase64Result()'. Naming it makes this a value
    #  class: Python owns every C++ QByteArray::FromBase64Result behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QByteArray16FromBase64ResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def __bool__(self) -> bool:
      """
      Calls Qt's 'bool QByteArray::FromBase64Result::operator bool() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qbytearray-frombase64result.html#operator bool
      """
      #  bool QByteArray::FromBase64Result::operator bool() const
      return self.uglySide.call(
          'ritual_ZNK10QByteArray16FromBase64ResultcvbEv',
      )

    @overload(THIS)
    def __eq__(self, rhs: QByteArray.FromBase64Result) -> bool:
      """
      Calls Qt's 'bool operator==(const QByteArray::FromBase64Result &lhs,
      const QByteArray::FromBase64Result &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qbytearray-frombase64result.html#operator==

      Parameters
      ----------

      rhs : QByteArray.FromBase64Result
        Passed on as a value: Qt reads the C++ QByteArray::FromBase64Result,
        which stays Python's own.
      """
      #  bool operator==(const QByteArray::FromBase64Result &lhs, const
      #      QByteArray::FromBase64Result &rhs)
      return Rituals.call(
          'ritual_ZeqRKN10QByteArray16FromBase64ResultES2_',
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
    def __ne__(self, rhs: QByteArray.FromBase64Result) -> bool:
      """
      Calls Qt's 'bool operator!=(const QByteArray::FromBase64Result &lhs,
      const QByteArray::FromBase64Result &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qbytearray-frombase64result.html#operator!=

      Parameters
      ----------

      rhs : QByteArray.FromBase64Result
        Passed on as a value: Qt reads the C++ QByteArray::FromBase64Result,
        which stays Python's own.
      """
      #  bool operator!=(const QByteArray::FromBase64Result &lhs, const
      #      QByteArray::FromBase64Result &rhs)
      return Rituals.call(
          'ritual_ZneRKN10QByteArray16FromBase64ResultES2_',
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  @overload(int, int)
  def number(a0: int, base: int = 10) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::number(int a0, int base)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#number

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    base : int
      Passed on as it is. May be left out, as in Qt: it is then 10.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::number(int a0, int base)
    address = Rituals.call('ritual_ZN10QByteArray6numberEii', a0, base)
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(str, int)
  @overload(NoneType, int)
  def fromRawData(data: Optional[str], size: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::fromRawData(const char *data,
    qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#fromRawData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::fromRawData(const char *data, qsizetype size)
    address = Rituals.call(
        'ritual_ZN10QByteArray11fromRawDataEPKcx',
        CuteMixin._bytesOf(data), size,
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  @overload(THIS, Base64Options)
  def fromBase64Encoding(
      base64: QByteArray,
      options: Base64Options = Base64Options.Base64Encoding,
  ) -> FromBase64Result:
    """
    Calls Qt's 'FromBase64Result QByteArray::fromBase64Encoding(const
    QByteArray &base64, Base64Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#fromBase64Encoding

    Parameters
    ----------

    base64 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : Base64Options
      Passed on as its number. May be left out, as in Qt: it is then
      Base64Options.Base64Encoding.

    Returns
    -------

    FromBase64Result
      A new cute QByteArray::FromBase64Result around the copy Qt gave back.
      Python owns it.
    """
    #  FromBase64Result QByteArray::fromBase64Encoding(const QByteArray
    #      &base64, Base64Options options)
    address = Rituals.call(
        'ritual_ZN10QByteArray18fromBase64EncodingERKS_6QFlagsINS_12Base64O'
        'ptionEE',
        CuteMixin._valueOf(base64), options.value,
    )
    return QByteArray.FromBase64Result._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  @overload(THIS, Base64Options)
  def fromBase64(
      base64: QByteArray,
      options: Base64Options = Base64Options.Base64Encoding,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::fromBase64(const QByteArray &base64,
    Base64Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#fromBase64

    Parameters
    ----------

    base64 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : Base64Options
      Passed on as its number. May be left out, as in Qt: it is then
      Base64Options.Base64Encoding.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::fromBase64(const QByteArray &base64,
    #      Base64Options options)
    address = Rituals.call(
        'ritual_ZN10QByteArray10fromBase64ERKS_6QFlagsINS_12Base64OptionEE',
        CuteMixin._valueOf(base64), options.value,
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(THIS)
  def fromHex(hexEncoded: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::fromHex(const QByteArray
    &hexEncoded)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#fromHex

    Parameters
    ----------

    hexEncoded : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::fromHex(const QByteArray &hexEncoded)
    address = Rituals.call(
        'ritual_ZN10QByteArray7fromHexERKS_', CuteMixin._valueOf(hexEncoded),
    )
    return QByteArray._cuteOwning(address)

  @staticmethod
  def maxSize() -> int:
    """
    Calls Qt's 'qsizetype QByteArray::maxSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#maxSize
    """
    #  qsizetype QByteArray::maxSize()
    return Rituals.call('ritual_ZN10QByteArray7maxSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QByteArray'

  #  Qt's '~QByteArray()'. Naming it makes this a value class: Python owns
  #  every C++ QByteArray behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QByteArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isEmpty
    """
    #  bool QByteArray::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QByteArray7isEmptyEv')

  def capacity(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::capacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#capacity
    """
    #  qsizetype QByteArray::capacity() const
    return self.uglySide.call('ritual_ZNK10QByteArray8capacityEv')

  def data(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QByteArray::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#data

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QByteArray::data() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray4dataEv')
    return None if chars is None else chars.decode()

  def constData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QByteArray::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#constData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QByteArray::constData() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray9constDataEv')
    return None if chars is None else chars.decode()

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isDetached
    """
    #  bool QByteArray::isDetached() const
    return self.uglySide.call('ritual_ZNK10QByteArray10isDetachedEv')

  @overload(THIS)
  def isSharedWith(self, other: QByteArray) -> bool:
    """
    Calls Qt's 'bool QByteArray::isSharedWith(const QByteArray &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isSharedWith

    Parameters
    ----------

    other : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QByteArray::isSharedWith(const QByteArray &other) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray12isSharedWithERKS_', self._valueOf(other),
    )

  @overload(QByteArrayView)
  @overload(QByteArrayView, int)
  def indexOf(self, bv: QByteArrayView, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::indexOf(QByteArrayView bv, qsizetype
    from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#indexOf

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QByteArray::indexOf(QByteArrayView bv, qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray7indexOfE14QByteArrayViewx',
        self._valueOf(bv), from_,
    )

  @overload(QByteArrayView)
  def lastIndexOf(self, bv: QByteArrayView) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::lastIndexOf(QByteArrayView bv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#lastIndexOf

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  qsizetype QByteArray::lastIndexOf(QByteArrayView bv) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray11lastIndexOfE14QByteArrayView',
        self._valueOf(bv),
    )

  @overload(QByteArrayView, int)
  def lastIndexOf(self, bv: QByteArrayView, from_: int) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::lastIndexOf(QByteArrayView bv,
    qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#lastIndexOf

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    from_ : int
      Passed on as it is.
    """
    #  qsizetype QByteArray::lastIndexOf(QByteArrayView bv, qsizetype from)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray11lastIndexOfE14QByteArrayViewx',
        self._valueOf(bv), from_,
    )

  @overload(QByteArrayView)
  def contains(self, bv: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArray::contains(QByteArrayView bv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#contains

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArray::contains(QByteArrayView bv) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray8containsE14QByteArrayView',
        self._valueOf(bv),
    )

  @overload(QByteArrayView)
  def count(self, bv: QByteArrayView) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::count(QByteArrayView bv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#count

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  qsizetype QByteArray::count(QByteArrayView bv) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray5countE14QByteArrayView', self._valueOf(bv),
    )

  @overload()
  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#count
    """
    #  qsizetype QByteArray::count() const
    return self.uglySide.call('ritual_ZNK10QByteArray5countEv')

  @overload(QByteArrayView)
  def compare(self, a: QByteArrayView) -> int:
    """
    Calls Qt's 'int QByteArray::compare(QByteArrayView a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#compare

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  int QByteArray::compare(QByteArrayView a) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray7compareE14QByteArrayView', self._valueOf(a),
    )

  @overload(QByteArrayView, Qt.CaseSensitivity)
  def compare(self, a: QByteArrayView, cs: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'int QByteArray::compare(QByteArrayView a, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#compare

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  int QByteArray::compare(QByteArrayView a, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray7compareE14QByteArrayViewN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(a), cs.value,
    )

  @overload(int)
  def left(self, n: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::left(qsizetype n) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray4leftEx', n)
    return QByteArray._cuteOwning(address)

  @overload(int)
  def right(self, n: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::right(qsizetype n) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray5rightEx', n)
    return QByteArray._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def mid(self, index: int, len: int = -1) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::mid(qsizetype index, qsizetype len)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#mid

    Parameters
    ----------

    index : int
      Passed on as it is.

    len : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::mid(qsizetype index, qsizetype len) const
    address = self.uglySide.call(
        'ritual_ZNKR10QByteArray3midExx', index, len,
    )
    return QByteArray._cuteOwning(address)

  @overload(int)
  def first(self, n: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::first(qsizetype n) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray5firstEx', n)
    return QByteArray._cuteOwning(address)

  @overload(int)
  def last(self, n: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::last(qsizetype n) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray4lastEx', n)
    return QByteArray._cuteOwning(address)

  @overload(int)
  def sliced(self, pos: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::sliced(qsizetype pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::sliced(qsizetype pos) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray6slicedEx', pos)
    return QByteArray._cuteOwning(address)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::sliced(qsizetype pos, qsizetype n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::sliced(qsizetype pos, qsizetype n) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray6slicedExx', pos, n)
    return QByteArray._cuteOwning(address)

  @overload(int)
  def chopped(self, len: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::chopped(qsizetype len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#chopped

    Parameters
    ----------

    len : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::chopped(qsizetype len) const
    address = self.uglySide.call('ritual_ZNKR10QByteArray7choppedEx', len)
    return QByteArray._cuteOwning(address)

  @overload(QByteArrayView)
  def startsWith(self, bv: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArray::startsWith(QByteArrayView bv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#startsWith

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArray::startsWith(QByteArrayView bv) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray10startsWithE14QByteArrayView',
        self._valueOf(bv),
    )

  @overload(QByteArrayView)
  def endsWith(self, bv: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArray::endsWith(QByteArrayView bv) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#endsWith

    Parameters
    ----------

    bv : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArray::endsWith(QByteArrayView bv) const
    return self.uglySide.call(
        'ritual_ZNK10QByteArray8endsWithE14QByteArrayView',
        self._valueOf(bv),
    )

  def isUpper(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isUpper
    """
    #  bool QByteArray::isUpper() const
    return self.uglySide.call('ritual_ZNK10QByteArray7isUpperEv')

  def isLower(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isLower
    """
    #  bool QByteArray::isLower() const
    return self.uglySide.call('ritual_ZNK10QByteArray7isLowerEv')

  def isValidUtf8(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isValidUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isValidUtf8
    """
    #  bool QByteArray::isValidUtf8() const
    return self.uglySide.call('ritual_ZNK10QByteArray11isValidUtf8Ev')

  def toLower(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::toLower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#toLower

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::toLower() const
    address = self.uglySide.call('ritual_ZNKR10QByteArray7toLowerEv')
    return QByteArray._cuteOwning(address)

  def toUpper(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::toUpper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#toUpper

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::toUpper() const
    address = self.uglySide.call('ritual_ZNKR10QByteArray7toUpperEv')
    return QByteArray._cuteOwning(address)

  def trimmed(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#trimmed

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::trimmed() const
    address = self.uglySide.call('ritual_ZNKR10QByteArray7trimmedEv')
    return QByteArray._cuteOwning(address)

  def simplified(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::simplified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#simplified

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::simplified() const
    address = self.uglySide.call('ritual_ZNKR10QByteArray10simplifiedEv')
    return QByteArray._cuteOwning(address)

  @overload(int)
  def repeated(self, times: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::repeated(qsizetype times) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#repeated

    Parameters
    ----------

    times : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::repeated(qsizetype times) const
    address = self.uglySide.call('ritual_ZNK10QByteArray8repeatedEx', times)
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(Base64Options)
  def toBase64(
      self,
      options: Base64Options = Base64Options.Base64Encoding,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::toBase64(Base64Options options)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#toBase64

    Parameters
    ----------

    options : Base64Options
      Passed on as its number. May be left out, as in Qt: it is then
      Base64Options.Base64Encoding.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::toBase64(Base64Options options) const
    address = self.uglySide.call(
        'ritual_ZNK10QByteArray8toBase64E6QFlagsINS_12Base64OptionEE',
        options.value,
    )
    return QByteArray._cuteOwning(address)

  def begin(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#begin

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::begin() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray5beginEv')
    return None if chars is None else chars.decode()

  def cbegin(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#cbegin

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::cbegin() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray6cbeginEv')
    return None if chars is None else chars.decode()

  def constBegin(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#constBegin

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::constBegin() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray10constBeginEv')
    return None if chars is None else chars.decode()

  def end(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#end

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::end() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray3endEv')
    return None if chars is None else chars.decode()

  def cend(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#cend

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::cend() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray4cendEv')
    return None if chars is None else chars.decode()

  def constEnd(self) -> Optional[str]:
    """
    Calls Qt's 'const_iterator QByteArray::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#constEnd

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const_iterator QByteArray::constEnd() const
    chars = self.uglySide.call('ritual_ZNK10QByteArray8constEndEv')
    return None if chars is None else chars.decode()

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#max_size
    """
    #  qsizetype QByteArray::max_size() const
    return self.uglySide.call('ritual_ZNK10QByteArray8max_sizeEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#size
    """
    #  qsizetype QByteArray::size() const
    return self.uglySide.call('ritual_ZNK10QByteArray4sizeEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArray::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#length
    """
    #  qsizetype QByteArray::length() const
    return self.uglySide.call('ritual_ZNK10QByteArray6lengthEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QByteArray::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#isNull
    """
    #  bool QByteArray::isNull() const
    return self.uglySide.call('ritual_ZNK10QByteArray6isNullEv')

  def nullTerminated(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArray::nullTerminated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#nullTerminated

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArray::nullTerminated() const
    address = self.uglySide.call('ritual_ZNKR10QByteArray14nullTerminatedEv')
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(NoneType)
  def __iadd__(self, s: Optional[str]) -> QByteArray:
    """
    Calls Qt's 'QByteArray &QByteArray::operator+=(const char *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator+=

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QByteArray &QByteArray::operator+=(const char *s)
    self.uglySide.call('ritual_ZN10QByteArraypLEPKc', self._bytesOf(s))
    return self

  @overload(THIS)
  def __iadd__(self, a: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray &QByteArray::operator+=(const QByteArray &a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator+=

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QByteArray &QByteArray::operator+=(const QByteArray &a)
    self.uglySide.call('ritual_ZN10QByteArraypLERKS_', self._valueOf(a))
    return self

  @overload(QByteArrayView)
  def __iadd__(self, a: QByteArrayView) -> QByteArray:
    """
    Calls Qt's 'QByteArray &QByteArray::operator+=(QByteArrayView a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator+=

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QByteArray &QByteArray::operator+=(QByteArrayView a)
    self.uglySide.call(
        'ritual_ZN10QByteArraypLE14QByteArrayView', self._valueOf(a),
    )
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator==(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator==

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator==(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __eq__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator==(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator==

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator==(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QByteArrayRK5QChar',
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
  def __ne__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator!=(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator!=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator!=(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZneRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __ne__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator!=(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator!=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator!=(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZneRK10QByteArrayRK5QChar',
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
  def __lt__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator<(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator<

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator<(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZltRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __lt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator<

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZltRK10QByteArrayRK5QChar',
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
  def __gt__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator>(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator>

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator>(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __gt__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator>

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QByteArrayRK5QChar',
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
  def __le__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator<=(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator<=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator<=(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZleRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __le__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator<=(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator<=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<=(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZleRK10QByteArrayRK5QChar',
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
  def __ge__(self, rhs: QByteArray) -> bool:
    """
    Calls Qt's 'bool operator>=(const QByteArray &lhs, const QByteArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator>=

    Parameters
    ----------

    rhs : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool operator>=(const QByteArray &lhs, const QByteArray &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QByteArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QChar)
  def __ge__(self, rhs: QChar) -> bool:
    """
    Calls Qt's 'bool operator>=(const QByteArray &lhs, const QChar &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#operator>=

    Parameters
    ----------

    rhs : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>=(const QByteArray &lhs, const QChar &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QByteArrayRK5QChar',
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
    Notes what was given, for Qt's 'QByteArray::QByteArray()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#QByteArray
    """
    #  QByteArray::QByteArray()
    self._noteCreation(QByteArray, lambda: Rituals.call(
        'ritual_ZN10QByteArrayC1Ev',
    ))

  @overload(str)
  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, a0: Optional[str], size: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QByteArray::QByteArray(const char *a0,
    qsizetype size)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#QByteArray

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QByteArray::QByteArray(const char *a0, qsizetype size)
    self._noteCreation(QByteArray, lambda: Rituals.call(
        'ritual_ZN10QByteArrayC1EPKcx', self._bytesOf(a0), size,
    ))

  @overload(int, Qt.Initialization)
  def __init__(self, size: int, a1: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'QByteArray::QByteArray(qsizetype size,
    Qt::Initialization a1)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#QByteArray

    Parameters
    ----------

    size : int
      Passed on as it is.

    a1 : Qt.Initialization
      Passed on as its number.
    """
    #  QByteArray::QByteArray(qsizetype size, Qt::Initialization a1)
    self._noteCreation(QByteArray, lambda: Rituals.call(
        'ritual_ZN10QByteArrayC1ExN2Qt14InitializationE', size, a1.value,
    ))

  @overload(QByteArrayView)
  def __init__(self, v: QByteArrayView) -> None:
    """
    Notes what was given, for Qt's 'QByteArray::QByteArray(QByteArrayView
    v)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#QByteArray

    Parameters
    ----------

    v : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QByteArray::QByteArray(QByteArrayView v)
    self._noteCreation(QByteArray, lambda: Rituals.call(
        'ritual_ZN10QByteArrayC1E14QByteArrayView', self._valueOf(v),
    ))

  @overload(THIS)
  def __init__(self, a0: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QByteArray::QByteArray(const QByteArray
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#QByteArray

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QByteArray::QByteArray(const QByteArray &a0)
    self._noteCreation(QByteArray, lambda: Rituals.call(
        'ritual_ZN10QByteArrayC1ERKS_', self._valueOf(a0),
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
  def resize(self, size: int) -> None:
    """
    Calls Qt's 'void QByteArray::resize(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#resize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QByteArray::resize(qsizetype size)
    self.uglySide.call('ritual_ZN10QByteArray6resizeEx', size)

  @overload(int)
  def resizeForOverwrite(self, size: int) -> None:
    """
    Calls Qt's 'void QByteArray::resizeForOverwrite(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#resizeForOverwrite

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QByteArray::resizeForOverwrite(qsizetype size)
    self.uglySide.call('ritual_ZN10QByteArray18resizeForOverwriteEx', size)

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QByteArray::reserve(qsizetype size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QByteArray::reserve(qsizetype size)
    self.uglySide.call('ritual_ZN10QByteArray7reserveEx', size)

  def squeeze(self) -> None:
    """
    Calls Qt's 'void QByteArray::squeeze()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#squeeze
    """
    #  void QByteArray::squeeze()
    self.uglySide.call('ritual_ZN10QByteArray7squeezeEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QByteArray::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#detach
    """
    #  void QByteArray::detach()
    self.uglySide.call('ritual_ZN10QByteArray6detachEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QByteArray::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#clear
    """
    #  void QByteArray::clear()
    self.uglySide.call('ritual_ZN10QByteArray5clearEv')

  @overload(int)
  def truncate(self, pos: int) -> None:
    """
    Calls Qt's 'void QByteArray::truncate(qsizetype pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#truncate

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QByteArray::truncate(qsizetype pos)
    self.uglySide.call('ritual_ZN10QByteArray8truncateEx', pos)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QByteArray::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QByteArray::chop(qsizetype n)
    self.uglySide.call('ritual_ZN10QByteArray4chopEx', n)

  @overload(str)
  @overload(NoneType)
  def push_back(self, s: Optional[str]) -> None:
    """
    Calls Qt's 'void QByteArray::push_back(const char *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_back

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QByteArray::push_back(const char *s)
    self.uglySide.call(
        'ritual_ZN10QByteArray9push_backEPKc', self._bytesOf(s),
    )

  @overload(THIS)
  def push_back(self, a: QByteArray) -> None:
    """
    Calls Qt's 'void QByteArray::push_back(const QByteArray &a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_back

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QByteArray::push_back(const QByteArray &a)
    self.uglySide.call(
        'ritual_ZN10QByteArray9push_backERKS_', self._valueOf(a),
    )

  @overload(QByteArrayView)
  def push_back(self, a: QByteArrayView) -> None:
    """
    Calls Qt's 'void QByteArray::push_back(QByteArrayView a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_back

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QByteArray::push_back(QByteArrayView a)
    self.uglySide.call(
        'ritual_ZN10QByteArray9push_backE14QByteArrayView', self._valueOf(a),
    )

  @overload(str)
  @overload(NoneType)
  def push_front(self, c: Optional[str]) -> None:
    """
    Calls Qt's 'void QByteArray::push_front(const char *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_front

    Parameters
    ----------

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QByteArray::push_front(const char *c)
    self.uglySide.call(
        'ritual_ZN10QByteArray10push_frontEPKc', self._bytesOf(c),
    )

  @overload(THIS)
  def push_front(self, a: QByteArray) -> None:
    """
    Calls Qt's 'void QByteArray::push_front(const QByteArray &a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_front

    Parameters
    ----------

    a : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QByteArray::push_front(const QByteArray &a)
    self.uglySide.call(
        'ritual_ZN10QByteArray10push_frontERKS_', self._valueOf(a),
    )

  @overload(QByteArrayView)
  def push_front(self, a: QByteArrayView) -> None:
    """
    Calls Qt's 'void QByteArray::push_front(QByteArrayView a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#push_front

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QByteArray::push_front(QByteArrayView a)
    self.uglySide.call(
        'ritual_ZN10QByteArray10push_frontE14QByteArrayView',
        self._valueOf(a),
    )

  def shrink_to_fit(self) -> None:
    """
    Calls Qt's 'void QByteArray::shrink_to_fit()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearray.html#shrink_to_fit
    """
    #  void QByteArray::shrink_to_fit()
    self.uglySide.call('ritual_ZN10QByteArray13shrink_to_fitEv')


#  Qt's 'QList<QByteArray>': the list of QByteArray, which
#  'QList[QByteArray]' gives. It is made here, so that there is one as soon
#  as there can be a QByteArray. Qt has a name of its own for it.
QByteArrayList = QList.createKind(
    QByteArray, 'value',
    name='QByteArrayList',
    make='ritual_list_make_QByteArray',
    add='ritual_list_add_QByteArray',
    size='ritual_list_size_QByteArray',
    at='ritual_list_at_QByteArray',
    drop='ritual_list_drop_QByteArray',
)


#  Qt's 'QHash<int, QByteArray>': the QHash from a number to QByteArray,
#  which 'QHash[int, QByteArray]' gives. It is completed here, in the file of
#  the class of its values.
QHash.createKind(
    int, QByteArray, 'value',
    make='ritual_map_make_QHash_int_QByteArray',
    put='ritual_map_put_QHash_int_QByteArray',
    size='ritual_map_size_QHash_int_QByteArray',
    key='ritual_map_key_QHash_int_QByteArray',
    value='ritual_map_value_QHash_int_QByteArray',
    has='ritual_map_has_QHash_int_QByteArray',
    get='ritual_map_get_QHash_int_QByteArray',
    drop='ritual_map_drop_QHash_int_QByteArray',
)
