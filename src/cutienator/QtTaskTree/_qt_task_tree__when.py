"""
QtTaskTree::When binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class When(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::When: a plain Python object standing in
  front of one C++ QtTaskTree::When.

  What exists
  -----------

  Every function of Qt's QtTaskTree::When that has a ritual and that Python
  can call so far, 1 name in all: '__rshift__'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::When::When(const BarrierKickerGetter &kicker,
    WorkflowPolicy policy)': takes a type Python has no way to hand over yet.
  - Qt's 'When &QtTaskTree::When::operator=(const When &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QtTaskTree::When::When(When &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QtTaskTree::When::swap(When &other)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 a template; 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree.

  What to expect
  --------------

  - The C++ QtTaskTree::When is created at the first use, not by
    'QtTaskTree::When(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::When.
  - Each name of Qt's QtTaskTree::When that has no cute function yet,
    'kickerForSignal', 'swap', holds a function that raises
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
  __qt_class__ = 'QtTaskTree::When'

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

  @overload(WAIT['QtTaskTree.Do'])
  def __rshift__(self, doItem: QtTaskTree.Do) -> QtTaskTree.Group:
    """
    Calls Qt's 'Group operator>>(const When &whenItem, const Do &doItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-when.html#operator>>

    Parameters
    ----------

    doItem : QtTaskTree.Do
      Passed on as a value: Qt reads the C++ QtTaskTree::Do, which stays
      Python's own.

    Returns
    -------

    QtTaskTree.Group
      A new cute QtTaskTree::Group around the copy Qt gave back. Python owns
      it.
    """
    #  Group operator>>(const When &whenItem, const Do &doItem)
    address = Rituals.call(
        'ritual_ZN10QtTaskTreersERKNS_4WhenERKNS_2DoE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(doItem),
    )
    return QtTaskTree.Group._cuteOwning(address)

  @overload.fallback
  def __rshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __init__(self, other: When) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::When::When(const When
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-when.html#When

    Parameters
    ----------

    other : When
      Passed on as a value: Qt reads the C++ QtTaskTree::When, which stays
      Python's own.
    """
    #  QtTaskTree::When::When(const When &other)
    self._noteCreation(When, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree4WhenC1ERKS0_', self._valueOf(other),
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
  def kickerForSignal(*__, **_) -> Never:
    """
    Qt's 'QtTaskTree::When::kickerForSignal': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtTaskTree.When.kickerForSignal' has no cute function yet. Qt's "
        "'QtTaskTree::When::kickerForSignal': a template: a pattern and no "
        "single function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::When::swap(When &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.When.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::When::swap(When &other)': takes a type Python has no "
        "way to hand over yet.")
