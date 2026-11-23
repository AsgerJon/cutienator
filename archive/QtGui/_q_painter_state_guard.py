"""
QPainterStateGuard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpainterstateguard.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPainterStateGuard(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterStateGuard: a plain Python object standing in
  front of one C++ QPainterStateGuard.

  What exists
  -----------

  Every function of Qt's QPainterStateGuard that has a ritual and that Python
  can call so far, 3 names in all: 'save', 'restore', 'verifyPainter'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainterStateGuard::~QPainterStateGuard()': the destructor: Python
    never removes a C++ QPainterStateGuard.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QPainterStateGuard is created at the first use, not by
    'QPainterStateGuard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPainterStateGuard.
  """

  #  The enums Qt writes inside QPainterStateGuard, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class InitialState(CuteNum, scoped=True):
    """
    The enum 'QPainterStateGuard::InitialState' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Save = Kee[int](0)
    NoSave = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterStateGuard'

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

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, InitialState)
  @overload(NoneType, InitialState)
  def __init__(
      self,
      painter: Optional[QPainter],
      state: InitialState = InitialState.Save,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPainterStateGuard::QPainterStateGuard(QPainter *painter, InitialState
    state)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterstateguard.html#QPainterStateGuard

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : InitialState
      Passed on as its number. May be left out, as in Qt: it is then
      InitialState.Save.
    """
    #  QPainterStateGuard::QPainterStateGuard(QPainter *painter, InitialState
    #      state)
    self._noteCreation(QPainterStateGuard, lambda: Rituals.call(
        'ritual_ZN18QPainterStateGuardC1EP8QPainterNS_12InitialStateE',
        self._addressOf(painter), state.value,
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

  def save(self) -> None:
    """
    Calls Qt's 'void QPainterStateGuard::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterstateguard.html#save
    """
    #  void QPainterStateGuard::save()
    self.uglySide.call('ritual_ZN18QPainterStateGuard4saveEv')

  def restore(self) -> None:
    """
    Calls Qt's 'void QPainterStateGuard::restore()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterstateguard.html#restore
    """
    #  void QPainterStateGuard::restore()
    self.uglySide.call('ritual_ZN18QPainterStateGuard7restoreEv')

  def verifyPainter(self) -> None:
    """
    Calls Qt's 'void QPainterStateGuard::verifyPainter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterstateguard.html#verifyPainter
    """
    #  void QPainterStateGuard::verifyPainter()
    self.uglySide.call('ritual_ZN18QPainterStateGuard13verifyPainterEv')
