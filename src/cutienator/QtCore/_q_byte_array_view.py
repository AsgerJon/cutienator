"""
QByteArrayView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbytearrayview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArray


class QByteArrayView(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QByteArrayView: a plain Python object standing in
  front of one C++ QByteArrayView.

  C++ hands a QByteArrayView around as a copy, so every C++ QByteArrayView
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QByteArrayView that has a ritual and that Python can
  call so far, 26 names in all: 'toByteArray', 'maxSize', 'size', 'first',
  'last', 'sliced', 'chopped', 'left', 'right', 'mid', 'truncate', 'chop',
  'trimmed', 'startsWith', 'endsWith', 'indexOf', 'contains', 'lastIndexOf',
  'count', 'compare', 'isValidUtf8', 'empty', 'max_size', 'isNull',
  'isEmpty', 'length'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char QByteArrayView::operator[](qsizetype n) const': an operator,
    which is not reflected yet.
  - Qt's 'char QByteArrayView::at(qsizetype n) const': gives a single letter
    as C has it.
  - Qt's 'short QByteArrayView::toShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ushort QByteArrayView::toUShort(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'int QByteArrayView::toInt(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'uint QByteArrayView::toUInt(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'long QByteArrayView::toLong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'ulong QByteArrayView::toULong(bool *ok, int base) const': takes a
    number to change where it is.
  - Qt's 'qlonglong QByteArrayView::toLongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'qulonglong QByteArrayView::toULongLong(bool *ok, int base) const':
    takes a number to change where it is.
  - Qt's 'float QByteArrayView::toFloat(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'double QByteArrayView::toDouble(bool *ok) const': takes a number to
    change where it is.
  - Qt's 'bool QByteArrayView::startsWith(char c) const': takes a single
    letter as C has it.
  - Qt's 'bool QByteArrayView::endsWith(char c) const': takes a single letter
    as C has it.
  - Qt's 'qsizetype QByteArrayView::indexOf(char ch, qsizetype from) const':
    takes a single letter as C has it.
  - Qt's 'bool QByteArrayView::contains(char c) const': takes a single letter
    as C has it.
  - Qt's 'qsizetype QByteArrayView::lastIndexOf(char ch, qsizetype from)
    const': takes a single letter as C has it.
  - Qt's 'qsizetype QByteArrayView::count(char ch) const': takes a single
    letter as C has it.
  - Qt's 'char QByteArrayView::front() const': gives a single letter as C has
    it.
  - Qt's 'char QByteArrayView::back() const': gives a single letter as C has
    it.
  - Qt's 'char QByteArrayView::first() const': gives a single letter as C has
    it.
  - Qt's 'char QByteArrayView::last() const': gives a single letter as C has
    it.
  - Qt's 'QByteArrayView::~QByteArrayView()': the destructor: Python removes
    its C++ QByteArrayView by it, and has no other use for it.

  What has no ritual
  ------------------

  27 of the 80 functions Qt declares: 14 takes or gives a type that cannot be
  passed yet; 10 a template; 3 private.

  What to expect
  --------------

  - The C++ QByteArrayView is created at the first use, not by
    'QByteArrayView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QByteArrayView back gives a copy the ritual made for
    Python, in a new cute QByteArrayView.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxSize() -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::maxSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#maxSize
    """
    #  qsizetype QByteArrayView::maxSize()
    return Rituals.call('ritual_ZN14QByteArrayView7maxSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QByteArrayView'

  #  Qt's '~QByteArrayView()'. Naming it makes this a value class: Python
  #  owns every C++ QByteArrayView behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QByteArrayViewD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toByteArray(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QByteArrayView::toByteArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#toByteArray

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QByteArrayView::toByteArray() const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView11toByteArrayEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#size
    """
    #  qsizetype QByteArrayView::size() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView4sizeEv')

  @overload(int)
  def first(self, n: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::first(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#first

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::first(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView5firstEx', n)
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def last(self, n: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::last(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#last

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::last(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView4lastEx', n)
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def sliced(self, pos: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::sliced(qsizetype pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::sliced(qsizetype pos) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView6slicedEx', pos)
    return QByteArrayView._cuteOwning(address)

  @overload(int, int)
  def sliced(self, pos: int, n: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::sliced(qsizetype pos,
    qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#sliced

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::sliced(qsizetype pos, qsizetype n)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QByteArrayView6slicedExx', pos, n,
    )
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def chopped(self, len: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::chopped(qsizetype len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#chopped

    Parameters
    ----------

    len : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::chopped(qsizetype len) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView7choppedEx', len)
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def left(self, n: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::left(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#left

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::left(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView4leftEx', n)
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def right(self, n: int) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::right(qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#right

    Parameters
    ----------

    n : int
      Passed on as it is.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::right(qsizetype n) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView5rightEx', n)
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def mid(self, pos: int, n: int = -1) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::mid(qsizetype pos, qsizetype
    n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#mid

    Parameters
    ----------

    pos : int
      Passed on as it is.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::mid(qsizetype pos, qsizetype n) const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView3midExx', pos, n)
    return QByteArrayView._cuteOwning(address)

  def trimmed(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QByteArrayView::trimmed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#trimmed

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QByteArrayView::trimmed() const
    address = self.uglySide.call('ritual_ZNK14QByteArrayView7trimmedEv')
    return QByteArrayView._cuteOwning(address)

  @overload(THIS)
  def startsWith(self, other: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::startsWith(QByteArrayView other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#startsWith

    Parameters
    ----------

    other : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArrayView::startsWith(QByteArrayView other) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView10startsWithES_', self._valueOf(other),
    )

  @overload(THIS)
  def endsWith(self, other: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::endsWith(QByteArrayView other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#endsWith

    Parameters
    ----------

    other : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArrayView::endsWith(QByteArrayView other) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView8endsWithES_', self._valueOf(other),
    )

  @overload(THIS)
  @overload(THIS, int)
  def indexOf(self, a: QByteArrayView, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::indexOf(QByteArrayView a, qsizetype
    from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#indexOf

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QByteArrayView::indexOf(QByteArrayView a, qsizetype from)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView7indexOfES_x', self._valueOf(a), from_,
    )

  @overload(THIS)
  def contains(self, a: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::contains(QByteArrayView a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#contains

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QByteArrayView::contains(QByteArrayView a) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView8containsES_', self._valueOf(a),
    )

  @overload(THIS)
  def lastIndexOf(self, a: QByteArrayView) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::lastIndexOf(QByteArrayView a)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#lastIndexOf

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  qsizetype QByteArrayView::lastIndexOf(QByteArrayView a) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView11lastIndexOfES_', self._valueOf(a),
    )

  @overload(THIS, int)
  def lastIndexOf(self, a: QByteArrayView, from_: int) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::lastIndexOf(QByteArrayView a,
    qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#lastIndexOf

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    from_ : int
      Passed on as it is.
    """
    #  qsizetype QByteArrayView::lastIndexOf(QByteArrayView a, qsizetype
    #      from) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView11lastIndexOfES_x',
        self._valueOf(a), from_,
    )

  @overload(THIS)
  def count(self, a: QByteArrayView) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::count(QByteArrayView a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#count

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  qsizetype QByteArrayView::count(QByteArrayView a) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView5countES_', self._valueOf(a),
    )

  @overload(THIS)
  def compare(self, a: QByteArrayView) -> int:
    """
    Calls Qt's 'int QByteArrayView::compare(QByteArrayView a) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#compare

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  int QByteArrayView::compare(QByteArrayView a) const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView7compareES_', self._valueOf(a),
    )

  @overload(THIS, Qt.CaseSensitivity)
  def compare(self, a: QByteArrayView, a1: Qt.CaseSensitivity) -> int:
    """
    Calls Qt's 'int QByteArrayView::compare(QByteArrayView a,
    Qt::CaseSensitivity a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#compare

    Parameters
    ----------

    a : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    a1 : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  int QByteArrayView::compare(QByteArrayView a, Qt::CaseSensitivity a1)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QByteArrayView7compareES_N2Qt15CaseSensitivityE',
        self._valueOf(a), a1.value,
    )

  def isValidUtf8(self) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::isValidUtf8() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#isValidUtf8
    """
    #  bool QByteArrayView::isValidUtf8() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView11isValidUtf8Ev')

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#empty
    """
    #  bool QByteArrayView::empty() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView5emptyEv')

  def max_size(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::max_size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#max_size
    """
    #  qsizetype QByteArrayView::max_size() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView8max_sizeEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#isNull
    """
    #  bool QByteArrayView::isNull() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView6isNullEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QByteArrayView::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#isEmpty
    """
    #  bool QByteArrayView::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView7isEmptyEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QByteArrayView::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#length
    """
    #  qsizetype QByteArrayView::length() const
    return self.uglySide.call('ritual_ZNK14QByteArrayView6lengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QByteArrayView::QByteArrayView()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#QByteArrayView
    """
    #  QByteArrayView::QByteArrayView()
    self._noteCreation(QByteArrayView, lambda: Rituals.call(
        'ritual_ZN14QByteArrayViewC1Ev',
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
    Calls Qt's 'void QByteArrayView::truncate(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#truncate

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QByteArrayView::truncate(qsizetype n)
    self.uglySide.call('ritual_ZN14QByteArrayView8truncateEx', n)

  @overload(int)
  def chop(self, n: int) -> None:
    """
    Calls Qt's 'void QByteArrayView::chop(qsizetype n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbytearrayview.html#chop

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  void QByteArrayView::chop(qsizetype n)
    self.uglySide.call('ritual_ZN14QByteArrayView4chopEx', n)
