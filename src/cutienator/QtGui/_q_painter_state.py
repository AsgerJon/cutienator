"""
QPainterState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPainterState to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPaintEngineState

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


class QPainterState(QPaintEngineState):
  """
  The cute side of Qt's QPainterState: a plain Python object standing in
  front of one C++ QPainterState.

  It is built on the cute 'QPaintEngineState', as Qt's QPainterState is built
  on Qt's QPaintEngineState, and has everything that class has.

  C++ hands a QPainterState around as a copy, so every C++ QPainterState
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPainterState that has a ritual and that Python can
  call so far, 1 name in all: 'init'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainterState::~QPainterState()': the destructor: Python removes
    its C++ QPainterState by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPainterState is created at the first use, not by
    'QPainterState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPainterState back gives a copy the ritual made for
    Python, in a new cute QPainterState.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterState'

  #  Qt's '~QPainterState()'. Naming it makes this a value class: Python owns
  #  every C++ QPainterState behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QPainterStateD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPainterState::QPainterState()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainterstate.html#QPainterState
    """
    #  QPainterState::QPainterState()
    self._noteCreation(QPainterState, lambda: Rituals.call(
        'ritual_ZN13QPainterStateC1Ev',
    ))

  @overload(THIS)
  @overload(NoneType)
  def __init__(self, s: Optional[QPainterState]) -> None:
    """
    Notes what was given, for Qt's 'QPainterState::QPainterState(const
    QPainterState *s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainterstate.html#QPainterState

    Parameters
    ----------

    s : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPainterState::QPainterState(const QPainterState *s)
    self._noteCreation(QPainterState, lambda: Rituals.call(
        'ritual_ZN13QPainterStateC1EPKS_', self._addressOf(s),
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

  @overload(QPainter)
  @overload(NoneType)
  def init(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QPainterState::init(QPainter *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterstate.html#init

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPainterState::init(QPainter *p)
    self.uglySide.call(
        'ritual_ZN13QPainterState4initEP8QPainter', self._addressOf(p),
    )
