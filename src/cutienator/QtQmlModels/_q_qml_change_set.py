"""
QQmlChangeSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlChangeSet to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlChangeSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlChangeSet: a plain Python object standing in
  front of one C++ QQmlChangeSet.

  C++ hands a QQmlChangeSet around as a copy, so every C++ QQmlChangeSet
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlChangeSet that has a ritual and that Python can
  call so far, 8 names in all: 'insert', 'remove', 'move', 'change', 'apply',
  'isEmpty', 'clear', 'difference'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlChangeSet::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQmlChangeSet::~QQmlChangeSet()': the destructor: Python removes
    its C++ QQmlChangeSet by it, and has no other use for it.
  - Qt's 'QQmlChangeSet &QQmlChangeSet::operator=(const QQmlChangeSet
    &changeSet)': assignment: Python binds a name and has no operator for it.
  - Qt's 'const QList<Change> &QQmlChangeSet::removes() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QList<Change> &QQmlChangeSet::inserts() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QList<Change> &QQmlChangeSet::changes() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QQmlChangeSet::insert(const QList<Change> &inserts)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQmlChangeSet::remove(const QList<Change> &removes,
    QList<Change> *inserts)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlChangeSet::move(const QList<Change> &removes, const
    QList<Change> &inserts)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlChangeSet::change(const QList<Change> &changes)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQmlChangeSet::remove(QList<Change> *removes, QList<Change>
    *inserts)': names 'QList<QQmlChangeSet::Change>', which has no cute class
    yet.
  - Qt's 'void QQmlChangeSet::change(QList<Change> *changes)': names
    'QList<QQmlChangeSet::Change>', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlChangeSet is created at the first use, not by
    'QQmlChangeSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlChangeSet back gives a copy the ritual made for
    Python, in a new cute QQmlChangeSet.
  - Each name of Qt's QQmlChangeSet that has no cute function yet, 'changes',
    'inserts', 'removes', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QQmlChangeSet, each a class in here as in
  #  C++.

  class Change(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlChangeSet::Change: a plain Python object
    standing in front of one C++ QQmlChangeSet::Change.

    C++ hands a QQmlChangeSet::Change around as a copy, so every C++
    QQmlChangeSet::Change behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlChangeSet::Change that has a ritual and that
    Python can call so far, 3 names in all: 'isMove', 'start', 'end'. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'MoveKey QQmlChangeSet::Change::moveKey(int index) const': gives
      'QQmlChangeSet::MoveKey', which stands beside this class inside
      'QQmlChangeSet' and cannot be named from here.
    - Qt's 'QQmlChangeSet::Change::~Change()': the destructor: Python removes
      its C++ QQmlChangeSet::Change by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlChangeSet::Change is created at the first use, not by
      'QQmlChangeSet::Change(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlChangeSet::Change back gives a copy the ritual
      made for Python, in a new cute QQmlChangeSet::Change.
    - Each name of Qt's QQmlChangeSet::Change that has no cute function yet,
      'moveKey', holds a function that raises 'NotImplementedError', and its
      docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlChangeSet::Change'

    #  Qt's '~QQmlChangeSet::Change()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlChangeSet::Change behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlChangeSet6ChangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isMove(self) -> bool:
      """
      Calls Qt's 'bool QQmlChangeSet::Change::isMove() const'.

      Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset-change.html#isMove
      """
      #  bool QQmlChangeSet::Change::isMove() const
      return self.uglySide.call('ritual_ZNK13QQmlChangeSet6Change6isMoveEv')

    def start(self) -> int:
      """
      Calls Qt's 'int QQmlChangeSet::Change::start() const'.

      Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset-change.html#start
      """
      #  int QQmlChangeSet::Change::start() const
      return self.uglySide.call('ritual_ZNK13QQmlChangeSet6Change5startEv')

    def end(self) -> int:
      """
      Calls Qt's 'int QQmlChangeSet::Change::end() const'.

      Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset-change.html#end
      """
      #  int QQmlChangeSet::Change::end() const
      return self.uglySide.call('ritual_ZNK13QQmlChangeSet6Change3endEv')

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
      Notes what was given, for Qt's 'QQmlChangeSet::Change::Change()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset-change.html#Change
      """
      #  QQmlChangeSet::Change::Change()
      self._noteCreation(QQmlChangeSet.Change, lambda: Rituals.call(
          'ritual_ZN13QQmlChangeSet6ChangeC1Ev',
      ))

    @overload(int, int)
    @overload(int, int, int)
    @overload(int, int, int, int)
    def __init__(
        self,
        index: int,
        count: int,
        moveId: int = -1,
        offset: int = 0,
    ) -> None:
      """
      Notes what was given, for Qt's 'QQmlChangeSet::Change::Change(int
      index, int count, int moveId, int offset)', which is called at the
      first use.

      Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset-change.html#Change

      Parameters
      ----------

      index : int
        Passed on as it is.

      count : int
        Passed on as it is.

      moveId : int
        Passed on as it is. May be left out, as in Qt: it is then -1.

      offset : int
        Passed on as it is. May be left out, as in Qt: it is then 0.
      """
      #  QQmlChangeSet::Change::Change(int index, int count, int moveId, int
      #      offset)
      self._noteCreation(QQmlChangeSet.Change, lambda: Rituals.call(
          'ritual_ZN13QQmlChangeSet6ChangeC1Eiiii',
          index, count, moveId, offset,
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

    @staticmethod
    def moveKey(*__, **_) -> Never:
      """
      Qt's 'MoveKey QQmlChangeSet::Change::moveKey(int index) const': gives
      'QQmlChangeSet::MoveKey', which stands beside this class inside
      'QQmlChangeSet' and cannot be named from here.
      """
      raise NotImplementedError(
          "'QQmlChangeSet.Change.moveKey' has no cute function yet. Qt's "
          "'MoveKey QQmlChangeSet::Change::moveKey(int index) const': gives "
          "'QQmlChangeSet::MoveKey', which stands beside this class inside "
          "'QQmlChangeSet' and cannot be named from here.")

  class ChangeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlChangeSet::ChangeData: a plain Python object
    standing in front of one C++ QQmlChangeSet::ChangeData.

    C++ hands a QQmlChangeSet::ChangeData around as a copy, so every C++
    QQmlChangeSet::ChangeData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlChangeSet::ChangeData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlChangeSet::ChangeData::~ChangeData()': the destructor: Python
      removes its C++ QQmlChangeSet::ChangeData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlChangeSet::ChangeData is created at the first use, not by
      'QQmlChangeSet::ChangeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlChangeSet::ChangeData back gives a copy the
      ritual made for Python, in a new cute QQmlChangeSet::ChangeData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlChangeSet::ChangeData'

    #  Qt's '~QQmlChangeSet::ChangeData()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlChangeSet::ChangeData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlChangeSet10ChangeDataD1Ev'

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

  class MoveKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlChangeSet::MoveKey: a plain Python object
    standing in front of one C++ QQmlChangeSet::MoveKey.

    C++ hands a QQmlChangeSet::MoveKey around as a copy, so every C++
    QQmlChangeSet::MoveKey behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlChangeSet::MoveKey yet. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlChangeSet::MoveKey::~MoveKey()': the destructor: Python
      removes its C++ QQmlChangeSet::MoveKey by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlChangeSet::MoveKey is created at the first use, not by
      'QQmlChangeSet::MoveKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlChangeSet::MoveKey back gives a copy the ritual
      made for Python, in a new cute QQmlChangeSet::MoveKey.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlChangeSet::MoveKey'

    #  Qt's '~QQmlChangeSet::MoveKey()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlChangeSet::MoveKey behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QQmlChangeSet7MoveKeyD1Ev'

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
      Notes what was given, for Qt's 'QQmlChangeSet::MoveKey::MoveKey()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlchangeset-movekey.html#MoveKey
      """
      #  QQmlChangeSet::MoveKey::MoveKey()
      self._noteCreation(QQmlChangeSet.MoveKey, lambda: Rituals.call(
          'ritual_ZN13QQmlChangeSet7MoveKeyC1Ev',
      ))

    @overload(int, int)
    def __init__(self, moveId: int, offset: int) -> None:
      """
      Notes what was given, for Qt's 'QQmlChangeSet::MoveKey::MoveKey(int
      moveId, int offset)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlchangeset-movekey.html#MoveKey

      Parameters
      ----------

      moveId : int
        Passed on as it is.

      offset : int
        Passed on as it is.
      """
      #  QQmlChangeSet::MoveKey::MoveKey(int moveId, int offset)
      self._noteCreation(QQmlChangeSet.MoveKey, lambda: Rituals.call(
          'ritual_ZN13QQmlChangeSet7MoveKeyC1Eii', moveId, offset,
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
  __qt_class__ = 'QQmlChangeSet'

  #  Qt's '~QQmlChangeSet()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlChangeSet behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QQmlChangeSetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlChangeSet::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#isEmpty
    """
    #  bool QQmlChangeSet::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QQmlChangeSet7isEmptyEv')

  def difference(self) -> int:
    """
    Calls Qt's 'int QQmlChangeSet::difference() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#difference
    """
    #  int QQmlChangeSet::difference() const
    return self.uglySide.call('ritual_ZNK13QQmlChangeSet10differenceEv')

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
    Notes what was given, for Qt's 'QQmlChangeSet::QQmlChangeSet()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#QQmlChangeSet
    """
    #  QQmlChangeSet::QQmlChangeSet()
    self._noteCreation(QQmlChangeSet, lambda: Rituals.call(
        'ritual_ZN13QQmlChangeSetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, changeSet: QQmlChangeSet) -> None:
    """
    Notes what was given, for Qt's 'QQmlChangeSet::QQmlChangeSet(const
    QQmlChangeSet &changeSet)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#QQmlChangeSet

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.
    """
    #  QQmlChangeSet::QQmlChangeSet(const QQmlChangeSet &changeSet)
    self._noteCreation(QQmlChangeSet, lambda: Rituals.call(
        'ritual_ZN13QQmlChangeSetC1ERKS_', self._valueOf(changeSet),
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

  @overload(int, int)
  def insert(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::insert(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlChangeSet::insert(int index, int count)
    self.uglySide.call('ritual_ZN13QQmlChangeSet6insertEii', index, count)

  @overload(int, int)
  def remove(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::remove(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlChangeSet::remove(int index, int count)
    self.uglySide.call('ritual_ZN13QQmlChangeSet6removeEii', index, count)

  @overload(int, int, int, int)
  def move(self, from_: int, to: int, count: int, moveId: int) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::move(int from, int to, int count, int
    moveId)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#move

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.

    count : int
      Passed on as it is.

    moveId : int
      Passed on as it is.
    """
    #  void QQmlChangeSet::move(int from, int to, int count, int moveId)
    self.uglySide.call(
        'ritual_ZN13QQmlChangeSet4moveEiiii', from_, to, count, moveId,
    )

  @overload(int, int)
  def change(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::change(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#change

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlChangeSet::change(int index, int count)
    self.uglySide.call('ritual_ZN13QQmlChangeSet6changeEii', index, count)

  @overload(THIS)
  def apply(self, changeSet: QQmlChangeSet) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::apply(const QQmlChangeSet &changeSet)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#apply

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.
    """
    #  void QQmlChangeSet::apply(const QQmlChangeSet &changeSet)
    self.uglySide.call(
        'ritual_ZN13QQmlChangeSet5applyERKS_', self._valueOf(changeSet),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlChangeSet::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlchangeset.html#clear
    """
    #  void QQmlChangeSet::clear()
    self.uglySide.call('ritual_ZN13QQmlChangeSet5clearEv')

  @staticmethod
  def changes(*__, **_) -> Never:
    """
    Qt's 'const QList<Change> &QQmlChangeSet::changes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlChangeSet.changes' has no cute function yet. Qt's 'const "
        "QList<Change> &QQmlChangeSet::changes() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def inserts(*__, **_) -> Never:
    """
    Qt's 'const QList<Change> &QQmlChangeSet::inserts() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlChangeSet.inserts' has no cute function yet. Qt's 'const "
        "QList<Change> &QQmlChangeSet::inserts() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def removes(*__, **_) -> Never:
    """
    Qt's 'const QList<Change> &QQmlChangeSet::removes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlChangeSet.removes' has no cute function yet. Qt's 'const "
        "QList<Change> &QQmlChangeSet::removes() const': gives a type "
        "Python has no way to take yet.")
