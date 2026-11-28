"""
QtTaskTree::ExecutableItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ExecutableItem(QtTaskTree.GroupItem):
  """
  The cute side of Qt's QtTaskTree::ExecutableItem: a plain Python object
  standing in front of one C++ QtTaskTree::ExecutableItem.

  It is built on the cute 'QtTaskTree::GroupItem', as Qt's
  QtTaskTree::ExecutableItem is built on Qt's QtTaskTree::GroupItem, and has
  everything that class has.

  C++ hands a QtTaskTree::ExecutableItem around as a copy, so every C++
  QtTaskTree::ExecutableItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtTaskTree::ExecutableItem that has a ritual and
  that Python can call so far, 1 name in all: 'withLog'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Group
    QtTaskTree::ExecutableItem::withTimeout(std::chrono::milliseconds
    timeout, const std::function<void ()> &handler) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::ExecutableItem::ExecutableItem(const TaskHandler
    &handler)': takes a type Python has no way to hand over yet.
  - Qt's 'Group operator!(const ExecutableItem &item)': an operator Python
    has no name for.
  - Qt's 'Group operator&&(const ExecutableItem &first, const ExecutableItem
    &second)': an operator Python has no name for.
  - Qt's 'Group operator||(const ExecutableItem &first, const ExecutableItem
    &second)': an operator Python has no name for.
  - Qt's 'Group operator&&(const ExecutableItem &item, DoneResult result)':
    an operator Python has no name for.
  - Qt's 'Group operator||(const ExecutableItem &item, DoneResult result)':
    an operator Python has no name for.
  - Qt's 'Group QtTaskTree::ExecutableItem::withCancelImpl(const
    ConnectWrapper &connectWrapper, const GroupItems &postCancelRecipe)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'Group QtTaskTree::ExecutableItem::withAcceptImpl(const
    ConnectWrapper &connectWrapper) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QtTaskTree::ExecutableItem::~ExecutableItem()': the destructor:
    Python removes its C++ QtTaskTree::ExecutableItem by it, and has no other
    use for it.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QtTaskTree::ExecutableItem is created at the first use, not by
    'QtTaskTree::ExecutableItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTaskTree::ExecutableItem back gives a copy the
    ritual made for Python, in a new cute QtTaskTree::ExecutableItem.
  - Each name of Qt's QtTaskTree::ExecutableItem that has no cute function
    yet, 'connectWrapper', 'withAccept', 'withAcceptImpl', 'withCancel',
    'withCancelImpl', 'withTimeout', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::ExecutableItem'

  #  Qt's '~QtTaskTree::ExecutableItem()'. Naming it makes this a value
  #  class: Python owns every C++ QtTaskTree::ExecutableItem behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QtTaskTree14ExecutableItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def withLog(self, logName: str) -> QtTaskTree.Group:
    """
    Calls Qt's 'Group QtTaskTree::ExecutableItem::withLog(const QString
    &logName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-executableitem.html#withLog

    Parameters
    ----------

    logName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QtTaskTree.Group
      A new cute QtTaskTree::Group around the copy Qt gave back. Python owns
      it.
    """
    #  Group QtTaskTree::ExecutableItem::withLog(const QString &logName)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree14ExecutableItem7withLogERK7QString', logName,
    )
    return QtTaskTree.Group._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QtTaskTree::ExecutableItem::ExecutableItem()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-executableitem.html#ExecutableItem
    """
    #  QtTaskTree::ExecutableItem::ExecutableItem()
    self._noteCreation(ExecutableItem, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree14ExecutableItemC1Ev',
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
  def connectWrapper(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::ExecutableItem::connectWrapper': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.connectWrapper' has no cute function "
        "yet. Qt's 'QtTaskTree::ExecutableItem::connectWrapper': a "
        "template: a pattern and no single function.")

  @staticmethod
  def withAccept(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::ExecutableItem::withAccept': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.withAccept' has no cute function yet. "
        "Qt's 'QtTaskTree::ExecutableItem::withAccept': a template: a "
        "pattern and no single function.")

  @staticmethod
  def withAcceptImpl(*__, **_) -> Never:
    """
    Qt's 'Group QtTaskTree::ExecutableItem::withAcceptImpl(const
    ConnectWrapper &connectWrapper) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.withAcceptImpl' has no cute function "
        "yet. Qt's 'Group QtTaskTree::ExecutableItem::withAcceptImpl(const "
        "ConnectWrapper &connectWrapper) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def withCancel(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::ExecutableItem::withCancel': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.withCancel' has no cute function yet. "
        "Qt's 'QtTaskTree::ExecutableItem::withCancel': a template: a "
        "pattern and no single function.")

  @staticmethod
  def withCancelImpl(*__, **_) -> Never:
    """
    Qt's 'Group QtTaskTree::ExecutableItem::withCancelImpl(const
    ConnectWrapper &connectWrapper, const GroupItems &postCancelRecipe)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.withCancelImpl' has no cute function "
        "yet. Qt's 'Group QtTaskTree::ExecutableItem::withCancelImpl(const "
        "ConnectWrapper &connectWrapper, const GroupItems "
        "&postCancelRecipe) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def withTimeout(*__, **_) -> Never:
    """
    Qt's 'Group
    QtTaskTree::ExecutableItem::withTimeout(std::chrono::milliseconds
    timeout, const std::function<void ()> &handler) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.ExecutableItem.withTimeout' has no cute function yet. "
        "Qt's 'Group "
        "QtTaskTree::ExecutableItem::withTimeout(std::chrono::milliseconds "
        "timeout, const std::function<void ()> &handler) const': takes a "
        "type Python has no way to hand over yet.")
