"""
QCborArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborarray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QList, QStringList, Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCborContainerPrivate, QCborValue, QCborValueConstRef
  from . import QCborValueRef, QJsonArray, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCborValue = WAIT['QCborValue']
  QCborValueConstRef = WAIT['QCborValueConstRef']
  QJsonArray = WAIT['QJsonArray']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborArray(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborArray: a plain Python object standing in front
  of one C++ QCborArray.

  C++ hands a QCborArray around as a copy, so every C++ QCborArray behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborArray that has a ritual and that Python can
  call so far, 41 names in all: 'toCborValue', 'size', 'isEmpty', 'clear',
  'at', 'first', 'last', '__getitem__', 'insert', 'prepend', 'append',
  'extract', 'removeAt', 'takeAt', 'removeFirst', 'removeLast', 'takeFirst',
  'takeLast', 'contains', 'compare', 'push_back', 'push_front', 'pop_front',
  'pop_back', 'empty', '__add__', '__iadd__', 'fromStringList',
  'fromVariantList', 'fromJsonArray', 'toVariantList', 'toJsonArray',
  '__eq__', '__ne__', '__lt__', '__gt__', '__le__', '__ge__',
  'comparesEqual_helper', 'compareThreeWay_helper', 'detach'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborArray::QCborArray(QCborArray &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QCborArray &QCborArray::operator=(const QCborArray &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCborArray &QCborArray::operator=(QCborArray &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCborArray::QCborArray(std::initializer_list<QCborValue> args)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCborArray::~QCborArray()': the destructor: Python removes its C++
    QCborArray by it, and has no other use for it.
  - Qt's 'void QCborArray::swap(QCborArray &other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QCborValueRef QCborArray::first()': takes in Python what
    'QCborValue QCborArray::first() const' takes.
  - Qt's 'QCborValueRef QCborArray::last()': takes in Python what 'QCborValue
    QCborArray::last() const' takes.
  - Qt's 'QCborValueRef QCborArray::operator[](qsizetype i)': takes in Python
    what 'const QCborValue QCborArray::operator[](qsizetype i) const' takes.
  - Qt's 'void QCborArray::insert(qsizetype i, QCborValue &&value)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QCborArray::prepend(QCborValue &&value)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QCborArray::append(QCborValue &&value)': takes a type Python
    has no way to hand over yet.
  - Qt's 'iterator QCborArray::begin()': gives a type Python has no way to
    take yet.
  - Qt's 'const_iterator QCborArray::constBegin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QCborArray::begin() const': gives a type Python has
    no way to take yet.
  - Qt's 'const_iterator QCborArray::cbegin() const': gives a type Python has
    no way to take yet.
  - Qt's 'iterator QCborArray::end()': gives a type Python has no way to take
    yet.
  - Qt's 'const_iterator QCborArray::constEnd() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QCborArray::end() const': gives a type Python has no
    way to take yet.
  - Qt's 'const_iterator QCborArray::cend() const': gives a type Python has
    no way to take yet.
  - Qt's 'iterator QCborArray::insert(iterator before, const QCborValue
    &value)': gives a type Python has no way to take yet.
  - Qt's 'iterator QCborArray::insert(const_iterator before, const QCborValue
    &value)': gives a type Python has no way to take yet.
  - Qt's 'iterator QCborArray::erase(iterator it)': gives a type Python has
    no way to take yet.
  - Qt's 'iterator QCborArray::erase(const_iterator it)': gives a type Python
    has no way to take yet.
  - Qt's 'QCborArray &QCborArray::operator<<(const QCborValue &v)': gives a
    type Python has no way to take yet.
  - Qt's 'QCborArray QCborArray::fromJsonArray(QJsonArray &&array)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool operator==(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator==(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator!=(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator!=(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator<(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator>(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator>(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator<(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator<=(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator>=(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator>=(const QCborValue &lhs, const QCborArray &rhs)':
    takes in Python what 'bool operator<=(const QCborArray &lhs, const
    QCborValue &rhs)' takes.
  - Qt's 'bool operator==(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator==(const QCborArray &lhs,
    const QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator!=(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator!=(const QCborArray &lhs,
    const QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator<(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator>(const QCborArray &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator>(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator<(const QCborArray &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator<=(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator>=(const QCborArray &lhs,
    const QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator>=(const QCborValueConstRef &lhs, const QCborArray
    &rhs)': takes in Python what 'bool operator<=(const QCborArray &lhs,
    const QCborValueConstRef &rhs)' takes.
  - Qt's 'QCborArray::QCborArray(QCborContainerPrivate &dd)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCborArray is created at the first use, not by 'QCborArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborArray back gives a copy the ritual made for
    Python, in a new cute QCborArray.
  - Each name of Qt's QCborArray that has no cute function yet, 'begin',
    'cbegin', 'cend', 'constBegin', 'constEnd', 'end', 'erase', 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QCborArray, each a class in here as in C++.

  class ConstIterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCborArray::ConstIterator: a plain Python object
    standing in front of one C++ QCborArray::ConstIterator.

    C++ hands a QCborArray::ConstIterator around as a copy, so every C++
    QCborArray::ConstIterator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QCborArray::ConstIterator that has a ritual and
    that Python can call so far, 13 names in all: '__getitem__', '__iadd__',
    '__isub__', '__add__', '__sub__', 'comparesEqual_helper',
    'compareThreeWay_helper', '__eq__', '__ne__', '__lt__', '__gt__',
    '__le__', '__ge__'. It can be made from Python, in 3 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'ConstIterator &QCborArray::ConstIterator::operator=(const
      ConstIterator &other)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'QCborValueConstRef QCborArray::ConstIterator::operator*() const':
      an operator Python has no name for.
    - Qt's 'const QCborValueConstRef *QCborArray::ConstIterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'ConstIterator &QCborArray::ConstIterator::operator++()': an
      operator Python has no name for.
    - Qt's 'ConstIterator QCborArray::ConstIterator::operator++(int a0)': an
      operator Python has no name for.
    - Qt's 'ConstIterator &QCborArray::ConstIterator::operator--()': an
      operator Python has no name for.
    - Qt's 'ConstIterator QCborArray::ConstIterator::operator--(int a0)': an
      operator Python has no name for.
    - Qt's 'QCborArray::ConstIterator::~ConstIterator()': the destructor:
      Python removes its C++ QCborArray::ConstIterator by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QCborArray::ConstIterator is created at the first use, not by
      'QCborArray::ConstIterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCborArray::ConstIterator back gives a copy the
      ritual made for Python, in a new cute QCborArray::ConstIterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QCborContainerPrivate = WAIT['QCborContainerPrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QCborArray.ConstIterator,
        rhs: QCborArray.ConstIterator,
    ) -> bool:
      """
      Calls Qt's 'bool QCborArray::ConstIterator::comparesEqual_helper(const
      ConstIterator &lhs, const ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html

      Parameters
      ----------

      lhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool QCborArray::ConstIterator::comparesEqual_helper(const
      #      ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZN10QCborArray13ConstIterator20comparesEqual_helperERKS0_'
          'S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QCborArray.ConstIterator,
        rhs: QCborArray.ConstIterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QCborArray::ConstIterator::compareThreeWay_helper(const ConstIterator
      &lhs, const ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html

      Parameters
      ----------

      lhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering
      #      QCborArray::ConstIterator::compareThreeWay_helper(const
      #      ConstIterator &lhs, const ConstIterator &rhs)
      address = Rituals.call(
          'ritual_ZN10QCborArray13ConstIterator22compareThreeWay_helperERKS'
          '0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCborArray::ConstIterator'

    #  Qt's '~QCborArray::ConstIterator()'. Naming it makes this a value
    #  class: Python owns every C++ QCborArray::ConstIterator behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QCborArray13ConstIteratorD1Ev'

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
    def __getitem__(self, j: int) -> QCborValueConstRef:
      """
      Calls Qt's 'QCborValueConstRef
      QCborArray::ConstIterator::operator[](qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator[]

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborValueConstRef
        A new cute QCborValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QCborValueConstRef QCborArray::ConstIterator::operator[](qsizetype
      #      j) const
      address = self.uglySide.call(
          'ritual_ZNK10QCborArray13ConstIteratorixEx', j,
      )
      from . import QCborValueConstRef
      return QCborValueConstRef._cuteOwning(address)

    @overload(int)
    def __iadd__(self, j: int) -> QCborArray.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      &QCborArray::ConstIterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  ConstIterator &QCborArray::ConstIterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN10QCborArray13ConstIteratorpLEx', j)
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
    def __isub__(self, j: int) -> QCborArray.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      &QCborArray::ConstIterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  ConstIterator &QCborArray::ConstIterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN10QCborArray13ConstIteratormIEx', j)
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
    def __add__(self, j: int) -> QCborArray.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      QCborArray::ConstIterator::operator+(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborArray.ConstIterator
        A new cute QCborArray::ConstIterator around the copy Qt gave back.
        Python owns it.
      """
      #  ConstIterator QCborArray::ConstIterator::operator+(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK10QCborArray13ConstIteratorplEx', j,
      )
      return QCborArray.ConstIterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QCborArray.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      QCborArray::ConstIterator::operator-(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborArray.ConstIterator
        A new cute QCborArray::ConstIterator around the copy Qt gave back.
        Python owns it.
      """
      #  ConstIterator QCborArray::ConstIterator::operator-(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK10QCborArray13ConstIteratormiEx', j,
      )
      return QCborArray.ConstIterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QCborArray.ConstIterator) -> int:
      """
      Calls Qt's 'qsizetype
      QCborArray::ConstIterator::operator-(ConstIterator j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator-

      Parameters
      ----------

      j : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  qsizetype QCborArray::ConstIterator::operator-(ConstIterator j)
      #      const
      return self.uglySide.call(
          'ritual_ZNK10QCborArray13ConstIteratormiES0_', self._valueOf(j),
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
    def __eq__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator==(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator==

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator==(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN10QCborArray13ConstIteratorES2_',
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
    def __ne__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator!=

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator!=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN10QCborArray13ConstIteratorES2_',
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
    def __lt__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator<(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator<

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator<(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN10QCborArray13ConstIteratorES2_',
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
    def __gt__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator>(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator>

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator>(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN10QCborArray13ConstIteratorES2_',
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
    def __le__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator<=

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator<=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN10QCborArray13ConstIteratorES2_',
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
    def __ge__(self, rhs: QCborArray.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#operator>=

      Parameters
      ----------

      rhs : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  bool operator>=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN10QCborArray13ConstIteratorES2_',
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

    @overload(QCborContainerPrivate, int)
    @overload(NoneType, int)
    def __init__(self, dd: Optional[QCborContainerPrivate], ii: int) -> None:
      """
      Notes what was given, for Qt's
      'QCborArray::ConstIterator::ConstIterator(QCborContainerPrivate *dd,
      qsizetype ii)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#ConstIterator

      Parameters
      ----------

      dd : Optional[QCborContainerPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      ii : int
        Passed on as it is.
      """
      #  QCborArray::ConstIterator::ConstIterator(QCborContainerPrivate *dd,
      #      qsizetype ii)
      self._noteCreation(QCborArray.ConstIterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray13ConstIteratorC1EP21QCborContainerPrivatex',
          self._addressOf(dd), ii,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QCborArray::ConstIterator::ConstIterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#ConstIterator
      """
      #  QCborArray::ConstIterator::ConstIterator()
      self._noteCreation(QCborArray.ConstIterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray13ConstIteratorC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: QCborArray.ConstIterator) -> None:
      """
      Notes what was given, for Qt's
      'QCborArray::ConstIterator::ConstIterator(const ConstIterator &a0)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-constiterator.html#ConstIterator

      Parameters
      ----------

      a0 : QCborArray.ConstIterator
        Passed on as a value: Qt reads the C++ QCborArray::ConstIterator,
        which stays Python's own.
      """
      #  QCborArray::ConstIterator::ConstIterator(const ConstIterator &a0)
      self._noteCreation(QCborArray.ConstIterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray13ConstIteratorC1ERKS0_', self._valueOf(a0),
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

  class Iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCborArray::Iterator: a plain Python object
    standing in front of one C++ QCborArray::Iterator.

    C++ hands a QCborArray::Iterator around as a copy, so every C++
    QCborArray::Iterator behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCborArray::Iterator that has a ritual and that
    Python can call so far, 13 names in all: '__getitem__', '__iadd__',
    '__isub__', '__add__', '__sub__', 'comparesEqual_helper',
    'compareThreeWay_helper', '__eq__', '__ne__', '__lt__', '__gt__',
    '__le__', '__ge__'. It can be made from Python, in 3 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Iterator &QCborArray::Iterator::operator=(const Iterator
      &other)': assignment: Python binds a name and has no operator for it.
    - Qt's 'QCborValueRef QCborArray::Iterator::operator*() const': an
      operator Python has no name for.
    - Qt's 'QCborValueRef *QCborArray::Iterator::operator->()': an operator
      Python has no name for.
    - Qt's 'const QCborValueConstRef *QCborArray::Iterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'Iterator &QCborArray::Iterator::operator++()': an operator Python
      has no name for.
    - Qt's 'Iterator QCborArray::Iterator::operator++(int a0)': an operator
      Python has no name for.
    - Qt's 'Iterator &QCborArray::Iterator::operator--()': an operator Python
      has no name for.
    - Qt's 'Iterator QCborArray::Iterator::operator--(int a0)': an operator
      Python has no name for.
    - Qt's 'bool QCborArray::Iterator::comparesEqual_helper(const Iterator
      &lhs, const ConstIterator &rhs)': names 'QCborArray::ConstIterator',
      which stands beside this class inside 'QCborArray' and cannot be named
      from here.
    - Qt's 'Qt::strong_ordering
      QCborArray::Iterator::compareThreeWay_helper(const Iterator &lhs, const
      ConstIterator &rhs)': names 'QCborArray::ConstIterator', which stands
      beside this class inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator==(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator!=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator<(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator>(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator<=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator>=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator==(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator!=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator<(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator>(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator<=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'bool operator>=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborArray::ConstIterator', which stands beside this class
      inside 'QCborArray' and cannot be named from here.
    - Qt's 'QCborArray::Iterator::~Iterator()': the destructor: Python
      removes its C++ QCborArray::Iterator by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCborArray::Iterator is created at the first use, not by
      'QCborArray::Iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCborArray::Iterator back gives a copy the ritual
      made for Python, in a new cute QCborArray::Iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QCborContainerPrivate = WAIT['QCborContainerPrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QCborArray.Iterator,
        rhs: QCborArray.Iterator,
    ) -> bool:
      """
      Calls Qt's 'bool QCborArray::Iterator::comparesEqual_helper(const
      Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#comparesEqual_helper

      Parameters
      ----------

      lhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool QCborArray::Iterator::comparesEqual_helper(const Iterator &lhs,
      #      const Iterator &rhs)
      return Rituals.call(
          'ritual_ZN10QCborArray8Iterator20comparesEqual_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QCborArray.Iterator,
        rhs: QCborArray.Iterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QCborArray::Iterator::compareThreeWay_helper(const Iterator &lhs, const
      Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#compareThreeWay_helper

      Parameters
      ----------

      lhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering
      #      QCborArray::Iterator::compareThreeWay_helper(const Iterator
      #      &lhs, const Iterator &rhs)
      address = Rituals.call(
          'ritual_ZN10QCborArray8Iterator22compareThreeWay_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCborArray::Iterator'

    #  Qt's '~QCborArray::Iterator()'. Naming it makes this a value class:
    #  Python owns every C++ QCborArray::Iterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QCborArray8IteratorD1Ev'

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
    def __getitem__(self, j: int) -> QCborValueRef:
      """
      Calls Qt's 'QCborValueRef QCborArray::Iterator::operator[](qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator[]

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborValueRef
        A new cute QCborValueRef around the copy Qt gave back. Python owns
        it.
      """
      #  QCborValueRef QCborArray::Iterator::operator[](qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QCborArray8IteratorixEx', j)
      from . import QCborValueRef
      return QCborValueRef._cuteOwning(address)

    @overload(int)
    def __iadd__(self, j: int) -> QCborArray.Iterator:
      """
      Calls Qt's 'Iterator &QCborArray::Iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  Iterator &QCborArray::Iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN10QCborArray8IteratorpLEx', j)
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
    def __isub__(self, j: int) -> QCborArray.Iterator:
      """
      Calls Qt's 'Iterator &QCborArray::Iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  Iterator &QCborArray::Iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN10QCborArray8IteratormIEx', j)
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
    def __add__(self, j: int) -> QCborArray.Iterator:
      """
      Calls Qt's 'Iterator QCborArray::Iterator::operator+(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborArray.Iterator
        A new cute QCborArray::Iterator around the copy Qt gave back. Python
        owns it.
      """
      #  Iterator QCborArray::Iterator::operator+(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QCborArray8IteratorplEx', j)
      return QCborArray.Iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QCborArray.Iterator:
      """
      Calls Qt's 'Iterator QCborArray::Iterator::operator-(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborArray.Iterator
        A new cute QCborArray::Iterator around the copy Qt gave back. Python
        owns it.
      """
      #  Iterator QCborArray::Iterator::operator-(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK10QCborArray8IteratormiEx', j)
      return QCborArray.Iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QCborArray.Iterator) -> int:
      """
      Calls Qt's 'qsizetype QCborArray::Iterator::operator-(Iterator j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator-

      Parameters
      ----------

      j : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  qsizetype QCborArray::Iterator::operator-(Iterator j) const
      return self.uglySide.call(
          'ritual_ZNK10QCborArray8IteratormiES0_', self._valueOf(j),
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
    def __eq__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator==

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator==(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN10QCborArray8IteratorES2_',
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
    def __ne__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator!=

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator!=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN10QCborArray8IteratorES2_',
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
    def __lt__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator<

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator<(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN10QCborArray8IteratorES2_',
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
    def __gt__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator>

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator>(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN10QCborArray8IteratorES2_',
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
    def __le__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator<=

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator<=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN10QCborArray8IteratorES2_',
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
    def __ge__(self, rhs: QCborArray.Iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#operator>=

      Parameters
      ----------

      rhs : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  bool operator>=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN10QCborArray8IteratorES2_',
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

    @overload(QCborContainerPrivate, int)
    @overload(NoneType, int)
    def __init__(self, dd: Optional[QCborContainerPrivate], ii: int) -> None:
      """
      Notes what was given, for Qt's
      'QCborArray::Iterator::Iterator(QCborContainerPrivate *dd, qsizetype
      ii)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#Iterator

      Parameters
      ----------

      dd : Optional[QCborContainerPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      ii : int
        Passed on as it is.
      """
      #  QCborArray::Iterator::Iterator(QCborContainerPrivate *dd, qsizetype
      #      ii)
      self._noteCreation(QCborArray.Iterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray8IteratorC1EP21QCborContainerPrivatex',
          self._addressOf(dd), ii,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QCborArray::Iterator::Iterator()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#Iterator
      """
      #  QCborArray::Iterator::Iterator()
      self._noteCreation(QCborArray.Iterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray8IteratorC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: QCborArray.Iterator) -> None:
      """
      Notes what was given, for Qt's 'QCborArray::Iterator::Iterator(const
      Iterator &a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcborarray-iterator.html#Iterator

      Parameters
      ----------

      a0 : QCborArray.Iterator
        Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
        stays Python's own.
      """
      #  QCborArray::Iterator::Iterator(const Iterator &a0)
      self._noteCreation(QCborArray.Iterator, lambda: Rituals.call(
          'ritual_ZN10QCborArray8IteratorC1ERKS0_', self._valueOf(a0),
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
  def fromStringList(list: QStringList) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborArray::fromStringList(const QStringList
    &list)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#fromStringList

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborArray::fromStringList(const QStringList &list)
    address = Rituals.call(
        'ritual_ZN10QCborArray14fromStringListERK5QListI7QStringE',
        CuteMixin._valueOf(list),
    )
    return QCborArray._cuteOwning(address)

  @staticmethod
  @overload(QList[QVariant])
  def fromVariantList(list: QList[QVariant]) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborArray::fromVariantList(const QVariantList
    &list)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#fromVariantList

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborArray::fromVariantList(const QVariantList &list)
    address = Rituals.call(
        'ritual_ZN10QCborArray15fromVariantListERK5QListI8QVariantE',
        CuteMixin._valueOf(list),
    )
    return QCborArray._cuteOwning(address)

  @staticmethod
  @overload(QJsonArray)
  def fromJsonArray(array: QJsonArray) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborArray::fromJsonArray(const QJsonArray
    &array)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#fromJsonArray

    Parameters
    ----------

    array : QJsonArray
      Passed on as a value: Qt reads the C++ QJsonArray, which stays Python's
      own.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborArray::fromJsonArray(const QJsonArray &array)
    address = Rituals.call(
        'ritual_ZN10QCborArray13fromJsonArrayERK10QJsonArray',
        CuteMixin._valueOf(array),
    )
    return QCborArray._cuteOwning(address)

  @staticmethod
  @overload(THIS, QCborValue)
  def comparesEqual_helper(lhs: QCborArray, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool QCborArray::comparesEqual_helper(const QCborArray &lhs,
    const QCborValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborarray.html#comparesEqual_helper

    Parameters
    ----------

    lhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool QCborArray::comparesEqual_helper(const QCborArray &lhs, const
    #      QCborValue &rhs)
    return Rituals.call(
        'ritual_ZN10QCborArray20comparesEqual_helperERKS_RK10QCborValue',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(THIS, QCborValueConstRef)
  def comparesEqual_helper(lhs: QCborArray, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool QCborArray::comparesEqual_helper(const QCborArray &lhs,
    QCborValueConstRef rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborarray.html#comparesEqual_helper

    Parameters
    ----------

    lhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool QCborArray::comparesEqual_helper(const QCborArray &lhs,
    #      QCborValueConstRef rhs)
    return Rituals.call(
        'ritual_ZN10QCborArray20comparesEqual_helperERKS_18QCborValueConstR'
        'ef',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(THIS, QCborValue)
  def compareThreeWay_helper(
      lhs: QCborArray,
      rhs: QCborValue,
  ) -> Qt.strong_ordering:
    """
    Calls Qt's 'Qt::strong_ordering QCborArray::compareThreeWay_helper(const
    QCborArray &lhs, const QCborValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborarray.html#compareThreeWay_helper

    Parameters
    ----------

    lhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    Qt.strong_ordering
      A new cute Qt::strong_ordering around the copy Qt gave back. Python
      owns it.
    """
    #  Qt::strong_ordering QCborArray::compareThreeWay_helper(const
    #      QCborArray &lhs, const QCborValue &rhs)
    address = Rituals.call(
        'ritual_ZN10QCborArray22compareThreeWay_helperERKS_RK10QCborValue',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )
    return Qt.strong_ordering._cuteOwning(address)

  @staticmethod
  @overload(THIS, QCborValueConstRef)
  def compareThreeWay_helper(
      lhs: QCborArray,
      rhs: QCborValueConstRef,
  ) -> Qt.strong_ordering:
    """
    Calls Qt's 'Qt::strong_ordering QCborArray::compareThreeWay_helper(const
    QCborArray &lhs, QCborValueConstRef rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborarray.html#compareThreeWay_helper

    Parameters
    ----------

    lhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.

    Returns
    -------

    Qt.strong_ordering
      A new cute Qt::strong_ordering around the copy Qt gave back. Python
      owns it.
    """
    #  Qt::strong_ordering QCborArray::compareThreeWay_helper(const
    #      QCborArray &lhs, QCborValueConstRef rhs)
    address = Rituals.call(
        'ritual_ZN10QCborArray22compareThreeWay_helperERKS_18QCborValueCons'
        'tRef',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )
    return Qt.strong_ordering._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborArray'

  #  Qt's '~QCborArray()'. Naming it makes this a value class: Python owns
  #  every C++ QCborArray behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QCborArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toCborValue(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::toCborValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#toCborValue

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::toCborValue() const
    address = self.uglySide.call('ritual_ZNK10QCborArray11toCborValueEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QCborArray::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#size
    """
    #  qsizetype QCborArray::size() const
    return self.uglySide.call('ritual_ZNK10QCborArray4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCborArray::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#isEmpty
    """
    #  bool QCborArray::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QCborArray7isEmptyEv')

  @overload(int)
  def at(self, i: int) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::at(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK10QCborArray2atEx', i)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def first(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#first

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::first() const
    address = self.uglySide.call('ritual_ZNK10QCborArray5firstEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def last(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::last() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#last

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::last() const
    address = self.uglySide.call('ritual_ZNK10QCborArray4lastEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def contains(self, value: QCborValue) -> bool:
    """
    Calls Qt's 'bool QCborArray::contains(const QCborValue &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#contains

    Parameters
    ----------

    value : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool QCborArray::contains(const QCborValue &value) const
    return self.uglySide.call(
        'ritual_ZNK10QCborArray8containsERK10QCborValue',
        self._valueOf(value),
    )

  @overload(THIS)
  def compare(self, other: QCborArray) -> int:
    """
    Calls Qt's 'int QCborArray::compare(const QCborArray &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#compare

    Parameters
    ----------

    other : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  int QCborArray::compare(const QCborArray &other) const
    return self.uglySide.call(
        'ritual_ZNK10QCborArray7compareERKS_', self._valueOf(other),
    )

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QCborArray::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#empty
    """
    #  bool QCborArray::empty() const
    return self.uglySide.call('ritual_ZNK10QCborArray5emptyEv')

  def toVariantList(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QCborArray::toVariantList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#toVariantList

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QCborArray::toVariantList() const
    address = self.uglySide.call('ritual_ZNK10QCborArray13toVariantListEv')
    from . import QVariant
    return QList[QVariant]._cuteOwning(address)

  def toJsonArray(self) -> QJsonArray:
    """
    Calls Qt's 'QJsonArray QCborArray::toJsonArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#toJsonArray

    Returns
    -------

    QJsonArray
      A new cute QJsonArray around the copy Qt gave back. Python owns it.
    """
    #  QJsonArray QCborArray::toJsonArray() const
    address = self.uglySide.call('ritual_ZNK10QCborArray11toJsonArrayEv')
    from . import QJsonArray
    return QJsonArray._cuteOwning(address)

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
  def __getitem__(self, i: int) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborArray::operator[](qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator[]

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborArray::operator[](qsizetype i) const
    address = self.uglySide.call('ritual_ZNK10QCborArrayixEx', i)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def __add__(self, v: QCborValue) -> QCborArray:
    """
    Calls Qt's 'QCborArray QCborArray::operator+(const QCborValue &v) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator+

    Parameters
    ----------

    v : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QCborArray
      A new cute QCborArray around the copy Qt gave back. Python owns it.
    """
    #  QCborArray QCborArray::operator+(const QCborValue &v) const
    address = self.uglySide.call(
        'ritual_ZNK10QCborArrayplERK10QCborValue', self._valueOf(v),
    )
    return QCborArray._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QCborValue)
  def __iadd__(self, v: QCborValue) -> QCborArray:
    """
    Calls Qt's 'QCborArray &QCborArray::operator+=(const QCborValue &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator+=

    Parameters
    ----------

    v : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  QCborArray &QCborArray::operator+=(const QCborValue &v)
    self.uglySide.call(
        'ritual_ZN10QCborArraypLERK10QCborValue', self._valueOf(v),
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
  def __eq__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator==

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator==(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __eq__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator==

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator==(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __eq__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator==

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QCborArrayRK18QCborValueConstRef',
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
  def __ne__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator!=

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator!=(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZneRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ne__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator!=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator!=(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZneRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __ne__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator!=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZneRK10QCborArrayRK18QCborValueConstRef',
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
  def __lt__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator<(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZltRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __lt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZltRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __lt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZltRK10QCborArrayRK18QCborValueConstRef',
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
  def __gt__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator>(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __gt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __gt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZgtRK10QCborArrayRK18QCborValueConstRef',
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
  def __le__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<=

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator<=(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZleRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __le__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<=(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZleRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __le__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator<=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<=(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZleRK10QCborArrayRK18QCborValueConstRef',
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
  def __ge__(self, rhs: QCborArray) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborArray &lhs, const QCborArray
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>=

    Parameters
    ----------

    rhs : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  bool operator>=(const QCborArray &lhs, const QCborArray &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QCborArrayS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ge__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborArray &lhs, const QCborValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>=(const QCborArray &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QCborArrayRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __ge__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborArray &lhs, const
    QCborValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#operator>=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>=(const QCborArray &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZgeRK10QCborArrayRK18QCborValueConstRef',
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
    Notes what was given, for Qt's 'QCborArray::QCborArray()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#QCborArray
    """
    #  QCborArray::QCborArray()
    self._noteCreation(QCborArray, lambda: Rituals.call(
        'ritual_ZN10QCborArrayC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCborArray) -> None:
    """
    Notes what was given, for Qt's 'QCborArray::QCborArray(const QCborArray
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#QCborArray

    Parameters
    ----------

    other : QCborArray
      Passed on as a value: Qt reads the C++ QCborArray, which stays Python's
      own.
    """
    #  QCborArray::QCborArray(const QCborArray &other)
    self._noteCreation(QCborArray, lambda: Rituals.call(
        'ritual_ZN10QCborArrayC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QCborArray::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#clear
    """
    #  void QCborArray::clear()
    self.uglySide.call('ritual_ZN10QCborArray5clearEv')

  @overload(int, QCborValue)
  def insert(self, i: int, value: QCborValue) -> None:
    """
    Calls Qt's 'void QCborArray::insert(qsizetype i, const QCborValue
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#insert

    Parameters
    ----------

    i : int
      Passed on as it is.

    value : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborArray::insert(qsizetype i, const QCborValue &value)
    self.uglySide.call(
        'ritual_ZN10QCborArray6insertExRK10QCborValue',
        i, self._valueOf(value),
    )

  @overload(QCborValue)
  def prepend(self, value: QCborValue) -> None:
    """
    Calls Qt's 'void QCborArray::prepend(const QCborValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#prepend

    Parameters
    ----------

    value : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborArray::prepend(const QCborValue &value)
    self.uglySide.call(
        'ritual_ZN10QCborArray7prependERK10QCborValue', self._valueOf(value),
    )

  @overload(QCborValue)
  def append(self, value: QCborValue) -> None:
    """
    Calls Qt's 'void QCborArray::append(const QCborValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#append

    Parameters
    ----------

    value : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborArray::append(const QCborValue &value)
    self.uglySide.call(
        'ritual_ZN10QCborArray6appendERK10QCborValue', self._valueOf(value),
    )

  @overload(ConstIterator)
  def extract(self, it: ConstIterator) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::extract(ConstIterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#extract

    Parameters
    ----------

    it : ConstIterator
      Passed on as a value: Qt reads the C++ QCborArray::ConstIterator, which
      stays Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::extract(ConstIterator it)
    address = self.uglySide.call(
        'ritual_ZN10QCborArray7extractENS_13ConstIteratorE',
        self._valueOf(it),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(Iterator)
  def extract(self, it: Iterator) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::extract(Iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#extract

    Parameters
    ----------

    it : Iterator
      Passed on as a value: Qt reads the C++ QCborArray::Iterator, which
      stays Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::extract(Iterator it)
    address = self.uglySide.call(
        'ritual_ZN10QCborArray7extractENS_8IteratorE', self._valueOf(it),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(int)
  def removeAt(self, i: int) -> None:
    """
    Calls Qt's 'void QCborArray::removeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#removeAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QCborArray::removeAt(qsizetype i)
    self.uglySide.call('ritual_ZN10QCborArray8removeAtEx', i)

  @overload(int)
  def takeAt(self, i: int) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::takeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#takeAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::takeAt(qsizetype i)
    address = self.uglySide.call('ritual_ZN10QCborArray6takeAtEx', i)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def removeFirst(self) -> None:
    """
    Calls Qt's 'void QCborArray::removeFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#removeFirst
    """
    #  void QCborArray::removeFirst()
    self.uglySide.call('ritual_ZN10QCborArray11removeFirstEv')

  def removeLast(self) -> None:
    """
    Calls Qt's 'void QCborArray::removeLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#removeLast
    """
    #  void QCborArray::removeLast()
    self.uglySide.call('ritual_ZN10QCborArray10removeLastEv')

  def takeFirst(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::takeFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#takeFirst

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::takeFirst()
    address = self.uglySide.call('ritual_ZN10QCborArray9takeFirstEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def takeLast(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborArray::takeLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#takeLast

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborArray::takeLast()
    address = self.uglySide.call('ritual_ZN10QCborArray8takeLastEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def push_back(self, t: QCborValue) -> None:
    """
    Calls Qt's 'void QCborArray::push_back(const QCborValue &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#push_back

    Parameters
    ----------

    t : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborArray::push_back(const QCborValue &t)
    self.uglySide.call(
        'ritual_ZN10QCborArray9push_backERK10QCborValue', self._valueOf(t),
    )

  @overload(QCborValue)
  def push_front(self, t: QCborValue) -> None:
    """
    Calls Qt's 'void QCborArray::push_front(const QCborValue &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#push_front

    Parameters
    ----------

    t : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborArray::push_front(const QCborValue &t)
    self.uglySide.call(
        'ritual_ZN10QCborArray10push_frontERK10QCborValue', self._valueOf(t),
    )

  def pop_front(self) -> None:
    """
    Calls Qt's 'void QCborArray::pop_front()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#pop_front
    """
    #  void QCborArray::pop_front()
    self.uglySide.call('ritual_ZN10QCborArray9pop_frontEv')

  def pop_back(self) -> None:
    """
    Calls Qt's 'void QCborArray::pop_back()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#pop_back
    """
    #  void QCborArray::pop_back()
    self.uglySide.call('ritual_ZN10QCborArray8pop_backEv')

  @overload()
  @overload(int)
  def detach(self, reserve: int = 0) -> None:
    """
    Calls Qt's 'void QCborArray::detach(qsizetype reserve)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborarray.html#detach

    Parameters
    ----------

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCborArray::detach(qsizetype reserve)
    self.uglySide.call('ritual_ZN10QCborArray6detachEx', reserve)

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborArray::begin()': gives a type Python has no way to
      take yet.
    - Qt's 'const_iterator QCborArray::begin() const': gives a type Python
      has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.begin' has no cute function yet. Qt's 'iterator "
        "QCborArray::begin()': gives a type Python has no way to take yet. "
        "Qt's 'const_iterator QCborArray::begin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborArray::cbegin() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.cbegin' has no cute function yet. Qt's 'const_iterator "
        "QCborArray::cbegin() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborArray::cend() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.cend' has no cute function yet. Qt's 'const_iterator "
        "QCborArray::cend() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborArray::constBegin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.constBegin' has no cute function yet. Qt's "
        "'const_iterator QCborArray::constBegin() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborArray::constEnd() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.constEnd' has no cute function yet. Qt's "
        "'const_iterator QCborArray::constEnd() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborArray::end()': gives a type Python has no way to
      take yet.
    - Qt's 'const_iterator QCborArray::end() const': gives a type Python has
      no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.end' has no cute function yet. Qt's 'iterator "
        "QCborArray::end()': gives a type Python has no way to take yet. "
        "Qt's 'const_iterator QCborArray::end() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def erase(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborArray::erase(iterator it)': gives a type Python has
      no way to take yet.
    - Qt's 'iterator QCborArray::erase(const_iterator it)': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborArray.erase' has no cute function yet. Qt's 'iterator "
        "QCborArray::erase(iterator it)': gives a type Python has no way to "
        "take yet. Qt's 'iterator QCborArray::erase(const_iterator it)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCborArray::swap(QCborArray &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCborArray.swap' has no cute function yet. Qt's 'void "
        "QCborArray::swap(QCborArray &other)': takes a type Python has no "
        "way to hand over yet.")


#  Qt's 'QList<QCborArray>': the list of QCborArray, which
#  'QList[QCborArray]' gives. It is made here, so that there is one as soon
#  as there can be a QCborArray.
QList.createKind(
    QCborArray, 'value',
    make='ritual_list_make_QCborArray',
    add='ritual_list_add_QCborArray',
    size='ritual_list_size_QCborArray',
    at='ritual_list_at_QCborArray',
    drop='ritual_list_drop_QCborArray',
)
