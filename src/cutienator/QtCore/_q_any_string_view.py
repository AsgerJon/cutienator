"""
QAnyStringView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qanystringview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray, QChar, QLatin1Char, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QLatin1Char = WAIT['QLatin1Char']
  QLatin1String = WAIT['QLatin1String']


class QAnyStringView(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAnyStringView: a plain Python object standing in
  front of one C++ QAnyStringView.

  C++ hands a QAnyStringView around as a copy, so every C++ QAnyStringView
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAnyStringView that has a ritual and that Python can
  call so far, 32 names in all: 'toQChar', 'mid', 'left', 'right', 'sliced',
  'first', 'last', 'chopped', 'truncate', 'chop', 'toString', 'size',
  'compare', 'equal', 'front', 'back', 'empty', 'size_bytes', 'max_size',
  'isNull', 'isEmpty', 'length', 'isUtf16', 'isUtf8', 'isLatin1',
  'asStringView', 'asLatin1StringView', 'charSize', 'setSize',
  'decreaseSize', 'advanceData', 'verify'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChar QAnyStringView::toQChar(char ch)': takes a single letter as C
    has it.
  - Qt's 'QAnyStringView::QAnyStringView(const void *d, qsizetype n,
    std::size_t sizeAndType)': names 'void', which has no cute class yet.
  - Qt's 'QAnyStringView::QAnyStringView(std::nullptr_t a0)': takes in Python
    what 'QAnyStringView::QAnyStringView()' takes.
  - Qt's 'QAnyStringView::QAnyStringView(QStringView v)': takes in Python
    what 'QAnyStringView::QAnyStringView(const QString &str)' takes.
  - Qt's 'QAnyStringView &QAnyStringView::slice(qsizetype pos)': gives a type
    Python has no way to take yet.
  - Qt's 'QAnyStringView &QAnyStringView::slice(qsizetype pos, qsizetype n)':
    gives a type Python has no way to take yet.
  - Qt's 'const void *QAnyStringView::data() const': gives 'void', which has
    no cute class yet.
  - Qt's 'bool operator==(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator<(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator>(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator<=(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator>=(const QAnyStringView &lhs, const QAnyStringView
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'QDebug operator<<(QDebug d, QAnyStringView s)': an operator between
    other classes, written inside this one.
  - Qt's 'Tag QAnyStringView::tag() const': gives the enum
    'QAnyStringView::Tag', whose class cannot be named here.
  - Qt's 'q_no_char8_t::QUtf8StringView QAnyStringView::asUtf8StringView()
    const': gives a type Python has no way to take yet.
  - Qt's 'QAnyStringView::~QAnyStringView()': the destructor: Python removes
    its C++ QAnyStringView by it, and has no other use for it.

  What has no ritual
  ------------------

  18 of the 73 functions Qt declares: 18 a template.

  What to expect
  --------------

  - The C++ QAnyStringView is created at the first use, not by
    'QAnyStringView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAnyStringView back gives a copy the ritual made for
    Python, in a new cute QAnyStringView.
  - Each name of Qt's QAnyStringView that has no cute function yet, 'arg',
    'asUtf8StringView', 'data', 'encodeType', 'fromArray',
    'fromCharInternal', 'isAsciiOnlyCharsAtCompileTime',
    'lengthHelperPointer', 'slice', 'tag', 'visit', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QChar)
  def toQChar(ch: QChar) -> QChar:
    """
    Calls Qt's 'QChar QAnyStringView::toQChar(QChar ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#toQChar

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QAnyStringView::toQChar(QChar ch)
    address = Rituals.call(
        'ritual_ZN14QAnyStringView7toQCharE5QChar', CuteMixin._valueOf(ch),
    )
    from . import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  @overload(QLatin1Char)
  def toQChar(ch: QLatin1Char) -> QChar:
    """
    Calls Qt's 'QChar QAnyStringView::toQChar(QLatin1Char ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#toQChar

    Parameters
    ----------

    ch : QLatin1Char
      Passed on as a value: Qt reads the C++ QLatin1Char, which stays
      Python's own.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QAnyStringView::toQChar(QLatin1Char ch)
    address = Rituals.call(
        'ritual_ZN14QAnyStringView7toQCharE11QLatin1Char',
        CuteMixin._valueOf(ch),
    )
    from . import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  @overload(str, str, Qt.CaseSensitivity)
  def compare(
      lhs: str,
      rhs: str,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QAnyStringView::compare(QAnyStringView lhs,
    QAnyStringView rhs, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#compare

    Parameters
    ----------

    lhs : str
      Passed on as it is: a QString is made of it for the call.

    rhs : str
      Passed on as it is: a QString is made of it for the call.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QAnyStringView::compare(QAnyStringView lhs, QAnyStringView rhs,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN14QAnyStringView7compareES_S_N2Qt15CaseSensitivityE',
        lhs, rhs, cs.value,
    )

  @staticmethod
  @overload(str, str)
  def equal(lhs: str, rhs: str) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::equal(QAnyStringView lhs, QAnyStringView
    rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#equal

    Parameters
    ----------

    lhs : str
      Passed on as it is: a QString is made of it for the call.

    rhs : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QAnyStringView::equal(QAnyStringView lhs, QAnyStringView rhs)
    return Rituals.call('ritual_ZN14QAnyStringView5equalES_S_', lhs, rhs)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAnyStringView'

  #  Qt's '~QAnyStringView()'. Naming it makes this a value class: Python
  #  owns every C++ QAnyStringView behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QAnyStringViewD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, int)
  def mid(self, pos: int, n: int = -1) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::mid(qsizetype pos, qsizetype
    n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#mid

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
    #  QAnyStringView QAnyStringView::mid(qsizetype pos, qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView3midExx', pos, n)

  @overload(int)
  def left(self, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::left(qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView4leftEx', n)

  @overload(int)
  def right(self, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::right(qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView5rightEx', n)

  @overload(int)
  def sliced(self, pos: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::sliced(qsizetype pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::sliced(qsizetype pos) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView6slicedEx', pos)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::sliced(qsizetype pos,
    qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#sliced

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
    #  QAnyStringView QAnyStringView::sliced(qsizetype pos, qsizetype n)
    #      const
    return self.uglySide.call('ritual_ZNK14QAnyStringView6slicedExx', pos, n)

  @overload(int)
  def first(self, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::first(qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView5firstEx', n)

  @overload(int)
  def last(self, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::last(qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView4lastEx', n)

  @overload(int)
  def chopped(self, n: int) -> str:
    """
    Calls Qt's 'QAnyStringView QAnyStringView::chopped(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#chopped

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QAnyStringView::chopped(qsizetype n) const
    return self.uglySide.call('ritual_ZNK14QAnyStringView7choppedEx', n)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QAnyStringView::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAnyStringView::toString() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView8toStringEv')

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QAnyStringView::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#size
    """
    #  qsizetype QAnyStringView::size() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView4sizeEv')

  def front(self) -> QChar:
    """
    Calls Qt's 'QChar QAnyStringView::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#front

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QAnyStringView::front() const
    address = self.uglySide.call('ritual_ZNK14QAnyStringView5frontEv')
    from . import QChar
    return QChar._cuteOwning(address)

  def back(self) -> QChar:
    """
    Calls Qt's 'QChar QAnyStringView::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#back

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QAnyStringView::back() const
    address = self.uglySide.call('ritual_ZNK14QAnyStringView4backEv')
    from . import QChar
    return QChar._cuteOwning(address)

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#empty
    """
    #  bool QAnyStringView::empty() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView5emptyEv')

  def size_bytes(self) -> int:
    """
    Calls Qt's 'qsizetype QAnyStringView::size_bytes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#size_bytes
    """
    #  qsizetype QAnyStringView::size_bytes() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView10size_bytesEv')

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QAnyStringView::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#max_size
    """
    #  qsizetype QAnyStringView::max_size() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView8max_sizeEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#isNull
    """
    #  bool QAnyStringView::isNull() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#isEmpty
    """
    #  bool QAnyStringView::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView7isEmptyEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QAnyStringView::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#length
    """
    #  qsizetype QAnyStringView::length() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView6lengthEv')

  def isUtf16(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::isUtf16() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#isUtf16
    """
    #  bool QAnyStringView::isUtf16() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView7isUtf16Ev')

  def isUtf8(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::isUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#isUtf8
    """
    #  bool QAnyStringView::isUtf8() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView6isUtf8Ev')

  def isLatin1(self) -> bool:
    """
    Calls Qt's 'bool QAnyStringView::isLatin1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#isLatin1
    """
    #  bool QAnyStringView::isLatin1() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView8isLatin1Ev')

  def asStringView(self) -> str:
    """
    Calls Qt's 'QStringView QAnyStringView::asStringView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#asStringView

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QAnyStringView::asStringView() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView12asStringViewEv')

  def asLatin1StringView(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QAnyStringView::asLatin1StringView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanystringview.html#asLatin1StringView

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QAnyStringView::asLatin1StringView() const
    address = self.uglySide.call(
        'ritual_ZNK14QAnyStringView18asLatin1StringViewEv',
    )
    from . import QLatin1String
    return QLatin1String._cuteOwning(address)

  def charSize(self) -> int:
    """
    Calls Qt's 'size_t QAnyStringView::charSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#charSize
    """
    #  size_t QAnyStringView::charSize() const
    return self.uglySide.call('ritual_ZNK14QAnyStringView8charSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSize(self, sz: int) -> None:
    """
    Calls Qt's 'void QAnyStringView::setSize(qsizetype sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#setSize

    Parameters
    ----------

    sz : int
      Passed on as it is.
    """
    #  void QAnyStringView::setSize(qsizetype sz)
    self.uglySide.call('ritual_ZN14QAnyStringView7setSizeEx', sz)

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
    Notes what was given, for Qt's 'QAnyStringView::QAnyStringView()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#QAnyStringView
    """
    #  QAnyStringView::QAnyStringView()
    self._noteCreation(QAnyStringView, lambda: Rituals.call(
        'ritual_ZN14QAnyStringViewC1Ev',
    ))

  @overload(QByteArray)
  def __init__(self, str: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QAnyStringView::QAnyStringView(const
    QByteArray &str)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#QAnyStringView

    Parameters
    ----------

    str : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QAnyStringView::QAnyStringView(const QByteArray &str)
    self._noteCreation(QAnyStringView, lambda: Rituals.call(
        'ritual_ZN14QAnyStringViewC1ERK10QByteArray', self._valueOf(str),
    ))

  @overload(str)
  def __init__(self, str: str) -> None:
    """
    Notes what was given, for Qt's 'QAnyStringView::QAnyStringView(const
    QString &str)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#QAnyStringView

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QAnyStringView::QAnyStringView(const QString &str)
    self._noteCreation(QAnyStringView, lambda: Rituals.call(
        'ritual_ZN14QAnyStringViewC1ERK7QString', str,
    ))

  @overload(QLatin1String)
  def __init__(self, str: QLatin1String) -> None:
    """
    Notes what was given, for Qt's
    'QAnyStringView::QAnyStringView(QLatin1StringView str)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#QAnyStringView

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  QAnyStringView::QAnyStringView(QLatin1StringView str)
    self._noteCreation(QAnyStringView, lambda: Rituals.call(
        'ritual_ZN14QAnyStringViewC1E13QLatin1String', self._valueOf(str),
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
    Calls Qt's 'void QAnyStringView::truncate(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#truncate

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QAnyStringView::truncate(qsizetype n)
    self.uglySide.call('ritual_ZN14QAnyStringView8truncateEx', n)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QAnyStringView::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QAnyStringView::chop(qsizetype n)
    self.uglySide.call('ritual_ZN14QAnyStringView4chopEx', n)

  @overload(int)
  def decreaseSize(self, delta: int) -> None:
    """
    Calls Qt's 'void QAnyStringView::decreaseSize(qsizetype delta)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#decreaseSize

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QAnyStringView::decreaseSize(qsizetype delta)
    self.uglySide.call('ritual_ZN14QAnyStringView12decreaseSizeEx', delta)

  @overload(int)
  def advanceData(self, delta: int) -> None:
    """
    Calls Qt's 'void QAnyStringView::advanceData(qsizetype delta)'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#advanceData

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QAnyStringView::advanceData(qsizetype delta)
    self.uglySide.call('ritual_ZN14QAnyStringView11advanceDataEx', delta)

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QAnyStringView::verify(qsizetype pos, qsizetype n)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qanystringview.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QAnyStringView::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK14QAnyStringView6verifyExx', pos, n)

  @staticmethod
  def arg(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::arg': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QAnyStringView.arg' has no cute function yet. Qt's "
        "'QAnyStringView::arg': a template: a pattern and no single "
        "function.")

  @staticmethod
  def asUtf8StringView(*__, **_) -> Never:
    """
    Qt's 'q_no_char8_t::QUtf8StringView QAnyStringView::asUtf8StringView()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAnyStringView.asUtf8StringView' has no cute function yet. Qt's "
        "'q_no_char8_t::QUtf8StringView QAnyStringView::asUtf8StringView() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'const void *QAnyStringView::data() const': gives 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QAnyStringView.data' has no cute function yet. Qt's 'const void "
        "*QAnyStringView::data() const': gives 'void', which has no cute "
        "class yet.")

  @staticmethod
  def encodeType(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::encodeType': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QAnyStringView.encodeType' has no cute function yet. Qt's "
        "'QAnyStringView::encodeType': a template: a pattern and no single "
        "function.")

  @staticmethod
  def fromArray(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::fromArray': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QAnyStringView.fromArray' has no cute function yet. Qt's "
        "'QAnyStringView::fromArray': a template: a pattern and no single "
        "function.")

  @staticmethod
  def fromCharInternal(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::fromCharInternal': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QAnyStringView.fromCharInternal' has no cute function yet. Qt's "
        "'QAnyStringView::fromCharInternal': a template: a pattern and no "
        "single function.")

  @staticmethod
  def isAsciiOnlyCharsAtCompileTime(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::isAsciiOnlyCharsAtCompileTime': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QAnyStringView.isAsciiOnlyCharsAtCompileTime' has no cute "
        "function yet. Qt's "
        "'QAnyStringView::isAsciiOnlyCharsAtCompileTime': a template: a "
        "pattern and no single function.")

  @staticmethod
  def lengthHelperPointer(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::lengthHelperPointer': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QAnyStringView.lengthHelperPointer' has no cute function yet. "
        "Qt's 'QAnyStringView::lengthHelperPointer': a template: a pattern "
        "and no single function.")

  @staticmethod
  def slice(*__, **_) -> Never:
    """
    - Qt's 'QAnyStringView &QAnyStringView::slice(qsizetype pos)': gives a
      type Python has no way to take yet.
    - Qt's 'QAnyStringView &QAnyStringView::slice(qsizetype pos, qsizetype
      n)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAnyStringView.slice' has no cute function yet. Qt's "
        "'QAnyStringView &QAnyStringView::slice(qsizetype pos)': gives a "
        "type Python has no way to take yet. Qt's 'QAnyStringView "
        "&QAnyStringView::slice(qsizetype pos, qsizetype n)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def tag(*__, **_) -> Never:
    """
    Qt's 'Tag QAnyStringView::tag() const': gives the enum
    'QAnyStringView::Tag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAnyStringView.tag' has no cute function yet. Qt's 'Tag "
        "QAnyStringView::tag() const': gives the enum "
        "'QAnyStringView::Tag', whose class cannot be named here.")

  @staticmethod
  def visit(*__, **_) -> Never:
    """
    Qt's 'QAnyStringView::visit': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QAnyStringView.visit' has no cute function yet. Qt's "
        "'QAnyStringView::visit': a template: a pattern and no single "
        "function.")
