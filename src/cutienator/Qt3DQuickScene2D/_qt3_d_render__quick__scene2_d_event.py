"""
Qt3DRender::Quick::Scene2DEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2devent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Quick::Scene2DEvent to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from ..QtCore import QEvent


class Scene2DEvent(QEvent):
  """
  The cute side of Qt's Qt3DRender::Quick::Scene2DEvent: a plain Python
  object standing in front of one C++ Qt3DRender::Quick::Scene2DEvent.

  It is built on the cute 'QEvent', as Qt's Qt3DRender::Quick::Scene2DEvent
  is built on Qt's QEvent, and has everything that class has.

  C++ hands a Qt3DRender::Quick::Scene2DEvent around as a copy, so every C++
  Qt3DRender::Quick::Scene2DEvent behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's Qt3DRender::Quick::Scene2DEvent yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Quick::Scene2DEvent::~Scene2DEvent()': the destructor:
    Python removes its C++ Qt3DRender::Quick::Scene2DEvent by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Quick::Scene2DEvent is created at the first use, not
    by 'Qt3DRender::Quick::Scene2DEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Quick::Scene2DEvent back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::Quick::Scene2DEvent.
  """

  #  The enums Qt writes inside Qt3DRender::Quick::Scene2DEvent, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DRender::Quick::Scene2DEvent::Type' of Qt, with the 8 names
    Qt gives in it.
    """

    Initialize = Kee[int](1001)
    Render = Kee[int](1002)
    RenderSync = Kee[int](1003)
    Prepare = Kee[int](1004)
    Initialized = Kee[int](1005)
    Rendered = Kee[int](1006)
    Invalidate = Kee[int](1007)
    Quit = Kee[int](1008)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Quick::Scene2DEvent'

  #  A C++ Qt3DRender::Quick::Scene2DEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Quick_Scene2DEvent'

  #  Qt's '~Qt3DRender::Quick::Scene2DEvent()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Quick::Scene2DEvent behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender5Quick12Scene2DEventD1Ev'

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

  @overload(Type)
  def __init__(self, type: Type) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Quick::Scene2DEvent::Scene2DEvent(Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-scene2devent.html#Scene2DEvent

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  Qt3DRender::Quick::Scene2DEvent::Scene2DEvent(Type type)
    self._noteCreation(Scene2DEvent, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender5Quick12Scene2DEventC1ENS1_4TypeE', type.value,
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
