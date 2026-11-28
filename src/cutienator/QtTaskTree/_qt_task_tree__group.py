"""
QtTaskTree::Group binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Group(QtTaskTree.ExecutableItem):
  """
  The cute side of Qt's QtTaskTree::Group: a plain Python object standing in
  front of one C++ QtTaskTree::Group.

  It is built on the cute 'QtTaskTree::ExecutableItem', as Qt's
  QtTaskTree::Group is built on Qt's QtTaskTree::ExecutableItem, and has
  everything that class has.

  C++ hands a QtTaskTree::Group around as a copy, so every C++
  QtTaskTree::Group behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtTaskTree::Group yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::Group::Group(const GroupItems &children)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Group::Group(std::initializer_list<GroupItem>
    children)': takes a type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Group::~Group()': the destructor: Python removes its
    C++ QtTaskTree::Group by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ QtTaskTree::Group is created at the first use, not by
    'QtTaskTree::Group(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTaskTree::Group back gives a copy the ritual made
    for Python, in a new cute QtTaskTree::Group.
  - Each name of Qt's QtTaskTree::Group that has no cute function yet,
    '__init__', 'onGroupDone', 'onGroupSetup', 'wrapGroupDone',
    'wrapGroupSetup', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::Group'

  #  Qt's '~QtTaskTree::Group()'. Naming it makes this a value class: Python
  #  owns every C++ QtTaskTree::Group behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN10QtTaskTree5GroupD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QtTaskTree::Group::Group(const GroupItems &children)': takes a
      type Python has no way to hand over yet.
    - Qt's 'QtTaskTree::Group::Group(std::initializer_list<GroupItem>
      children)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Group.__init__' has no cute function yet. Qt's "
        "'QtTaskTree::Group::Group(const GroupItems &children)': takes a "
        "type Python has no way to hand over yet. Qt's "
        "'QtTaskTree::Group::Group(std::initializer_list<GroupItem> "
        "children)': takes a type Python has no way to hand over yet.")

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
  def onGroupDone(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::Group::onGroupDone': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.Group.onGroupDone' has no cute function yet. Qt's "
        "'QtTaskTree::Group::onGroupDone': a template: a pattern and no "
        "single function.")

  @staticmethod
  def onGroupSetup(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::Group::onGroupSetup': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.Group.onGroupSetup' has no cute function yet. Qt's "
        "'QtTaskTree::Group::onGroupSetup': a template: a pattern and no "
        "single function.")

  @staticmethod
  def wrapGroupDone(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::Group::wrapGroupDone': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.Group.wrapGroupDone' has no cute function yet. Qt's "
        "'QtTaskTree::Group::wrapGroupDone': a template: a pattern and no "
        "single function.")

  @staticmethod
  def wrapGroupSetup(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::Group::wrapGroupSetup': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.Group.wrapGroupSetup' has no cute function yet. Qt's "
        "'QtTaskTree::Group::wrapGroupSetup': a template: a pattern and no "
        "single function.")
