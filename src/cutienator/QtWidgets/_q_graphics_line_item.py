"""
QGraphicsLineItem binding of the Qt C++
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
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLineF, QPointF, QRectF, QVariant
  from ..QtGui import QPainter, QPainterPath, QPen
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLineF = WAIT['QLineF']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLineItem(QGraphicsItem):
  """
  The cute side of Qt's QGraphicsLineItem: a plain Python object standing in
  front of one C++ QGraphicsLineItem.

  It is built on the cute 'QGraphicsItem', as Qt's QGraphicsLineItem is built
  on Qt's QGraphicsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsLineItem that has a ritual and that Python
  can call so far, 12 names in all: 'pen', 'setPen', 'line', 'setLine',
  'boundingRect', 'shape', 'contains', 'paint', 'isObscuredBy', 'opaqueArea',
  'type', 'extension'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsLineItem::~QGraphicsLineItem()': the destructor: Python
    never removes a C++ QGraphicsLineItem.

  What has no ritual
  ------------------

  6 of the 23 functions Qt declares: 2 protected; 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsLineItem is created at the first use, not by
    'QGraphicsLineItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsLineItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLineItem'

  #  A C++ QGraphicsLineItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsLineItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QGraphicsLineItem::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QGraphicsLineItem::pen() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsLineItem3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def line(self) -> QLineF:
    """
    Calls Qt's 'QLineF QGraphicsLineItem::line() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#line

    Returns
    -------

    QLineF
      A new cute QLineF around the copy Qt gave back. Python owns it.
    """
    #  QLineF QGraphicsLineItem::line() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsLineItem4lineEv')
    from ..QtCore import QLineF
    return QLineF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsLineItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslineitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsLineItem::boundingRect() const
    ritual = 'ritual_ZNK17QGraphicsLineItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsLineItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsLineItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsLineItem::shape() const
    ritual = 'ritual_ZNK17QGraphicsLineItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsLineItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsLineItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsLineItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK17QGraphicsLineItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsLineItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslineitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK17QGraphicsLineItem12isObscuredByEPK13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGraphicsLineItem12isObscuredByEPK13QGraphicsIte'
          'm')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsLineItem::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsLineItem::opaqueArea() const
    ritual = 'ritual_ZNK17QGraphicsLineItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsLineItem10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsLineItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#type
    """
    #  int QGraphicsLineItem::type() const
    ritual = 'ritual_ZNK17QGraphicsLineItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsLineItem4typeEv'
    return self.uglySide.call(ritual)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsLineItem::extension(const QVariant
    &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#extension

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsLineItem::extension(const QVariant &variant) const
    address = self.uglySide.call(
        'ritual_own_ZNK17QGraphicsLineItem9extensionERK8QVariant',
        self._valueOf(variant),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QGraphicsLineItem::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QGraphicsLineItem::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN17QGraphicsLineItem6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QLineF)
  def setLine(self, line: QLineF) -> None:
    """
    Calls Qt's 'void QGraphicsLineItem::setLine(const QLineF &line)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#setLine

    Parameters
    ----------

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.
    """
    #  void QGraphicsLineItem::setLine(const QLineF &line)
    self.uglySide.call(
        'ritual_ZN17QGraphicsLineItem7setLineERK6QLineF',
        self._valueOf(line),
    )

  @overload(float, float, float, float)
  def setLine(self, x1: float, y1: float, x2: float, y2: float) -> None:
    """
    Calls Qt's 'void QGraphicsLineItem::setLine(qreal x1, qreal y1, qreal x2,
    qreal y2)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#setLine

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.
    """
    #  void QGraphicsLineItem::setLine(qreal x1, qreal y1, qreal x2, qreal
    #      y2)
    self.uglySide.call(
        'ritual_ZN17QGraphicsLineItem7setLineEdddd', x1, y1, x2, y2,
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
    'QGraphicsLineItem::QGraphicsLineItem(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsLineItem::QGraphicsLineItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsLineItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsLineItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(QLineF)
  @overload(QLineF, QGraphicsItem)
  @overload(QLineF, NoneType)
  def __init__(
      self,
      line: QLineF,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLineItem::QGraphicsLineItem(const QLineF &line, QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem

    Parameters
    ----------

    line : QLineF
      Passed on as a value: Qt reads the C++ QLineF, which stays Python's
      own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsLineItem::QGraphicsLineItem(const QLineF &line, QGraphicsItem
    #      *parent)
    self._noteCreation(QGraphicsLineItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsLineItemC1ERK6QLineFP13QGraphicsItem',
        self._valueOf(line), self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, QGraphicsItem)
  @overload(float, float, float, float, NoneType)
  def __init__(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLineItem::QGraphicsLineItem(qreal x1, qreal y1, qreal x2, qreal
    y2, QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslineitem.html#QGraphicsLineItem

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsLineItem::QGraphicsLineItem(qreal x1, qreal y1, qreal x2,
    #      qreal y2, QGraphicsItem *parent)
    self._noteCreation(QGraphicsLineItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsLineItemC1EddddP13QGraphicsItem',
        x1, y1, x2, y2, self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void QGraphicsLineItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslineitem.html#paint

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
    #  void QGraphicsLineItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN17QGraphicsLineItem5paintEP8QPainterPK24QStyleOptionGraph'
        'icsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsLineItem5paintEP8QPainterPK24QStyleOptio'
          'nGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
