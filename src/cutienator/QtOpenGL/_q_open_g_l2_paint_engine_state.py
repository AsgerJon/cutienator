"""
QOpenGL2PaintEngineState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglpaintengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGL2PaintEngineState to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtGui import QPainterState


class QOpenGL2PaintEngineState(QPainterState):
  """
  The cute side of Qt's QOpenGL2PaintEngineState: a plain Python object
  standing in front of one C++ QOpenGL2PaintEngineState.

  It is built on the cute 'QPainterState', as Qt's QOpenGL2PaintEngineState
  is built on Qt's QPainterState, and has everything that class has.

  C++ hands a QOpenGL2PaintEngineState around as a copy, so every C++
  QOpenGL2PaintEngineState behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QOpenGL2PaintEngineState yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGL2PaintEngineState::~QOpenGL2PaintEngineState()': the
    destructor: Python removes its C++ QOpenGL2PaintEngineState by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGL2PaintEngineState is created at the first use, not by
    'QOpenGL2PaintEngineState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGL2PaintEngineState back gives a copy the ritual
    made for Python, in a new cute QOpenGL2PaintEngineState.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGL2PaintEngineState'

  #  Qt's '~QOpenGL2PaintEngineState()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGL2PaintEngineState behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QOpenGL2PaintEngineStateD1Ev'

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
  def __init__(self, other: QOpenGL2PaintEngineState) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGL2PaintEngineState::QOpenGL2PaintEngineState(const
    QOpenGL2PaintEngineState &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintenginestate.html

    Parameters
    ----------

    other : QOpenGL2PaintEngineState
      Passed on as a value: Qt reads the C++ QOpenGL2PaintEngineState, which
      stays Python's own.
    """
    #  QOpenGL2PaintEngineState::QOpenGL2PaintEngineState(const
    #      QOpenGL2PaintEngineState &other)
    self._noteCreation(QOpenGL2PaintEngineState, lambda: Rituals.call(
        'ritual_ZN24QOpenGL2PaintEngineStateC1ERKS_', self._valueOf(other),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGL2PaintEngineState::QOpenGL2PaintEngineState()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengl2paintenginestate.html
    """
    #  QOpenGL2PaintEngineState::QOpenGL2PaintEngineState()
    self._noteCreation(QOpenGL2PaintEngineState, lambda: Rituals.call(
        'ritual_ZN24QOpenGL2PaintEngineStateC1Ev',
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
