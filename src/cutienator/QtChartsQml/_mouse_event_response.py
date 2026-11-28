"""
MouseEventResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means MouseEventResponse to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint
  from ..QtCharts import QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MouseEventResponse(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's MouseEventResponse: a plain Python object standing in
  front of one C++ MouseEventResponse.

  C++ hands a MouseEventResponse around as a copy, so every C++
  MouseEventResponse behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's MouseEventResponse yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'MouseEventResponse::~MouseEventResponse()': the destructor: Python
    removes its C++ MouseEventResponse by it, and has no other use for it.

  What to expect
  --------------

  - The C++ MouseEventResponse is created at the first use, not by
    'MouseEventResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a MouseEventResponse back gives a copy the ritual made
    for Python, in a new cute MouseEventResponse.
  """

  #  The enums Qt writes inside MouseEventResponse, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MouseEventType(CuteNum):
    """
    The enum 'MouseEventResponse::MouseEventType' of Qt, with the 7 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Pressed = Kee[int](1)
    Released = Kee[int](2)
    Clicked = Kee[int](3)
    DoubleClicked = Kee[int](4)
    HoverEnter = Kee[int](5)
    HoverLeave = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'MouseEventResponse'

  #  Qt's '~MouseEventResponse()'. Naming it makes this a value class: Python
  #  owns every C++ MouseEventResponse behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18MouseEventResponseD1Ev'

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
    Notes what was given, for Qt's
    'MouseEventResponse::MouseEventResponse()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/mouseeventresponse.html#MouseEventResponse
    """
    #  MouseEventResponse::MouseEventResponse()
    self._noteCreation(MouseEventResponse, lambda: Rituals.call(
        'ritual_ZN18MouseEventResponseC1Ev',
    ))

  @overload(MouseEventType, QPoint, QXYSeries)
  @overload(MouseEventType, QPoint, NoneType)
  def __init__(
      self,
      t: MouseEventType,
      p: QPoint,
      s: Optional[QXYSeries],
  ) -> None:
    """
    Notes what was given, for Qt's
    'MouseEventResponse::MouseEventResponse(MouseEventType t, const QPoint
    &p, const QXYSeries *s)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/mouseeventresponse.html#MouseEventResponse

    Parameters
    ----------

    t : MouseEventType
      Passed on as its number.

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    s : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  MouseEventResponse::MouseEventResponse(MouseEventType t, const QPoint
    #      &p, const QXYSeries *s)
    self._noteCreation(MouseEventResponse, lambda: Rituals.call(
        'ritual_ZN18MouseEventResponseC1ENS_14MouseEventTypeERK6QPointPK9QX'
        'YSeries',
        t.value, self._valueOf(p), self._addressOf(s),
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
