"""
LegendScroller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/legendscroller_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means LegendScroller to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QLegend, Scroller

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QPainter
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import QChart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChart = WAIT['QChart']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LegendScroller(QLegend, Scroller):
  """
  The cute side of Qt's LegendScroller: a plain Python object standing in
  front of one C++ LegendScroller.

  It is built on the cute 'QLegend', as Qt's LegendScroller is built on Qt's
  QLegend, and has everything that class has. It is built on the cute
  'Scroller' as well, as Qt's LegendScroller is built on Qt's Scroller too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's LegendScroller that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'paint', 'setOffset',
  'offset', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'hoverEnterEvent', 'hoverMoveEvent',
  'hoverLeaveEvent', 'handleInteractiveChanged', 'updateForResizerChange',
  'handleDetached'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LegendScroller::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int LegendScroller::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ LegendScroller is created at the first use, not by
    'LegendScroller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LegendScroller.
  - Qt tells when it has removed the C++ LegendScroller. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString LegendScroller::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#tr

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
    #  QString LegendScroller::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14LegendScroller2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LegendScroller'

  #  Qt's LegendScroller is built on more than one class. The part of a C++
  #  LegendScroller that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'Scroller': 'ritual_cast_LegendScroller_Scroller',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LegendScroller::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LegendScroller::metaObject() const
    address = self.uglySide.call('ritual_ZNK14LegendScroller10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF LegendScroller::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF LegendScroller::offset() const
    ritual = 'ritual_ZNK14LegendScroller6offsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14LegendScroller6offsetEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setOffset(self, point: QPointF) -> None:
    """
    Calls Qt's 'void LegendScroller::setOffset(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#setOffset

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void LegendScroller::setOffset(const QPointF &point)
    ritual = 'ritual_ZN14LegendScroller9setOffsetERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14LegendScroller9setOffsetERK7QPointF'
    self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChart)
  @overload(NoneType)
  def __init__(self, chart: Optional[QChart]) -> None:
    """
    Notes what was given, for Qt's 'LegendScroller::LegendScroller(QChart
    *chart)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#LegendScroller

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  LegendScroller::LegendScroller(QChart *chart)
    self._noteCreation(LegendScroller, lambda: Rituals.call(
        'ritual_ZN14LegendScrollerC1EP6QChart', self._addressOf(chart),
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

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
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
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void LegendScroller::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN14LegendScroller5paintEP8QPainterPK24QStyleOptionGraphics'
        'ItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller5paintEP8QPainterPK24QStyleOptionGr'
          'aphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN14LegendScroller15mousePressEventEP24QGraphicsSceneMouseE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller15mousePressEventEP24QGraphicsScene'
          'MouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::mouseMoveEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN14LegendScroller14mouseMoveEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller14mouseMoveEventEP24QGraphicsSceneM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendScroller::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::mouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN14LegendScroller17mouseReleaseEventEP24QGraphicsSceneMous'
        'eEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller17mouseReleaseEventEP24QGraphicsSce'
          'neMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendScroller::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN14LegendScroller21mouseDoubleClickEventEP24QGraphicsScene'
        'MouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller21mouseDoubleClickEventEP24QGraphic'
          'sSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN14LegendScroller15hoverEnterEventEP24QGraphicsSceneHoverE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller15hoverEnterEventEP24QGraphicsScene'
          'HoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::hoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN14LegendScroller14hoverMoveEventEP24QGraphicsSceneHoverEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller14hoverMoveEventEP24QGraphicsSceneH'
          'overEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void LegendScroller::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendScroller::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN14LegendScroller15hoverLeaveEventEP24QGraphicsSceneHoverE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14LegendScroller15hoverLeaveEventEP24QGraphicsScene'
          'HoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def handleInteractiveChanged(self, interactive: bool) -> None:
    """
    Calls Qt's 'void LegendScroller::handleInteractiveChanged(bool
    interactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#handleInteractiveChanged

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void LegendScroller::handleInteractiveChanged(bool interactive)
    self.uglySide.call(
        'ritual_ZN14LegendScroller24handleInteractiveChangedEb', interactive,
    )

  def updateForResizerChange(self) -> None:
    """
    Calls Qt's 'void LegendScroller::updateForResizerChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendscroller.html#updateForResizerChange
    """
    #  void LegendScroller::updateForResizerChange()
    self.uglySide.call('ritual_ZN14LegendScroller22updateForResizerChangeEv')

  @overload(bool)
  def handleDetached(self, attached: bool) -> None:
    """
    Calls Qt's 'void LegendScroller::handleDetached(bool attached)'.

    Qt's own words: https://doc.qt.io/qt-6/legendscroller.html#handleDetached

    Parameters
    ----------

    attached : bool
      Passed on as it is.
    """
    #  void LegendScroller::handleDetached(bool attached)
    self.uglySide.call(
        'ritual_ZN14LegendScroller14handleDetachedEb', attached,
    )
