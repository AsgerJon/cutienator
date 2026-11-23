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
from . import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDebug, QJsonValue, QJsonValueConstRef, QJsonValueRef
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QJsonValue = WAIT['QJsonValue']
  QVariant = WAIT['QVariant']

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
  call so far, 37 names in all: 'fromStringList', 'fromVariantList',
  'toVariantList', 'size', 'count', 'isEmpty', 'at', 'first', 'last',
  'prepend', 'append', 'removeAt', 'takeAt', 'removeFirst', 'removeLast',
  'insert', 'replace', 'contains', '__getitem__', 'begin', 'constBegin',
  'cbegin', 'end', 'constEnd', 'cend', 'erase', '__add__', '__iadd__',
  'push_back', 'push_front', 'pop_front', 'pop_back', 'empty', '__rlshift__',
  '__eq__', '__ne__', 'detach'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonArray::~QJsonArray()': the destructor: Python removes its C++
    QJsonArray by it, and has no other use for it.
  - Qt's 'QJsonValue QJsonArray::operator[](qsizetype i) const': takes in
    Python what 'QJsonValueRef QJsonArray::operator[](qsizetype i)' takes.
  - Qt's 'const_iterator QJsonArray::begin() const': takes in Python what
    'iterator QJsonArray::begin()' takes.
  - Qt's 'const_iterator QJsonArray::end() const': takes in Python what
    'iterator QJsonArray::end()' takes.
  - Qt's 'bool operator==(const QJsonValue &lhs, const QJsonArray &rhs)':
    takes in Python what 'bool operator==(const QJsonArray &lhs, const
    QJsonValue &rhs)' takes.
  - Qt's 'bool operator!=(const QJsonValue &lhs, const QJsonArray &rhs)':
    takes in Python what 'bool operator!=(const QJsonArray &lhs, const
    QJsonValue &rhs)' takes.

  What has no ritual
  ------------------

  7 of the 55 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet.

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

    Every function of Qt's QJsonArray::const_iterator that has a ritual and
    that Python can call so far, 12 names in all: '__getitem__', '__iadd__',
    '__isub__', '__add__', '__sub__', 'comparesEqual_helper', '__eq__',
    '__ne__', '__lt__', '__gt__', '__le__', '__ge__'. It can be made from
    Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonArray::const_iterator::const_iterator(const iterator &o)':
      names 'QJsonArray::iterator', which stands beside this class inside
      'QJsonArray' and cannot be named from here.
    - Qt's 'const QJsonValueConstRef QJsonArray::const_iterator::operator*()
      const': an operator Python has no name for.
    - Qt's 'const QJsonValueConstRef
      *QJsonArray::const_iterator::operator->() const': an operator Python
      has no name for.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator++(int a0)':
      an operator Python has no name for.
    - Qt's 'const_iterator QJsonArray::const_iterator::operator--(int a0)':
      an operator Python has no name for.
    - Qt's 'QJsonArray::const_iterator::~const_iterator()': the destructor:
      Python removes its C++ QJsonArray::const_iterator by it, and has no
      other use for it.

    What has no ritual
    ------------------

    4 of the 26 functions Qt declares: 4 takes or gives a type that cannot be
    passed yet.

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

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QJsonArray.const_iterator,
        rhs: QJsonArray.const_iterator,
    ) -> bool:
      """
      Calls Qt's 'bool QJsonArray::const_iterator::comparesEqual_helper(const
      const_iterator &lhs, const const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html

      Parameters
      ----------

      lhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool QJsonArray::const_iterator::comparesEqual_helper(const
      #      const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZN10QJsonArray14const_iterator20comparesEqual_helperERKS0'
          '_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

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

    @overload(int)
    def __getitem__(self, j: int) -> QJsonValueConstRef:
      """
      Calls Qt's 'QJsonValueConstRef
      QJsonArray::const_iterator::operator[](qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator[]

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonValueConstRef
        A new cute QJsonValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QJsonValueConstRef QJsonArray::const_iterator::operator[](qsizetype
      #      j) const
      address = self.uglySide.call(
          'ritual_ZNK10QJsonArray14const_iteratorixEx', j,
      )
      from . import QJsonValueConstRef
      return QJsonValueConstRef._cuteOwning(address)

    @overload(int)
    def __iadd__(self, j: int) -> QJsonArray.const_iterator:
      """
      Calls Qt's 'const_iterator
      &QJsonArray::const_iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  const_iterator &QJsonArray::const_iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN10QJsonArray14const_iteratorpLEx', j)
      return self

    @overload.fallback
    def __iadd__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __isub__(self, j: int) -> QJsonArray.const_iterator:
      """
      Calls Qt's 'const_iterator
      &QJsonArray::const_iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  const_iterator &QJsonArray::const_iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN10QJsonArray14const_iteratormIEx', j)
      return self

    @overload.fallback
    def __isub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __add__(self, j: int) -> QJsonArray.const_iterator:
      """
      Calls Qt's 'const_iterator
      QJsonArray::const_iterator::operator+(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonArray.const_iterator
        A new cute QJsonArray::const_iterator around the copy Qt gave back.
        Python owns it.
      """
      #  const_iterator QJsonArray::const_iterator::operator+(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK10QJsonArray14const_iteratorplEx', j,
      )
      return QJsonArray.const_iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QJsonArray.const_iterator:
      """
      Calls Qt's 'const_iterator
      QJsonArray::const_iterator::operator-(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonArray.const_iterator
        A new cute QJsonArray::const_iterator around the copy Qt gave back.
        Python owns it.
      """
      #  const_iterator QJsonArray::const_iterator::operator-(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK10QJsonArray14const_iteratormiEx', j,
      )
      return QJsonArray.const_iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QJsonArray.const_iterator) -> int:
      """
      Calls Qt's 'qsizetype
      QJsonArray::const_iterator::operator-(const_iterator j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator-

      Parameters
      ----------

      j : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  qsizetype QJsonArray::const_iterator::operator-(const_iterator j)
      #      const
      return self.uglySide.call(
          'ritual_ZNK10QJsonArray14const_iteratormiES0_', self._valueOf(j),
      )

    @overload.fallback
    def __sub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator==

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator==(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZeqRKN10QJsonArray14const_iteratorES2_',
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
    def __ne__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator!=

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator!=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZneRKN10QJsonArray14const_iteratorES2_',
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
    def __lt__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator<

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator<(const const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN10QJsonArray14const_iteratorES2_',
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
    def __gt__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator>

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator>(const const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN10QJsonArray14const_iteratorES2_',
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
    def __le__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator<=

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator<=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZleRKN10QJsonArray14const_iteratorES2_',
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
    def __ge__(self, rhs: QJsonArray.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-const_iterator.html#operator>=

      Parameters
      ----------

      rhs : QJsonArray.const_iterator
        Passed on as a value: Qt reads the C++ QJsonArray::const_iterator,
        which stays Python's own.
      """
      #  bool operator>=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZgeRKN10QJsonArray14const_iteratorES2_',
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

    Every function of Qt's QJsonArray::iterator that has a ritual and that
    Python can call so far, 12 names in all: '__getitem__', '__iadd__',
    '__isub__', '__add__', '__sub__', 'comparesEqual_helper', '__eq__',
    '__ne__', '__lt__', '__gt__', '__le__', '__ge__'. It can be made from
    Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonValueRef QJsonArray::iterator::operator*() const': an
      operator Python has no name for.
    - Qt's 'const QJsonValueConstRef *QJsonArray::iterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'QJsonValueRef *QJsonArray::iterator::operator->()': an operator
      Python has no name for.
    - Qt's 'iterator QJsonArray::iterator::operator++(int a0)': an operator
      Python has no name for.
    - Qt's 'iterator QJsonArray::iterator::operator--(int a0)': an operator
      Python has no name for.
    - Qt's 'bool QJsonArray::iterator::comparesEqual_helper(const iterator
      &lhs, const const_iterator &rhs)': names 'QJsonArray::const_iterator',
      which stands beside this class inside 'QJsonArray' and cannot be named
      from here.
    - Qt's 'bool operator==(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator!=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator<(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator>(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator<=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator>=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator==(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator!=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator<(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator>(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator<=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'bool operator>=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonArray::const_iterator', which stands beside this class
      inside 'QJsonArray' and cannot be named from here.
    - Qt's 'QJsonArray::iterator::~iterator()': the destructor: Python
      removes its C++ QJsonArray::iterator by it, and has no other use for
      it.

    What has no ritual
    ------------------

    5 of the 40 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet.

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

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QJsonArray.iterator,
        rhs: QJsonArray.iterator,
    ) -> bool:
      """
      Calls Qt's 'bool QJsonArray::iterator::comparesEqual_helper(const
      iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#comparesEqual_helper

      Parameters
      ----------

      lhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool QJsonArray::iterator::comparesEqual_helper(const iterator &lhs,
      #      const iterator &rhs)
      return Rituals.call(
          'ritual_ZN10QJsonArray8iterator20comparesEqual_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

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

    @overload(int)
    def __getitem__(self, j: int) -> QJsonValueRef:
      """
      Calls Qt's 'QJsonValueRef QJsonArray::iterator::operator[](qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator[]

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonValueRef
        A new cute QJsonValueRef around the copy Qt gave back. Python owns
        it.
      """
      #  QJsonValueRef QJsonArray::iterator::operator[](qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QJsonArray8iteratorixEx', j)
      from . import QJsonValueRef
      return QJsonValueRef._cuteOwning(address)

    @overload(int)
    def __iadd__(self, j: int) -> QJsonArray.iterator:
      """
      Calls Qt's 'iterator &QJsonArray::iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  iterator &QJsonArray::iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN10QJsonArray8iteratorpLEx', j)
      return self

    @overload.fallback
    def __iadd__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __isub__(self, j: int) -> QJsonArray.iterator:
      """
      Calls Qt's 'iterator &QJsonArray::iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  iterator &QJsonArray::iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN10QJsonArray8iteratormIEx', j)
      return self

    @overload.fallback
    def __isub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __add__(self, j: int) -> QJsonArray.iterator:
      """
      Calls Qt's 'iterator QJsonArray::iterator::operator+(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonArray.iterator
        A new cute QJsonArray::iterator around the copy Qt gave back. Python
        owns it.
      """
      #  iterator QJsonArray::iterator::operator+(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QJsonArray8iteratorplEx', j)
      return QJsonArray.iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QJsonArray.iterator:
      """
      Calls Qt's 'iterator QJsonArray::iterator::operator-(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonArray.iterator
        A new cute QJsonArray::iterator around the copy Qt gave back. Python
        owns it.
      """
      #  iterator QJsonArray::iterator::operator-(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QJsonArray8iteratormiEx', j)
      return QJsonArray.iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QJsonArray.iterator) -> int:
      """
      Calls Qt's 'qsizetype QJsonArray::iterator::operator-(iterator j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator-

      Parameters
      ----------

      j : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  qsizetype QJsonArray::iterator::operator-(iterator j) const
      return self.uglySide.call(
          'ritual_ZNK10QJsonArray8iteratormiES0_', self._valueOf(j),
      )

    @overload.fallback
    def __sub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator==

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator==(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN10QJsonArray8iteratorES2_',
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
    def __ne__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator!=

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator!=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN10QJsonArray8iteratorES2_',
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
    def __lt__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator<

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator<(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN10QJsonArray8iteratorES2_',
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
    def __gt__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator>

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator>(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN10QJsonArray8iteratorES2_',
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
    def __le__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator<=

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator<=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN10QJsonArray8iteratorES2_',
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
    def __ge__(self, rhs: QJsonArray.iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonarray-iterator.html#operator>=

      Parameters
      ----------

      rhs : QJsonArray.iterator
        Passed on as a value: Qt reads the C++ QJsonArray::iterator, which
        stays Python's own.
      """
      #  bool operator>=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN10QJsonArray8iteratorES2_',
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

  @staticmethod
  @overload(QStringList)
  def fromStringList(list: QStringList) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonArray::fromStringList(const QStringList
    &list)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#fromStringList

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonArray::fromStringList(const QStringList &list)
    address = Rituals.call(
        'ritual_ZN10QJsonArray14fromStringListERK5QListI7QStringE',
        CuteMixin._valueOf(list),
    )
    return QJsonArray._cuteOwning(address)

  @staticmethod
  @overload(QList[QVariant])
  def fromVariantList(list: QList[QVariant]) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonArray::fromVariantList(const QVariantList
    &list)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#fromVariantList

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonArray::fromVariantList(const QVariantList &list)
    address = Rituals.call(
        'ritual_ZN10QJsonArray15fromVariantListERK5QListI8QVariantE',
        CuteMixin._valueOf(list),
    )
    return QJsonArray._cuteOwning(address)

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

  def toVariantList(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QJsonArray::toVariantList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#toVariantList

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QJsonArray::toVariantList() const
    address = self.uglySide.call('ritual_ZNK10QJsonArray13toVariantListEv')
    from . import QVariant
    return QList[QVariant]._cuteOwning(address)

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

  @overload(int)
  def __getitem__(self, i: int) -> QJsonValueRef:
    """
    Calls Qt's 'QJsonValueRef QJsonArray::operator[](qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValueRef
      A new cute QJsonValueRef around the copy Qt gave back. Python owns it.
    """
    #  QJsonValueRef QJsonArray::operator[](qsizetype i)
    address = self.uglySide.call('ritual_ZN10QJsonArrayixEx', i)
    from . import QJsonValueRef
    return QJsonValueRef._cuteOwning(address)

  @overload(QJsonValue)
  def __add__(self, v: QJsonValue) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QJsonArray::operator+(const QJsonValue &v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator+

    Parameters
    ----------

    v : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QJsonArray::operator+(const QJsonValue &v) const
    address = self.uglySide.call(
        'ritual_ZNK10QJsonArrayplERK10QJsonValue', self._valueOf(v),
    )
    return QJsonArray._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QJsonValue)
  def __iadd__(self, v: QJsonValue) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray &QJsonArray::operator+=(const QJsonValue &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator+=

    Parameters
    ----------

    v : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  QJsonArray &QJsonArray::operator+=(const QJsonValue &v)
    self.uglySide.call(
        'ritual_ZN10QJsonArraypLERK10QJsonValue', self._valueOf(v),
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

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QJsonArray &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QJsonArray &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK10QJsonArray',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from . import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QJsonArray) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonArray &lhs, const QJsonArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator==

    Parameters
    ----------

    rhs : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  bool operator==(const QJsonArray &lhs, const QJsonArray &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QJsonArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __eq__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonArray &lhs, const QJsonValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator==

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator==(const QJsonArray &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QJsonArrayRK10QJsonValue',
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
  def __ne__(self, rhs: QJsonArray) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonArray &lhs, const QJsonArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator!=

    Parameters
    ----------

    rhs : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.
    """
    #  bool operator!=(const QJsonArray &lhs, const QJsonArray &rhs)
    return Rituals.call(
        'ritual_ZneRK10QJsonArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __ne__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonArray &lhs, const QJsonValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#operator!=

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator!=(const QJsonArray &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZneRK10QJsonArrayRK10QJsonValue',
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

  @overload()
  @overload(int)
  def detach(self, reserve: int = 0) -> bool:
    """
    Calls Qt's 'bool QJsonArray::detach(qsizetype reserve)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonarray.html#detach

    Parameters
    ----------

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QJsonArray::detach(qsizetype reserve)
    return self.uglySide.call('ritual_ZN10QJsonArray6detachEx', reserve)
