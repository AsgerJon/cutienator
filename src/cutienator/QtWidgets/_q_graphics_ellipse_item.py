"""
QGraphicsEllipseItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractGraphicsShapeItem, QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainter, QPainterPath
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
  """
  The cute side of Qt's QGraphicsEllipseItem: a plain Python object standing
  in front of one C++ QGraphicsEllipseItem.

  It is built on the cute 'QAbstractGraphicsShapeItem', as Qt's
  QGraphicsEllipseItem is built on Qt's QAbstractGraphicsShapeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsEllipseItem that has a ritual and that
  Python can call so far, 13 names in all: 'rect', 'setRect', 'startAngle',
  'setStartAngle', 'spanAngle', 'setSpanAngle', 'boundingRect', 'shape',
  'contains', 'paint', 'isObscuredBy', 'opaqueArea', 'type'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsEllipseItem::~QGraphicsEllipseItem()': the destructor:
    Python never removes a C++ QGraphicsEllipseItem.

  What has no ritual
  ------------------

  7 of the 25 functions Qt declares: 3 protected; 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsEllipseItem is created at the first use, not by
    'QGraphicsEllipseItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsEllipseItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsEllipseItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsEllipseItem::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEllipseItem::rect() const
    address = self.uglySide.call('ritual_ZNK20QGraphicsEllipseItem4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def startAngle(self) -> int:
    """
    Calls Qt's 'int QGraphicsEllipseItem::startAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#startAngle
    """
    #  int QGraphicsEllipseItem::startAngle() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsEllipseItem10startAngleEv',
    )

  def spanAngle(self) -> int:
    """
    Calls Qt's 'int QGraphicsEllipseItem::spanAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#spanAngle
    """
    #  int QGraphicsEllipseItem::spanAngle() const
    return self.uglySide.call('ritual_ZNK20QGraphicsEllipseItem9spanAngleEv')

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsEllipseItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEllipseItem::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsEllipseItem12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsEllipseItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsEllipseItem::shape() const
    address = self.uglySide.call('ritual_ZNK20QGraphicsEllipseItem5shapeEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsEllipseItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsEllipseItem::contains(const QPointF &point) const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsEllipseItem8containsERK7QPointF',
        self._valueOf(point),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsEllipseItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsEllipseItem::isObscuredBy(const QGraphicsItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsEllipseItem12isObscuredByEPK13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsEllipseItem::opaqueArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsEllipseItem::opaqueArea() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsEllipseItem10opaqueAreaEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsEllipseItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#type
    """
    #  int QGraphicsEllipseItem::type() const
    return self.uglySide.call('ritual_ZNK20QGraphicsEllipseItem4typeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsEllipseItem::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsEllipseItem::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20QGraphicsEllipseItem7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsEllipseItem::setRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#setRect

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
    """
    #  void QGraphicsEllipseItem::setRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN20QGraphicsEllipseItem7setRectEdddd', x, y, w, h,
    )

  @overload(int)
  def setStartAngle(self, angle: int) -> None:
    """
    Calls Qt's 'void QGraphicsEllipseItem::setStartAngle(int angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#setStartAngle

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void QGraphicsEllipseItem::setStartAngle(int angle)
    self.uglySide.call(
        'ritual_ZN20QGraphicsEllipseItem13setStartAngleEi', angle,
    )

  @overload(int)
  def setSpanAngle(self, angle: int) -> None:
    """
    Calls Qt's 'void QGraphicsEllipseItem::setSpanAngle(int angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#setSpanAngle

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void QGraphicsEllipseItem::setSpanAngle(int angle)
    self.uglySide.call(
        'ritual_ZN20QGraphicsEllipseItem12setSpanAngleEi', angle,
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
    Notes what was given, for Qt's
    'QGraphicsEllipseItem::QGraphicsEllipseItem(QGraphicsItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#QGraphicsEllipseItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsEllipseItem::QGraphicsEllipseItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsEllipseItem, lambda: Rituals.call(
        'ritual_ZN20QGraphicsEllipseItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(QRectF)
  @overload(QRectF, QGraphicsItem)
  @overload(QRectF, NoneType)
  def __init__(
      self,
      rect: QRectF,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsEllipseItem::QGraphicsEllipseItem(const QRectF &rect,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#QGraphicsEllipseItem

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsEllipseItem::QGraphicsEllipseItem(const QRectF &rect,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsEllipseItem, lambda: Rituals.call(
        'ritual_ZN20QGraphicsEllipseItemC1ERK6QRectFP13QGraphicsItem',
        self._valueOf(rect), self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, QGraphicsItem)
  @overload(float, float, float, float, NoneType)
  def __init__(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsEllipseItem::QGraphicsEllipseItem(qreal x, qreal y, qreal w,
    qreal h, QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsellipseitem.html#QGraphicsEllipseItem

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

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsEllipseItem::QGraphicsEllipseItem(qreal x, qreal y, qreal w,
    #      qreal h, QGraphicsItem *parent)
    self._noteCreation(QGraphicsEllipseItem, lambda: Rituals.call(
        'ritual_ZN20QGraphicsEllipseItemC1EddddP13QGraphicsItem',
        x, y, w, h, self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void QGraphicsEllipseItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsellipseitem.html#paint

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
    #  void QGraphicsEllipseItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN20QGraphicsEllipseItem5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget',
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
