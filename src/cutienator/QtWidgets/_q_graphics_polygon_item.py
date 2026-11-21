"""
QGraphicsPolygonItem binding of the Qt C++
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
from ..QtCore import Qt
from . import QAbstractGraphicsShapeItem, QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainter, QPainterPath, QPolygonF
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QPolygonF = WAIT['QPolygonF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
  """
  The cute side of Qt's QGraphicsPolygonItem: a plain Python object standing
  in front of one C++ QGraphicsPolygonItem.

  It is built on the cute 'QAbstractGraphicsShapeItem', as Qt's
  QGraphicsPolygonItem is built on Qt's QAbstractGraphicsShapeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsPolygonItem that has a ritual and that
  Python can call so far, 11 names in all: 'polygon', 'setPolygon',
  'fillRule', 'setFillRule', 'boundingRect', 'shape', 'contains', 'paint',
  'isObscuredBy', 'opaqueArea', 'type'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsPolygonItem::~QGraphicsPolygonItem()': the destructor:
    Python never removes a C++ QGraphicsPolygonItem.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 3 protected; 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsPolygonItem is created at the first use, not by
    'QGraphicsPolygonItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsPolygonItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsPolygonItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def polygon(self) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QGraphicsPolygonItem::polygon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#polygon

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QGraphicsPolygonItem::polygon() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem7polygonEv',
    )
    from ..QtGui import QPolygonF
    return QPolygonF._cuteOwning(address)

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QGraphicsPolygonItem::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QGraphicsPolygonItem::fillRule() const
    return Qt.FillRule(self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem8fillRuleEv',
    ))

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsPolygonItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsPolygonItem::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPolygonItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPolygonItem::shape() const
    address = self.uglySide.call('ritual_ZNK20QGraphicsPolygonItem5shapeEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsPolygonItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsPolygonItem::contains(const QPointF &point) const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem8containsERK7QPointF',
        self._valueOf(point),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsPolygonItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsPolygonItem::isObscuredBy(const QGraphicsItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem12isObscuredByEPK13QGraphicsItem',
        self._addressOf(item),
    )

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPolygonItem::opaqueArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPolygonItem::opaqueArea() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsPolygonItem10opaqueAreaEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsPolygonItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#type
    """
    #  int QGraphicsPolygonItem::type() const
    return self.uglySide.call('ritual_ZNK20QGraphicsPolygonItem4typeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPolygonF)
  def setPolygon(self, polygon: QPolygonF) -> None:
    """
    Calls Qt's 'void QGraphicsPolygonItem::setPolygon(const QPolygonF
    &polygon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#setPolygon

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  void QGraphicsPolygonItem::setPolygon(const QPolygonF &polygon)
    self.uglySide.call(
        'ritual_ZN20QGraphicsPolygonItem10setPolygonERK9QPolygonF',
        self._valueOf(polygon),
    )

  @overload(Qt.FillRule)
  def setFillRule(self, rule: Qt.FillRule) -> None:
    """
    Calls Qt's 'void QGraphicsPolygonItem::setFillRule(Qt::FillRule rule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#setFillRule

    Parameters
    ----------

    rule : Qt.FillRule
      Passed on as its number.
    """
    #  void QGraphicsPolygonItem::setFillRule(Qt::FillRule rule)
    self.uglySide.call(
        'ritual_ZN20QGraphicsPolygonItem11setFillRuleEN2Qt8FillRuleE',
        rule.value,
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
    'QGraphicsPolygonItem::QGraphicsPolygonItem(QGraphicsItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#QGraphicsPolygonItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPolygonItem::QGraphicsPolygonItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsPolygonItem, lambda: Rituals.call(
        'ritual_ZN20QGraphicsPolygonItemC1EP13QGraphicsItem',
        self._addressOf(parent),
    ))

  @overload(QPolygonF)
  @overload(QPolygonF, QGraphicsItem)
  @overload(QPolygonF, NoneType)
  def __init__(
      self,
      polygon: QPolygonF,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsPolygonItem::QGraphicsPolygonItem(const QPolygonF &polygon,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspolygonitem.html#QGraphicsPolygonItem

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPolygonItem::QGraphicsPolygonItem(const QPolygonF &polygon,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsPolygonItem, lambda: Rituals.call(
        'ritual_ZN20QGraphicsPolygonItemC1ERK9QPolygonFP13QGraphicsItem',
        self._valueOf(polygon), self._addressOf(parent),
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
    Calls Qt's 'void QGraphicsPolygonItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspolygonitem.html#paint

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
    #  void QGraphicsPolygonItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN20QGraphicsPolygonItem5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget',
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
