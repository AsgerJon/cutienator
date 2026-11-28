"""
PieChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/piechartitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means PieChartItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import ChartAnimation, PieAnimation, PieSliceData, QPieSeries
  from . import QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  PieAnimation = WAIT['PieAnimation']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPieSeries = WAIT['QtCharts:QPieSeries']
  QPieSlice = WAIT['QtCharts:QPieSlice']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PieChartItem(ChartItem):
  """
  The cute side of Qt's PieChartItem: a plain Python object standing in front
  of one C++ PieChartItem.

  It is built on the cute 'ChartItem', as Qt's PieChartItem is built on Qt's
  ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PieChartItem that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'boundingRect', 'paint',
  'animation', 'hoverEnterEvent', 'hoverLeaveEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'handleDomainUpdated',
  'updateLayout', 'handleSlicesAdded', 'handleSlicesRemoved',
  'handleSliceChanged', 'handleSeriesVisibleChanged', 'handleOpacityChanged',
  'setAnimation', 'cleanup', 'updateSliceGeometry'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PieChartItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PieChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PieChartItem::~PieChartItem()': the destructor: Python never
    removes a C++ PieChartItem.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PieChartItem is created at the first use, not by
    'PieChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PieChartItem.
  - Qt tells when it has removed the C++ PieChartItem. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString PieChartItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString PieChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12PieChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PieChartItem'

  #  A C++ PieChartItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PieChartItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PieChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PieChartItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK12PieChartItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF PieChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF PieChartItem::boundingRect() const
    ritual = 'ritual_ZNK12PieChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12PieChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def animation(self) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *PieChartItem::animation() const'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#animation

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *PieChartItem::animation() const
    ritual = 'ritual_ZNK12PieChartItem9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12PieChartItem9animationEv'
    address = self.uglySide.call(ritual)
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PieAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[PieAnimation]) -> None:
    """
    Calls Qt's 'void PieChartItem::setAnimation(PieAnimation *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#setAnimation

    Parameters
    ----------

    animation : Optional[PieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::setAnimation(PieAnimation *animation)
    self.uglySide.call(
        'ritual_ZN12PieChartItem12setAnimationEP12PieAnimation',
        self._addressOf(animation),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPieSeries)
  @overload(NoneType)
  @overload(QPieSeries, QGraphicsItem)
  @overload(QPieSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QPieSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'PieChartItem::PieChartItem(QPieSeries
    *series, QGraphicsItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#PieChartItem

    Parameters
    ----------

    series : Optional[QPieSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  PieChartItem::PieChartItem(QPieSeries *series, QGraphicsItem *item)
    self._noteCreation(PieChartItem, lambda: Rituals.call(
        'ritual_ZN12PieChartItemC1EP10QPieSeriesP13QGraphicsItem',
        self._addressOf(series), self._addressOf(item, 'QGraphicsItem'),
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

  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      a0: Optional[QPainter],
      a1: Optional[QStyleOptionGraphicsItem],
      a2: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void PieChartItem::paint(QPainter *a0, const
    QStyleOptionGraphicsItem *a1, QWidget *a2)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#paint

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::paint(QPainter *a0, const QStyleOptionGraphicsItem
    #      *a1, QWidget *a2)
    ritual = (
        'ritual_ZN12PieChartItem5paintEP8QPainterPK24QStyleOptionGraphicsIt'
        'emP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem5paintEP8QPainterPK24QStyleOptionGrap'
          'hicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(a0), self._addressOf(a1), self._addressOf(a2),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void PieChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN12PieChartItem15hoverEnterEventEP24QGraphicsSceneHoverEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem15hoverEnterEventEP24QGraphicsSceneHo'
          'verEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void PieChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN12PieChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem15hoverLeaveEventEP24QGraphicsSceneHo'
          'verEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void PieChartItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN12PieChartItem15mousePressEventEP24QGraphicsSceneMouseEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem15mousePressEventEP24QGraphicsSceneMo'
          'useEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void PieChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN12PieChartItem17mouseReleaseEventEP24QGraphicsSceneMouseE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem17mouseReleaseEventEP24QGraphicsScene'
          'MouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    PieChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN12PieChartItem21mouseDoubleClickEventEP24QGraphicsSceneMo'
        'useEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieChartItem21mouseDoubleClickEventEP24QGraphicsS'
          'ceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void PieChartItem::handleDomainUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleDomainUpdated
    """
    #  void PieChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN12PieChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12PieChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  def updateLayout(self) -> None:
    """
    Calls Qt's 'void PieChartItem::updateLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#updateLayout
    """
    #  void PieChartItem::updateLayout()
    self.uglySide.call('ritual_ZN12PieChartItem12updateLayoutEv')

  @overload(QList[QPieSlice])
  def handleSlicesAdded(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void PieChartItem::handleSlicesAdded(const QList<QPieSlice *>
    &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleSlicesAdded

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void PieChartItem::handleSlicesAdded(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN12PieChartItem17handleSlicesAddedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def handleSlicesRemoved(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void PieChartItem::handleSlicesRemoved(const QList<QPieSlice
    *> &slices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleSlicesRemoved

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void PieChartItem::handleSlicesRemoved(const QList<QPieSlice *>
    #      &slices)
    self.uglySide.call(
        'ritual_ZN12PieChartItem19handleSlicesRemovedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  def handleSliceChanged(self) -> None:
    """
    Calls Qt's 'void PieChartItem::handleSliceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleSliceChanged
    """
    #  void PieChartItem::handleSliceChanged()
    self.uglySide.call('ritual_ZN12PieChartItem18handleSliceChangedEv')

  def handleSeriesVisibleChanged(self) -> None:
    """
    Calls Qt's 'void PieChartItem::handleSeriesVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleSeriesVisibleChanged
    """
    #  void PieChartItem::handleSeriesVisibleChanged()
    self.uglySide.call(
        'ritual_ZN12PieChartItem26handleSeriesVisibleChangedEv',
    )

  def handleOpacityChanged(self) -> None:
    """
    Calls Qt's 'void PieChartItem::handleOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#handleOpacityChanged
    """
    #  void PieChartItem::handleOpacityChanged()
    self.uglySide.call('ritual_ZN12PieChartItem20handleOpacityChangedEv')

  def cleanup(self) -> None:
    """
    Calls Qt's 'void PieChartItem::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/piechartitem.html#cleanup
    """
    #  void PieChartItem::cleanup()
    ritual = 'ritual_ZN12PieChartItem7cleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12PieChartItem7cleanupEv'
    self.uglySide.call(ritual)

  @overload(QPieSlice)
  @overload(NoneType)
  def updateSliceGeometry(self, slice: Optional[QPieSlice]) -> PieSliceData:
    """
    Calls Qt's 'PieSliceData PieChartItem::updateSliceGeometry(QPieSlice
    *slice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piechartitem.html#updateSliceGeometry

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    PieSliceData
      A new cute PieSliceData around the copy Qt gave back. Python owns it.
    """
    #  PieSliceData PieChartItem::updateSliceGeometry(QPieSlice *slice)
    address = self.uglySide.call(
        'ritual_ZN12PieChartItem19updateSliceGeometryEP9QPieSlice',
        self._addressOf(slice),
    )
    from . import PieSliceData
    return PieSliceData._cuteOwning(address)
