"""
qdesigner_internal::ActionData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/newactiondialog_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class ActionData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::ActionData: a plain Python object
  standing in front of one C++ qdesigner_internal::ActionData.

  C++ hands a qdesigner_internal::ActionData around as a copy, so every C++
  qdesigner_internal::ActionData behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionData that has a ritual and
  that Python can call so far, 3 names in all: 'compare', '__eq__', '__ne__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::ActionData::~ActionData()': the destructor:
    Python removes its C++ qdesigner_internal::ActionData by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionData is created at the first use, not
    by 'qdesigner_internal::ActionData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::ActionData back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::ActionData.
  """

  #  The enums Qt writes inside qdesigner_internal::ActionData, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ChangeMask(CuteNum):
    """
    The enum 'qdesigner_internal::ActionData::ChangeMask' of Qt, with the 7
    names Qt gives in it.
    """

    TextChanged = Kee[int](1)
    NameChanged = Kee[int](2)
    ToolTipChanged = Kee[int](4)
    IconChanged = Kee[int](8)
    CheckableChanged = Kee[int](16)
    KeysequenceChanged = Kee[int](32)
    MenuRoleChanged = Kee[int](64)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionData'

  #  Qt's '~qdesigner_internal::ActionData()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::ActionData behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal10ActionDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def compare(self, rhs: ActionData) -> int:
    """
    Calls Qt's 'unsigned int qdesigner_internal::ActionData::compare(const
    ActionData &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiondata.html#compare

    Parameters
    ----------

    rhs : ActionData
      Passed on as a value: Qt reads the C++ qdesigner_internal::ActionData,
      which stays Python's own.
    """
    #  unsigned int qdesigner_internal::ActionData::compare(const ActionData
    #      &rhs) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionData7compareERKS0_',
        self._valueOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: ActionData) -> bool:
    """
    Calls Qt's 'bool operator==(const ActionData &lhs, const ActionData
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiondata.html#operator==

    Parameters
    ----------

    rhs : ActionData
      Passed on as a value: Qt reads the C++ qdesigner_internal::ActionData,
      which stays Python's own.
    """
    #  bool operator==(const ActionData &lhs, const ActionData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_10ActionDataES2_',
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
  def __ne__(self, rhs: ActionData) -> bool:
    """
    Calls Qt's 'bool operator!=(const ActionData &lhs, const ActionData
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiondata.html#operator!=

    Parameters
    ----------

    rhs : ActionData
      Passed on as a value: Qt reads the C++ qdesigner_internal::ActionData,
      which stays Python's own.
    """
    #  bool operator!=(const ActionData &lhs, const ActionData &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_10ActionDataES2_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
