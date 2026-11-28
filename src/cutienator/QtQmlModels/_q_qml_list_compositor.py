"""
QQmlListCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlListCompositor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlListCompositor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlListCompositor: a plain Python object standing in
  front of one C++ QQmlListCompositor.

  C++ hands a QQmlListCompositor around as a copy, so every C++
  QQmlListCompositor behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlListCompositor that has a ritual and that Python
  can call so far, 9 names in all: 'defaultGroups', 'setDefaultGroups',
  'setDefaultGroup', 'clearDefaultGroup', 'setRemoveGroups', 'setGroupCount',
  'count', 'end', 'erase'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlListCompositor::~QQmlListCompositor()': the destructor: Python
    removes its C++ QQmlListCompositor by it, and has no other use for it.
  - Qt's 'void QQmlListCompositor::transition(Group from, Group to,
    QList<QQmlChangeSet::Change> *removes, QList<QQmlChangeSet::Change>
    *inserts)': names 'QList<QQmlChangeSet::Change>', which has no cute class
    yet.
  - Qt's 'Range *QQmlListCompositor::insert(Range *before, void *list, int
    index, int count, uint flags)': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  25 of the 38 functions Qt declares: 18 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 6 leans on
  'QQmlListCompositor; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlListCompositor is created at the first use, not by
    'QQmlListCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlListCompositor back gives a copy the ritual made
    for Python, in a new cute QQmlListCompositor.
  - Each name of Qt's QQmlListCompositor that has no cute function yet,
    'append', 'clear', 'clearFlags', 'find', 'findInsertPosition', 'insert',
    'listItemsChanged', 'listItemsInserted', 'listItemsMoved',
    'listItemsRemoved', 'move', 'setFlags', 'transition', 'verifyMoveTo',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQmlListCompositor, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteNum):
    """
    The enum 'QQmlListCompositor::Flag' of Qt, with the 8 names Qt gives in
    it.
    """

    CacheFlag = Kee[int](1)
    DefaultFlag = Kee[int](2)
    PersistedFlag = Kee[int](4)
    PrependFlag = Kee[int](268435456)
    AppendFlag = Kee[int](536870912)
    UnresolvedFlag = Kee[int](1073741824)
    MovedFlag = Kee[int](2147483648)
    GroupMask = Kee[int](268435454)

  class Group(CuteNum):
    """
    The enum 'QQmlListCompositor::Group' of Qt, with the 3 names Qt gives in
    it.
    """

    Cache = Kee[int](0)
    Default = Kee[int](1)
    Persisted = Kee[int](2)

  #  The classes Qt writes inside QQmlListCompositor, each a class in here as
  #  in C++.

  class Change(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlListCompositor::Change: a plain Python object
    standing in front of one C++ QQmlListCompositor::Change.

    C++ hands a QQmlListCompositor::Change around as a copy, so every C++
    QQmlListCompositor::Change behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlListCompositor::Change that has a ritual and
    that Python can call so far, 6 names in all: 'cacheIndex',
    'setCacheIndex', 'isMove', 'inCache', 'inGroup', 'groups'. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::Change::Change(const iterator &it, int count,
      uint flags, int moveId)': names 'QQmlListCompositor::iterator', which
      stands beside this class inside 'QQmlListCompositor' and cannot be
      named from here.
    - Qt's 'QQmlListCompositor::Change::~Change()': the destructor: Python
      removes its C++ QQmlListCompositor::Change by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlListCompositor::Change is created at the first use, not by
      'QQmlListCompositor::Change(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::Change back gives a copy the
      ritual made for Python, in a new cute QQmlListCompositor::Change.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::Change'

    #  Qt's '~QQmlListCompositor::Change()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlListCompositor::Change behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor6ChangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def cacheIndex(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::Change::cacheIndex() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#cacheIndex
      """
      #  int QQmlListCompositor::Change::cacheIndex() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change10cacheIndexEv',
      )

    def isMove(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Change::isMove() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#isMove
      """
      #  bool QQmlListCompositor::Change::isMove() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change6isMoveEv',
      )

    def inCache(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Change::inCache() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#inCache
      """
      #  bool QQmlListCompositor::Change::inCache() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change7inCacheEv',
      )

    @overload()
    def inGroup(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Change::inGroup() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#inGroup
      """
      #  bool QQmlListCompositor::Change::inGroup() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change7inGroupEv',
      )

    @overload(int)
    def inGroup(self, group: int) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Change::inGroup(int group) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#inGroup

      Parameters
      ----------

      group : int
        Passed on as it is.
      """
      #  bool QQmlListCompositor::Change::inGroup(int group) const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change7inGroupEi', group,
      )

    def groups(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::Change::groups() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#groups
      """
      #  int QQmlListCompositor::Change::groups() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor6Change6groupsEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def setCacheIndex(self, cacheIndex: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::Change::setCacheIndex(int
      cacheIndex)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#setCacheIndex

      Parameters
      ----------

      cacheIndex : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::Change::setCacheIndex(int cacheIndex)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor6Change13setCacheIndexEi',
          cacheIndex,
      )

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
      Notes what was given, for Qt's 'QQmlListCompositor::Change::Change()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-change.html#Change
      """
      #  QQmlListCompositor::Change::Change()
      self._noteCreation(QQmlListCompositor.Change, lambda: Rituals.call(
          'ritual_ZN18QQmlListCompositor6ChangeC1Ev',
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

  class Insert(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlListCompositor::Insert: a plain Python object
    standing in front of one C++ QQmlListCompositor::Insert.

    C++ hands a QQmlListCompositor::Insert around as a copy, so every C++
    QQmlListCompositor::Insert behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlListCompositor::Insert yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::Insert::Insert(const iterator &it, int count,
      uint flags, int moveId)': names 'QQmlListCompositor::iterator', which
      stands beside this class inside 'QQmlListCompositor' and cannot be
      named from here.
    - Qt's 'QQmlListCompositor::Insert::~Insert()': the destructor: Python
      removes its C++ QQmlListCompositor::Insert by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlListCompositor::Insert is created at the first use, not by
      'QQmlListCompositor::Insert(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::Insert back gives a copy the
      ritual made for Python, in a new cute QQmlListCompositor::Insert.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::Insert'

    #  Qt's '~QQmlListCompositor::Insert()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlListCompositor::Insert behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor6InsertD1Ev'

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
      Notes what was given, for Qt's 'QQmlListCompositor::Insert::Insert()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-insert.html#Insert
      """
      #  QQmlListCompositor::Insert::Insert()
      self._noteCreation(QQmlListCompositor.Insert, lambda: Rituals.call(
          'ritual_ZN18QQmlListCompositor6InsertC1Ev',
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

  class Range(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlListCompositor::Range: a plain Python object
    standing in front of one C++ QQmlListCompositor::Range.

    C++ hands a QQmlListCompositor::Range around as a copy, so every C++
    QQmlListCompositor::Range behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlListCompositor::Range that has a ritual and
    that Python can call so far, 8 names in all: 'start', 'end', 'groups',
    'inGroup', 'inCache', 'isUnresolved', 'prepend', 'append'. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::Range::Range(Range *next, void *list, int
      index, int count, uint flags)': names 'void', which has no cute class
      yet.
    - Qt's 'QQmlListCompositor::Range::~Range()': the destructor: Python
      removes its C++ QQmlListCompositor::Range by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlListCompositor::Range is created at the first use, not by
      'QQmlListCompositor::Range(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::Range back gives a copy the
      ritual made for Python, in a new cute QQmlListCompositor::Range.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::Range'

    #  Qt's '~QQmlListCompositor::Range()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlListCompositor::Range behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor5RangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def start(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::Range::start() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#start
      """
      #  int QQmlListCompositor::Range::start() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range5startEv',
      )

    def end(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::Range::end() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#end
      """
      #  int QQmlListCompositor::Range::end() const
      return self.uglySide.call('ritual_ZNK18QQmlListCompositor5Range3endEv')

    def groups(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::Range::groups() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#groups
      """
      #  int QQmlListCompositor::Range::groups() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range6groupsEv',
      )

    @overload()
    def inGroup(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::inGroup() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#inGroup
      """
      #  bool QQmlListCompositor::Range::inGroup() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range7inGroupEv',
      )

    @overload(int)
    def inGroup(self, group: int) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::inGroup(int group) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#inGroup

      Parameters
      ----------

      group : int
        Passed on as it is.
      """
      #  bool QQmlListCompositor::Range::inGroup(int group) const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range7inGroupEi', group,
      )

    def inCache(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::inCache() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#inCache
      """
      #  bool QQmlListCompositor::Range::inCache() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range7inCacheEv',
      )

    def isUnresolved(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::isUnresolved() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#isUnresolved
      """
      #  bool QQmlListCompositor::Range::isUnresolved() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range12isUnresolvedEv',
      )

    def prepend(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::prepend() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#prepend
      """
      #  bool QQmlListCompositor::Range::prepend() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range7prependEv',
      )

    def append(self) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::Range::append() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#append
      """
      #  bool QQmlListCompositor::Range::append() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor5Range6appendEv',
      )

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
      Notes what was given, for Qt's 'QQmlListCompositor::Range::Range()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-range.html#Range
      """
      #  QQmlListCompositor::Range::Range()
      self._noteCreation(QQmlListCompositor.Range, lambda: Rituals.call(
          'ritual_ZN18QQmlListCompositor5RangeC1Ev',
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

  class Remove(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlListCompositor::Remove: a plain Python object
    standing in front of one C++ QQmlListCompositor::Remove.

    C++ hands a QQmlListCompositor::Remove around as a copy, so every C++
    QQmlListCompositor::Remove behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlListCompositor::Remove yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::Remove::Remove(const iterator &it, int count,
      uint flags, int moveId)': names 'QQmlListCompositor::iterator', which
      stands beside this class inside 'QQmlListCompositor' and cannot be
      named from here.
    - Qt's 'QQmlListCompositor::Remove::~Remove()': the destructor: Python
      removes its C++ QQmlListCompositor::Remove by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlListCompositor::Remove is created at the first use, not by
      'QQmlListCompositor::Remove(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::Remove back gives a copy the
      ritual made for Python, in a new cute QQmlListCompositor::Remove.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::Remove'

    #  Qt's '~QQmlListCompositor::Remove()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlListCompositor::Remove behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor6RemoveD1Ev'

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
      Notes what was given, for Qt's 'QQmlListCompositor::Remove::Remove()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-remove.html#Remove
      """
      #  QQmlListCompositor::Remove::Remove()
      self._noteCreation(QQmlListCompositor.Remove, lambda: Rituals.call(
          'ritual_ZN18QQmlListCompositor6RemoveC1Ev',
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

  class insert_iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlListCompositor::insert_iterator: a plain Python
    object standing in front of one C++ QQmlListCompositor::insert_iterator.

    C++ hands a QQmlListCompositor::insert_iterator around as a copy, so
    every C++ QQmlListCompositor::insert_iterator behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlListCompositor::insert_iterator that has a
    ritual and that Python can call so far, 1 name in all: '__iadd__'. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::insert_iterator::insert_iterator(const
      iterator &it)': names 'QQmlListCompositor::iterator', which stands
      beside this class inside 'QQmlListCompositor' and cannot be named from
      here.
    - Qt's 'QQmlListCompositor::insert_iterator::insert_iterator(Range *a0,
      int a1, Group a2, int a3)': names 'QQmlListCompositor::Range', which
      stands beside this class inside 'QQmlListCompositor' and cannot be
      named from here.
    - Qt's 'QQmlListCompositor::insert_iterator::~insert_iterator()': the
      destructor: Python removes its C++ QQmlListCompositor::insert_iterator
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlListCompositor::insert_iterator is created at the first
      use, not by 'QQmlListCompositor::insert_iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::insert_iterator back gives a
      copy the ritual made for Python, in a new cute
      QQmlListCompositor::insert_iterator.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::insert_iterator'

    #  Qt's '~QQmlListCompositor::insert_iterator()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlListCompositor::insert_iterator
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor15insert_iteratorD1Ev'

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
    def __iadd__(
        self,
        difference: int,
    ) -> QQmlListCompositor.insert_iterator:
      """
      Calls Qt's 'insert_iterator
      &QQmlListCompositor::insert_iterator::operator+=(int difference)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-insert_iterator.html

      Parameters
      ----------

      difference : int
        Passed on as it is.
      """
      #  insert_iterator &QQmlListCompositor::insert_iterator::operator+=(int
      #      difference)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor15insert_iteratorpLEi', difference,
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlListCompositor::insert_iterator::insert_iterator()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-insert_iterator.html
      """
      #  QQmlListCompositor::insert_iterator::insert_iterator()
      self._noteCreation(
          QQmlListCompositor.insert_iterator, lambda: Rituals.call(
              'ritual_ZN18QQmlListCompositor15insert_iteratorC1Ev',
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
    The cute side of Qt's QQmlListCompositor::iterator: a plain Python object
    standing in front of one C++ QQmlListCompositor::iterator.

    C++ hands a QQmlListCompositor::iterator around as a copy, so every C++
    QQmlListCompositor::iterator behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlListCompositor::iterator that has a ritual and
    that Python can call so far, 8 names in all: '__eq__', '__ne__',
    '__iadd__', 'modelIndex', 'incrementIndexes', 'decrementIndexes',
    'cacheIndex', 'setCacheIndex'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlListCompositor::iterator::iterator(Range *range, int offset,
      Group group, int groupCount)': names 'QQmlListCompositor::Range', which
      stands beside this class inside 'QQmlListCompositor' and cannot be
      named from here.
    - Qt's 'bool QQmlListCompositor::iterator::operator==(Group group)
      const': names the enum 'QQmlListCompositor::Group', whose class cannot
      be named here.
    - Qt's 'bool QQmlListCompositor::iterator::operator!=(Group group)
      const': names the enum 'QQmlListCompositor::Group', whose class cannot
      be named here.
    - Qt's 'Range *const &QQmlListCompositor::iterator::operator*() const':
      an operator Python has no name for.
    - Qt's 'Range *QQmlListCompositor::iterator::operator->()': an operator
      Python has no name for.
    - Qt's 'const Range *QQmlListCompositor::iterator::operator->() const':
      an operator Python has no name for.
    - Qt's 'void QQmlListCompositor::iterator::setGroup(Group g)': names the
      enum 'QQmlListCompositor::Group', whose class cannot be named here.
    - Qt's 'QQmlListCompositor::iterator::~iterator()': the destructor:
      Python removes its C++ QQmlListCompositor::iterator by it, and has no
      other use for it.

    What has no ritual
    ------------------

    2 of the 21 functions Qt declares: 1 takes or gives a type that cannot be
    passed yet; 1 a template.

    What to expect
    --------------

    - The C++ QQmlListCompositor::iterator is created at the first use, not
      by 'QQmlListCompositor::iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlListCompositor::iterator back gives a copy the
      ritual made for Python, in a new cute QQmlListCompositor::iterator.
    - Each name of Qt's QQmlListCompositor::iterator that has no cute
      function yet, 'list', 'setGroup', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlListCompositor::iterator'

    #  Qt's '~QQmlListCompositor::iterator()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlListCompositor::iterator behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QQmlListCompositor8iteratorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def modelIndex(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::iterator::modelIndex() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#modelIndex
      """
      #  int QQmlListCompositor::iterator::modelIndex() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor8iterator10modelIndexEv',
      )

    def cacheIndex(self) -> int:
      """
      Calls Qt's 'int QQmlListCompositor::iterator::cacheIndex() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#cacheIndex
      """
      #  int QQmlListCompositor::iterator::cacheIndex() const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor8iterator10cacheIndexEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def setCacheIndex(self, cacheIndex: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::iterator::setCacheIndex(int
      cacheIndex)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#setCacheIndex

      Parameters
      ----------

      cacheIndex : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::iterator::setCacheIndex(int cacheIndex)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iterator13setCacheIndexEi',
          cacheIndex,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, it: QQmlListCompositor.iterator) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::iterator::operator==(const
      iterator &it) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#operator==

      Parameters
      ----------

      it : QQmlListCompositor.iterator
        Passed on as a value: Qt reads the C++ QQmlListCompositor::iterator,
        which stays Python's own.
      """
      #  bool QQmlListCompositor::iterator::operator==(const iterator &it)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor8iteratoreqERKS0_',
          self._valueOf(it),
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
    def __ne__(self, it: QQmlListCompositor.iterator) -> bool:
      """
      Calls Qt's 'bool QQmlListCompositor::iterator::operator!=(const
      iterator &it) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#operator!=

      Parameters
      ----------

      it : QQmlListCompositor.iterator
        Passed on as a value: Qt reads the C++ QQmlListCompositor::iterator,
        which stays Python's own.
      """
      #  bool QQmlListCompositor::iterator::operator!=(const iterator &it)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QQmlListCompositor8iteratorneERKS0_',
          self._valueOf(it),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(int)
    def __iadd__(self, difference: int) -> QQmlListCompositor.iterator:
      """
      Calls Qt's 'iterator &QQmlListCompositor::iterator::operator+=(int
      difference)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#operator+=

      Parameters
      ----------

      difference : int
        Passed on as it is.
      """
      #  iterator &QQmlListCompositor::iterator::operator+=(int difference)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iteratorpLEi', difference,
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlListCompositor::iterator::iterator()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html#iterator
      """
      #  QQmlListCompositor::iterator::iterator()
      self._noteCreation(QQmlListCompositor.iterator, lambda: Rituals.call(
          'ritual_ZN18QQmlListCompositor8iteratorC1Ev',
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

    @overload(int)
    def incrementIndexes(self, difference: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::iterator::incrementIndexes(int
      difference)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html

      Parameters
      ----------

      difference : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::iterator::incrementIndexes(int difference)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEi',
          difference,
      )

    @overload(int, int)
    def incrementIndexes(self, difference: int, flags: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::iterator::incrementIndexes(int
      difference, uint flags)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html

      Parameters
      ----------

      difference : int
        Passed on as it is.

      flags : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::iterator::incrementIndexes(int difference,
      #      uint flags)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEij',
          difference, flags,
      )

    @overload(int)
    def decrementIndexes(self, difference: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::iterator::decrementIndexes(int
      difference)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html

      Parameters
      ----------

      difference : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::iterator::decrementIndexes(int difference)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEi',
          difference,
      )

    @overload(int, int)
    def decrementIndexes(self, difference: int, flags: int) -> None:
      """
      Calls Qt's 'void QQmlListCompositor::iterator::decrementIndexes(int
      difference, uint flags)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmllistcompositor-iterator.html

      Parameters
      ----------

      difference : int
        Passed on as it is.

      flags : int
        Passed on as it is.
      """
      #  void QQmlListCompositor::iterator::decrementIndexes(int difference,
      #      uint flags)
      self.uglySide.call(
          'ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEij',
          difference, flags,
      )

    @staticmethod
    def list(*__, **_) -> Never:
      """
      Qt's 'QQmlListCompositor::iterator::list': a template: a pattern and no
      single function.
      """
      raise NotImplementedError(
          "'QQmlListCompositor.iterator.list' has no cute function yet. "
          "Qt's 'QQmlListCompositor::iterator::list': a template: a pattern "
          "and no single function.")

    @staticmethod
    def setGroup(*__, **_) -> Never:
      """
      Qt's 'void QQmlListCompositor::iterator::setGroup(Group g)': names the
      enum 'QQmlListCompositor::Group', whose class cannot be named here.
      """
      raise NotImplementedError(
          "'QQmlListCompositor.iterator.setGroup' has no cute function yet. "
          "Qt's 'void QQmlListCompositor::iterator::setGroup(Group g)': "
          "names the enum 'QQmlListCompositor::Group', whose class cannot "
          "be named here.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlListCompositor'

  #  Qt's '~QQmlListCompositor()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlListCompositor behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlListCompositorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultGroups(self) -> int:
    """
    Calls Qt's 'int QQmlListCompositor::defaultGroups() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#defaultGroups
    """
    #  int QQmlListCompositor::defaultGroups() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlListCompositor13defaultGroupsEv',
    )

  @overload(Group)
  def count(self, group: Group) -> int:
    """
    Calls Qt's 'int QQmlListCompositor::count(Group group) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistcompositor.html#count

    Parameters
    ----------

    group : Group
      Passed on as its number.
    """
    #  int QQmlListCompositor::count(Group group) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlListCompositor5countENS_5GroupE', group.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDefaultGroups(self, groups: int) -> None:
    """
    Calls Qt's 'void QQmlListCompositor::setDefaultGroups(int groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#setDefaultGroups

    Parameters
    ----------

    groups : int
      Passed on as it is.
    """
    #  void QQmlListCompositor::setDefaultGroups(int groups)
    self.uglySide.call(
        'ritual_ZN18QQmlListCompositor16setDefaultGroupsEi', groups,
    )

  @overload(Group)
  def setDefaultGroup(self, group: Group) -> None:
    """
    Calls Qt's 'void QQmlListCompositor::setDefaultGroup(Group group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#setDefaultGroup

    Parameters
    ----------

    group : Group
      Passed on as its number.
    """
    #  void QQmlListCompositor::setDefaultGroup(Group group)
    self.uglySide.call(
        'ritual_ZN18QQmlListCompositor15setDefaultGroupENS_5GroupE',
        group.value,
    )

  @overload(int)
  def setRemoveGroups(self, groups: int) -> None:
    """
    Calls Qt's 'void QQmlListCompositor::setRemoveGroups(int groups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#setRemoveGroups

    Parameters
    ----------

    groups : int
      Passed on as it is.
    """
    #  void QQmlListCompositor::setRemoveGroups(int groups)
    self.uglySide.call(
        'ritual_ZN18QQmlListCompositor15setRemoveGroupsEi', groups,
    )

  @overload(int)
  def setGroupCount(self, count: int) -> None:
    """
    Calls Qt's 'void QQmlListCompositor::setGroupCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#setGroupCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQmlListCompositor::setGroupCount(int count)
    self.uglySide.call(
        'ritual_ZN18QQmlListCompositor13setGroupCountEi', count,
    )

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
    Notes what was given, for Qt's
    'QQmlListCompositor::QQmlListCompositor()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#QQmlListCompositor
    """
    #  QQmlListCompositor::QQmlListCompositor()
    self._noteCreation(QQmlListCompositor, lambda: Rituals.call(
        'ritual_ZN18QQmlListCompositorC1Ev',
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

  @overload(Group)
  def clearDefaultGroup(self, group: Group) -> None:
    """
    Calls Qt's 'void QQmlListCompositor::clearDefaultGroup(Group group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllistcompositor.html#clearDefaultGroup

    Parameters
    ----------

    group : Group
      Passed on as its number.
    """
    #  void QQmlListCompositor::clearDefaultGroup(Group group)
    self.uglySide.call(
        'ritual_ZN18QQmlListCompositor17clearDefaultGroupENS_5GroupE',
        group.value,
    )

  def end(self) -> iterator:
    """
    Calls Qt's 'const iterator &QQmlListCompositor::end()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistcompositor.html#end

    Returns
    -------

    iterator
      A new cute QQmlListCompositor::iterator around the copy Qt gave back.
      Python owns it.
    """
    #  const iterator &QQmlListCompositor::end()
    address = self.uglySide.call('ritual_ZN18QQmlListCompositor3endEv')
    return QQmlListCompositor.iterator._cuteOwning(address)

  @overload(Range)
  @overload(NoneType)
  def erase(self, range: Optional[Range]) -> Optional[Range]:
    """
    Calls Qt's 'Range *QQmlListCompositor::erase(Range *range)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllistcompositor.html#erase

    Parameters
    ----------

    range : Optional[Range]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Range]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Range *QQmlListCompositor::erase(Range *range)
    address = self.uglySide.call(
        'ritual_ZN18QQmlListCompositor5eraseEPNS_5RangeE',
        self._addressOf(range),
    )
    return QQmlListCompositor.Range._cuteAt(address)

  @staticmethod
  def append(*__, **_) -> Never:
    """
    Qt's 'void QQmlListCompositor::append(void *list, int index, int count,
    uint flags, QList<Insert> *inserts)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.append' has no cute function yet. Qt's 'void "
        "QQmlListCompositor::append(void *list, int index, int count, uint "
        "flags, QList<Insert> *inserts)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "expected expression.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QQmlListCompositor::clear()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file:
    expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.clear' has no cute function yet. Qt's 'void "
        "QQmlListCompositor::clear()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "expected expression.")

  @staticmethod
  def clearFlags(*__, **_) -> Never:
    """
    - Qt's 'void QQmlListCompositor::clearFlags(Group fromGroup, int from,
      int count, Group group, uint flags, QList<Remove> *removals)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: expected expression.
    - Qt's 'void QQmlListCompositor::clearFlags(iterator from, int count,
      Group group, uint flags, QList<Remove> *removals)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: expected expression.
    - Qt's 'void QQmlListCompositor::clearFlags(Group fromGroup, int from,
      int count, uint flags, QList<Remove> *removals)': leans on
      'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, int,
      QQmlListCompositor::Group, unsigned int,
      QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QQmlListCompositor::clearFlags(const iterator &from, int
      count, uint flags, QList<Remove> *removals)': leans on
      'QQmlListCompositor::clearFlags(QQmlListCompositor::iterator, int,
      QQmlListCompositor::Group, unsigned int,
      QList<QQmlListCompositor::Remove>*)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.clearFlags' has no cute function yet. Qt's "
        "'void QQmlListCompositor::clearFlags(Group fromGroup, int from, "
        "int count, Group group, uint flags, QList<Remove> *removals)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::clearFlags(iterator from, int count, Group "
        "group, uint flags, QList<Remove> *removals)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::clearFlags(Group fromGroup, int from, int "
        "count, uint flags, QList<Remove> *removals)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::Group, int, "
        "int, QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QQmlListCompositor::clearFlags(const iterator "
        "&from, int count, uint flags, QList<Remove> *removals)': leans on "
        "'QQmlListCompositor::clearFlags(QQmlListCompositor::iterator, int, "
        "QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Remove>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def find(*__, **_) -> Never:
    """
    - Qt's 'iterator QQmlListCompositor::find(Group group, int index)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: expected expression.
    - Qt's 'iterator QQmlListCompositor::find(Group group, int index) const':
      leans on 'QQmlListCompositor::find(QQmlListCompositor::Group, int)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.find' has no cute function yet. Qt's 'iterator "
        "QQmlListCompositor::find(Group group, int index)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: expected expression. Qt's 'iterator "
        "QQmlListCompositor::find(Group group, int index) const': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def findInsertPosition(*__, **_) -> Never:
    """
    Qt's 'insert_iterator QQmlListCompositor::findInsertPosition(Group group,
    int index)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.findInsertPosition' has no cute function yet. "
        "Qt's 'insert_iterator QQmlListCompositor::findInsertPosition(Group "
        "group, int index)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: expected "
        "expression.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    - Qt's 'Range *QQmlListCompositor::insert(Range *before, void *list, int
      index, int count, uint flags)': names 'void', which has no cute class
      yet.
    - Qt's 'void QQmlListCompositor::insert(Group group, int before, void
      *list, int index, int count, uint flags, QList<Insert> *inserts)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: expected expression.
    - Qt's 'iterator QQmlListCompositor::insert(iterator before, void *list,
      int index, int count, uint flags, QList<Insert> *inserts)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.insert' has no cute function yet. Qt's 'Range "
        "*QQmlListCompositor::insert(Range *before, void *list, int index, "
        "int count, uint flags)': names 'void', which has no cute class "
        "yet. Qt's 'void QQmlListCompositor::insert(Group group, int "
        "before, void *list, int index, int count, uint flags, "
        "QList<Insert> *inserts)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: expected "
        "expression. Qt's 'iterator QQmlListCompositor::insert(iterator "
        "before, void *list, int index, int count, uint flags, "
        "QList<Insert> *inserts)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: expected "
        "expression.")

  @staticmethod
  def listItemsChanged(*__, **_) -> Never:
    """
    - Qt's 'void QQmlListCompositor::listItemsChanged(void *list, int index,
      int count, QList<Change> *changes)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file:
      expected expression.
    - Qt's 'void QQmlListCompositor::listItemsChanged(QList<Change>
      *translatedChanges, void *list, const QList<QQmlChangeSet::Change>
      &changes)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.listItemsChanged' has no cute function yet. "
        "Qt's 'void QQmlListCompositor::listItemsChanged(void *list, int "
        "index, int count, QList<Change> *changes)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::listItemsChanged(QList<Change> "
        "*translatedChanges, void *list, const QList<QQmlChangeSet::Change> "
        "&changes)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: expected expression.")

  @staticmethod
  def listItemsInserted(*__, **_) -> Never:
    """
    - Qt's 'void QQmlListCompositor::listItemsInserted(void *list, int index,
      int count, QList<Insert> *inserts)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file:
      expected expression.
    - Qt's 'void QQmlListCompositor::listItemsInserted(QList<Insert>
      *translatedInsertions, void *list, const QList<QQmlChangeSet::Change>
      &insertions, const QList<MovedFlags> *movedFlags)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.listItemsInserted' has no cute function yet. "
        "Qt's 'void QQmlListCompositor::listItemsInserted(void *list, int "
        "index, int count, QList<Insert> *inserts)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::listItemsInserted(QList<Insert> "
        "*translatedInsertions, void *list, const "
        "QList<QQmlChangeSet::Change> &insertions, const QList<MovedFlags> "
        "*movedFlags)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: expected "
        "expression.")

  @staticmethod
  def listItemsMoved(*__, **_) -> Never:
    """
    Qt's 'void QQmlListCompositor::listItemsMoved(void *list, int from, int
    to, int count, QList<Remove> *removals, QList<Insert> *inserts)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.listItemsMoved' has no cute function yet. Qt's "
        "'void QQmlListCompositor::listItemsMoved(void *list, int from, int "
        "to, int count, QList<Remove> *removals, QList<Insert> *inserts)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: expected expression.")

  @staticmethod
  def listItemsRemoved(*__, **_) -> Never:
    """
    - Qt's 'void QQmlListCompositor::listItemsRemoved(void *list, int index,
      int count, QList<Remove> *removals)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file:
      expected expression.
    - Qt's 'void QQmlListCompositor::listItemsRemoved(QList<Remove>
      *translatedRemovals, void *list, QList<QQmlChangeSet::Change>
      *removals, QList<QQmlChangeSet::Change> *insertions, QList<MovedFlags>
      *movedFlags)': Qt's library has no name for it, and its code in Qt's
      source does not compile apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.listItemsRemoved' has no cute function yet. "
        "Qt's 'void QQmlListCompositor::listItemsRemoved(void *list, int "
        "index, int count, QList<Remove> *removals)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::listItemsRemoved(QList<Remove> "
        "*translatedRemovals, void *list, QList<QQmlChangeSet::Change> "
        "*removals, QList<QQmlChangeSet::Change> *insertions, "
        "QList<MovedFlags> *movedFlags)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "expected expression.")

  @staticmethod
  def move(*__, **_) -> Never:
    """
    Qt's 'void QQmlListCompositor::move(Group fromGroup, int from, Group
    toGroup, int to, int count, Group group, QList<Remove> *removals,
    QList<Insert> *inserts)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: expected expression.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.move' has no cute function yet. Qt's 'void "
        "QQmlListCompositor::move(Group fromGroup, int from, Group toGroup, "
        "int to, int count, Group group, QList<Remove> *removals, "
        "QList<Insert> *inserts)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: expected "
        "expression.")

  @staticmethod
  def setFlags(*__, **_) -> Never:
    """
    - Qt's 'void QQmlListCompositor::setFlags(Group fromGroup, int from, int
      count, Group group, int flags, QList<Insert> *inserts)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: expected expression.
    - Qt's 'void QQmlListCompositor::setFlags(iterator from, int count, Group
      group, uint flags, QList<Insert> *inserts)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: expected expression.
    - Qt's 'void QQmlListCompositor::setFlags(Group fromGroup, int from, int
      count, uint flags, QList<Insert> *inserts)': leans on
      'QQmlListCompositor::setFlags(QQmlListCompositor::Group, int, int,
      QQmlListCompositor::Group, int, QList<QQmlListCompositor::Insert>*)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'void QQmlListCompositor::setFlags(const iterator from, int count,
      uint flags, QList<Insert> *inserts)': leans on
      'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int,
      QQmlListCompositor::Group, unsigned int,
      QList<QQmlListCompositor::Insert>*)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.setFlags' has no cute function yet. Qt's 'void "
        "QQmlListCompositor::setFlags(Group fromGroup, int from, int count, "
        "Group group, int flags, QList<Insert> *inserts)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::setFlags(iterator from, int count, Group "
        "group, uint flags, QList<Insert> *inserts)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: expected expression. Qt's 'void "
        "QQmlListCompositor::setFlags(Group fromGroup, int from, int count, "
        "uint flags, QList<Insert> *inserts)': leans on "
        "'QQmlListCompositor::setFlags(QQmlListCompositor::Group, int, int, "
        "QQmlListCompositor::Group, int, "
        "QList<QQmlListCompositor::Insert>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QQmlListCompositor::setFlags(const iterator "
        "from, int count, uint flags, QList<Insert> *inserts)': leans on "
        "'QQmlListCompositor::setFlags(QQmlListCompositor::iterator, int, "
        "QQmlListCompositor::Group, unsigned int, "
        "QList<QQmlListCompositor::Insert>*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def transition(*__, **_) -> Never:
    """
    Qt's 'void QQmlListCompositor::transition(Group from, Group to,
    QList<QQmlChangeSet::Change> *removes, QList<QQmlChangeSet::Change>
    *inserts)': names 'QList<QQmlChangeSet::Change>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.transition' has no cute function yet. Qt's "
        "'void QQmlListCompositor::transition(Group from, Group to, "
        "QList<QQmlChangeSet::Change> *removes, "
        "QList<QQmlChangeSet::Change> *inserts)': names "
        "'QList<QQmlChangeSet::Change>', which has no cute class yet.")

  @staticmethod
  def verifyMoveTo(*__, **_) -> Never:
    """
    Qt's 'bool QQmlListCompositor::verifyMoveTo(Group fromGroup, int from,
    Group toGroup, int to, int count, Group group) const': leans on
    'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlListCompositor.verifyMoveTo' has no cute function yet. Qt's "
        "'bool QQmlListCompositor::verifyMoveTo(Group fromGroup, int from, "
        "Group toGroup, int to, int count, Group group) const': leans on "
        "'QQmlListCompositor::find(QQmlListCompositor::Group, int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
