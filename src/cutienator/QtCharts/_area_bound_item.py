"""
AreaBoundItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/areachartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means AreaBoundItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import LineChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import AreaChartItem, QLineSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AreaChartItem = WAIT['AreaChartItem']
  QLineSeries = WAIT['QtCharts:QLineSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AreaBoundItem(LineChartItem):
  """
  The cute side of Qt's AreaBoundItem: a plain Python object standing in
  front of one C++ AreaBoundItem.

  It is built on the cute 'LineChartItem', as Qt's AreaBoundItem is built on
  Qt's LineChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AreaBoundItem that has a ritual and that Python can
  call so far, 1 name in all: 'updateGeometry'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'AreaBoundItem::~AreaBoundItem()': the destructor: Python never
    removes a C++ AreaBoundItem.

  What to expect
  --------------

  - The C++ AreaBoundItem is created at the first use, not by
    'AreaBoundItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AreaBoundItem.
  - Qt tells when it has removed the C++ AreaBoundItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AreaBoundItem'

  #  A C++ AreaBoundItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AreaBoundItem'

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

  @overload(AreaChartItem, QLineSeries)
  @overload(AreaChartItem, NoneType)
  @overload(NoneType, QLineSeries)
  @overload(NoneType, NoneType)
  @overload(AreaChartItem, QLineSeries, QGraphicsItem)
  @overload(AreaChartItem, QLineSeries, NoneType)
  @overload(AreaChartItem, NoneType, QGraphicsItem)
  @overload(AreaChartItem, NoneType, NoneType)
  @overload(NoneType, QLineSeries, QGraphicsItem)
  @overload(NoneType, QLineSeries, NoneType)
  @overload(NoneType, NoneType, QGraphicsItem)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      area: Optional[AreaChartItem],
      lineSeries: Optional[QLineSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'AreaBoundItem::AreaBoundItem(AreaChartItem *area, QLineSeries
    *lineSeries, QGraphicsItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/areabounditem.html#AreaBoundItem

    Parameters
    ----------

    area : Optional[AreaChartItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineSeries : Optional[QLineSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  AreaBoundItem::AreaBoundItem(AreaChartItem *area, QLineSeries
    #      *lineSeries, QGraphicsItem *item)
    self._noteCreation(AreaBoundItem, lambda: Rituals.call(
        'ritual_ZN13AreaBoundItemC1EP13AreaChartItemP11QLineSeriesP13QGraph'
        'icsItem',
        self._addressOf(area), self._addressOf(lineSeries),
        self._addressOf(item, 'QGraphicsItem'),
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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void AreaBoundItem::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/areabounditem.html#updateGeometry
    """
    #  void AreaBoundItem::updateGeometry()
    ritual = 'ritual_ZN13AreaBoundItem14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13AreaBoundItem14updateGeometryEv'
    self.uglySide.call(ritual)
