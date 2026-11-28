"""
LineArrowItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/linearrowitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means LineArrowItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem, QGraphicsLineItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QPainterPath
  from ..QtWidgets import QGraphicsSceneMouseEvent
  from . import ChartAxisElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartAxisElement = WAIT['ChartAxisElement']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LineArrowItem(QGraphicsLineItem):
  """
  The cute side of Qt's LineArrowItem: a plain Python object standing in
  front of one C++ LineArrowItem.

  It is built on the cute 'QGraphicsLineItem', as Qt's LineArrowItem is built
  on Qt's QGraphicsLineItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's LineArrowItem that has a ritual and that Python can
  call so far, 3 names in all: 'mousePressEvent', 'boundingRect', 'shape'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ LineArrowItem is created at the first use, not by
    'LineArrowItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LineArrowItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LineArrowItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF LineArrowItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/linearrowitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF LineArrowItem::boundingRect() const
    ritual = 'ritual_ZNK13LineArrowItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LineArrowItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath LineArrowItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/linearrowitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath LineArrowItem::shape() const
    ritual = 'ritual_ZNK13LineArrowItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13LineArrowItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

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

  @overload(ChartAxisElement)
  @overload(NoneType)
  @overload(ChartAxisElement, QGraphicsItem)
  @overload(ChartAxisElement, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[ChartAxisElement],
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'LineArrowItem::LineArrowItem(ChartAxisElement *axis, QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/linearrowitem.html#LineArrowItem

    Parameters
    ----------

    axis : Optional[ChartAxisElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  LineArrowItem::LineArrowItem(ChartAxisElement *axis, QGraphicsItem
    #      *parent)
    self._noteCreation(LineArrowItem, lambda: Rituals.call(
        'ritual_ZN13LineArrowItemC1EP16ChartAxisElementP13QGraphicsItem',
        self._addressOf(axis), self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void LineArrowItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/linearrowitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LineArrowItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN13LineArrowItem15mousePressEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13LineArrowItem15mousePressEventEP24QGraphicsSceneM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))
