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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QJsonValue, QJsonValueConstRef, QJsonValueRef, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonValue = WAIT['QJsonValue']
  QLatin1String = WAIT['QLatin1String']

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
  call so far, 19 names in all: 'size', 'count', 'length', 'isEmpty',
  'value', 'remove', 'take', 'contains', 'begin', 'cbegin', 'constBegin',
  'end', 'cend', 'constEnd', 'erase', 'find', 'constFind', 'insert', 'empty'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonObject::~QJsonObject()': the destructor: Python removes its
    C++ QJsonObject by it, and has no other use for it.
  - Qt's 'QJsonValue QJsonObject::operator[](const QString &key) const': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](const QString &key)': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValue QJsonObject::value(QStringView key) const': takes in
    Python what 'QJsonValue QJsonObject::value(const QString &key) const'
    takes.
  - Qt's 'QJsonValue QJsonObject::operator[](QStringView key) const': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValue QJsonObject::operator[](QLatin1StringView key) const':
    an operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QStringView key)': an
    operator, which is not reflected yet.
  - Qt's 'QJsonValueRef QJsonObject::operator[](QLatin1StringView key)': an
    operator, which is not reflected yet.
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

  What has no ritual
  ------------------

  35 of the 82 functions Qt declares: 18 takes or gives a type that cannot be
  passed yet; 9 a template; 6 private; 2 can only be called on a value about
  to be thrown away.

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
    that Python can call so far, 3 names in all: 'key', 'keyView', 'value'.
    It can be made from Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonObject::const_iterator::const_iterator(const iterator
      &other)': names 'QJsonObject::iterator', which stands beside this class
      inside 'QJsonObject' and cannot be named from here.
    - Qt's 'const QJsonValueConstRef QJsonObject::const_iterator::operator*()
      const': an operator, which is not reflected yet.
    - Qt's 'const QJsonValueConstRef
      *QJsonObject::const_iterator::operator->() const': an operator, which
      is not reflected yet.
    - Qt's 'QJsonValueConstRef
      QJsonObject::const_iterator::operator[](qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator++(int a0)':
      an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator--(int a0)':
      an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator+(qsizetype
      j) const': an operator, which is not reflected yet.
    - Qt's 'const_iterator QJsonObject::const_iterator::operator-(qsizetype
      j) const': an operator, which is not reflected yet.
    - Qt's 'qsizetype QJsonObject::const_iterator::operator-(const_iterator
      j) const': an operator, which is not reflected yet.
    - Qt's 'QJsonObject::const_iterator::~const_iterator()': the destructor:
      Python removes its C++ QJsonObject::const_iterator by it, and has no
      other use for it.

    What has no ritual
    ------------------

    7 of the 23 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet; 2 private.

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
    Python can call so far, 3 names in all: 'key', 'keyView', 'value'. It can
    be made from Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QJsonValueRef QJsonObject::iterator::operator*() const': an
      operator, which is not reflected yet.
    - Qt's 'const QJsonValueConstRef *QJsonObject::iterator::operator->()
      const': an operator, which is not reflected yet.
    - Qt's 'QJsonValueRef *QJsonObject::iterator::operator->()': an operator,
      which is not reflected yet.
    - Qt's 'QJsonValueRef QJsonObject::iterator::operator[](qsizetype j)
      const': an operator, which is not reflected yet.
    - Qt's 'iterator QJsonObject::iterator::operator++(int a0)': an operator,
      which is not reflected yet.
    - Qt's 'iterator QJsonObject::iterator::operator--(int a0)': an operator,
      which is not reflected yet.
    - Qt's 'iterator QJsonObject::iterator::operator+(qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'iterator QJsonObject::iterator::operator-(qsizetype j) const': an
      operator, which is not reflected yet.
    - Qt's 'qsizetype QJsonObject::iterator::operator-(iterator j) const': an
      operator, which is not reflected yet.
    - Qt's 'QJsonObject::iterator::~iterator()': the destructor: Python
      removes its C++ QJsonObject::iterator by it, and has no other use for
      it.

    What has no ritual
    ------------------

    9 of the 25 functions Qt declares: 5 takes or gives a type that cannot be
    passed yet; 4 private.

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
