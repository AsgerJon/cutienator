"""
PieSliceItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/piesliceitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means PieSliceItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsItem, QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainter, QPainterPath
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import PieSliceData, QPieSlice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  PieSliceData = WAIT['PieSliceData']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPieSlice = WAIT['QtCharts:QPieSlice']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PieSliceItem(QGraphicsObject):
  """
  The cute side of Qt's PieSliceItem: a plain Python object standing in front
  of one C++ PieSliceItem.

  It is built on the cute 'QGraphicsObject', as Qt's PieSliceItem is built on
  Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PieSliceItem that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'boundingRect', 'shape',
  'paint', 'hoverEnterEvent', 'hoverLeaveEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'setLayout', 'sliceCenter',
  'clicked', 'hovered', 'pressed', 'released', 'doubleClicked',
  'updateGeometry', 'labelArmPath'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PieSliceItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PieSliceItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PieSliceItem::~PieSliceItem()': the destructor: Python never
    removes a C++ PieSliceItem.
  - Qt's 'QPainterPath PieSliceItem::slicePath(QPointF center, qreal radius,
    qreal startAngle, qreal angleSpan, qreal *centerAngle, QPointF
    *armStart)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PieSliceItem is created at the first use, not by
    'PieSliceItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PieSliceItem.
  - Qt tells when it has removed the C++ PieSliceItem. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's PieSliceItem that has no cute function yet,
    'slicePath', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString PieSliceItem::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#tr

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
    #  QString PieSliceItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12PieSliceItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPointF, float, QPieSlice)
  @overload(QPointF, float, NoneType)
  def sliceCenter(
      point: QPointF,
      radius: float,
      slice: Optional[QPieSlice],
  ) -> QPointF:
    """
    Calls Qt's 'QPointF PieSliceItem::sliceCenter(QPointF point, qreal
    radius, QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#sliceCenter

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF PieSliceItem::sliceCenter(QPointF point, qreal radius,
    #      QPieSlice *slice)
    address = Rituals.call(
        'ritual_ZN12PieSliceItem11sliceCenterE7QPointFdP9QPieSlice',
        CuteMixin._valueOf(point, 'QPointF'), radius,
        CuteMixin._addressOf(slice),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PieSliceItem'

  #  A C++ PieSliceItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PieSliceItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PieSliceItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PieSliceItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK12PieSliceItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF PieSliceItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF PieSliceItem::boundingRect() const
    ritual = 'ritual_ZNK12PieSliceItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12PieSliceItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath PieSliceItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath PieSliceItem::shape() const
    ritual = 'ritual_ZNK12PieSliceItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12PieSliceItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PieSliceData)
  def setLayout(self, sliceData: PieSliceData) -> None:
    """
    Calls Qt's 'void PieSliceItem::setLayout(const PieSliceData &sliceData)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#setLayout

    Parameters
    ----------

    sliceData : PieSliceData
      Passed on as a value: Qt reads the C++ PieSliceData, which stays
      Python's own.
    """
    #  void PieSliceItem::setLayout(const PieSliceData &sliceData)
    self.uglySide.call(
        'ritual_ZN12PieSliceItem9setLayoutERK12PieSliceData',
        self._valueOf(sliceData),
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

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's 'PieSliceItem::PieSliceItem(QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#PieSliceItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  PieSliceItem::PieSliceItem(QGraphicsItem *parent)
    self._noteCreation(PieSliceItem, lambda: Rituals.call(
        'ritual_ZN12PieSliceItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void PieSliceItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#paint

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
      object.
    """
    #  void PieSliceItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN12PieSliceItem5paintEP8QPainterPK24QStyleOptionGraphicsIt'
        'emP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem5paintEP8QPainterPK24QStyleOptionGrap'
          'hicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void PieSliceItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieSliceItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN12PieSliceItem15hoverEnterEventEP24QGraphicsSceneHoverEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem15hoverEnterEventEP24QGraphicsSceneHo'
          'verEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void PieSliceItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieSliceItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN12PieSliceItem15hoverLeaveEventEP24QGraphicsSceneHoverEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem15hoverLeaveEventEP24QGraphicsSceneHo'
          'verEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void PieSliceItem::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieSliceItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN12PieSliceItem15mousePressEventEP24QGraphicsSceneMouseEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem15mousePressEventEP24QGraphicsSceneMo'
          'useEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void PieSliceItem::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceitem.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieSliceItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN12PieSliceItem17mouseReleaseEventEP24QGraphicsSceneMouseE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem17mouseReleaseEventEP24QGraphicsScene'
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
    PieSliceItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/piesliceitem.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void PieSliceItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN12PieSliceItem21mouseDoubleClickEventEP24QGraphicsSceneMo'
        'useEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12PieSliceItem21mouseDoubleClickEventEP24QGraphicsS'
          'ceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(Qt.MouseButtons)
  def clicked(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void PieSliceItem::clicked(Qt::MouseButtons buttons)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#clicked

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void PieSliceItem::clicked(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN12PieSliceItem7clickedE6QFlagsIN2Qt11MouseButtonEE',
        buttons.value,
    )

  @overload(bool)
  def hovered(self, state: bool) -> None:
    """
    Calls Qt's 'void PieSliceItem::hovered(bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#hovered

    Parameters
    ----------

    state : bool
      Passed on as it is.
    """
    #  void PieSliceItem::hovered(bool state)
    self.uglySide.call('ritual_ZN12PieSliceItem7hoveredEb', state)

  @overload(Qt.MouseButtons)
  def pressed(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void PieSliceItem::pressed(Qt::MouseButtons buttons)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#pressed

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void PieSliceItem::pressed(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN12PieSliceItem7pressedE6QFlagsIN2Qt11MouseButtonEE',
        buttons.value,
    )

  @overload(Qt.MouseButtons)
  def released(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void PieSliceItem::released(Qt::MouseButtons buttons)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#released

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void PieSliceItem::released(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN12PieSliceItem8releasedE6QFlagsIN2Qt11MouseButtonEE',
        buttons.value,
    )

  @overload(Qt.MouseButtons)
  def doubleClicked(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void PieSliceItem::doubleClicked(Qt::MouseButtons buttons)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#doubleClicked

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void PieSliceItem::doubleClicked(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN12PieSliceItem13doubleClickedE6QFlagsIN2Qt11MouseButtonEE',
        buttons.value,
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void PieSliceItem::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#updateGeometry
    """
    #  void PieSliceItem::updateGeometry()
    self.uglySide.call('ritual_ZN12PieSliceItem14updateGeometryEv')

  @overload(QPointF, float, float, float, QPointF)
  @overload(QPointF, float, float, float, NoneType)
  def labelArmPath(
      self,
      start: QPointF,
      angle: float,
      length: float,
      textWidth: float,
      textStart: Optional[QPointF],
  ) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath PieSliceItem::labelArmPath(QPointF start, qreal
    angle, qreal length, qreal textWidth, QPointF *textStart)'.

    Qt's own words: https://doc.qt.io/qt-6/piesliceitem.html#labelArmPath

    Parameters
    ----------

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    angle : float
      Passed on as it is.

    length : float
      Passed on as it is.

    textWidth : float
      Passed on as it is.

    textStart : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath PieSliceItem::labelArmPath(QPointF start, qreal angle,
    #      qreal length, qreal textWidth, QPointF *textStart)
    address = self.uglySide.call(
        'ritual_ZN12PieSliceItem12labelArmPathE7QPointFdddPS0_',
        self._valueOf(start, 'QPointF'), angle, length, textWidth,
        self._addressOf(textStart, 'QPointF'),
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @staticmethod
  def slicePath(*__, **_) -> Never:
    """
    Qt's 'QPainterPath PieSliceItem::slicePath(QPointF center, qreal radius,
    qreal startAngle, qreal angleSpan, qreal *centerAngle, QPointF
    *armStart)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'PieSliceItem.slicePath' has no cute function yet. Qt's "
        "'QPainterPath PieSliceItem::slicePath(QPointF center, qreal "
        "radius, qreal startAngle, qreal angleSpan, qreal *centerAngle, "
        "QPointF *armStart)': takes a number to change where it is.")
