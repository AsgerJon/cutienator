"""
QtTaskTree::QSyncTask binding of the Qt C++
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


class QSyncTask(QtTaskTree.ExecutableItem):
  """
  The cute side of Qt's QtTaskTree::QSyncTask: a plain Python object standing
  in front of one C++ QtTaskTree::QSyncTask.

  It is built on the cute 'QtTaskTree::ExecutableItem', as Qt's
  QtTaskTree::QSyncTask is built on Qt's QtTaskTree::ExecutableItem, and has
  everything that class has.

  C++ hands a QtTaskTree::QSyncTask around as a copy, so every C++
  QtTaskTree::QSyncTask behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtTaskTree::QSyncTask yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::QSyncTask::~QSyncTask()': the destructor: Python
    removes its C++ QtTaskTree::QSyncTask by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QtTaskTree::QSyncTask is created at the first use, not by
    'QtTaskTree::QSyncTask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTaskTree::QSyncTask back gives a copy the ritual
    made for Python, in a new cute QtTaskTree::QSyncTask.
  - Each name of Qt's QtTaskTree::QSyncTask that has no cute function yet,
    '__init__', 'wrapHandler', holds a function that raises
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
  __qt_class__ = 'QtTaskTree::QSyncTask'

  #  Qt's '~QtTaskTree::QSyncTask()'. Naming it makes this a value class:
  #  Python owns every C++ QtTaskTree::QSyncTask behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QtTaskTree9QSyncTaskD1Ev'

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
    Qt's 'QtTaskTree::QSyncTask::QSyncTask': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QSyncTask.__init__' has no cute function yet. Qt's "
        "'QtTaskTree::QSyncTask::QSyncTask': a template: a pattern and no "
        "single function.")

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
  def wrapHandler(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::QSyncTask::wrapHandler': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.QSyncTask.wrapHandler' has no cute function yet. Qt's "
        "'QtTaskTree::QSyncTask::wrapHandler': a template: a pattern and no "
        "single function.")
