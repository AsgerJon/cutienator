"""
QStringRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qstringref.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QChar, QLatin1String, QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QLatin1String = WAIT['QLatin1String']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringRef(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringRef: a plain Python object standing in front
  of one C++ QStringRef.

  C++ hands a QStringRef around as a copy, so every C++ QStringRef behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStringRef that has a ritual and that Python can
  call so far, 49 names in all: 'string', 'position', 'size', 'count',
  'length', 'indexOf', 'lastIndexOf', 'contains', 'split', 'left', 'right',
  'mid', 'chopped', 'truncate', 'chop', 'isRightToLeft', 'startsWith',
  'endsWith', 'unicode', 'data', 'constData', 'begin', 'cbegin',
  'constBegin', 'end', 'cend', 'constEnd', 'toLatin1', 'toUtf8',
  'toLocal8Bit', 'clear', 'toString', 'isEmpty', 'isNull', 'appendTo', 'at',
  '__getitem__', 'front', 'back', '__eq__', '__ne__', '__lt__', '__le__',
  '__gt__', '__ge__', 'compare', 'localeAwareCompare', 'trimmed',
  'compare_helper'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QStringRef::indexOf(QStringView s, int from,
    Qt::CaseSensitivity cs) const': takes in Python what 'int
    QStringRef::indexOf(const QString &str, int from, Qt::CaseSensitivity cs)
    const' takes.
  - Qt's 'int QStringRef::lastIndexOf(QStringView s, int from,
    Qt::CaseSensitivity cs) const': takes in Python what 'int
    QStringRef::lastIndexOf(const QString &str, int from, Qt::CaseSensitivity
    cs) const' takes.
  - Qt's 'bool QStringRef::contains(QStringView str, Qt::CaseSensitivity cs)
    const': takes in Python what 'bool QStringRef::contains(const QString
    &str, Qt::CaseSensitivity cs) const' takes.
  - Qt's 'bool QStringRef::startsWith(const QString &s, Qt::CaseSensitivity
    cs) const': takes in Python what 'bool QStringRef::startsWith(QStringView
    s, Qt::CaseSensitivity cs) const' takes.
  - Qt's 'bool QStringRef::endsWith(const QString &s, Qt::CaseSensitivity cs)
    const': takes in Python what 'bool QStringRef::endsWith(QStringView s,
    Qt::CaseSensitivity cs) const' takes.
  - Qt's 'QStringView QStringRef::operator QStringView() const': an operator
    Python has no name for.
  - Qt's 'QAnyStringView QStringRef::operator QAnyStringView() const': an
    operator Python has no name for.
  - Qt's 'QStringRef &QStringRef::operator=(const QString *string)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const_reverse_iterator QStringRef::rbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringRef::crbegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringRef::rend() const': gives a type
    Python has no way to take yet.
  - Qt's 'const_reverse_iterator QStringRef::crend() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<uint> QStringRef::toUcs4() const': gives a type Python has no
    way to take yet.
  - Qt's 'short QStringRef::toShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ushort QStringRef::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'int QStringRef::toInt(bool *ok, int base) const': takes a number to
    change where it is.
  - Qt's 'uint QStringRef::toUInt(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'long QStringRef::toLong(bool *ok, int base) const': takes a number
    to change where it is.
  - Qt's 'ulong QStringRef::toULong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QStringRef::toLongLong(bool *ok, int base) const': takes
    a number to change where it is.
  - Qt's 'qulonglong QStringRef::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'float QStringRef::toFloat(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'double QStringRef::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'bool operator==(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator==(const char *s) const' takes.
  - Qt's 'bool operator!=(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator!=(const char *s) const' takes.
  - Qt's 'bool operator<(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator>(const char *s) const' takes.
  - Qt's 'bool operator>(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator<(const char *s) const' takes.
  - Qt's 'bool operator<=(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator>=(const char *s) const' takes.
  - Qt's 'bool operator>=(const char *s1, const QStringRef &s2)': takes in
    Python what 'bool QStringRef::operator<=(const char *s) const' takes.
  - Qt's 'QStringRef::~QStringRef()': the destructor: Python removes its C++
    QStringRef by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QStringRef is created at the first use, not by 'QStringRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStringRef back gives a copy the ritual made for
    Python, in a new cute QStringRef.
  - Each name of Qt's QStringRef that has no cute function yet, 'crbegin',
    'crend', 'rbegin', 'rend', 'toDouble', 'toFloat', 'toInt', 'toLong',
    'toLongLong', 'toShort', 'toUInt', 'toULong', 'toULongLong', 'toUShort',
    'toUcs4', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QChar, int, QChar, int)
  @overload(QChar, int, NoneType, int)
  @overload(NoneType, int, QChar, int)
  @overload(NoneType, int, NoneType, int)
  @overload(QChar, int, QChar, int, Qt.CaseSensitivity)
  @overload(QChar, int, NoneType, int, Qt.CaseSensitivity)
  @overload(NoneType, int, QChar, int, Qt.CaseSensitivity)
  @overload(NoneType, int, NoneType, int, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      data2: Optional[QChar],
      length2: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare_helper(const QChar *data1, qsizetype
    length1, const QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    data2 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length2 : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
    #      const QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN10QStringRef14compare_helperEPK5QCharxS2_xN2Qt15CaseSensi'
        'tivityE',
        CuteMixin._addressOf(data1), length1, CuteMixin._addressOf(data2),
        length2, cs.value,
    )

  @staticmethod
  @overload(QChar, int, str, int)
  @overload(NoneType, int, str, int)
  @overload(QChar, int, str, int, Qt.CaseSensitivity)
  @overload(NoneType, int, str, int, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      data2: Optional[str],
      length2: int,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare_helper(const QChar *data1, qsizetype
    length1, const char *data2, qsizetype length2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare_helper

    Parameters
    ----------

    data1 : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length1 : int
      Passed on as it is.

    data2 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length2 : int
      Passed on as it is.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
    #      const char *data2, qsizetype length2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN10QStringRef14compare_helperEPK5QCharxPKcxN2Qt15CaseSensi'
        'tivityE',
        CuteMixin._addressOf(data1), length1, CuteMixin._bytesOf(data2),
        length2, cs.value,
    )

  @staticmethod
  @overload(QChar, int, QLatin1String)
  @overload(NoneType, int, QLatin1String)
  @overload(QChar, int, QLatin1String, Qt.CaseSensitivity)
  @overload(NoneType, int, QLatin1String, Qt.CaseSensitivity)
  def compare_helper(
      data1: Optional[QChar],
      length1: int,
      s2: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare_helper(const QChar *data1, qsizetype
    length1, QLatin1String s2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare_helper

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
    #  int QStringRef::compare_helper(const QChar *data1, qsizetype length1,
    #      QLatin1String s2, Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN10QStringRef14compare_helperEPK5QCharx13QLatin1StringN2Qt'
        '15CaseSensitivityE',
        CuteMixin._addressOf(data1), length1, CuteMixin._valueOf(s2),
        cs.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringRef'

  #  Qt's '~QStringRef()'. Naming it makes this a value class: Python owns
  #  every C++ QStringRef behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QStringRefD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def string(self) -> Optional[QString]:
    """
    Calls Qt's 'const QString *QStringRef::string() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#string

    Returns
    -------

    Optional[QString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QString *QStringRef::string() const
    address = self.uglySide.call('ritual_ZNK10QStringRef6stringEv')
    from ..QtCore import QString
    return QString._cuteAt(address)

  def position(self) -> int:
    """
    Calls Qt's 'int QStringRef::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#position
    """
    #  int QStringRef::position() const
    return self.uglySide.call('ritual_ZNK10QStringRef8positionEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QStringRef::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#size
    """
    #  int QStringRef::size() const
    return self.uglySide.call('ritual_ZNK10QStringRef4sizeEv')

  @overload()
  def count(self) -> int:
    """
    Calls Qt's 'int QStringRef::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#count
    """
    #  int QStringRef::count() const
    return self.uglySide.call('ritual_ZNK10QStringRef5countEv')

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def count(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::count(const QString &s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#count

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::count(const QString &s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef5countERK7QStringN2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def count(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::count(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#count

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::count(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef5countE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def count(
      self,
      s: QStringRef,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::count(const QStringRef &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#count

    Parameters
    ----------

    s : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::count(const QStringRef &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef5countERKS_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  def length(self) -> int:
    """
    Calls Qt's 'int QStringRef::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#length
    """
    #  int QStringRef::length() const
    return self.uglySide.call('ritual_ZNK10QStringRef6lengthEv')

  @overload(str)
  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      str: str,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::indexOf(const QString &str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#indexOf

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::indexOf(const QString &str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7indexOfERK7QStringiN2Qt15CaseSensitivityE',
        str, from_, cs.value,
    )

  @overload(THIS)
  @overload(THIS, int)
  @overload(THIS, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      str: QStringRef,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::indexOf(const QStringRef &str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#indexOf

    Parameters
    ----------

    str : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::indexOf(const QStringRef &str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7indexOfERKS_iN2Qt15CaseSensitivityE',
        self._valueOf(str), from_, cs.value,
    )

  @overload(QChar)
  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      ch: QChar,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::indexOf(QChar ch, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#indexOf

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::indexOf(QChar ch, int from, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7indexOfE5QChariN2Qt15CaseSensitivityE',
        self._valueOf(ch), from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def indexOf(
      self,
      str: QLatin1String,
      from_: int = 0,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::indexOf(QLatin1String str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#indexOf

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::indexOf(QLatin1String str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7indexOfE13QLatin1StringiN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(str), from_, cs.value,
    )

  @overload(THIS)
  @overload(THIS, int)
  @overload(THIS, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      str: QStringRef,
      from_: int = -1,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::lastIndexOf(const QStringRef &str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#lastIndexOf

    Parameters
    ----------

    str : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::lastIndexOf(const QStringRef &str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef11lastIndexOfERKS_iN2Qt15CaseSensitivityE',
        self._valueOf(str), from_, cs.value,
    )

  @overload(str)
  @overload(str, int)
  @overload(str, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      str: str,
      from_: int = -1,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::lastIndexOf(const QString &str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#lastIndexOf

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::lastIndexOf(const QString &str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef11lastIndexOfERK7QStringiN2Qt15CaseSensitivi'
        'tyE',
        str, from_, cs.value,
    )

  @overload(QChar)
  @overload(QChar, int)
  @overload(QChar, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      ch: QChar,
      from_: int = -1,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::lastIndexOf(QChar ch, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#lastIndexOf

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::lastIndexOf(QChar ch, int from, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef11lastIndexOfE5QChariN2Qt15CaseSensitivityE',
        self._valueOf(ch), from_, cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, int)
  @overload(QLatin1String, int, Qt.CaseSensitivity)
  def lastIndexOf(
      self,
      str: QLatin1String,
      from_: int = -1,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::lastIndexOf(QLatin1String str, int from,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#lastIndexOf

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::lastIndexOf(QLatin1String str, int from,
    #      Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef11lastIndexOfE13QLatin1StringiN2Qt15CaseSens'
        'itivityE',
        self._valueOf(str), from_, cs.value,
    )

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def contains(
      self,
      str: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::contains(const QString &str,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#contains

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::contains(const QString &str, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8containsERK7QStringN2Qt15CaseSensitivityE',
        str, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def contains(
      self,
      str: QStringRef,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::contains(const QStringRef &str,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#contains

    Parameters
    ----------

    str : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::contains(const QStringRef &str, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8containsERKS_N2Qt15CaseSensitivityE',
        self._valueOf(str), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def contains(
      self,
      ch: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::contains(QChar ch, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#contains

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::contains(QChar ch, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8containsE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(ch), cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def contains(
      self,
      str: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::contains(QLatin1String str,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#contains

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::contains(QLatin1String str, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8containsE13QLatin1StringN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(str), cs.value,
    )

  @overload(str)
  @overload(str, Qt.SplitBehavior)
  @overload(str, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: str,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QList[QStringRef]:
    """
    Calls Qt's 'QList<QStringRef> QStringRef::split(const QString &sep,
    Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#split

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

    QList[QStringRef]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStringRef> QStringRef::split(const QString &sep,
    #      Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK10QStringRef5splitERK7QString6QFlagsIN2Qt18SplitBehavior'
        'FlagsEENS4_15CaseSensitivityE',
        sep, behavior.value, cs.value,
    )
    return QList[QStringRef]._cuteOwning(address)

  @overload(QChar)
  @overload(QChar, Qt.SplitBehavior)
  @overload(QChar, Qt.SplitBehavior, Qt.CaseSensitivity)
  def split(
      self,
      sep: QChar,
      behavior: Qt.SplitBehavior = Qt.SplitBehavior.KeepEmptyParts,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> QList[QStringRef]:
    """
    Calls Qt's 'QList<QStringRef> QStringRef::split(QChar sep,
    Qt::SplitBehavior behavior, Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#split

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

    QList[QStringRef]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QStringRef> QStringRef::split(QChar sep, Qt::SplitBehavior
    #      behavior, Qt::CaseSensitivity cs) const
    address = self.uglySide.call(
        'ritual_ZNK10QStringRef5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFlag'
        'sEENS2_15CaseSensitivityE',
        self._valueOf(sep), behavior.value, cs.value,
    )
    return QList[QStringRef]._cuteOwning(address)

  @overload(int)
  def left(self, n: int) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::left(int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::left(int n) const
    address = self.uglySide.call('ritual_ZNK10QStringRef4leftEi', n)
    return QStringRef._cuteOwning(address)

  @overload(int)
  def right(self, n: int) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::right(int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::right(int n) const
    address = self.uglySide.call('ritual_ZNK10QStringRef5rightEi', n)
    return QStringRef._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def mid(self, pos: int, n: int = -1) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::mid(int pos, int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#mid

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::mid(int pos, int n) const
    address = self.uglySide.call('ritual_ZNK10QStringRef3midEii', pos, n)
    return QStringRef._cuteOwning(address)

  @overload(int)
  def chopped(self, n: int) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::chopped(int n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#chopped

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::chopped(int n) const
    address = self.uglySide.call('ritual_ZNK10QStringRef7choppedEi', n)
    return QStringRef._cuteOwning(address)

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QStringRef::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#isRightToLeft
    """
    #  bool QStringRef::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK10QStringRef13isRightToLeftEv')

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def startsWith(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::startsWith(QStringView s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#startsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::startsWith(QStringView s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef10startsWithE11QStringViewN2Qt15CaseSensitiv'
        'ityE',
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
    Calls Qt's 'bool QStringRef::startsWith(QLatin1String s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#startsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::startsWith(QLatin1String s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef10startsWithE13QLatin1StringN2Qt15CaseSensit'
        'ivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def startsWith(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::startsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#startsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::startsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef10startsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def startsWith(
      self,
      c: QStringRef,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::startsWith(const QStringRef &c,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#startsWith

    Parameters
    ----------

    c : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::startsWith(const QStringRef &c, Qt::CaseSensitivity
    #      cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef10startsWithERKS_N2Qt15CaseSensitivityE',
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
    Calls Qt's 'bool QStringRef::endsWith(QStringView s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#endsWith

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::endsWith(QStringView s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8endsWithE11QStringViewN2Qt15CaseSensitivity'
        'E',
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
    Calls Qt's 'bool QStringRef::endsWith(QLatin1String s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#endsWith

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::endsWith(QLatin1String s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8endsWithE13QLatin1StringN2Qt15CaseSensitivi'
        'tyE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def endsWith(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::endsWith(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#endsWith

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::endsWith(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8endsWithE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def endsWith(
      self,
      c: QStringRef,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> bool:
    """
    Calls Qt's 'bool QStringRef::endsWith(const QStringRef &c,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#endsWith

    Parameters
    ----------

    c : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  bool QStringRef::endsWith(const QStringRef &c, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef8endsWithERKS_N2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  def unicode(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QStringRef::unicode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#unicode

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QStringRef::unicode() const
    address = self.uglySide.call('ritual_ZNK10QStringRef7unicodeEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def data(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QStringRef::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#data

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QStringRef::data() const
    address = self.uglySide.call('ritual_ZNK10QStringRef4dataEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def constData(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QStringRef::constData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#constData

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QStringRef::constData() const
    address = self.uglySide.call('ritual_ZNK10QStringRef9constDataEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def begin(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#begin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::begin() const
    address = self.uglySide.call('ritual_ZNK10QStringRef5beginEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def cbegin(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#cbegin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::cbegin() const
    address = self.uglySide.call('ritual_ZNK10QStringRef6cbeginEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def constBegin(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#constBegin

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::constBegin() const
    address = self.uglySide.call('ritual_ZNK10QStringRef10constBeginEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def end(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#end

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::end() const
    address = self.uglySide.call('ritual_ZNK10QStringRef3endEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def cend(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#cend

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::cend() const
    address = self.uglySide.call('ritual_ZNK10QStringRef4cendEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def constEnd(self) -> Optional[QChar]:
    """
    Calls Qt's 'const_iterator QStringRef::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#constEnd

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const_iterator QStringRef::constEnd() const
    address = self.uglySide.call('ritual_ZNK10QStringRef8constEndEv')
    from ..QtCore import QChar
    return QChar._cuteAt(address)

  def toLatin1(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringRef::toLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#toLatin1

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringRef::toLatin1() const
    address = self.uglySide.call('ritual_ZNK10QStringRef8toLatin1Ev')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toUtf8(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringRef::toUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#toUtf8

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringRef::toUtf8() const
    address = self.uglySide.call('ritual_ZNK10QStringRef6toUtf8Ev')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toLocal8Bit(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QStringRef::toLocal8Bit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#toLocal8Bit

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QStringRef::toLocal8Bit() const
    address = self.uglySide.call('ritual_ZNK10QStringRef11toLocal8BitEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QStringRef::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringRef::toString() const
    return self.uglySide.call('ritual_ZNK10QStringRef8toStringEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QStringRef::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#isEmpty
    """
    #  bool QStringRef::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QStringRef7isEmptyEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QStringRef::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#isNull
    """
    #  bool QStringRef::isNull() const
    return self.uglySide.call('ritual_ZNK10QStringRef6isNullEv')

  @overload(QString)
  @overload(NoneType)
  def appendTo(self, string: Optional[QString]) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::appendTo(QString *string) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#appendTo

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::appendTo(QString *string) const
    address = self.uglySide.call(
        'ritual_ZNK10QStringRef8appendToEP7QString', self._addressOf(string),
    )
    return QStringRef._cuteOwning(address)

  @overload(int)
  def at(self, i: int) -> QChar:
    """
    Calls Qt's 'const QChar QStringRef::at(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  const QChar QStringRef::at(int i) const
    address = self.uglySide.call('ritual_ZNK10QStringRef2atEi', i)
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def front(self) -> QChar:
    """
    Calls Qt's 'QChar QStringRef::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#front

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringRef::front() const
    address = self.uglySide.call('ritual_ZNK10QStringRef5frontEv')
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  def back(self) -> QChar:
    """
    Calls Qt's 'QChar QStringRef::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#back

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringRef::back() const
    address = self.uglySide.call('ritual_ZNK10QStringRef4backEv')
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  @overload(str)
  @overload(str, Qt.CaseSensitivity)
  def compare(
      self,
      s: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QString &s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QString &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7compareERK7QStringN2Qt15CaseSensitivityE',
        s, cs.value,
    )

  @overload(THIS)
  @overload(THIS, Qt.CaseSensitivity)
  def compare(
      self,
      s: QStringRef,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QStringRef &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QStringRef &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7compareERKS_N2Qt15CaseSensitivityE',
        self._valueOf(s), cs.value,
    )

  @overload(QChar)
  @overload(QChar, Qt.CaseSensitivity)
  def compare(
      self,
      c: QChar,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(QChar c, Qt::CaseSensitivity cs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(QChar c, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7compareE5QCharN2Qt15CaseSensitivityE',
        self._valueOf(c), cs.value,
    )

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def compare(
      self,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(QLatin1String s, Qt::CaseSensitivity
    cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(QLatin1String s, Qt::CaseSensitivity cs) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7compareE13QLatin1StringN2Qt15CaseSensitivit'
        'yE',
        self._valueOf(s), cs.value,
    )

  @overload(QByteArray)
  @overload(QByteArray, Qt.CaseSensitivity)
  def compare(
      self,
      s: QByteArray,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QByteArray &s,
    Qt::CaseSensitivity cs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QByteArray &s, Qt::CaseSensitivity cs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef7compareERK10QByteArrayN2Qt15CaseSensitivity'
        'E',
        self._valueOf(s), cs.value,
    )

  @staticmethod
  @overload(THIS, str)
  @overload(THIS, str, Qt.CaseSensitivity)
  def compare(
      s1: QStringRef,
      s2: str,
      a2: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QStringRef &s1, const QString
    &s2, Qt::CaseSensitivity a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s1 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    s2 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QStringRef &s1, const QString &s2,
    #      Qt::CaseSensitivity a2)
    return Rituals.call(
        'ritual_ZN10QStringRef7compareERKS_RK7QStringN2Qt15CaseSensitivityE',
        CuteMixin._valueOf(s1), s2, a2.value,
    )

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, THIS, Qt.CaseSensitivity)
  def compare(
      s1: QStringRef,
      s2: QStringRef,
      a2: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QStringRef &s1, const
    QStringRef &s2, Qt::CaseSensitivity a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s1 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    s2 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    a2 : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QStringRef &s1, const QStringRef &s2,
    #      Qt::CaseSensitivity a2)
    return Rituals.call(
        'ritual_ZN10QStringRef7compareERKS_S1_N2Qt15CaseSensitivityE',
        CuteMixin._valueOf(s1), CuteMixin._valueOf(s2), a2.value,
    )

  @staticmethod
  @overload(THIS, QLatin1String)
  @overload(THIS, QLatin1String, Qt.CaseSensitivity)
  def compare(
      s1: QStringRef,
      s2: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QStringRef::compare(const QStringRef &s1, QLatin1String
    s2, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#compare

    Parameters
    ----------

    s1 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    s2 : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QStringRef::compare(const QStringRef &s1, QLatin1String s2,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN10QStringRef7compareERKS_13QLatin1StringN2Qt15CaseSensiti'
        'vityE',
        CuteMixin._valueOf(s1), CuteMixin._valueOf(s2), cs.value,
    )

  @overload(str)
  def localeAwareCompare(self, s: str) -> int:
    """
    Calls Qt's 'int QStringRef::localeAwareCompare(const QString &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#localeAwareCompare

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QStringRef::localeAwareCompare(const QString &s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef18localeAwareCompareERK7QString', s,
    )

  @overload(THIS)
  def localeAwareCompare(self, s: QStringRef) -> int:
    """
    Calls Qt's 'int QStringRef::localeAwareCompare(const QStringRef &s)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#localeAwareCompare

    Parameters
    ----------

    s : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.
    """
    #  int QStringRef::localeAwareCompare(const QStringRef &s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRef18localeAwareCompareERKS_', self._valueOf(s),
    )

  @staticmethod
  @overload(THIS, str)
  def localeAwareCompare(s1: QStringRef, s2: str) -> int:
    """
    Calls Qt's 'int QStringRef::localeAwareCompare(const QStringRef &s1,
    const QString &s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#localeAwareCompare

    Parameters
    ----------

    s1 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    s2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QStringRef::localeAwareCompare(const QStringRef &s1, const QString
    #      &s2)
    return Rituals.call(
        'ritual_ZN10QStringRef18localeAwareCompareERKS_RK7QString',
        CuteMixin._valueOf(s1), s2,
    )

  @staticmethod
  @overload(THIS, THIS)
  def localeAwareCompare(s1: QStringRef, s2: QStringRef) -> int:
    """
    Calls Qt's 'int QStringRef::localeAwareCompare(const QStringRef &s1,
    const QStringRef &s2)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#localeAwareCompare

    Parameters
    ----------

    s1 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.

    s2 : QStringRef
      Passed on as a value: Qt reads the C++ QStringRef, which stays Python's
      own.
    """
    #  int QStringRef::localeAwareCompare(const QStringRef &s1, const
    #      QStringRef &s2)
    return Rituals.call(
        'ritual_ZN10QStringRef18localeAwareCompareERKS_S1_',
        CuteMixin._valueOf(s1), CuteMixin._valueOf(s2),
    )

  def trimmed(self) -> QStringRef:
    """
    Calls Qt's 'QStringRef QStringRef::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#trimmed

    Returns
    -------

    QStringRef
      A new cute QStringRef around the copy Qt gave back. Python owns it.
    """
    #  QStringRef QStringRef::trimmed() const
    address = self.uglySide.call('ritual_ZNK10QStringRef7trimmedEv')
    return QStringRef._cuteOwning(address)

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
  def __getitem__(self, i: int) -> QChar:
    """
    Calls Qt's 'QChar QStringRef::operator[](int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QStringRef::operator[](int i) const
    address = self.uglySide.call('ritual_ZNK10QStringRefixEi', i)
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  @overload(str)
  @overload(NoneType)
  def __eq__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator==(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator==

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator==(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefeqEPKc', self._bytesOf(s),
    )

  @overload(QChar)
  def __eq__(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool operator==(QChar a0, const QStringRef &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator==

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator==(QChar a0, const QStringRef &a1)
    return Rituals.call(
        'ritual_Zeq5QCharRK10QStringRef',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  @overload(NoneType)
  def __ne__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator!=(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator!=

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator!=(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefneEPKc', self._bytesOf(s),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  @overload(NoneType)
  def __lt__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator<(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator<

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator<(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefltEPKc', self._bytesOf(s),
    )

  @overload(QChar)
  def __lt__(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool operator>(QChar a0, const QStringRef &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator>

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator>(QChar a0, const QStringRef &a1)
    return Rituals.call(
        'ritual_Zgt5QCharRK10QStringRef',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  @overload(NoneType)
  def __le__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator<=(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator<=

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator<=(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefleEPKc', self._bytesOf(s),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  @overload(NoneType)
  def __gt__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator>(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator>

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator>(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefgtEPKc', self._bytesOf(s),
    )

  @overload(QChar)
  def __gt__(self, a0: QChar) -> bool:
    """
    Calls Qt's 'bool operator<(QChar a0, const QStringRef &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator<

    Parameters
    ----------

    a0 : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool operator<(QChar a0, const QStringRef &a1)
    return Rituals.call(
        'ritual_Zlt5QCharRK10QStringRef',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  @overload(NoneType)
  def __ge__(self, s: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QStringRef::operator>=(const char *s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#operator>=

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QStringRef::operator>=(const char *s) const
    return self.uglySide.call(
        'ritual_ZNK10QStringRefgeEPKc', self._bytesOf(s),
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
    Notes what was given, for Qt's 'QStringRef::QStringRef()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#QStringRef
    """
    #  QStringRef::QStringRef()
    self._noteCreation(QStringRef, lambda: Rituals.call(
        'ritual_ZN10QStringRefC1Ev',
    ))

  @overload(QString, int, int)
  @overload(NoneType, int, int)
  def __init__(
      self,
      string: Optional[QString],
      position: int,
      size: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringRef::QStringRef(const QString
    *string, qsizetype position, qsizetype size)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#QStringRef

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  QStringRef::QStringRef(const QString *string, qsizetype position,
    #      qsizetype size)
    self._noteCreation(QStringRef, lambda: Rituals.call(
        'ritual_ZN10QStringRefC1EPK7QStringxx',
        self._addressOf(string), position, size,
    ))

  @overload(QString)
  @overload(NoneType)
  def __init__(self, string: Optional[QString]) -> None:
    """
    Notes what was given, for Qt's 'QStringRef::QStringRef(const QString
    *string)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#QStringRef

    Parameters
    ----------

    string : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStringRef::QStringRef(const QString *string)
    self._noteCreation(QStringRef, lambda: Rituals.call(
        'ritual_ZN10QStringRefC1EPK7QString', self._addressOf(string),
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
  def truncate(self, pos: int) -> None:
    """
    Calls Qt's 'void QStringRef::truncate(int pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#truncate

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QStringRef::truncate(int pos)
    self.uglySide.call('ritual_ZN10QStringRef8truncateEi', pos)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QStringRef::chop(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QStringRef::chop(int n)
    self.uglySide.call('ritual_ZN10QStringRef4chopEi', n)

  def clear(self) -> None:
    """
    Calls Qt's 'void QStringRef::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qstringref.html#clear
    """
    #  void QStringRef::clear()
    self.uglySide.call('ritual_ZN10QStringRef5clearEv')

  @staticmethod
  def crbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringRef::crbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringRef.crbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringRef::crbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def crend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringRef::crend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringRef.crend' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringRef::crend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rbegin(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringRef::rbegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringRef.rbegin' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringRef::rbegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rend(*__, **_) -> Never:
    """
    Qt's 'const_reverse_iterator QStringRef::rend() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStringRef.rend' has no cute function yet. Qt's "
        "'const_reverse_iterator QStringRef::rend() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toDouble(*__, **_) -> Never:
    """
    Qt's 'double QStringRef::toDouble(bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toDouble' has no cute function yet. Qt's 'double "
        "QStringRef::toDouble(bool *ok) const': takes a number to change "
        "where it is.")

  @staticmethod
  def toFloat(*__, **_) -> Never:
    """
    Qt's 'float QStringRef::toFloat(bool *ok) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toFloat' has no cute function yet. Qt's 'float "
        "QStringRef::toFloat(bool *ok) const': takes a number to change "
        "where it is.")

  @staticmethod
  def toInt(*__, **_) -> Never:
    """
    Qt's 'int QStringRef::toInt(bool *ok, int base) const': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toInt' has no cute function yet. Qt's 'int "
        "QStringRef::toInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toLong(*__, **_) -> Never:
    """
    Qt's 'long QStringRef::toLong(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toLong' has no cute function yet. Qt's 'long "
        "QStringRef::toLong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toLongLong(*__, **_) -> Never:
    """
    Qt's 'qlonglong QStringRef::toLongLong(bool *ok, int base) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toLongLong' has no cute function yet. Qt's 'qlonglong "
        "QStringRef::toLongLong(bool *ok, int base) const': takes a number "
        "to change where it is.")

  @staticmethod
  def toShort(*__, **_) -> Never:
    """
    Qt's 'short QStringRef::toShort(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toShort' has no cute function yet. Qt's 'short "
        "QStringRef::toShort(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUInt(*__, **_) -> Never:
    """
    Qt's 'uint QStringRef::toUInt(bool *ok, int base) const': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toUInt' has no cute function yet. Qt's 'uint "
        "QStringRef::toUInt(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULong(*__, **_) -> Never:
    """
    Qt's 'ulong QStringRef::toULong(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toULong' has no cute function yet. Qt's 'ulong "
        "QStringRef::toULong(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toULongLong(*__, **_) -> Never:
    """
    Qt's 'qulonglong QStringRef::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toULongLong' has no cute function yet. Qt's "
        "'qulonglong QStringRef::toULongLong(bool *ok, int base) const': "
        "takes a number to change where it is.")

  @staticmethod
  def toUShort(*__, **_) -> Never:
    """
    Qt's 'ushort QStringRef::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QStringRef.toUShort' has no cute function yet. Qt's 'ushort "
        "QStringRef::toUShort(bool *ok, int base) const': takes a number to "
        "change where it is.")

  @staticmethod
  def toUcs4(*__, **_) -> Never:
    """
    Qt's 'QList<uint> QStringRef::toUcs4() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QStringRef.toUcs4' has no cute function yet. Qt's 'QList<uint> "
        "QStringRef::toUcs4() const': gives a type Python has no way to "
        "take yet.")


#  Qt's 'QList<QStringRef>': the list of QStringRef, which
#  'QList[QStringRef]' gives. It is made here, so that there is one as soon
#  as there can be a QStringRef.
QList.createKind(
    QStringRef, 'value',
    make='ritual_list_make_QStringRef',
    add='ritual_list_add_QStringRef',
    size='ritual_list_size_QStringRef',
    at='ritual_list_at_QStringRef',
    drop='ritual_list_drop_QStringRef',
)
