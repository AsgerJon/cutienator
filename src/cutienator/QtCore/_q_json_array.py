"""
QJsonArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonarray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QJsonValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonValue = WAIT['QJsonValue']


class QJsonArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonArray: a plain Python object standing in front
  of one C++ QJsonArray.

  C++ hands a QJsonArray around as a copy, so every C++ QJsonArray behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonArray that has a ritual and that Python can
  call so far, 20 names in all: 'size', 'count', 'isEmpty', 'at', 'first',
  'last', 'prepend', 'append', 'removeAt', 'takeAt', 'removeFirst',
  'removeLast', 'insert', 'replace', 'contains', 'push_back', 'push_front',
  'pop_front', 'pop_back', 'empty'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonArray::~QJsonArray()': the destructor: Python removes its C++
    QJsonArray by it, and has no other use for it.
  - Qt's 'QJsonValueRef QJsonArray::operator[](qsizetype i)': an operator,
    which is not reflected yet.
  - Qt's 'QJsonValue QJsonArray::operator[](qsizetype i) const': an operator,
    which is not reflected yet.
  - Qt's 'iterator QJsonArray::begin()': gives 'QJsonArray::iterator', which
    has no cute class yet.
  - Qt's 'const_iterator QJsonArray::begin() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonArray::constBegin() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonArray::cbegin() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'iterator QJsonArray::end()': gives 'QJsonArray::iterator', which
    has no cute class yet.
  - Qt's 'const_iterator QJsonArray::end() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonArray::constEnd() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'const_iterator QJsonArray::cend() const': gives
    'QJsonArray::const_iterator', which has no cute class yet.
  - Qt's 'iterator QJsonArray::insert(iterator before, const QJsonValue
    &value)': names 'QJsonArray::iterator', which has no cute class yet.
  - Qt's 'iterator QJsonArray::erase(iterator it)': names
    'QJsonArray::iterator', which has no cute class yet.
  - Qt's 'QJsonArray QJsonArray::operator+(const QJsonValue &v) const': an
    operator, which is not reflected yet.

  What has no ritual
  ------------------

  12 of the 48 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet; 2 private.

  What to expect
  --------------

  - The C++ QJsonArray is created at the first use, not by 'QJsonArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonArray back gives a copy the ritual made for
    Python, in a new cute QJsonArray.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonArray'

  #  Qt's '~QJsonArray()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonArray behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QJsonArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonArray::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#size
    """
    #  qsizetype QJsonArray::size() const
    return self.uglySide.call('ritual_ZNK10QJsonArray4sizeEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonArray::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#count
    """
    #  qsizetype QJsonArray::count() const
    return self.uglySide.call('ritual_ZNK10QJsonArray5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QJsonArray::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#isEmpty
    """
    #  bool QJsonArray::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QJsonArray7isEmptyEv')

  @overload(int)
  def at(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonArray::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonArray::at(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK10QJsonArray2atEx', i)
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  def first(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonArray::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#first

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonArray::first() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray5firstEv')
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  def last(self) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonArray::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#last

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonArray::last() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray4lastEv')
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QJsonValue)
  def contains(self, element: QJsonValue) -> bool:
    """
    Calls Qt's 'bool QJsonArray::contains(const QJsonValue &element) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#contains

    Parameters
    ----------

    element : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool QJsonArray::contains(const QJsonValue &element) const
    return self.uglySide.call(
        'ritual_ZNK10QJsonArray8containsERK10QJsonValue',
        self._valueOf(element),
    )

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QJsonArray::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#empty
    """
    #  bool QJsonArray::empty() const
    return self.uglySide.call('ritual_ZNK10QJsonArray5emptyEv')

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
    Notes what was given, for Qt's 'QJsonArray::QJsonArray()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#QJsonArray
    """
    #  QJsonArray::QJsonArray()
    self._noteCreation(QJsonArray, lambda: Rituals.call(
        'ritual_ZN10QJsonArrayC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QJsonArray) -> None:
    """
    Notes what was given, for Qt's 'QJsonArray::QJsonArray(const QJsonArray
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#QJsonArray

    Parameters
    ----------

    other : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  QJsonArray::QJsonArray(const QJsonArray &other)
    self._noteCreation(QJsonArray, lambda: Rituals.call(
        'ritual_ZN10QJsonArrayC1ERKS_', self._valueOf(other),
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

  @overload(QJsonValue)
  def prepend(self, value: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::prepend(const QJsonValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#prepend

    Parameters
    ----------

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::prepend(const QJsonValue &value)
    self.uglySide.call(
        'ritual_ZN10QJsonArray7prependERK10QJsonValue', self._valueOf(value),
    )

  @overload(QJsonValue)
  def append(self, value: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::append(const QJsonValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#append

    Parameters
    ----------

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::append(const QJsonValue &value)
    self.uglySide.call(
        'ritual_ZN10QJsonArray6appendERK10QJsonValue', self._valueOf(value),
    )

  @overload(int)
  def removeAt(self, i: int) -> None:
    """
    Calls Qt's 'void QJsonArray::removeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#removeAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QJsonArray::removeAt(qsizetype i)
    self.uglySide.call('ritual_ZN10QJsonArray8removeAtEx', i)

  @overload(int)
  def takeAt(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonArray::takeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#takeAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonArray::takeAt(qsizetype i)
    address = self.uglySide.call('ritual_ZN10QJsonArray6takeAtEx', i)
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  def removeFirst(self) -> None:
    """
    Calls Qt's 'void QJsonArray::removeFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#removeFirst
    """
    #  void QJsonArray::removeFirst()
    self.uglySide.call('ritual_ZN10QJsonArray11removeFirstEv')

  def removeLast(self) -> None:
    """
    Calls Qt's 'void QJsonArray::removeLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#removeLast
    """
    #  void QJsonArray::removeLast()
    self.uglySide.call('ritual_ZN10QJsonArray10removeLastEv')

  @overload(int, QJsonValue)
  def insert(self, i: int, value: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::insert(qsizetype i, const QJsonValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#insert

    Parameters
    ----------

    i : int
      Passed on as it is.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::insert(qsizetype i, const QJsonValue &value)
    self.uglySide.call(
        'ritual_ZN10QJsonArray6insertExRK10QJsonValue',
        i, self._valueOf(value),
    )

  @overload(int, QJsonValue)
  def replace(self, i: int, value: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::replace(qsizetype i, const QJsonValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#replace

    Parameters
    ----------

    i : int
      Passed on as it is.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::replace(qsizetype i, const QJsonValue &value)
    self.uglySide.call(
        'ritual_ZN10QJsonArray7replaceExRK10QJsonValue',
        i, self._valueOf(value),
    )

  @overload(QJsonValue)
  def push_back(self, t: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::push_back(const QJsonValue &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#push_back

    Parameters
    ----------

    t : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::push_back(const QJsonValue &t)
    self.uglySide.call(
        'ritual_ZN10QJsonArray9push_backERK10QJsonValue', self._valueOf(t),
    )

  @overload(QJsonValue)
  def push_front(self, t: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonArray::push_front(const QJsonValue &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#push_front

    Parameters
    ----------

    t : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonArray::push_front(const QJsonValue &t)
    self.uglySide.call(
        'ritual_ZN10QJsonArray10push_frontERK10QJsonValue', self._valueOf(t),
    )

  def pop_front(self) -> None:
    """
    Calls Qt's 'void QJsonArray::pop_front()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#pop_front
    """
    #  void QJsonArray::pop_front()
    self.uglySide.call('ritual_ZN10QJsonArray9pop_frontEv')

  def pop_back(self) -> None:
    """
    Calls Qt's 'void QJsonArray::pop_back()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#pop_back
    """
    #  void QJsonArray::pop_back()
    self.uglySide.call('ritual_ZN10QJsonArray8pop_backEv')
