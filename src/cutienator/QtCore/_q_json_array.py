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
  from typing import Optional

  from . import QJsonValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonValue = WAIT['QJsonValue']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


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
  call so far, 27 names in all: 'size', 'count', 'isEmpty', 'at', 'first',
  'last', 'prepend', 'append', 'removeAt', 'takeAt', 'removeFirst',
  'removeLast', 'insert', 'replace', 'contains', 'begin', 'constBegin',
  'cbegin', 'end', 'constEnd', 'cend', 'erase', 'push_back', 'push_front',
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
  - Qt's 'const_iterator QJsonArray::begin() const': takes in Python what
    'iterator QJsonArray::begin()' takes.
  - Qt's 'const_iterator QJsonArray::end() const': takes in Python what
    'iterator QJsonArray::end()' takes.
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

  #  The classes Qt writes inside QJsonArray, each a class in here as in C++.

  class const_iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QJsonArray::const_iterator: a plain Python object
    standing in front of one C++ QJsonArray::const_iterator.

    C++ hands a QJsonArray::const_iterator around as a copy, so every C++
    QJsonArray::const_iterator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QJsonArray::const_iterator yet. It can be made from
    Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonArray::const_iterator::const_iterator(const iterator &o)':
      names 'QJsonArray::iterator', which stands beside this class inside
      'QJsonArray' and cannot be named from here.
    - Qt's 'const QJsonValueConstRef QJsonArray::const_iterator::operator*()
      const': an operator, which is not reflected yet.
    - Qt's 'const QJsonValueConstRef
      *QJsonArray::const_iterator::operator->() const': an operator, which is
      not reflected yet.
    - Qt's 'QJsonValueConstRef
      QJsonArray::const_iterator::operator[](qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator++(int a0)':
      an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator--(int a0)':
      an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator+(qsizetype j)
      const': an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator-(qsizetype j)
      const': an operator, which is not reflected yet.
    - Qt's 'qsizetype QJsonArray::const_iterator::operator-(const_iterator j)
      const': an operator, which is not reflected yet.
    - Qt's 'QJsonArray::const_iterator::~const_iterator()': the destructor:
      Python removes its C++ QJsonArray::const_iterator by it, and has no
      other use for it.

    What has no ritual
    ------------------

    7 of the 20 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet; 2 private.

    What to expect
    --------------

    - The C++ QJsonArray::const_iterator is created at the first use, not by
      'QJsonArray::const_iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QJsonArray::const_iterator back gives a copy the
      ritual made for Python, in a new cute QJsonArray::const_iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonArray = WAIT['QJsonArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QJsonArray::const_iterator'

    #  Qt's '~QJsonArray::const_iterator()'. Naming it makes this a value
    #  class: Python owns every C++ QJsonArray::const_iterator behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QJsonArray14const_iteratorD1Ev'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QJsonArray::const_iterator::const_iterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#const_iterator
      """
      #  QJsonArray::const_iterator::const_iterator()
      self._noteCreation(QJsonArray.const_iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray14const_iteratorC1Ev',
      ))

    @overload(QJsonArray, int)
    @overload(NoneType, int)
    def __init__(self, array: Optional[QJsonArray], index: int) -> None:
      """
      Notes what was given, for Qt's
      'QJsonArray::const_iterator::const_iterator(const QJsonArray *array,
      qsizetype index)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#const_iterator

      Parameters
      ----------

      array : Optional[QJsonArray]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      index : int
        Passed on as it is.
      """
      #  QJsonArray::const_iterator::const_iterator(const QJsonArray *array,
      #      qsizetype index)
      self._noteCreation(QJsonArray.const_iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray14const_iteratorC1EPKS_x',
          self._addressOf(array), index,
      ))

    @overload(THIS)
    def __init__(self, other: QJsonArray.const_iterator) -> None:
      """
      Notes what was given, for Qt's
      'QJsonArray::const_iterator::const_iterator(const const_iterator
      &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#const_iterator

      Parameters
      ----------

      other : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  QJsonArray::const_iterator::const_iterator(const const_iterator
      #      &other)
      self._noteCreation(QJsonArray.const_iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray14const_iteratorC1ERKS0_',
          self._valueOf(other),
      ))

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

  class iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QJsonArray::iterator: a plain Python object
    standing in front of one C++ QJsonArray::iterator.

    C++ hands a QJsonArray::iterator around as a copy, so every C++
    QJsonArray::iterator behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QJsonArray::iterator yet. It can be made from Python,
    in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonValueRef QJsonArray::iterator::operator*() const': an
      operator, which is not reflected yet.
    - Qt's 'const QJsonValueConstRef *QJsonArray::iterator::operator->()
      const': an operator, which is not reflected yet.
    - Qt's 'QJsonValueRef *QJsonArray::iterator::operator->()': an operator,
      which is not reflected yet.
    - Qt's 'QJsonValueRef QJsonArray::iterator::operator[](qsizetype j)
      const': an operator, which is not reflected yet.
    - Qt's 'iterator QJsonArray::iterator::operator++(int a0)': an operator,
      which is not reflected yet.
    - Qt's 'iterator QJsonArray::iterator::operator--(int a0)': an operator,
      which is not reflected yet.
    - Qt's 'iterator QJsonArray::iterator::operator+(qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'iterator QJsonArray::iterator::operator-(qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'qsizetype QJsonArray::iterator::operator-(iterator j) const': an
      operator, which is not reflected yet.
    - Qt's 'QJsonArray::iterator::~iterator()': the destructor: Python
      removes its C++ QJsonArray::iterator by it, and has no other use for
      it.

    What has no ritual
    ------------------

    9 of the 22 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet; 4 private.

    What to expect
    --------------

    - The C++ QJsonArray::iterator is created at the first use, not by
      'QJsonArray::iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QJsonArray::iterator back gives a copy the ritual
      made for Python, in a new cute QJsonArray::iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonArray = WAIT['QJsonArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QJsonArray::iterator'

    #  Qt's '~QJsonArray::iterator()'. Naming it makes this a value class:
    #  Python owns every C++ QJsonArray::iterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QJsonArray8iteratorD1Ev'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QJsonArray::iterator::iterator()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#iterator
      """
      #  QJsonArray::iterator::iterator()
      self._noteCreation(QJsonArray.iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray8iteratorC1Ev',
      ))

    @overload(QJsonArray, int)
    @overload(NoneType, int)
    def __init__(self, array: Optional[QJsonArray], index: int) -> None:
      """
      Notes what was given, for Qt's
      'QJsonArray::iterator::iterator(QJsonArray *array, qsizetype index)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#iterator

      Parameters
      ----------

      array : Optional[QJsonArray]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      index : int
        Passed on as it is.
      """
      #  QJsonArray::iterator::iterator(QJsonArray *array, qsizetype index)
      self._noteCreation(QJsonArray.iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray8iteratorC1EPS_x',
          self._addressOf(array), index,
      ))

    @overload(THIS)
    def __init__(self, other: QJsonArray.iterator) -> None:
      """
      Notes what was given, for Qt's 'QJsonArray::iterator::iterator(const
      iterator &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#iterator

      Parameters
      ----------

      other : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  QJsonArray::iterator::iterator(const iterator &other)
      self._noteCreation(QJsonArray.iterator, lambda: Rituals.call(
          'ritual_ZN10QJsonArray8iteratorC1ERKS0_', self._valueOf(other),
      ))

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

  def constBegin(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonArray::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#constBegin

    Returns
    -------

    const_iterator
      A new cute QJsonArray::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonArray::constBegin() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray10constBeginEv')
    return QJsonArray.const_iterator._cuteOwning(address)

  def cbegin(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonArray::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#cbegin

    Returns
    -------

    const_iterator
      A new cute QJsonArray::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonArray::cbegin() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray6cbeginEv')
    return QJsonArray.const_iterator._cuteOwning(address)

  def constEnd(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonArray::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#constEnd

    Returns
    -------

    const_iterator
      A new cute QJsonArray::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonArray::constEnd() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray8constEndEv')
    return QJsonArray.const_iterator._cuteOwning(address)

  def cend(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonArray::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#cend

    Returns
    -------

    const_iterator
      A new cute QJsonArray::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonArray::cend() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray4cendEv')
    return QJsonArray.const_iterator._cuteOwning(address)

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

  @overload(iterator, QJsonValue)
  def insert(self, before: iterator, value: QJsonValue) -> iterator:
    """
    Calls Qt's 'iterator QJsonArray::insert(iterator before, const QJsonValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#insert

    Parameters
    ----------

    before : iterator
      Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
      stays Python's own.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    Returns
    -------

    iterator
      A new cute QJsonArray::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonArray::insert(iterator before, const QJsonValue &value)
    address = self.uglySide.call(
        'ritual_ZN10QJsonArray6insertENS_8iteratorERK10QJsonValue',
        self._valueOf(before), self._valueOf(value),
    )
    return QJsonArray.iterator._cuteOwning(address)

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

  def begin(self) -> iterator:
    """
    Calls Qt's 'iterator QJsonArray::begin()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#begin

    Returns
    -------

    iterator
      A new cute QJsonArray::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonArray::begin()
    address = self.uglySide.call('ritual_ZN10QJsonArray5beginEv')
    return QJsonArray.iterator._cuteOwning(address)

  def end(self) -> iterator:
    """
    Calls Qt's 'iterator QJsonArray::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#end

    Returns
    -------

    iterator
      A new cute QJsonArray::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonArray::end()
    address = self.uglySide.call('ritual_ZN10QJsonArray3endEv')
    return QJsonArray.iterator._cuteOwning(address)

  @overload(iterator)
  def erase(self, it: iterator) -> iterator:
    """
    Calls Qt's 'iterator QJsonArray::erase(iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#erase

    Parameters
    ----------

    it : iterator
      Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
      stays Python's own.

    Returns
    -------

    iterator
      A new cute QJsonArray::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonArray::erase(iterator it)
    address = self.uglySide.call(
        'ritual_ZN10QJsonArray5eraseENS_8iteratorE', self._valueOf(it),
    )
    return QJsonArray.iterator._cuteOwning(address)

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
