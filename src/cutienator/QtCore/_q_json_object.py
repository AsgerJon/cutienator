"""
QJsonObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qjsonobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QHash, QMap, QStringList, Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCborContainerPrivate, QDebug, QJsonValue, QJsonValueConstRef
  from . import QJsonValueRef, QLatin1String, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCborContainerPrivate = WAIT['QCborContainerPrivate']
  QDebug = WAIT['QDebug']
  QJsonValue = WAIT['QJsonValue']
  QJsonValueConstRef = WAIT['QJsonValueConstRef']
  QLatin1String = WAIT['QLatin1String']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QJsonObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonObject: a plain Python object standing in front
  of one C++ QJsonObject.

  C++ hands a QJsonObject around as a copy, so every C++ QJsonObject behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJsonObject that has a ritual and that Python can
  call so far, 33 names in all: 'fromVariantMap', 'toVariantMap',
  'fromVariantHash', 'toVariantHash', 'keys', 'size', 'count', 'length',
  'isEmpty', 'value', '__getitem__', 'remove', 'take', 'contains', 'begin',
  'cbegin', 'constBegin', 'end', 'cend', 'constEnd', 'erase', 'find',
  'constFind', 'insert', 'empty', '__eq__', '__ne__', '__rlshift__',
  'detach', 'keyAt', 'valueAt', 'setValueAt', 'removeAt'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonObject::QJsonObject(std::initializer_list<std::pair<QString,
    QJsonValue>> args)': takes a type Python has no way to hand over yet.
  - Qt's 'QJsonObject::~QJsonObject()': the destructor: Python removes its
    C++ QJsonObject by it, and has no other use for it.
  - Qt's 'QJsonObject &QJsonObject::operator=(const QJsonObject &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QJsonObject::QJsonObject(QJsonObject &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QJsonObject &QJsonObject::operator=(QJsonObject &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QJsonObject::swap(QJsonObject &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](const QString &key)': takes
    in Python what 'QJsonValue QJsonObject::operator[](const QString &key)
    const' takes.
  - Qt's 'QJsonValue QJsonObject::value(QStringView key) const': takes in
    Python what 'QJsonValue QJsonObject::value(const QString &key) const'
    takes.
  - Qt's 'QJsonValue QJsonObject::operator[](QStringView key) const': takes
    in Python what 'QJsonValue QJsonObject::operator[](const QString &key)
    const' takes.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QStringView key)': takes in
    Python what 'QJsonValue QJsonObject::operator[](const QString &key)
    const' takes.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QLatin1StringView key)':
    takes in Python what 'QJsonValue
    QJsonObject::operator[](QLatin1StringView key) const' takes.
  - Qt's 'void QJsonObject::remove(QStringView key)': takes in Python what
    'void QJsonObject::remove(const QString &key)' takes.
  - Qt's 'QJsonValue QJsonObject::take(QStringView key)': takes in Python
    what 'QJsonValue QJsonObject::take(const QString &key)' takes.
  - Qt's 'bool QJsonObject::contains(QStringView key) const': takes in Python
    what 'bool QJsonObject::contains(const QString &key) const' takes.
  - Qt's 'const_iterator QJsonObject::begin() const': takes in Python what
    'iterator QJsonObject::begin()' takes.
  - Qt's 'const_iterator QJsonObject::end() const': takes in Python what
    'iterator QJsonObject::end()' takes.
  - Qt's 'key_value_iterator QJsonObject::keyValueBegin()': gives a type
    Python has no way to take yet.
  - Qt's 'key_value_iterator QJsonObject::keyValueEnd()': gives a type Python
    has no way to take yet.
  - Qt's 'const_key_value_iterator QJsonObject::keyValueBegin() const': gives
    a type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QJsonObject::constKeyValueBegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QJsonObject::keyValueEnd() const': gives a
    type Python has no way to take yet.
  - Qt's 'const_key_value_iterator QJsonObject::constKeyValueEnd() const':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::QKeyValueRange<QJsonObject &>
    QJsonObject::asKeyValueRange()': gives a type Python has no way to take
    yet.
  - Qt's 'QtPrivate::QKeyValueRange<const QJsonObject &>
    QJsonObject::asKeyValueRange() const': gives a type Python has no way to
    take yet.
  - Qt's 'const_iterator QJsonObject::find(const QString &key) const': takes
    in Python what 'iterator QJsonObject::find(const QString &key)' takes.
  - Qt's 'iterator QJsonObject::find(QStringView key)': takes in Python what
    'iterator QJsonObject::find(const QString &key)' takes.
  - Qt's 'const_iterator QJsonObject::find(QStringView key) const': takes in
    Python what 'iterator QJsonObject::find(const QString &key)' takes.
  - Qt's 'const_iterator QJsonObject::find(QLatin1StringView key) const':
    takes in Python what 'iterator QJsonObject::find(QLatin1StringView key)'
    takes.
  - Qt's 'const_iterator QJsonObject::constFind(QStringView key) const':
    takes in Python what 'const_iterator QJsonObject::constFind(const QString
    &key) const' takes.
  - Qt's 'iterator QJsonObject::insert(QStringView key, const QJsonValue
    &value)': takes in Python what 'iterator QJsonObject::insert(const
    QString &key, const QJsonValue &value)' takes.
  - Qt's 'bool operator==(const QJsonValue &lhs, const QJsonObject &rhs)':
    takes in Python what 'bool operator==(const QJsonObject &lhs, const
    QJsonValue &rhs)' takes.
  - Qt's 'bool operator!=(const QJsonValue &lhs, const QJsonObject &rhs)':
    takes in Python what 'bool operator!=(const QJsonObject &lhs, const
    QJsonValue &rhs)' takes.
  - Qt's 'bool operator==(const QJsonValueConstRef &lhs, const QJsonObject
    &rhs)': takes in Python what 'bool operator==(const QJsonObject &lhs,
    const QJsonValueConstRef &rhs)' takes.
  - Qt's 'bool operator!=(const QJsonValueConstRef &lhs, const QJsonObject
    &rhs)': takes in Python what 'bool operator!=(const QJsonObject &lhs,
    const QJsonValueConstRef &rhs)' takes.

  What has no ritual
  ------------------

  11 of the 93 functions Qt declares: 9 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QJsonObject is created at the first use, not by
    'QJsonObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJsonObject back gives a copy the ritual made for
    Python, in a new cute QJsonObject.
  - Each name of Qt's QJsonObject that has no cute function yet,
    'asKeyValueRange', 'atImpl', 'constFindImpl', 'constKeyValueBegin',
    'constKeyValueEnd', 'containsImpl', 'findImpl', 'insertAt', 'insertImpl',
    'keyValueBegin', 'keyValueEnd', 'removeImpl', 'swap', 'takeImpl',
    'valueImpl', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QJsonObject, each a class in here as in
  #  C++.

  class const_iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QJsonObject::const_iterator: a plain Python object
    standing in front of one C++ QJsonObject::const_iterator.

    C++ hands a QJsonObject::const_iterator around as a copy, so every C++
    QJsonObject::const_iterator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QJsonObject::const_iterator that has a ritual and
    that Python can call so far, 16 names in all: 'key', 'keyView', 'value',
    '__getitem__', '__add__', '__sub__', '__iadd__', '__isub__',
    'comparesEqual_helper', 'compareThreeWay_helper', '__eq__', '__ne__',
    '__lt__', '__gt__', '__le__', '__ge__'. It can be made from Python, in 3
    ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonObject::const_iterator::const_iterator(const iterator
      &other)': names 'QJsonObject::iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'const_iterator &QJsonObject::const_iterator::operator=(const
      const_iterator &other)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'const QJsonValueConstRef QJsonObject::const_iterator::operator*()
      const': an operator Python has no name for.
    - Qt's 'const QJsonValueConstRef
      *QJsonObject::const_iterator::operator->() const': an operator Python
      has no name for.
    - Qt's 'const_iterator &QJsonObject::const_iterator::operator++()': an
      operator Python has no name for.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator++(int a0)':
      an operator Python has no name for.
    - Qt's 'const_iterator &QJsonObject::const_iterator::operator--()': an
      operator Python has no name for.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator--(int a0)':
      an operator Python has no name for.
    - Qt's 'QJsonObject::const_iterator::~const_iterator()': the destructor:
      Python removes its C++ QJsonObject::const_iterator by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QJsonObject::const_iterator is created at the first use, not by
      'QJsonObject::const_iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QJsonObject::const_iterator back gives a copy the
      ritual made for Python, in a new cute QJsonObject::const_iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QJsonObject.const_iterator,
        rhs: QJsonObject.const_iterator,
    ) -> bool:
      """
      Calls Qt's 'bool
      QJsonObject::const_iterator::comparesEqual_helper(const const_iterator
      &lhs, const const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html

      Parameters
      ----------

      lhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool QJsonObject::const_iterator::comparesEqual_helper(const
      #      const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZN11QJsonObject14const_iterator20comparesEqual_helperERKS'
          '0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QJsonObject.const_iterator,
        rhs: QJsonObject.const_iterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QJsonObject::const_iterator::compareThreeWay_helper(const
      const_iterator &lhs, const const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html

      Parameters
      ----------

      lhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering
      #      QJsonObject::const_iterator::compareThreeWay_helper(const
      #      const_iterator &lhs, const const_iterator &rhs)
      address = Rituals.call(
          'ritual_ZN11QJsonObject14const_iterator22compareThreeWay_helperER'
          'KS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QJsonObject::const_iterator'

    #  Qt's '~QJsonObject::const_iterator()'. Naming it makes this a value
    #  class: Python owns every C++ QJsonObject::const_iterator behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QJsonObject14const_iteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def key(self) -> str:
      """
      Calls Qt's 'QString QJsonObject::const_iterator::key() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#key

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QJsonObject::const_iterator::key() const
      return self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iterator3keyEv',
      )

    def keyView(self) -> str:
      """
      Calls Qt's 'QAnyStringView QJsonObject::const_iterator::keyView()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#keyView

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QAnyStringView QJsonObject::const_iterator::keyView() const
      return self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iterator7keyViewEv',
      )

    def value(self) -> QJsonValueConstRef:
      """
      Calls Qt's 'QJsonValueConstRef QJsonObject::const_iterator::value()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#value

      Returns
      -------

      QJsonValueConstRef
        A new cute QJsonValueConstRef around the copy Qt gave back. Python
        owns it.
      """
      #  QJsonValueConstRef QJsonObject::const_iterator::value() const
      address = self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iterator5valueEv',
      )
      from . import QJsonValueConstRef
      return QJsonValueConstRef._cuteOwning(address)

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
      QJsonObject::const_iterator::operator[](qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator[]

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
      #  QJsonValueConstRef QJsonObject::const_iterator::operator[](qsizetype
      #      j) const
      address = self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iteratorixEx', j,
      )
      from . import QJsonValueConstRef
      return QJsonValueConstRef._cuteOwning(address)

    @overload(int)
    def __add__(self, j: int) -> QJsonObject.const_iterator:
      """
      Calls Qt's 'const_iterator
      QJsonObject::const_iterator::operator+(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonObject.const_iterator
        A new cute QJsonObject::const_iterator around the copy Qt gave back.
        Python owns it.
      """
      #  const_iterator QJsonObject::const_iterator::operator+(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iteratorplEx', j,
      )
      return QJsonObject.const_iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QJsonObject.const_iterator:
      """
      Calls Qt's 'const_iterator
      QJsonObject::const_iterator::operator-(qsizetype j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonObject.const_iterator
        A new cute QJsonObject::const_iterator around the copy Qt gave back.
        Python owns it.
      """
      #  const_iterator QJsonObject::const_iterator::operator-(qsizetype j)
      #      const
      address = self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iteratormiEx', j,
      )
      return QJsonObject.const_iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QJsonObject.const_iterator) -> int:
      """
      Calls Qt's 'qsizetype
      QJsonObject::const_iterator::operator-(const_iterator j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator-

      Parameters
      ----------

      j : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  qsizetype QJsonObject::const_iterator::operator-(const_iterator j)
      #      const
      return self.uglySide.call(
          'ritual_ZNK11QJsonObject14const_iteratormiES0_', self._valueOf(j),
      )

    @overload.fallback
    def __sub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __iadd__(self, j: int) -> QJsonObject.const_iterator:
      """
      Calls Qt's 'const_iterator
      &QJsonObject::const_iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  const_iterator &QJsonObject::const_iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN11QJsonObject14const_iteratorpLEx', j)
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
    def __isub__(self, j: int) -> QJsonObject.const_iterator:
      """
      Calls Qt's 'const_iterator
      &QJsonObject::const_iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  const_iterator &QJsonObject::const_iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN11QJsonObject14const_iteratormIEx', j)
      return self

    @overload.fallback
    def __isub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator==

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator==(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZeqRKN11QJsonObject14const_iteratorES2_',
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
    def __ne__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator!=

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator!=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZneRKN11QJsonObject14const_iteratorES2_',
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
    def __lt__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator<

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator<(const const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN11QJsonObject14const_iteratorES2_',
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
    def __gt__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator>

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator>(const const_iterator &lhs, const const_iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN11QJsonObject14const_iteratorES2_',
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
    def __le__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator<=

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator<=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZleRKN11QJsonObject14const_iteratorES2_',
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
    def __ge__(self, rhs: QJsonObject.const_iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const const_iterator &lhs, const
      const_iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#operator>=

      Parameters
      ----------

      rhs : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  bool operator>=(const const_iterator &lhs, const const_iterator
      #      &rhs)
      return Rituals.call(
          'ritual_ZgeRKN11QJsonObject14const_iteratorES2_',
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
      'QJsonObject::const_iterator::const_iterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#const_iterator
      """
      #  QJsonObject::const_iterator::const_iterator()
      self._noteCreation(QJsonObject.const_iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject14const_iteratorC1Ev',
      ))

    @overload(QJsonObject, int)
    @overload(NoneType, int)
    def __init__(self, obj: Optional[QJsonObject], index: int) -> None:
      """
      Notes what was given, for Qt's
      'QJsonObject::const_iterator::const_iterator(const QJsonObject *obj,
      qsizetype index)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#const_iterator

      Parameters
      ----------

      obj : Optional[QJsonObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      index : int
        Passed on as it is.
      """
      #  QJsonObject::const_iterator::const_iterator(const QJsonObject *obj,
      #      qsizetype index)
      self._noteCreation(QJsonObject.const_iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject14const_iteratorC1EPKS_x',
          self._addressOf(obj), index,
      ))

    @overload(THIS)
    def __init__(self, other: QJsonObject.const_iterator) -> None:
      """
      Notes what was given, for Qt's
      'QJsonObject::const_iterator::const_iterator(const const_iterator
      &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-const_iterator.html#const_iterator

      Parameters
      ----------

      other : QJsonObject.const_iterator
        Passed on as a value: Qt reads the C++ QJsonObject::const_iterator,
        which stays Python's own.
      """
      #  QJsonObject::const_iterator::const_iterator(const const_iterator
      #      &other)
      self._noteCreation(QJsonObject.const_iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject14const_iteratorC1ERKS0_',
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
    The cute side of Qt's QJsonObject::iterator: a plain Python object
    standing in front of one C++ QJsonObject::iterator.

    C++ hands a QJsonObject::iterator around as a copy, so every C++
    QJsonObject::iterator behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QJsonObject::iterator that has a ritual and that
    Python can call so far, 16 names in all: 'key', 'keyView', 'value',
    '__getitem__', '__add__', '__sub__', '__iadd__', '__isub__',
    'comparesEqual_helper', 'compareThreeWay_helper', '__eq__', '__ne__',
    '__lt__', '__gt__', '__le__', '__ge__'. It can be made from Python, in 3
    ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'iterator &QJsonObject::iterator::operator=(const iterator
      &other)': assignment: Python binds a name and has no operator for it.
    - Qt's 'QJsonValueRef QJsonObject::iterator::operator*() const': an
      operator Python has no name for.
    - Qt's 'const QJsonValueConstRef *QJsonObject::iterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'QJsonValueRef *QJsonObject::iterator::operator->()': an operator
      Python has no name for.
    - Qt's 'iterator &QJsonObject::iterator::operator++()': an operator
      Python has no name for.
    - Qt's 'iterator QJsonObject::iterator::operator++(int a0)': an operator
      Python has no name for.
    - Qt's 'iterator &QJsonObject::iterator::operator--()': an operator
      Python has no name for.
    - Qt's 'iterator QJsonObject::iterator::operator--(int a0)': an operator
      Python has no name for.
    - Qt's 'bool QJsonObject::iterator::comparesEqual_helper(const iterator
      &lhs, const const_iterator &rhs)': names 'QJsonObject::const_iterator',
      which stands beside this class inside 'QJsonObject' and cannot be named
      from here.
    - Qt's 'Qt::strong_ordering
      QJsonObject::iterator::compareThreeWay_helper(const iterator &lhs,
      const const_iterator &rhs)': names 'QJsonObject::const_iterator', which
      stands beside this class inside 'QJsonObject' and cannot be named from
      here.
    - Qt's 'bool operator==(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator!=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator<(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator>(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator<=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator>=(const iterator &lhs, const const_iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator==(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator!=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator<(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator>(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator<=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'bool operator>=(const const_iterator &lhs, const iterator &rhs)':
      names 'QJsonObject::const_iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'QJsonObject::iterator::~iterator()': the destructor: Python
      removes its C++ QJsonObject::iterator by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QJsonObject::iterator is created at the first use, not by
      'QJsonObject::iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QJsonObject::iterator back gives a copy the ritual
      made for Python, in a new cute QJsonObject::iterator.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QJsonObject = WAIT['QJsonObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def comparesEqual_helper(
        lhs: QJsonObject.iterator,
        rhs: QJsonObject.iterator,
    ) -> bool:
      """
      Calls Qt's 'bool QJsonObject::iterator::comparesEqual_helper(const
      iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#comparesEqual_helper

      Parameters
      ----------

      lhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool QJsonObject::iterator::comparesEqual_helper(const iterator
      #      &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZN11QJsonObject8iterator20comparesEqual_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )

    @staticmethod
    @overload(THIS, THIS)
    def compareThreeWay_helper(
        lhs: QJsonObject.iterator,
        rhs: QJsonObject.iterator,
    ) -> Qt.strong_ordering:
      """
      Calls Qt's 'Qt::strong_ordering
      QJsonObject::iterator::compareThreeWay_helper(const iterator &lhs,
      const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#compareThreeWay_helper

      Parameters
      ----------

      lhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.

      Returns
      -------

      Qt.strong_ordering
        A new cute Qt::strong_ordering around the copy Qt gave back. Python
        owns it.
      """
      #  Qt::strong_ordering
      #      QJsonObject::iterator::compareThreeWay_helper(const iterator
      #      &lhs, const iterator &rhs)
      address = Rituals.call(
          'ritual_ZN11QJsonObject8iterator22compareThreeWay_helperERKS0_S2_',
          CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
      )
      return Qt.strong_ordering._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QJsonObject::iterator'

    #  Qt's '~QJsonObject::iterator()'. Naming it makes this a value class:
    #  Python owns every C++ QJsonObject::iterator behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QJsonObject8iteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def key(self) -> str:
      """
      Calls Qt's 'QString QJsonObject::iterator::key() const'.

      Qt's own words: https://doc.qt.io/qt-6/qjsonobject-iterator.html#key

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QJsonObject::iterator::key() const
      return self.uglySide.call('ritual_ZNK11QJsonObject8iterator3keyEv')

    def keyView(self) -> str:
      """
      Calls Qt's 'QAnyStringView QJsonObject::iterator::keyView() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#keyView

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QAnyStringView QJsonObject::iterator::keyView() const
      return self.uglySide.call('ritual_ZNK11QJsonObject8iterator7keyViewEv')

    def value(self) -> QJsonValueRef:
      """
      Calls Qt's 'QJsonValueRef QJsonObject::iterator::value() const'.

      Qt's own words: https://doc.qt.io/qt-6/qjsonobject-iterator.html#value

      Returns
      -------

      QJsonValueRef
        A new cute QJsonValueRef around the copy Qt gave back. Python owns
        it.
      """
      #  QJsonValueRef QJsonObject::iterator::value() const
      address = self.uglySide.call(
          'ritual_ZNK11QJsonObject8iterator5valueEv',
      )
      from . import QJsonValueRef
      return QJsonValueRef._cuteOwning(address)

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
      Calls Qt's 'QJsonValueRef QJsonObject::iterator::operator[](qsizetype
      j) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator[]

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
      #  QJsonValueRef QJsonObject::iterator::operator[](qsizetype j) const
      address = self.uglySide.call('ritual_ZNK11QJsonObject8iteratorixEx', j)
      from . import QJsonValueRef
      return QJsonValueRef._cuteOwning(address)

    @overload(int)
    def __add__(self, j: int) -> QJsonObject.iterator:
      """
      Calls Qt's 'iterator QJsonObject::iterator::operator+(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator+

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonObject.iterator
        A new cute QJsonObject::iterator around the copy Qt gave back. Python
        owns it.
      """
      #  iterator QJsonObject::iterator::operator+(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK11QJsonObject8iteratorplEx', j)
      return QJsonObject.iterator._cuteOwning(address)

    @overload.fallback
    def __add__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __sub__(self, j: int) -> QJsonObject.iterator:
      """
      Calls Qt's 'iterator QJsonObject::iterator::operator-(qsizetype j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator-

      Parameters
      ----------

      j : int
        Passed on as it is.

      Returns
      -------

      QJsonObject.iterator
        A new cute QJsonObject::iterator around the copy Qt gave back. Python
        owns it.
      """
      #  iterator QJsonObject::iterator::operator-(qsizetype j) const
      address = self.uglySide.call('ritual_ZNK11QJsonObject8iteratormiEx', j)
      return QJsonObject.iterator._cuteOwning(address)

    @overload(THIS)
    def __sub__(self, j: QJsonObject.iterator) -> int:
      """
      Calls Qt's 'qsizetype QJsonObject::iterator::operator-(iterator j)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator-

      Parameters
      ----------

      j : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  qsizetype QJsonObject::iterator::operator-(iterator j) const
      return self.uglySide.call(
          'ritual_ZNK11QJsonObject8iteratormiES0_', self._valueOf(j),
      )

    @overload.fallback
    def __sub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __iadd__(self, j: int) -> QJsonObject.iterator:
      """
      Calls Qt's 'iterator &QJsonObject::iterator::operator+=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator+=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  iterator &QJsonObject::iterator::operator+=(qsizetype j)
      self.uglySide.call('ritual_ZN11QJsonObject8iteratorpLEx', j)
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
    def __isub__(self, j: int) -> QJsonObject.iterator:
      """
      Calls Qt's 'iterator &QJsonObject::iterator::operator-=(qsizetype j)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator-=

      Parameters
      ----------

      j : int
        Passed on as it is.
      """
      #  iterator &QJsonObject::iterator::operator-=(qsizetype j)
      self.uglySide.call('ritual_ZN11QJsonObject8iteratormIEx', j)
      return self

    @overload.fallback
    def __isub__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator==(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator==

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator==(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZeqRKN11QJsonObject8iteratorES2_',
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
    def __ne__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator!=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator!=

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator!=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZneRKN11QJsonObject8iteratorES2_',
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
    def __lt__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator<(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator<

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator<(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZltRKN11QJsonObject8iteratorES2_',
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
    def __gt__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator>(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator>

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator>(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZgtRKN11QJsonObject8iteratorES2_',
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
    def __le__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator<=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator<=

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator<=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZleRKN11QJsonObject8iteratorES2_',
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
    def __ge__(self, rhs: QJsonObject.iterator) -> bool:
      """
      Calls Qt's 'bool operator>=(const iterator &lhs, const iterator &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#operator>=

      Parameters
      ----------

      rhs : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  bool operator>=(const iterator &lhs, const iterator &rhs)
      return Rituals.call(
          'ritual_ZgeRKN11QJsonObject8iteratorES2_',
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
      Notes what was given, for Qt's 'QJsonObject::iterator::iterator()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#iterator
      """
      #  QJsonObject::iterator::iterator()
      self._noteCreation(QJsonObject.iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject8iteratorC1Ev',
      ))

    @overload(QJsonObject, int)
    @overload(NoneType, int)
    def __init__(self, obj: Optional[QJsonObject], index: int) -> None:
      """
      Notes what was given, for Qt's
      'QJsonObject::iterator::iterator(QJsonObject *obj, qsizetype index)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#iterator

      Parameters
      ----------

      obj : Optional[QJsonObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      index : int
        Passed on as it is.
      """
      #  QJsonObject::iterator::iterator(QJsonObject *obj, qsizetype index)
      self._noteCreation(QJsonObject.iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject8iteratorC1EPS_x',
          self._addressOf(obj), index,
      ))

    @overload(THIS)
    def __init__(self, other: QJsonObject.iterator) -> None:
      """
      Notes what was given, for Qt's 'QJsonObject::iterator::iterator(const
      iterator &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qjsonobject-iterator.html#iterator

      Parameters
      ----------

      other : QJsonObject.iterator
        Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
        stays Python's own.
      """
      #  QJsonObject::iterator::iterator(const iterator &other)
      self._noteCreation(QJsonObject.iterator, lambda: Rituals.call(
          'ritual_ZN11QJsonObject8iteratorC1ERKS0_', self._valueOf(other),
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
  def fromVariantMap(map: QMap[str, QVariant]) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonObject::fromVariantMap(const QVariantMap
    &map)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#fromVariantMap

    Parameters
    ----------

    map : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonObject::fromVariantMap(const QVariantMap &map)
    address = Rituals.call(
        'ritual_ZN11QJsonObject14fromVariantMapERK4QMapI7QString8QVariantE',
        CuteMixin._valueOf(map),
    )
    return QJsonObject._cuteOwning(address)

  @staticmethod
  @overload(QHash[str, QVariant])
  def fromVariantHash(map: QHash[str, QVariant]) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QJsonObject::fromVariantHash(const QVariantHash
    &map)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#fromVariantHash

    Parameters
    ----------

    map : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QJsonObject::fromVariantHash(const QVariantHash &map)
    address = Rituals.call(
        'ritual_ZN11QJsonObject15fromVariantHashERK5QHashI7QString8QVariant'
        'E',
        CuteMixin._valueOf(map),
    )
    return QJsonObject._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJsonObject'

  #  Qt's '~QJsonObject()'. Naming it makes this a value class: Python owns
  #  every C++ QJsonObject behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QJsonObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toVariantMap(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QJsonObject::toVariantMap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#toVariantMap

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QJsonObject::toVariantMap() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject12toVariantMapEv')
    from . import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def toVariantHash(self) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QVariantHash QJsonObject::toVariantHash() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#toVariantHash

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantHash QJsonObject::toVariantHash() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject13toVariantHashEv')
    from . import QVariant
    return QHash[str, QVariant]._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QJsonObject::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QJsonObject::keys() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject4keysEv')
    return QStringList._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#size
    """
    #  qsizetype QJsonObject::size() const
    return self.uglySide.call('ritual_ZNK11QJsonObject4sizeEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#count
    """
    #  qsizetype QJsonObject::count() const
    return self.uglySide.call('ritual_ZNK11QJsonObject5countEv')

  def length(self) -> int:
    """
    Calls Qt's 'qsizetype QJsonObject::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#length
    """
    #  qsizetype QJsonObject::length() const
    return self.uglySide.call('ritual_ZNK11QJsonObject6lengthEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QJsonObject::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#isEmpty
    """
    #  bool QJsonObject::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QJsonObject7isEmptyEv')

  @overload(str)
  def value(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::value(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#value

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::value(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObject5valueERK7QString', key,
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def value(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::value(QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#value

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::value(QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObject5valueE13QLatin1String', self._valueOf(key),
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(str)
  def contains(self, key: str) -> bool:
    """
    Calls Qt's 'bool QJsonObject::contains(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#contains

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QJsonObject::contains(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK11QJsonObject8containsERK7QString', key,
    )

  @overload(QLatin1String)
  def contains(self, key: QLatin1String) -> bool:
    """
    Calls Qt's 'bool QJsonObject::contains(QLatin1StringView key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#contains

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  bool QJsonObject::contains(QLatin1StringView key) const
    return self.uglySide.call(
        'ritual_ZNK11QJsonObject8containsE13QLatin1String',
        self._valueOf(key),
    )

  def cbegin(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::cbegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#cbegin

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::cbegin() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject6cbeginEv')
    return QJsonObject.const_iterator._cuteOwning(address)

  def constBegin(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::constBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#constBegin

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::constBegin() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject10constBeginEv')
    return QJsonObject.const_iterator._cuteOwning(address)

  def cend(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::cend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#cend

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::cend() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject4cendEv')
    return QJsonObject.const_iterator._cuteOwning(address)

  def constEnd(self) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::constEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#constEnd

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::constEnd() const
    address = self.uglySide.call('ritual_ZNK11QJsonObject8constEndEv')
    return QJsonObject.const_iterator._cuteOwning(address)

  @overload(str)
  def constFind(self, key: str) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::constFind(const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#constFind

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::constFind(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObject9constFindERK7QString', key,
    )
    return QJsonObject.const_iterator._cuteOwning(address)

  @overload(QLatin1String)
  def constFind(self, key: QLatin1String) -> const_iterator:
    """
    Calls Qt's 'const_iterator QJsonObject::constFind(QLatin1StringView key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#constFind

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    const_iterator
      A new cute QJsonObject::const_iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const_iterator QJsonObject::constFind(QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObject9constFindE13QLatin1String',
        self._valueOf(key),
    )
    return QJsonObject.const_iterator._cuteOwning(address)

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QJsonObject::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#empty
    """
    #  bool QJsonObject::empty() const
    return self.uglySide.call('ritual_ZNK11QJsonObject5emptyEv')

  @overload(int)
  def keyAt(self, i: int) -> str:
    """
    Calls Qt's 'QString QJsonObject::keyAt(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#keyAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJsonObject::keyAt(qsizetype i) const
    return self.uglySide.call('ritual_ZNK11QJsonObject5keyAtEx', i)

  @overload(int)
  def valueAt(self, i: int) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::valueAt(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#valueAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::valueAt(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK11QJsonObject7valueAtEx', i)
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QJsonValue)
  def setValueAt(self, i: int, val: QJsonValue) -> None:
    """
    Calls Qt's 'void QJsonObject::setValueAt(qsizetype i, const QJsonValue
    &val)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#setValueAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    val : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  void QJsonObject::setValueAt(qsizetype i, const QJsonValue &val)
    self.uglySide.call(
        'ritual_ZN11QJsonObject10setValueAtExRK10QJsonValue',
        i, self._valueOf(val),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __getitem__(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::operator[](const QString &key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator[]

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::operator[](const QString &key) const
    address = self.uglySide.call('ritual_ZNK11QJsonObjectixERK7QString', key)
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def __getitem__(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::operator[](QLatin1StringView key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator[]

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::operator[](QLatin1StringView key) const
    address = self.uglySide.call(
        'ritual_ZNK11QJsonObjectixE13QLatin1String', self._valueOf(key),
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(THIS)
  def __eq__(self, rhs: QJsonObject) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonObject &lhs, const QJsonObject
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator==

    Parameters
    ----------

    rhs : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  bool operator==(const QJsonObject &lhs, const QJsonObject &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QJsonObjectS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __eq__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonObject &lhs, const QJsonValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator==

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator==(const QJsonObject &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QJsonObjectRK10QJsonValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValueConstRef)
  def __eq__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator==(const QJsonObject &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator==

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator==(const QJsonObject &lhs, const QJsonValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QJsonObjectRK18QJsonValueConstRef',
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
  def __ne__(self, rhs: QJsonObject) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonObject &lhs, const QJsonObject
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator!=

    Parameters
    ----------

    rhs : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonObject &lhs, const QJsonObject &rhs)
    return Rituals.call(
        'ritual_ZneRK11QJsonObjectS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValue)
  def __ne__(self, rhs: QJsonValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonObject &lhs, const QJsonValue
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator!=

    Parameters
    ----------

    rhs : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.
    """
    #  bool operator!=(const QJsonObject &lhs, const QJsonValue &rhs)
    return Rituals.call(
        'ritual_ZneRK11QJsonObjectRK10QJsonValue',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(QJsonValueConstRef)
  def __ne__(self, rhs: QJsonValueConstRef) -> bool:
    """
    Calls Qt's 'bool operator!=(const QJsonObject &lhs, const
    QJsonValueConstRef &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator!=

    Parameters
    ----------

    rhs : QJsonValueConstRef
      Passed on as a value: Qt reads the C++ QJsonValueConstRef, which stays
      Python's own.
    """
    #  bool operator!=(const QJsonObject &lhs, const QJsonValueConstRef &rhs)
    return Rituals.call(
        'ritual_ZneRK11QJsonObjectRK18QJsonValueConstRef',
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

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QJsonObject &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#operator<<

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
    #  QDebug operator<<(QDebug a0, const QJsonObject &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK11QJsonObject',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QJsonObject::QJsonObject()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#QJsonObject
    """
    #  QJsonObject::QJsonObject()
    self._noteCreation(QJsonObject, lambda: Rituals.call(
        'ritual_ZN11QJsonObjectC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QJsonObject) -> None:
    """
    Notes what was given, for Qt's 'QJsonObject::QJsonObject(const
    QJsonObject &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#QJsonObject

    Parameters
    ----------

    other : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  QJsonObject::QJsonObject(const QJsonObject &other)
    self._noteCreation(QJsonObject, lambda: Rituals.call(
        'ritual_ZN11QJsonObjectC1ERKS_', self._valueOf(other),
    ))

  @overload(QCborContainerPrivate)
  @overload(NoneType)
  def __init__(self, object: Optional[QCborContainerPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QJsonObject::QJsonObject(QCborContainerPrivate *object)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#QJsonObject

    Parameters
    ----------

    object : Optional[QCborContainerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QJsonObject::QJsonObject(QCborContainerPrivate *object)
    self._noteCreation(QJsonObject, lambda: Rituals.call(
        'ritual_ZN11QJsonObjectC1EP21QCborContainerPrivate',
        self._addressOf(object),
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

  @overload(str)
  def remove(self, key: str) -> None:
    """
    Calls Qt's 'void QJsonObject::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QJsonObject::remove(const QString &key)
    self.uglySide.call('ritual_ZN11QJsonObject6removeERK7QString', key)

  @overload(QLatin1String)
  def remove(self, key: QLatin1String) -> None:
    """
    Calls Qt's 'void QJsonObject::remove(QLatin1StringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#remove

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QJsonObject::remove(QLatin1StringView key)
    self.uglySide.call(
        'ritual_ZN11QJsonObject6removeE13QLatin1String', self._valueOf(key),
    )

  @overload(str)
  def take(self, key: str) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::take(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#take

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::take(const QString &key)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject4takeERK7QString', key,
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  @overload(QLatin1String)
  def take(self, key: QLatin1String) -> QJsonValue:
    """
    Calls Qt's 'QJsonValue QJsonObject::take(QLatin1StringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#take

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    QJsonValue
      A new cute QJsonValue around the copy Qt gave back. Python owns it.
    """
    #  QJsonValue QJsonObject::take(QLatin1StringView key)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject4takeE13QLatin1String', self._valueOf(key),
    )
    from . import QJsonValue
    return QJsonValue._cuteOwning(address)

  def begin(self) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::begin()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#begin

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::begin()
    address = self.uglySide.call('ritual_ZN11QJsonObject5beginEv')
    return QJsonObject.iterator._cuteOwning(address)

  def end(self) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#end

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::end()
    address = self.uglySide.call('ritual_ZN11QJsonObject3endEv')
    return QJsonObject.iterator._cuteOwning(address)

  @overload(iterator)
  def erase(self, it: iterator) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::erase(iterator it)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#erase

    Parameters
    ----------

    it : iterator
      Passed on as a value: Qt reads the C++ QJsonObject::iterator, which
      stays Python's own.

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::erase(iterator it)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject5eraseENS_8iteratorE', self._valueOf(it),
    )
    return QJsonObject.iterator._cuteOwning(address)

  @overload(str)
  def find(self, key: str) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::find(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#find

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::find(const QString &key)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject4findERK7QString', key,
    )
    return QJsonObject.iterator._cuteOwning(address)

  @overload(QLatin1String)
  def find(self, key: QLatin1String) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::find(QLatin1StringView key)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#find

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::find(QLatin1StringView key)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject4findE13QLatin1String', self._valueOf(key),
    )
    return QJsonObject.iterator._cuteOwning(address)

  @overload(str, QJsonValue)
  def insert(self, key: str, value: QJsonValue) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::insert(const QString &key, const
    QJsonValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#insert

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::insert(const QString &key, const QJsonValue
    #      &value)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject6insertERK7QStringRK10QJsonValue',
        key, self._valueOf(value),
    )
    return QJsonObject.iterator._cuteOwning(address)

  @overload(QLatin1String, QJsonValue)
  def insert(self, key: QLatin1String, value: QJsonValue) -> iterator:
    """
    Calls Qt's 'iterator QJsonObject::insert(QLatin1StringView key, const
    QJsonValue &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#insert

    Parameters
    ----------

    key : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    value : QJsonValue
      Passed on as a value: Qt reads the C++ QJsonValue, which stays Python's
      own.

    Returns
    -------

    iterator
      A new cute QJsonObject::iterator around the copy Qt gave back. Python
      owns it.
    """
    #  iterator QJsonObject::insert(QLatin1StringView key, const QJsonValue
    #      &value)
    address = self.uglySide.call(
        'ritual_ZN11QJsonObject6insertE13QLatin1StringRK10QJsonValue',
        self._valueOf(key), self._valueOf(value),
    )
    return QJsonObject.iterator._cuteOwning(address)

  @overload()
  @overload(int)
  def detach(self, reserve: int = 0) -> bool:
    """
    Calls Qt's 'bool QJsonObject::detach(qsizetype reserve)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#detach

    Parameters
    ----------

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QJsonObject::detach(qsizetype reserve)
    return self.uglySide.call('ritual_ZN11QJsonObject6detachEx', reserve)

  @overload(int)
  def removeAt(self, i: int) -> None:
    """
    Calls Qt's 'void QJsonObject::removeAt(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonobject.html#removeAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QJsonObject::removeAt(qsizetype i)
    self.uglySide.call('ritual_ZN11QJsonObject8removeAtEx', i)

  @staticmethod
  def asKeyValueRange(*__, **_) -> Never:
    """
    - Qt's 'QtPrivate::QKeyValueRange<QJsonObject &>
      QJsonObject::asKeyValueRange()': gives a type Python has no way to take
      yet.
    - Qt's 'QtPrivate::QKeyValueRange<const QJsonObject &>
      QJsonObject::asKeyValueRange() const': gives a type Python has no way
      to take yet.
    """
    raise NotImplementedError(
        "'QJsonObject.asKeyValueRange' has no cute function yet. Qt's "
        "'QtPrivate::QKeyValueRange<QJsonObject &> "
        "QJsonObject::asKeyValueRange()': gives a type Python has no way to "
        "take yet. Qt's 'QtPrivate::QKeyValueRange<const QJsonObject &> "
        "QJsonObject::asKeyValueRange() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def atImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::atImpl': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QJsonObject.atImpl' has no cute function yet. Qt's "
        "'QJsonObject::atImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def constFindImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::constFindImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.constFindImpl' has no cute function yet. Qt's "
        "'QJsonObject::constFindImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def constKeyValueBegin(*__, **_) -> Never:
    """
    Qt's 'const_key_value_iterator QJsonObject::constKeyValueBegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJsonObject.constKeyValueBegin' has no cute function yet. Qt's "
        "'const_key_value_iterator QJsonObject::constKeyValueBegin() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def constKeyValueEnd(*__, **_) -> Never:
    """
    Qt's 'const_key_value_iterator QJsonObject::constKeyValueEnd() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJsonObject.constKeyValueEnd' has no cute function yet. Qt's "
        "'const_key_value_iterator QJsonObject::constKeyValueEnd() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def containsImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::containsImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.containsImpl' has no cute function yet. Qt's "
        "'QJsonObject::containsImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def findImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::findImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.findImpl' has no cute function yet. Qt's "
        "'QJsonObject::findImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def insertAt(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::insertAt': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.insertAt' has no cute function yet. Qt's "
        "'QJsonObject::insertAt': a template: a pattern and no single "
        "function.")

  @staticmethod
  def insertImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::insertImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.insertImpl' has no cute function yet. Qt's "
        "'QJsonObject::insertImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def keyValueBegin(*__, **_) -> Never:
    """
    - Qt's 'key_value_iterator QJsonObject::keyValueBegin()': gives a type
      Python has no way to take yet.
    - Qt's 'const_key_value_iterator QJsonObject::keyValueBegin() const':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJsonObject.keyValueBegin' has no cute function yet. Qt's "
        "'key_value_iterator QJsonObject::keyValueBegin()': gives a type "
        "Python has no way to take yet. Qt's 'const_key_value_iterator "
        "QJsonObject::keyValueBegin() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def keyValueEnd(*__, **_) -> Never:
    """
    - Qt's 'key_value_iterator QJsonObject::keyValueEnd()': gives a type
      Python has no way to take yet.
    - Qt's 'const_key_value_iterator QJsonObject::keyValueEnd() const': gives
      a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QJsonObject.keyValueEnd' has no cute function yet. Qt's "
        "'key_value_iterator QJsonObject::keyValueEnd()': gives a type "
        "Python has no way to take yet. Qt's 'const_key_value_iterator "
        "QJsonObject::keyValueEnd() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def removeImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::removeImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.removeImpl' has no cute function yet. Qt's "
        "'QJsonObject::removeImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QJsonObject::swap(QJsonObject &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJsonObject.swap' has no cute function yet. Qt's 'void "
        "QJsonObject::swap(QJsonObject &other)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def takeImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::takeImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.takeImpl' has no cute function yet. Qt's "
        "'QJsonObject::takeImpl': a template: a pattern and no single "
        "function.")

  @staticmethod
  def valueImpl(*__, **_) -> Never:
    """
    Qt's 'QJsonObject::valueImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QJsonObject.valueImpl' has no cute function yet. Qt's "
        "'QJsonObject::valueImpl': a template: a pattern and no single "
        "function.")


#  Qt's 'QMap<QString, QJsonObject>': the QMap from text to QJsonObject,
#  which 'QMap[str, QJsonObject]' gives. It is completed here, in the file of
#  the class of its values.
QMap.createKind(
    str, QJsonObject, 'value',
    make='ritual_map_make_QMap_QString_QJsonObject',
    put='ritual_map_put_QMap_QString_QJsonObject',
    size='ritual_map_size_QMap_QString_QJsonObject',
    key='ritual_map_key_QMap_QString_QJsonObject',
    value='ritual_map_value_QMap_QString_QJsonObject',
    has='ritual_map_has_QMap_QString_QJsonObject',
    get='ritual_map_get_QMap_QString_QJsonObject',
    drop='ritual_map_drop_QMap_QString_QJsonObject',
)
