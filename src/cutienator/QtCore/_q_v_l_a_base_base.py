"""
QVLABaseBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qvarlengtharray.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QVLABaseBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVLABaseBase: a plain Python object standing in front
  of one C++ QVLABaseBase.

  What exists
  -----------

  Every function of Qt's QVLABaseBase that has a ritual and that Python can
  call so far, 4 names in all: 'verify', 'capacity', 'size', 'empty'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVLABaseBase::~QVLABaseBase()': the destructor: Python never
    removes a C++ QVLABaseBase.
  - Qt's 'QVLABaseBase::QVLABaseBase(const QVLABaseBase &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QVLABaseBase::QVLABaseBase(QVLABaseBase &&a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVLABaseBase &QVLABaseBase::operator=(const QVLABaseBase &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVLABaseBase &QVLABaseBase::operator=(QVLABaseBase &&a0)':
    assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QVLABaseBase is created at the first use, not by
    'QVLABaseBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVLABaseBase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVLABaseBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def capacity(self) -> int:
    """
    Calls Qt's 'size_type QVLABaseBase::capacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvlabasebase.html#capacity
    """
    #  size_type QVLABaseBase::capacity() const
    return self.uglySide.call('ritual_ZNK12QVLABaseBase8capacityEv')

  def size(self) -> int:
    """
    Calls Qt's 'size_type QVLABaseBase::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvlabasebase.html#size
    """
    #  size_type QVLABaseBase::size() const
    return self.uglySide.call('ritual_ZNK12QVLABaseBase4sizeEv')

  def empty(self) -> bool:
    """
    Calls Qt's 'bool QVLABaseBase::empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvlabasebase.html#empty
    """
    #  bool QVLABaseBase::empty() const
    return self.uglySide.call('ritual_ZNK12QVLABaseBase5emptyEv')

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
    Notes what was given, for Qt's 'QVLABaseBase::QVLABaseBase()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvlabasebase.html#QVLABaseBase
    """
    #  QVLABaseBase::QVLABaseBase()
    self._noteCreation(QVLABaseBase, lambda: Rituals.call(
        'ritual_ZN12QVLABaseBaseC1Ev',
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

  @overload()
  @overload(int)
  @overload(int, int)
  def verify(self, pos: int = 0, n: int = 1) -> None:
    """
    Calls Qt's 'void QVLABaseBase::verify(qsizetype pos, qsizetype n) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvlabasebase.html#verify

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QVLABaseBase::verify(qsizetype pos, qsizetype n) const
    self.uglySide.call('ritual_ZNK12QVLABaseBase6verifyExx', pos, n)
