"""
QCborMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcbormap.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QHash, QList, QMap, Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCborContainerPrivate, QCborValue, QCborValueConstRef
  from . import QCborValueRef, QJsonObject, QLatin1String, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCborValue = WAIT['QCborValue']
  QCborValueConstRef = WAIT['QCborValueConstRef']
  QJsonObject = WAIT['QJsonObject']
  QLatin1String = WAIT['QLatin1String']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborMap: a plain Python object standing in front of
  one C++ QCborMap.

  C++ hands a QCborMap around as a copy, so every C++ QCborMap behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCborMap that has a ritual and that Python can call
  so far, 28 names in all: 'toCborValue', 'size', 'isEmpty', 'clear', 'keys',
  'value', '__getitem__', 'take', 'remove', 'contains', 'compare', 'extract',
  'empty', 'fromVariantMap', 'fromVariantHash', 'fromJsonObject',
  'toVariantMap', 'toVariantHash', 'toJsonObject', 'detach', '__eq__',
  '__ne__', '__lt__', '__gt__', '__le__', '__ge__', 'comparesEqual_helper',
  'compareThreeWay_helper'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborMap::QCborMap(QCborMap &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QCborMap &QCborMap::operator=(const QCborMap &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCborMap &QCborMap::operator=(QCborMap &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCborMap::QCborMap(std::initializer_list<value_type> args)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QCborMap::~QCborMap()': the destructor: Python removes its C++
    QCborMap by it, and has no other use for it.
  - Qt's 'void QCborMap::swap(QCborMap &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QCborValueRef QCborMap::operator[](qint64 key)': takes in Python
    what 'const QCborValue QCborMap::operator[](qint64 key) const' takes.
  - Qt's 'QCborValueRef QCborMap::operator[](QLatin1StringView key)': takes
    in Python what 'const QCborValue QCborMap::operator[](QLatin1StringView
    key) const' takes.
  - Qt's 'QCborValueRef QCborMap::operator[](const QString &key)': takes in
    Python what 'const QCborValue QCborMap::operator[](const QString &key)
    const' takes.
  - Qt's 'QCborValueRef QCborMap::operator[](const QCborValue &key)': takes
    in Python what 'const QCborValue QCborMap::operator[](const QCborValue
    &key) const' takes.
  - Qt's 'iterator QCborMap::begin()': gives a type Python has no way to take
    yet.
  - Qt's 'const_iterator QCborMap::constBegin() const': gives a type Python
    has no way to take yet.
  - Qt's 'const_iterator QCborMap::begin() const': gives a type Python has no
    way to take yet.
  - Qt's 'const_iterator QCborMap::cbegin() const': gives a type Python has
    no way to take yet.
  - Qt's 'iterator QCborMap::end()': gives a type Python has no way to take
    yet.
  - Qt's 'const_iterator QCborMap::constEnd() const': gives a type Python has
    no way to take yet.
  - Qt's 'const_iterator QCborMap::end() const': gives a type Python has no
    way to take yet.
  - Qt's 'const_iterator QCborMap::cend() const': gives a type Python has no
    way to take yet.
  - Qt's 'iterator QCborMap::erase(iterator it)': gives a type Python has no
    way to take yet.
  - Qt's 'iterator QCborMap::erase(const_iterator it)': gives a type Python
    has no way to take yet.
  - Qt's 'key_value_iterator QCborMap::keyValueBegin()': gives a type Python
    has no way to take yet.
  - Qt's 'key_value_iterator QCborMap::keyValueEnd()': gives a type Python
    has no way to take yet.
  - Qt's 'const_key_value_iterator QCborMap::keyValueBegin() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QCborMap::constKeyValueBegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QCborMap::keyValueEnd() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QCborMap::constKeyValueEnd() const': gives
    a type Python has no way to take yet.
  - Qt's 'QtPrivate::QKeyValueRange<QCborMap &> QCborMap::asKeyValueRange()':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::QKeyValueRange<const QCborMap &>
    QCborMap::asKeyValueRange() const': gives a type Python has no way to
    take yet.
  - Qt's 'iterator QCborMap::find(qint64 key)': gives a type Python has no
    way to take yet.
  - Qt's 'iterator QCborMap::find(QLatin1StringView key)': gives a type
    Python has no way to take yet.
  - Qt's 'iterator QCborMap::find(const QString &key)': gives a type Python
    has no way to take yet.
  - Qt's 'iterator QCborMap::find(const QCborValue &key)': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::constFind(qint64 key) const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::constFind(QLatin1StringView key) const':
    gives a type Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::constFind(const QString &key) const':
    gives a type Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::constFind(const QCborValue &key) const':
    gives a type Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::find(qint64 key) const': gives a type
    Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::find(QLatin1StringView key) const': gives
    a type Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::find(const QString &key) const': gives a
    type Python has no way to take yet.
  - Qt's 'const_iterator QCborMap::find(const QCborValue &key) const': gives
    a type Python has no way to take yet.
  - Qt's 'iterator QCborMap::insert(qint64 key, const QCborValue &value_)':
    gives a type Python has no way to take yet.
  - Qt's 'iterator QCborMap::insert(QLatin1StringView key, const QCborValue
    &value_)': gives a type Python has no way to take yet.
  - Qt's 'iterator QCborMap::insert(const QString &key, const QCborValue
    &value_)': gives a type Python has no way to take yet.
  - Qt's 'iterator QCborMap::insert(const QCborValue &key, const QCborValue
    &value_)': gives a type Python has no way to take yet.
  - Qt's 'iterator QCborMap::insert(value_type v)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QCborMap QCborMap::fromJsonObject(QJsonObject &&o)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool operator==(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator==(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator!=(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator!=(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator<(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator>(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator>(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator<(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator<=(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator>=(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator>=(const QCborValue &lhs, const QCborMap &rhs)': takes
    in Python what 'bool operator<=(const QCborMap &lhs, const QCborValue
    &rhs)' takes.
  - Qt's 'bool operator==(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator==(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator!=(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator!=(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator<(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator>(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator>(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator<(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator<=(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator>=(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'bool operator>=(const QCborValueConstRef &lhs, const QCborMap
    &rhs)': takes in Python what 'bool operator<=(const QCborMap &lhs, const
    QCborValueConstRef &rhs)' takes.
  - Qt's 'QCborMap::QCborMap(QCborContainerPrivate &dd)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 123 functions Qt declares: 2 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QCborMap is created at the first use, not by 'QCborMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCborMap back gives a copy the ritual made for
    Python, in a new cute QCborMap.
  - Each name of Qt's QCborMap that has no cute function yet,
    'asKeyValueRange', 'begin', 'cbegin', 'cend', 'constBegin', 'constEnd',
    'constFind', 'constKeyValueBegin', 'constKeyValueEnd', 'end', 'erase',
    'find', 'insert', 'keyValueBegin', 'keyValueEnd', 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QCborMap, each a class in here as in C++.

  class ConstIterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCborMap::ConstIterator: a plain Python object
    standing in front of one C++ QCborMap::ConstIterator.

    C++ hands a QCborMap::ConstIterator around as a copy, so every C++
    QCborMap::ConstIterator behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCborMap::ConstIterator that has a ritual and that
    Python can call so far, 15 names in all: 'key', 'keyRef', 'value',
    '__iadd__', '__isub__', '__add__', '__sub__', 'comparesEqual_helper',
    'compareThreeWay_helper', '__eq__', '__ne__', '__lt__', '__gt__',
    '__le__', '__ge__'. It can be made from Python, in 4 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCborMap::ConstIterator::~ConstIterator()': the destructor:
      Python removes its C++ QCborMap::ConstIterator by it, and has no other
      use for it.
    - Qt's 'ConstIterator &QCborMap::ConstIterator::operator=(const
      ConstIterator &other)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'value_type QCborMap::ConstIterator::operator*() const': an
      operator Python has no name for.
    - Qt's 'value_type QCborMap::ConstIterator::operator[](qsizetype j)
      const': gives a type Python has no way to take yet.
    - Qt's 'const QCborValueConstRef *QCborMap::ConstIterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'ConstIterator &QCborMap::ConstIterator::operator++()': an
      operator Python has no name for.
    - Qt's 'ConstIterator QCborMap::ConstIterator::operator++(int a0)': an
      operator Python has no name for.
    - Qt's 'ConstIterator &QCborMap::ConstIterator::operator--()': an
      operator Python has no name for.
    - Qt's 'ConstIterator QCborMap::ConstIterator::operator--(int a0)': an
      operator Python has no name for.

    What to expect
    --------------

    - The C++ QCborMap::ConstIterator is created at the first use, not by
      'QCborMap::ConstIterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCborMap::ConstIterator back gives a copy the
      ritual made for Python, in a new cute QCborMap::ConstIterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QCborContainerPrivate = WAIT['QCborContainerPrivate']
      QCborValueConstRef = WAIT['QCborValueConstRef']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QCborMap.ConstIterator,
        rhs: QCborMap.ConstIterator,
    ) -> bool:
      """
      Calls Qt's 'bool QCborMap::ConstIterator::comparesEqual_helper(const
      ConstIterator &lhs, const ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#comparesEqual_helper

      Parameters
      ----------

      lhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool QCborMap::ConstIterator::comparesEqual_helper(const
      #      ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZN8QCborMap13ConstIterator20comparesEqual_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QCborMap.ConstIterator,
        rhs: QCborMap.ConstIterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QCborMap::ConstIterator::compareThreeWay_helper(const ConstIterator
      &lhs, const ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html

      Parameters
      ----------

      lhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering
      #      QCborMap::ConstIterator::compareThreeWay_helper(const
      #      ConstIterator &lhs, const ConstIterator &rhs)
      address = Rituals.call(
          'ritual_ZN8QCborMap13ConstIterator22compareThreeWay_helperERKS0_S'
          '2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCborMap::ConstIterator'

    #  Qt's '~QCborMap::ConstIterator()'. Naming it makes this a value class:
    #  Python owns every C++ QCborMap::ConstIterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QCborMap13ConstIteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def key(self) -> QCborValue:
      """
      Calls Qt's 'QCborValue QCborMap::ConstIterator::key() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-constiterator.html#key

      Returns
      -------

      QCborValue
        A new cute QCborValue around the copy Qt gave back. Python owns it.
      """
      #  QCborValue QCborMap::ConstIterator::key() const
      address = self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIterator3keyEv',
      )
      from . import QCborValue
      return QCborValue._cuteOwning(address)

    def keyRef(self) -> QCborValueConstRef:
      """
      Calls Qt's 'QCborValueConstRef QCborMap::ConstIterator::keyRef()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#keyRef

      Returns
      -------

      QCborValueConstRef
        A new cute QCborValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QCborValueConstRef QCborMap::ConstIterator::keyRef() const
      address = self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIterator6keyRefEv',
      )
      from . import QCborValueConstRef
      return QCborValueConstRef._cuteOwning(address)

    def value(self) -> QCborValueConstRef:
      """
      Calls Qt's 'QCborValueConstRef QCborMap::ConstIterator::value() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#value

      Returns
      -------

      QCborValueConstRef
        A new cute QCborValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QCborValueConstRef QCborMap::ConstIterator::value() const
      address = self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIterator5valueEv',
      )
      from . import QCborValueConstRef
      return QCborValueConstRef._cuteOwning(address)

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
    def __iadd__(self, j: int) -> QCborMap.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      &QCborMap::ConstIterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  ConstIterator &QCborMap::ConstIterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN8QCborMap13ConstIteratorpLEx', j)
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
    def __isub__(self, j: int) -> QCborMap.ConstIterator:
      """
      Calls Qt's 'ConstIterator
      &QCborMap::ConstIterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  ConstIterator &QCborMap::ConstIterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN8QCborMap13ConstIteratormIEx', j)
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
    def __add__(self, j: int) -> QCborMap.ConstIterator:
      """
      Calls Qt's 'ConstIterator QCborMap::ConstIterator::operator+(qsizetype
      j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborMap.ConstIterator
        A new cute QCborMap::ConstIterator around the copy Qt gave back.
        Python owns it.
      """
      #  ConstIterator QCborMap::ConstIterator::operator+(qsizetype j) const
      address = self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIteratorplEx', j,
      )
      return QCborMap.ConstIterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QCborMap.ConstIterator:
      """
      Calls Qt's 'ConstIterator QCborMap::ConstIterator::operator-(qsizetype
      j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborMap.ConstIterator
        A new cute QCborMap::ConstIterator around the copy Qt gave back.
        Python owns it.
      """
      #  ConstIterator QCborMap::ConstIterator::operator-(qsizetype j) const
      address = self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIteratormiEx', j,
      )
      return QCborMap.ConstIterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QCborMap.ConstIterator) -> int:
      """
      Calls Qt's 'qsizetype QCborMap::ConstIterator::operator-(ConstIterator
      j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator-

      Parameters
      ----------

      j : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  qsizetype QCborMap::ConstIterator::operator-(ConstIterator j) const
      return self.uglySide.call(
          'ritual_ZNK8QCborMap13ConstIteratormiES0_', self._valueOf(j),
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
    def __eq__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator==(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator==

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator==(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN8QCborMap13ConstIteratorES2_',
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
    def __ne__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator!=

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator!=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN8QCborMap13ConstIteratorES2_',
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
    def __lt__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator<(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator<

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator<(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN8QCborMap13ConstIteratorES2_',
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
    def __gt__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator>(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator>

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator>(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN8QCborMap13ConstIteratorES2_',
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
    def __le__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator<=

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator<=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN8QCborMap13ConstIteratorES2_',
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
    def __ge__(self, rhs: QCborMap.ConstIterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const ConstIterator &lhs, const
      ConstIterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#operator>=

      Parameters
      ----------

      rhs : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  bool operator>=(const ConstIterator &lhs, const ConstIterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN8QCborMap13ConstIteratorES2_',
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

    @overload(QCborValueConstRef)
    def __init__(self, it: QCborValueConstRef) -> None:
      """
      Notes what was given, for Qt's
      'QCborMap::ConstIterator::ConstIterator(QCborValueConstRef it)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#ConstIterator

      Parameters
      ----------

      it : QCborValueConstRef
        Passed on as a value: Qt reads the C++ QCborValueConstRef, which
        stays Python's own.
      """
      #  QCborMap::ConstIterator::ConstIterator(QCborValueConstRef it)
      self._noteCreation(QCborMap.ConstIterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap13ConstIteratorC1E18QCborValueConstRef',
          self._valueOf(it),
      ))

    @overload(QCborContainerPrivate, int)
    @overload(NoneType, int)
    def __init__(self, dd: Optional[QCborContainerPrivate], ii: int) -> None:
      """
      Notes what was given, for Qt's
      'QCborMap::ConstIterator::ConstIterator(QCborContainerPrivate *dd,
      qsizetype ii)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#ConstIterator

      Parameters
      ----------

      dd : Optional[QCborContainerPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      ii : int
        Passed on as it is.
      """
      #  QCborMap::ConstIterator::ConstIterator(QCborContainerPrivate *dd,
      #      qsizetype ii)
      self._noteCreation(QCborMap.ConstIterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap13ConstIteratorC1EP21QCborContainerPrivatex',
          self._addressOf(dd), ii,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QCborMap::ConstIterator::ConstIterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#ConstIterator
      """
      #  QCborMap::ConstIterator::ConstIterator()
      self._noteCreation(QCborMap.ConstIterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap13ConstIteratorC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: QCborMap.ConstIterator) -> None:
      """
      Notes what was given, for Qt's
      'QCborMap::ConstIterator::ConstIterator(const ConstIterator &a0)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-constiterator.html#ConstIterator

      Parameters
      ----------

      a0 : QCborMap.ConstIterator
        Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
        stays Python's own.
      """
      #  QCborMap::ConstIterator::ConstIterator(const ConstIterator &a0)
      self._noteCreation(QCborMap.ConstIterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap13ConstIteratorC1ERKS0_', self._valueOf(a0),
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
    The cute side of Qt's QCborMap::Iterator: a plain Python object standing
    in front of one C++ QCborMap::Iterator.

    C++ hands a QCborMap::Iterator around as a copy, so every C++
    QCborMap::Iterator behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCborMap::Iterator that has a ritual and that
    Python can call so far, 15 names in all: 'key', 'keyRef', 'value',
    '__iadd__', '__isub__', '__add__', '__sub__', 'comparesEqual_helper',
    'compareThreeWay_helper', '__eq__', '__ne__', '__lt__', '__gt__',
    '__le__', '__ge__'. It can be made from Python, in 3 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCborMap::Iterator::~Iterator()': the destructor: Python removes
      its C++ QCborMap::Iterator by it, and has no other use for it.
    - Qt's 'Iterator &QCborMap::Iterator::operator=(const Iterator &other)':
      assignment: Python binds a name and has no operator for it.
    - Qt's 'value_type QCborMap::Iterator::operator*() const': an operator
      Python has no name for.
    - Qt's 'value_type QCborMap::Iterator::operator[](qsizetype j) const':
      gives a type Python has no way to take yet.
    - Qt's 'QCborValueRef *QCborMap::Iterator::operator->()': an operator
      Python has no name for.
    - Qt's 'const QCborValueConstRef *QCborMap::Iterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'Iterator &QCborMap::Iterator::operator++()': an operator Python
      has no name for.
    - Qt's 'Iterator QCborMap::Iterator::operator++(int a0)': an operator
      Python has no name for.
    - Qt's 'Iterator &QCborMap::Iterator::operator--()': an operator Python
      has no name for.
    - Qt's 'Iterator QCborMap::Iterator::operator--(int a0)': an operator
      Python has no name for.
    - Qt's 'bool QCborMap::Iterator::comparesEqual_helper(const Iterator
      &lhs, const ConstIterator &rhs)': names 'QCborMap::ConstIterator',
      which stands beside this class inside 'QCborMap' and cannot be named
      from here.
    - Qt's 'Qt::strong_ordering
      QCborMap::Iterator::compareThreeWay_helper(const Iterator &lhs, const
      ConstIterator &rhs)': names 'QCborMap::ConstIterator', which stands
      beside this class inside 'QCborMap' and cannot be named from here.
    - Qt's 'bool operator==(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator!=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator<(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator>(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator<=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator>=(const Iterator &lhs, const ConstIterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator==(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator!=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator<(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator>(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator<=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.
    - Qt's 'bool operator>=(const ConstIterator &lhs, const Iterator &rhs)':
      names 'QCborMap::ConstIterator', which stands beside this class inside
      'QCborMap' and cannot be named from here.

    What to expect
    --------------

    - The C++ QCborMap::Iterator is created at the first use, not by
      'QCborMap::Iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCborMap::Iterator back gives a copy the ritual
      made for Python, in a new cute QCborMap::Iterator.
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
        lhs: QCborMap.Iterator,
        rhs: QCborMap.Iterator,
    ) -> bool:
      """
      Calls Qt's 'bool QCborMap::Iterator::comparesEqual_helper(const
      Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#comparesEqual_helper

      Parameters
      ----------

      lhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool QCborMap::Iterator::comparesEqual_helper(const Iterator &lhs,
      #      const Iterator &rhs)
      return Rituals.call(
          'ritual_ZN8QCborMap8Iterator20comparesEqual_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QCborMap.Iterator,
        rhs: QCborMap.Iterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QCborMap::Iterator::compareThreeWay_helper(const Iterator &lhs, const
      Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#compareThreeWay_helper

      Parameters
      ----------

      lhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering QCborMap::Iterator::compareThreeWay_helper(const
      #      Iterator &lhs, const Iterator &rhs)
      address = Rituals.call(
          'ritual_ZN8QCborMap8Iterator22compareThreeWay_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCborMap::Iterator'

    #  Qt's '~QCborMap::Iterator()'. Naming it makes this a value class:
    #  Python owns every C++ QCborMap::Iterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN8QCborMap8IteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def key(self) -> QCborValue:
      """
      Calls Qt's 'QCborValue QCborMap::Iterator::key() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#key

      Returns
      -------

      QCborValue
        A new cute QCborValue around the copy Qt gave back. Python owns it.
      """
      #  QCborValue QCborMap::Iterator::key() const
      address = self.uglySide.call('ritual_ZNK8QCborMap8Iterator3keyEv')
      from . import QCborValue
      return QCborValue._cuteOwning(address)

    def keyRef(self) -> QCborValueConstRef:
      """
      Calls Qt's 'QCborValueConstRef QCborMap::Iterator::keyRef() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#keyRef

      Returns
      -------

      QCborValueConstRef
        A new cute QCborValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QCborValueConstRef QCborMap::Iterator::keyRef() const
      address = self.uglySide.call('ritual_ZNK8QCborMap8Iterator6keyRefEv')
      from . import QCborValueConstRef
      return QCborValueConstRef._cuteOwning(address)

    def value(self) -> QCborValueRef:
      """
      Calls Qt's 'QCborValueRef QCborMap::Iterator::value() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#value

      Returns
      -------

      QCborValueRef
        A new cute QCborValueRef around the copy Qt gave back. Python owns
        it.
      """
      #  QCborValueRef QCborMap::Iterator::value() const
      address = self.uglySide.call('ritual_ZNK8QCborMap8Iterator5valueEv')
      from . import QCborValueRef
      return QCborValueRef._cuteOwning(address)

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
    def __iadd__(self, j: int) -> QCborMap.Iterator:
      """
      Calls Qt's 'Iterator &QCborMap::Iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  Iterator &QCborMap::Iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN8QCborMap8IteratorpLEx', j)
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
    def __isub__(self, j: int) -> QCborMap.Iterator:
      """
      Calls Qt's 'Iterator &QCborMap::Iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  Iterator &QCborMap::Iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN8QCborMap8IteratormIEx', j)
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
    def __add__(self, j: int) -> QCborMap.Iterator:
      """
      Calls Qt's 'Iterator QCborMap::Iterator::operator+(qsizetype j) const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborMap.Iterator
        A new cute QCborMap::Iterator around the copy Qt gave back. Python
        owns it.
      """
      #  Iterator QCborMap::Iterator::operator+(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK8QCborMap8IteratorplEx', j)
      return QCborMap.Iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QCborMap.Iterator:
      """
      Calls Qt's 'Iterator QCborMap::Iterator::operator-(qsizetype j) const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QCborMap.Iterator
        A new cute QCborMap::Iterator around the copy Qt gave back. Python
        owns it.
      """
      #  Iterator QCborMap::Iterator::operator-(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK8QCborMap8IteratormiEx', j)
      return QCborMap.Iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QCborMap.Iterator) -> int:
      """
      Calls Qt's 'qsizetype QCborMap::Iterator::operator-(Iterator j) const'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#operator-

      Parameters
      ----------

      j : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  qsizetype QCborMap::Iterator::operator-(Iterator j) const
      return self.uglySide.call(
          'ritual_ZNK8QCborMap8IteratormiES0_', self._valueOf(j),
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
    def __eq__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator==

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator==(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN8QCborMap8IteratorES2_',
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
    def __ne__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator!=

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator!=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN8QCborMap8IteratorES2_',
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
    def __lt__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#operator<

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator<(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN8QCborMap8IteratorES2_',
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
    def __gt__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#operator>

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator>(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN8QCborMap8IteratorES2_',
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
    def __le__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator<=

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator<=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN8QCborMap8IteratorES2_',
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
    def __ge__(self, rhs: QCborMap.Iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const Iterator &lhs, const Iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcbormap-iterator.html#operator>=

      Parameters
      ----------

      rhs : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  bool operator>=(const Iterator &lhs, const Iterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN8QCborMap8IteratorES2_',
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
      'QCborMap::Iterator::Iterator(QCborContainerPrivate *dd, qsizetype
      ii)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#Iterator

      Parameters
      ----------

      dd : Optional[QCborContainerPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      ii : int
        Passed on as it is.
      """
      #  QCborMap::Iterator::Iterator(QCborContainerPrivate *dd, qsizetype
      #      ii)
      self._noteCreation(QCborMap.Iterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap8IteratorC1EP21QCborContainerPrivatex',
          self._addressOf(dd), ii,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QCborMap::Iterator::Iterator()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#Iterator
      """
      #  QCborMap::Iterator::Iterator()
      self._noteCreation(QCborMap.Iterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap8IteratorC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: QCborMap.Iterator) -> None:
      """
      Notes what was given, for Qt's 'QCborMap::Iterator::Iterator(const
      Iterator &a0)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcbormap-iterator.html#Iterator

      Parameters
      ----------

      a0 : QCborMap.Iterator
        Passed on as a value: Qt reads the C++ QCborMap::Iterator, which
        stays Python's own.
      """
      #  QCborMap::Iterator::Iterator(const Iterator &a0)
      self._noteCreation(QCborMap.Iterator, lambda: Rituals.call(
          'ritual_ZN8QCborMap8IteratorC1ERKS0_', self._valueOf(a0),
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
  @overload(QMap[str, QVariant])
  def fromVariantMap(map: QMap[str, QVariant]) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborMap::fromVariantMap(const QVariantMap &map)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#fromVariantMap

    Parameters
    ----------

    map : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborMap::fromVariantMap(const QVariantMap &map)
    address = Rituals.call(
        'ritual_ZN8QCborMap14fromVariantMapERK4QMapI7QString8QVariantE',
        CuteMixin._valueOf(map),
    )
    return QCborMap._cuteOwning(address)

  @staticmethod
  @overload(QHash[str, QVariant])
  def fromVariantHash(hash: QHash[str, QVariant]) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborMap::fromVariantHash(const QVariantHash
    &hash)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#fromVariantHash

    Parameters
    ----------

    hash : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborMap::fromVariantHash(const QVariantHash &hash)
    address = Rituals.call(
        'ritual_ZN8QCborMap15fromVariantHashERK5QHashI7QString8QVariantE',
        CuteMixin._valueOf(hash),
    )
    return QCborMap._cuteOwning(address)

  @staticmethod
  @overload(QJsonObject)
  def fromJsonObject(o: QJsonObject) -> QCborMap:
    """
    Calls Qt's 'QCborMap QCborMap::fromJsonObject(const QJsonObject &o)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#fromJsonObject

    Parameters
    ----------

    o : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QCborMap::fromJsonObject(const QJsonObject &o)
    address = Rituals.call(
        'ritual_ZN8QCborMap14fromJsonObjectERK11QJsonObject',
        CuteMixin._valueOf(o),
    )
    return QCborMap._cuteOwning(address)

  @staticmethod
  @overload(THIS, QCborValue)
  def comparesEqual_helper(lhs: QCborMap, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool QCborMap::comparesEqual_helper(const QCborMap &lhs,
    const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#comparesEqual_helper

    Parameters
    ----------

    lhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool QCborMap::comparesEqual_helper(const QCborMap &lhs, const
    #      QCborValue &rhs)
    return Rituals.call(
        'ritual_ZN8QCborMap20comparesEqual_helperERKS_RK10QCborValue',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(THIS, QCborValueConstRef)
  def comparesEqual_helper(lhs: QCborMap, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool QCborMap::comparesEqual_helper(const QCborMap &lhs,
    QCborValueConstRef rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#comparesEqual_helper

    Parameters
    ----------

    lhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool QCborMap::comparesEqual_helper(const QCborMap &lhs,
    #      QCborValueConstRef rhs)
    return Rituals.call(
        'ritual_ZN8QCborMap20comparesEqual_helperERKS_18QCborValueConstRef',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(THIS, QCborValue)
  def compareThreeWay_helper(
      lhs: QCborMap,
      rhs: QCborValue,
  ) -> Qt.strong_ordering:
    """
    Calls Qt's 'Qt::strong_ordering QCborMap::compareThreeWay_helper(const
    QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcbormap.html#compareThreeWay_helper

    Parameters
    ----------

    lhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
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
    #  Qt::strong_ordering QCborMap::compareThreeWay_helper(const QCborMap
    #      &lhs, const QCborValue &rhs)
    address = Rituals.call(
        'ritual_ZN8QCborMap22compareThreeWay_helperERKS_RK10QCborValue',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )
    return Qt.strong_ordering._cuteOwning(address)

  @staticmethod
  @overload(THIS, QCborValueConstRef)
  def compareThreeWay_helper(
      lhs: QCborMap,
      rhs: QCborValueConstRef,
  ) -> Qt.strong_ordering:
    """
    Calls Qt's 'Qt::strong_ordering QCborMap::compareThreeWay_helper(const
    QCborMap &lhs, QCborValueConstRef rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcbormap.html#compareThreeWay_helper

    Parameters
    ----------

    lhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
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
    #  Qt::strong_ordering QCborMap::compareThreeWay_helper(const QCborMap
    #      &lhs, QCborValueConstRef rhs)
    address = Rituals.call(
        'ritual_ZN8QCborMap22compareThreeWay_helperERKS_18QCborValueConstRe'
        'f',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )
    return Qt.strong_ordering._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborMap'

  #  Qt's '~QCborMap()'. Naming it makes this a value class: Python owns
  #  every C++ QCborMap behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QCborMapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toCborValue(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::toCborValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#toCborValue

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::toCborValue() const
    address = self.uglySide.call('ritual_ZNK8QCborMap11toCborValueEv')
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QCborMap::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#size
    """
    #  qsizetype QCborMap::size() const
    return self.uglySide.call('ritual_ZNK8QCborMap4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCborMap::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#isEmpty
    """
    #  bool QCborMap::isEmpty() const
    return self.uglySide.call('ritual_ZNK8QCborMap7isEmptyEv')

  def keys(self) -> QList[QCborValue]:
    """
    Calls Qt's 'QList<QCborValue> QCborMap::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#keys

    Returns
    -------

    QList[QCborValue]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCborValue> QCborMap::keys() const
    address = self.uglySide.call('ritual_ZNK8QCborMap4keysEv')
    from . import QCborValue
    return QList[QCborValue]._cuteOwning(address)

  @overload(int)
  def value(self, key: int) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::value(qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#value

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::value(qint64 key) const
    address = self.uglySide.call('ritual_ZNK8QCborMap5valueEx', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QLatin1String)
  def value(self, key: QLatin1String) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::value(QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#value

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::value(QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK8QCborMap5valueE13QLatin1String', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(str)
  def value(self, key: str) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::value(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::value(const QString &key) const
    address = self.uglySide.call('ritual_ZNK8QCborMap5valueERK7QString', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def value(self, key: QCborValue) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::value(const QCborValue &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#value

    Parameters
    ----------

    key : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::value(const QCborValue &key) const
    address = self.uglySide.call(
        'ritual_ZNK8QCborMap5valueERK10QCborValue', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(int)
  def contains(self, key: int) -> bool:
    """
    Calls Qt's 'bool QCborMap::contains(qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#contains

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  bool QCborMap::contains(qint64 key) const
    return self.uglySide.call('ritual_ZNK8QCborMap8containsEx', key)

  @overload(QLatin1String)
  def contains(self, key: QLatin1String) -> bool:
    """
    Calls Qt's 'bool QCborMap::contains(QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#contains

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool QCborMap::contains(QLatin1StringView key) const
    return self.uglySide.call(
        'ritual_ZNK8QCborMap8containsE13QLatin1String', self._valueOf(key),
    )

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QCborMap::contains(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCborMap::contains(const QString &key) const
    return self.uglySide.call('ritual_ZNK8QCborMap8containsERK7QString', key)

  @overload(QCborValue)
  def contains(self, key: QCborValue) -> bool:
    """
    Calls Qt's 'bool QCborMap::contains(const QCborValue &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#contains

    Parameters
    ----------

    key : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool QCborMap::contains(const QCborValue &key) const
    return self.uglySide.call(
        'ritual_ZNK8QCborMap8containsERK10QCborValue', self._valueOf(key),
    )

  @overload(THIS)
  def compare(self, other: QCborMap) -> int:
    """
    Calls Qt's 'int QCborMap::compare(const QCborMap &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#compare

    Parameters
    ----------

    other : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  int QCborMap::compare(const QCborMap &other) const
    return self.uglySide.call(
        'ritual_ZNK8QCborMap7compareERKS_', self._valueOf(other),
    )

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QCborMap::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#empty
    """
    #  bool QCborMap::empty() const
    return self.uglySide.call('ritual_ZNK8QCborMap5emptyEv')

  def toVariantMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QCborMap::toVariantMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#toVariantMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QCborMap::toVariantMap() const
    address = self.uglySide.call('ritual_ZNK8QCborMap12toVariantMapEv')
    from . import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def toVariantHash(self) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QVariantHash QCborMap::toVariantHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#toVariantHash

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantHash QCborMap::toVariantHash() const
    address = self.uglySide.call('ritual_ZNK8QCborMap13toVariantHashEv')
    from . import QVariant
    return QHash[str, QVariant]._cuteOwning(address)

  def toJsonObject(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QCborMap::toJsonObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#toJsonObject

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QCborMap::toJsonObject() const
    address = self.uglySide.call('ritual_ZNK8QCborMap12toJsonObjectEv')
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

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
  def __getitem__(self, key: int) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborMap::operator[](qint64 key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator[]

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborMap::operator[](qint64 key) const
    address = self.uglySide.call('ritual_ZNK8QCborMapixEx', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborMap::operator[](QLatin1StringView key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator[]

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborMap::operator[](QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK8QCborMapixE13QLatin1String', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(str)
  def __getitem__(self, key: str) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborMap::operator[](const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborMap::operator[](const QString &key) const
    address = self.uglySide.call('ritual_ZNK8QCborMapixERK7QString', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def __getitem__(self, key: QCborValue) -> QCborValue:
    """
    Calls Qt's 'const QCborValue QCborMap::operator[](const QCborValue &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator[]

    Parameters
    ----------

    key : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  const QCborValue QCborMap::operator[](const QCborValue &key) const
    address = self.uglySide.call(
        'ritual_ZNK8QCborMapixERK10QCborValue', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator==

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator==(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZeqRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __eq__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator==

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator==(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __eq__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator==

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK8QCborMapRK18QCborValueConstRef',
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
  def __ne__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator!=

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator!=(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZneRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ne__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator!=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator!=(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZneRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __ne__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator!=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZneRK8QCborMapRK18QCborValueConstRef',
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
  def __lt__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator<(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZltRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __lt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZltRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __lt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZltRK8QCborMapRK18QCborValueConstRef',
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
  def __gt__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator>(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZgtRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __gt__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgtRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __gt__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZgtRK8QCborMapRK18QCborValueConstRef',
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
  def __le__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<=

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator<=(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZleRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __le__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator<=(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZleRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __le__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator<=(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator<=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator<=(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZleRK8QCborMapRK18QCborValueConstRef',
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
  def __ge__(self, rhs: QCborMap) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborMap &lhs, const QCborMap &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>=

    Parameters
    ----------

    rhs : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  bool operator>=(const QCborMap &lhs, const QCborMap &rhs)
    return Rituals.call(
        'ritual_ZgeRK8QCborMapS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValue)
  def __ge__(self, rhs: QCborValue) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborMap &lhs, const QCborValue &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>=

    Parameters
    ----------

    rhs : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  bool operator>=(const QCborMap &lhs, const QCborValue &rhs)
    return Rituals.call(
        'ritual_ZgeRK8QCborMapRK10QCborValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QCborValueConstRef)
  def __ge__(self, rhs: QCborValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator>=(const QCborMap &lhs, const QCborValueConstRef
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#operator>=

    Parameters
    ----------

    rhs : QCborValueConstRef
      Passed on as a value: Qt reads the C++ QCborValueConstRef, which stays
      Python's own.
    """
    #  bool operator>=(const QCborMap &lhs, const QCborValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZgeRK8QCborMapRK18QCborValueConstRef',
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
    Notes what was given, for Qt's 'QCborMap::QCborMap()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#QCborMap
    """
    #  QCborMap::QCborMap()
    self._noteCreation(QCborMap, lambda: Rituals.call(
        'ritual_ZN8QCborMapC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCborMap) -> None:
    """
    Notes what was given, for Qt's 'QCborMap::QCborMap(const QCborMap
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#QCborMap

    Parameters
    ----------

    other : QCborMap
      Passed on as a value: Qt reads the C++ QCborMap, which stays Python's
      own.
    """
    #  QCborMap::QCborMap(const QCborMap &other)
    self._noteCreation(QCborMap, lambda: Rituals.call(
        'ritual_ZN8QCborMapC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QCborMap::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#clear
    """
    #  void QCborMap::clear()
    self.uglySide.call('ritual_ZN8QCborMap5clearEv')

  @overload(int)
  def take(self, key: int) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::take(qint64 key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#take

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::take(qint64 key)
    address = self.uglySide.call('ritual_ZN8QCborMap4takeEx', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QLatin1String)
  def take(self, key: QLatin1String) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::take(QLatin1StringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#take

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::take(QLatin1StringView key)
    address = self.uglySide.call(
        'ritual_ZN8QCborMap4takeE13QLatin1String', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(str)
  def take(self, key: str) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::take(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#take

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::take(const QString &key)
    address = self.uglySide.call('ritual_ZN8QCborMap4takeERK7QString', key)
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(QCborValue)
  def take(self, key: QCborValue) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::take(const QCborValue &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#take

    Parameters
    ----------

    key : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::take(const QCborValue &key)
    address = self.uglySide.call(
        'ritual_ZN8QCborMap4takeERK10QCborValue', self._valueOf(key),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(int)
  def remove(self, key: int) -> None:
    """
    Calls Qt's 'void QCborMap::remove(qint64 key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#remove

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  void QCborMap::remove(qint64 key)
    self.uglySide.call('ritual_ZN8QCborMap6removeEx', key)

  @overload(QLatin1String)
  def remove(self, key: QLatin1String) -> None:
    """
    Calls Qt's 'void QCborMap::remove(QLatin1StringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#remove

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QCborMap::remove(QLatin1StringView key)
    self.uglySide.call(
        'ritual_ZN8QCborMap6removeE13QLatin1String', self._valueOf(key),
    )

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QCborMap::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCborMap::remove(const QString &key)
    self.uglySide.call('ritual_ZN8QCborMap6removeERK7QString', key)

  @overload(QCborValue)
  def remove(self, key: QCborValue) -> None:
    """
    Calls Qt's 'void QCborMap::remove(const QCborValue &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#remove

    Parameters
    ----------

    key : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.
    """
    #  void QCborMap::remove(const QCborValue &key)
    self.uglySide.call(
        'ritual_ZN8QCborMap6removeERK10QCborValue', self._valueOf(key),
    )

  @overload(Iterator)
  def extract(self, it: Iterator) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::extract(iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#extract

    Parameters
    ----------

    it : Iterator
      Passed on as a value: Qt reads the C++ QCborMap::Iterator, which stays
      Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::extract(iterator it)
    address = self.uglySide.call(
        'ritual_ZN8QCborMap7extractENS_8IteratorE', self._valueOf(it),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload(ConstIterator)
  def extract(self, it: ConstIterator) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborMap::extract(const_iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#extract

    Parameters
    ----------

    it : ConstIterator
      Passed on as a value: Qt reads the C++ QCborMap::ConstIterator, which
      stays Python's own.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborMap::extract(const_iterator it)
    address = self.uglySide.call(
        'ritual_ZN8QCborMap7extractENS_13ConstIteratorE', self._valueOf(it),
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @overload()
  @overload(int)
  def detach(self, reserve: int = 0) -> None:
    """
    Calls Qt's 'void QCborMap::detach(qsizetype reserve)'.

    Qt's own words: https://doc.qt.io/qt-6/qcbormap.html#detach

    Parameters
    ----------

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCborMap::detach(qsizetype reserve)
    self.uglySide.call('ritual_ZN8QCborMap6detachEx', reserve)

  @staticmethod
  def asKeyValueRange(*__, **_) -> Never:
    """
    - Qt's 'QtPrivate::QKeyValueRange<QCborMap &>
      QCborMap::asKeyValueRange()': gives a type Python has no way to take
      yet.
    - Qt's 'QtPrivate::QKeyValueRange<const QCborMap &>
      QCborMap::asKeyValueRange() const': gives a type Python has no way to
      take yet.
    """
    raise NotImplementedError(
        "'QCborMap.asKeyValueRange' has no cute function yet. Qt's "
        "'QtPrivate::QKeyValueRange<QCborMap &> "
        "QCborMap::asKeyValueRange()': gives a type Python has no way to "
        "take yet. Qt's 'QtPrivate::QKeyValueRange<const QCborMap &> "
        "QCborMap::asKeyValueRange() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborMap::begin()': gives a type Python has no way to
      take yet.
    - Qt's 'const_iterator QCborMap::begin() const': gives a type Python has
      no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.begin' has no cute function yet. Qt's 'iterator "
        "QCborMap::begin()': gives a type Python has no way to take yet. "
        "Qt's 'const_iterator QCborMap::begin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def cbegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborMap::cbegin() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.cbegin' has no cute function yet. Qt's 'const_iterator "
        "QCborMap::cbegin() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def cend(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborMap::cend() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.cend' has no cute function yet. Qt's 'const_iterator "
        "QCborMap::cend() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def constBegin(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborMap::constBegin() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.constBegin' has no cute function yet. Qt's "
        "'const_iterator QCborMap::constBegin() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def constEnd(*__, **_) -> Never:
    """
    Qt's 'const_iterator QCborMap::constEnd() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.constEnd' has no cute function yet. Qt's 'const_iterator "
        "QCborMap::constEnd() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def constFind(*__, **_) -> Never:
    """
    - Qt's 'const_iterator QCborMap::constFind(qint64 key) const': gives a
      type Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::constFind(QLatin1StringView key) const':
      gives a type Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::constFind(const QString &key) const':
      gives a type Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::constFind(const QCborValue &key) const':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.constFind' has no cute function yet. Qt's "
        "'const_iterator QCborMap::constFind(qint64 key) const': gives a "
        "type Python has no way to take yet. Qt's 'const_iterator "
        "QCborMap::constFind(QLatin1StringView key) const': gives a type "
        "Python has no way to take yet. Qt's 'const_iterator "
        "QCborMap::constFind(const QString &key) const': gives a type "
        "Python has no way to take yet. Qt's 'const_iterator "
        "QCborMap::constFind(const QCborValue &key) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def constKeyValueBegin(*__, **_) -> Never:
    """
    Qt's 'const_key_value_iterator QCborMap::constKeyValueBegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.constKeyValueBegin' has no cute function yet. Qt's "
        "'const_key_value_iterator QCborMap::constKeyValueBegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def constKeyValueEnd(*__, **_) -> Never:
    """
    Qt's 'const_key_value_iterator QCborMap::constKeyValueEnd() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.constKeyValueEnd' has no cute function yet. Qt's "
        "'const_key_value_iterator QCborMap::constKeyValueEnd() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborMap::end()': gives a type Python has no way to take
      yet.
    - Qt's 'const_iterator QCborMap::end() const': gives a type Python has no
      way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.end' has no cute function yet. Qt's 'iterator "
        "QCborMap::end()': gives a type Python has no way to take yet. Qt's "
        "'const_iterator QCborMap::end() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def erase(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborMap::erase(iterator it)': gives a type Python has
      no way to take yet.
    - Qt's 'iterator QCborMap::erase(const_iterator it)': gives a type Python
      has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.erase' has no cute function yet. Qt's 'iterator "
        "QCborMap::erase(iterator it)': gives a type Python has no way to "
        "take yet. Qt's 'iterator QCborMap::erase(const_iterator it)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def find(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborMap::find(qint64 key)': gives a type Python has no
      way to take yet.
    - Qt's 'iterator QCborMap::find(QLatin1StringView key)': gives a type
      Python has no way to take yet.
    - Qt's 'iterator QCborMap::find(const QString &key)': gives a type Python
      has no way to take yet.
    - Qt's 'iterator QCborMap::find(const QCborValue &key)': gives a type
      Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::find(qint64 key) const': gives a type
      Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::find(QLatin1StringView key) const':
      gives a type Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::find(const QString &key) const': gives a
      type Python has no way to take yet.
    - Qt's 'const_iterator QCborMap::find(const QCborValue &key) const':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.find' has no cute function yet. Qt's 'iterator "
        "QCborMap::find(qint64 key)': gives a type Python has no way to "
        "take yet. Qt's 'iterator QCborMap::find(QLatin1StringView key)': "
        "gives a type Python has no way to take yet. Qt's 'iterator "
        "QCborMap::find(const QString &key)': gives a type Python has no "
        "way to take yet. Qt's 'iterator QCborMap::find(const QCborValue "
        "&key)': gives a type Python has no way to take yet. Qt's "
        "'const_iterator QCborMap::find(qint64 key) const': gives a type "
        "Python has no way to take yet. Qt's 'const_iterator "
        "QCborMap::find(QLatin1StringView key) const': gives a type Python "
        "has no way to take yet. Qt's 'const_iterator QCborMap::find(const "
        "QString &key) const': gives a type Python has no way to take yet. "
        "Qt's 'const_iterator QCborMap::find(const QCborValue &key) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    - Qt's 'iterator QCborMap::insert(qint64 key, const QCborValue &value_)':
      gives a type Python has no way to take yet.
    - Qt's 'iterator QCborMap::insert(QLatin1StringView key, const QCborValue
      &value_)': gives a type Python has no way to take yet.
    - Qt's 'iterator QCborMap::insert(const QString &key, const QCborValue
      &value_)': gives a type Python has no way to take yet.
    - Qt's 'iterator QCborMap::insert(const QCborValue &key, const QCborValue
      &value_)': gives a type Python has no way to take yet.
    - Qt's 'iterator QCborMap::insert(value_type v)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCborMap.insert' has no cute function yet. Qt's 'iterator "
        "QCborMap::insert(qint64 key, const QCborValue &value_)': gives a "
        "type Python has no way to take yet. Qt's 'iterator "
        "QCborMap::insert(QLatin1StringView key, const QCborValue "
        "&value_)': gives a type Python has no way to take yet. Qt's "
        "'iterator QCborMap::insert(const QString &key, const QCborValue "
        "&value_)': gives a type Python has no way to take yet. Qt's "
        "'iterator QCborMap::insert(const QCborValue &key, const QCborValue "
        "&value_)': gives a type Python has no way to take yet. Qt's "
        "'iterator QCborMap::insert(value_type v)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def keyValueBegin(*__, **_) -> Never:
    """
    - Qt's 'key_value_iterator QCborMap::keyValueBegin()': gives a type
      Python has no way to take yet.
    - Qt's 'const_key_value_iterator QCborMap::keyValueBegin() const': gives
      a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.keyValueBegin' has no cute function yet. Qt's "
        "'key_value_iterator QCborMap::keyValueBegin()': gives a type "
        "Python has no way to take yet. Qt's 'const_key_value_iterator "
        "QCborMap::keyValueBegin() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def keyValueEnd(*__, **_) -> Never:
    """
    - Qt's 'key_value_iterator QCborMap::keyValueEnd()': gives a type Python
      has no way to take yet.
    - Qt's 'const_key_value_iterator QCborMap::keyValueEnd() const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCborMap.keyValueEnd' has no cute function yet. Qt's "
        "'key_value_iterator QCborMap::keyValueEnd()': gives a type Python "
        "has no way to take yet. Qt's 'const_key_value_iterator "
        "QCborMap::keyValueEnd() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCborMap::swap(QCborMap &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QCborMap.swap' has no cute function yet. Qt's 'void "
        "QCborMap::swap(QCborMap &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QCborMap>': the list of QCborMap, which 'QList[QCborMap]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QCborMap.
QList.createKind(
    QCborMap, 'value',
    make='ritual_list_make_QCborMap',
    add='ritual_list_add_QCborMap',
    size='ritual_list_size_QCborMap',
    at='ritual_list_at_QCborMap',
    drop='ritual_list_drop_QCborMap',
)
