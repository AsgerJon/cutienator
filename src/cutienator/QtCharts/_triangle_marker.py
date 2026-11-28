"""
TriangleMarker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means TriangleMarker to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QPolygonF
  from . import ScatterChartItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ScatterChartItem = WAIT['ScatterChartItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TriangleMarker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's TriangleMarker: a plain Python object standing in
  front of one C++ TriangleMarker.

  What exists
  -----------

  Every function of Qt's TriangleMarker that has a ritual and that Python can
  call so far, 1 name in all: 'polygon'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ TriangleMarker is created at the first use, not by
    'TriangleMarker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ TriangleMarker.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(float)
  @overload(float, float)
  @overload(float, float, float)
  @overload(float, float, float, float)
  def polygon(
      x: float = 0.0,
      y: float = 0.0,
      w: float = 10.0,
      h: float = 10.0,
  ) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF TriangleMarker::polygon(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/trianglemarker.html#polygon

    Parameters
    ----------

    x : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    y : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    w : float
      Passed on as it is. May be left out, as in Qt: it is then 10.0.

    h : float
      Passed on as it is. May be left out, as in Qt: it is then 10.0.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF TriangleMarker::polygon(qreal x, qreal y, qreal w, qreal h)
    address = Rituals.call(
        'ritual_ZN14TriangleMarker7polygonEdddd', x, y, w, h,
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TriangleMarker'

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

  @overload(float, float, float, float, ScatterChartItem)
  @overload(float, float, float, float, NoneType)
  def __init__(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      parent: Optional[ScatterChartItem],
  ) -> None:
    """
    Notes what was given, for Qt's 'TriangleMarker::TriangleMarker(qreal x,
    qreal y, qreal w, qreal h, ScatterChartItem *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/trianglemarker.html#TriangleMarker

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    parent : Optional[ScatterChartItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  TriangleMarker::TriangleMarker(qreal x, qreal y, qreal w, qreal h,
    #      ScatterChartItem *parent)
    self._noteCreation(TriangleMarker, lambda: Rituals.call(
        'ritual_ZN14TriangleMarkerC1EddddP16ScatterChartItem',
        x, y, w, h, self._addressOf(parent),
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
