"""
QtTaskTree::GroupItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class GroupItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::GroupItem: a plain Python object standing
  in front of one C++ QtTaskTree::GroupItem.

  What exists
  -----------

  No function of Qt's QtTaskTree::GroupItem yet. It can be made from Python,
  in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::GroupItem::GroupItem(const GroupItems &children)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::GroupItem::GroupItem(std::initializer_list<GroupItem>
    children)': takes a type Python has no way to hand over yet.
  - Qt's 'GroupItem &QtTaskTree::GroupItem::operator=(const GroupItem
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QtTaskTree::GroupItem::GroupItem(GroupItem &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QtTaskTree::GroupItem::swap(GroupItem &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::GroupItem::GroupItem(Type type)': names the enum
    'QtTaskTree::GroupItem::Type', whose class cannot be named here.
  - Qt's 'QtTaskTree::GroupItem::GroupItem(const GroupData &data)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::GroupItem::GroupItem(const TaskHandler &handler)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QtTaskTree::GroupItem::addChildren(const GroupItems
    &children)': takes a type Python has no way to hand over yet.
  - Qt's 'GroupItem QtTaskTree::GroupItem::groupHandler(const GroupHandler
    &handler)': takes a type Python has no way to hand over yet.
  - Qt's 'TaskHandler QtTaskTree::GroupItem::taskHandler() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree; 1 a template; 1 written with the
  class 'QtTaskTree.

  What to expect
  --------------

  - The C++ QtTaskTree::GroupItem is created at the first use, not by
    'QtTaskTree::GroupItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::GroupItem.
  - Each name of Qt's QtTaskTree::GroupItem that has no cute function yet,
    'addChildren', 'groupHandler', 'swap', 'taskHandler', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::GroupItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(THIS)
  def __init__(self, other: GroupItem) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::GroupItem::GroupItem(const
    GroupItem &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-groupitem.html#GroupItem

    Parameters
    ----------

    other : GroupItem
      Passed on as a value: Qt reads the C++ QtTaskTree::GroupItem, which
      stays Python's own.
    """
    #  QtTaskTree::GroupItem::GroupItem(const GroupItem &other)
    self._noteCreation(GroupItem, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9GroupItemC1ERKS0_', self._valueOf(other),
    ))

  @overload(WAIT['QtTaskTree.Iterator'])
  def __init__(self, loop: QtTaskTree.Iterator) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::GroupItem::GroupItem(const
    Iterator &loop)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-groupitem.html#GroupItem

    Parameters
    ----------

    loop : QtTaskTree.Iterator
      Passed on as a value: Qt reads the C++ QtTaskTree::Iterator, which
      stays Python's own.
    """
    #  QtTaskTree::GroupItem::GroupItem(const Iterator &loop)
    self._noteCreation(GroupItem, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9GroupItemC1ERKNS_8IteratorE',
        self._valueOf(loop),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::GroupItem::GroupItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-groupitem.html#GroupItem
    """
    #  QtTaskTree::GroupItem::GroupItem()
    self._noteCreation(GroupItem, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9GroupItemC1Ev',
    ))

  @overload(WAIT['QtTaskTree.StorageBase'])
  def __init__(self, storage: QtTaskTree.StorageBase) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::GroupItem::GroupItem(const
    StorageBase &storage)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-groupitem.html#GroupItem

    Parameters
    ----------

    storage : QtTaskTree.StorageBase
      Passed on as a value: Qt reads the C++ QtTaskTree::StorageBase, which
      stays Python's own.
    """
    #  QtTaskTree::GroupItem::GroupItem(const StorageBase &storage)
    self._noteCreation(GroupItem, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree9GroupItemC1ERKNS_11StorageBaseE',
        self._valueOf(storage),
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

  @staticmethod
  def addChildren(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::GroupItem::addChildren(const GroupItems
    &children)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.GroupItem.addChildren' has no cute function yet. Qt's "
        "'void QtTaskTree::GroupItem::addChildren(const GroupItems "
        "&children)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def groupHandler(*__, **_) -> Never:
    """
    Qt's 'GroupItem QtTaskTree::GroupItem::groupHandler(const GroupHandler
    &handler)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.GroupItem.groupHandler' has no cute function yet. Qt's "
        "'GroupItem QtTaskTree::GroupItem::groupHandler(const GroupHandler "
        "&handler)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::GroupItem::swap(GroupItem &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.GroupItem.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::GroupItem::swap(GroupItem &other)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def taskHandler(*__, **_) -> Never:
    """
    Qt's 'TaskHandler QtTaskTree::GroupItem::taskHandler() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.GroupItem.taskHandler' has no cute function yet. Qt's "
        "'TaskHandler QtTaskTree::GroupItem::taskHandler() const': gives a "
        "type Python has no way to take yet.")
